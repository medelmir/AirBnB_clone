#!/usr/bin/python3
"""Defines the City class, inheriting from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Represents a city within the application.

    Attributes:
        state_id (str): The state id to which the city belongs.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
