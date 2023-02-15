#!/usr/bin/python3
"""Defines the review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review.
    Attributes:
        place_id (str): The place id of the review.
        user_id (str): The user id of the review.
        text (str): The text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""
