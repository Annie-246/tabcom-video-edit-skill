# -*- coding: utf-8 -*-
"""Tai truoc 2 model rembg dung trong pipeline (moi model 100-200 MB).

Chay: python cai-dat/tai_model.py
"""
from rembg import new_session

for ten in ("birefnet-portrait", "isnet-general-use"):
    print("Dang tai", ten, "...", flush=True)
    new_session(ten)
    print("  xong", ten, flush=True)
print("\nDa tai xong. Model nam trong ~/.u2net/")
