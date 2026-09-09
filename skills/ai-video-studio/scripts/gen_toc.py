#!/usr/bin/env python3
"""Sinh mục lục cho các file trong references/.

Vì sao cần: quy tắc viết skill của Anthropic yêu cầu file reference dài hơn
100 dòng phải có mục lục. Mục lục ở đây kèm SỐ DÒNG để agent đọc thẳng đúng
đoạn cần (Read với offset, hoặc sed -n), thay vì nạp cả file vào context.

Script tự thay thế mục lục cũ nếu đã có, nên chạy lại bao nhiêu lần cũng được.
Chạy lại sau mỗi lần sửa nội dung file reference, nếu không số dòng sẽ lệch.

    python scripts/gen_toc.py            # ghi vào file
    python scripts/gen_toc.py --check    # chỉ báo file nào lệch, không ghi
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Windows: console mặc định là cp1252, in tiếng Việt sẽ ném UnicodeEncodeError.
# Ép UTF-8 cho stdout/stderr để script chạy được mà không cần set biến môi trường.
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass

BAT_DAU = "<!-- MUCLUC:BAT-DAU (sinh bang scripts/gen_toc.py, dung sua tay) -->"
KET_THUC = "<!-- MUCLUC:KET-THUC -->"
NGUONG_DONG = 100

RE_MUCLUC = re.compile(
    re.escape(BAT_DAU) + r".*?" + re.escape(KET_THUC) + r"\n*",
    re.S,
)


def doc_tieu_de(dong: list[str]) -> list[tuple[int, str]]:
    """Trả về [(so_dong_1_based, tieu_de)] cho mọi heading cấp 2, bỏ qua code block."""
    ket_qua = []
    trong_code = False
    for i, d in enumerate(dong, start=1):
        if d.lstrip().startswith("```"):
            trong_code = not trong_code
            continue
        if trong_code:
            continue
        if d.startswith("## "):
            ket_qua.append((i, d[3:].strip()))
    return ket_qua


def dung_muc_luc(muc: list[tuple[int, str]]) -> str:
    # Tiêu đề trong các file này thường đã tự đánh số ("## 4. Chế độ tạo"),
    # nên dùng gạch đầu dòng để khỏi ra "2. 1. Chế độ tạo".
    hang = [f"- {ten} — dòng {so}" for so, ten in muc]
    return "\n".join(
        [
            BAT_DAU,
            "**Mục lục** (số dòng để đọc thẳng đúng đoạn, không cần nạp cả file)",
            "",
            *hang,
            "",
            KET_THUC,
            "",
        ]
    )


def vi_tri_chen(noi_dung: str) -> int:
    """Chèn ngay trước heading cấp 2 đầu tiên. Trả về offset ký tự."""
    m = re.search(r"^## ", noi_dung, re.M)
    return m.start() if m else len(noi_dung)


def xu_ly(duong_dan: Path, chi_kiem: bool) -> str:
    goc = duong_dan.read_text(encoding="utf-8")
    sach = RE_MUCLUC.sub("", goc)

    if len(sach.splitlines()) <= NGUONG_DONG:
        if goc != sach:
            if not chi_kiem:
                duong_dan.write_text(sach, encoding="utf-8")
            return "go bo (file ngan hon nguong)"
        return "bo qua (ngan hon nguong)"

    # Lặp tới khi số dòng ổn định: chèn mục lục làm dịch chính số dòng nó ghi.
    moi = sach
    for _ in range(5):
        muc = doc_tieu_de(moi.splitlines())
        if not muc:
            return "bo qua (khong co heading cap 2)"
        khoi = dung_muc_luc(muc)
        vt = vi_tri_chen(sach)
        ung_vien = sach[:vt] + khoi + sach[vt:]
        if ung_vien == moi:
            break
        moi = ung_vien
    else:
        return "KHONG HOI TU, bo qua"

    if moi == goc:
        return "da dung san"
    if not chi_kiem:
        duong_dan.write_text(moi, encoding="utf-8")
    return f"cap nhat ({len(doc_tieu_de(moi.splitlines()))} muc)"


def main() -> int:
    bo_phan_tich = argparse.ArgumentParser(description=__doc__)
    bo_phan_tich.add_argument(
        "--check", action="store_true", help="chi bao file nao lech, khong ghi"
    )
    bo_phan_tich.add_argument(
        "--dir", default=None, help="thu muc references (mac dinh: canh script)"
    )
    doi_so = bo_phan_tich.parse_args()

    goc_skill = Path(doi_so.dir) if doi_so.dir else Path(__file__).resolve().parent.parent / "references"
    if not goc_skill.is_dir():
        print(f"khong thay thu muc: {goc_skill}", file=sys.stderr)
        return 1

    tep = sorted(goc_skill.glob("*.md"))
    if not tep:
        print(f"khong co file .md trong {goc_skill}", file=sys.stderr)
        return 1

    co_thay_doi = False
    for t in tep:
        kq = xu_ly(t, doi_so.check)
        if "cap nhat" in kq or "go bo" in kq:
            co_thay_doi = True
        print(f"  {t.name:24} {kq}")

    if doi_so.check and co_thay_doi:
        print("\nCo file muc luc da lech. Chay lai khong kem --check de sua.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
