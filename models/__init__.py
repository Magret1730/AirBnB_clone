#!/usr/bin/python3
"""Constructor"""
from models.engine.file_storage import FileStorage

storage = FileStorage("file.json")
storage.reload()
