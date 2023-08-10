#!/usr/bin/python3
"""Defines the Amenity class, inheriting from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Represents a amenity within the application.

    Attributes:
        name (str): The name of amenity.
    """

    name = ""
