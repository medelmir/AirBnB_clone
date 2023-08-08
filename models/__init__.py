#!/usr/bin/python3
"""__init__ magic method that initializes the models package.

It serves as an entry point for the models package. It imports the
`FileStorage` class from the `models.engine.file_storage` module, which
provides the storage engine for persistently managing object instances.
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
