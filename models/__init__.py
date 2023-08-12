#!/usr/bin/python3
"""This is the magic method that initializes the models package

It serves as an entry point for the models package, which provides the
storage engine for persistently managing object instances.
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
