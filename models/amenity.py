#!/usr/bin/python3
"""Amenity Module for Airbnb project"""
from models.base_model import BaseModel

class Amenity(BaseModel):
    """Class for amenity"""
    
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)