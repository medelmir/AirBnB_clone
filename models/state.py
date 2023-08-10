#!/usr/bin/python3
"""Defines the State class, inheriting from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Represents a state within the application.

    Attributes:
        name (str): The name of the state.
    """

    name = ""
