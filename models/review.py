#!/usr/bin/python3
""" Review module for the AirBnb project """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class to store review information """
    place_id = ""
    user_id = ""
    text = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)