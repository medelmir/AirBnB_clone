#!/usr/bin/python3
"""Defines the User class, inheriting from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user in the application.

    Attributes:
        email (str): The user email address.
        password (str): The user's password.
        first_name (str): The user first name.
        last_name (str): The user last name.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
