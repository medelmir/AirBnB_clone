#!/usr/bin/python3
"""Defines the Place class, inheriting from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Represents a place within the application.

    Attributes:
        city_id (str): The id of the city where the place is located.
        user_id (str): The id of the user who owns the place.
        name (str): The name of the place.
        description (str): A description of the place.
        number_rooms (int): The number of rooms in the place.
        number_bathrooms (int): The number of bathrooms in the place.
        max_guest (int): The number of guests the place can accommodate.
        price_by_night (int): The price to stay at the place.
        latitude (float): The latitude coordinates location.
        longitude (float): The longitude coordinates location.
        amenity_ids (list): A list of ids representing amenities.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
