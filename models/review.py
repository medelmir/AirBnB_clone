#!/usr/bin/python3
"""Defines the Review class, inheriting from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Represents a review in the application.

    Attributes:
        place_id (str): The id of the place to review.
        password (str): The id of user who wrote the review.
        text (str): The review text content.
    """

    place_id = ""
    user_id = ""
    text = ""
