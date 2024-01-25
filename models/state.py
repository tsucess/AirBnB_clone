#!/usr/bin/python3
""" State Module for AirBnb project """
from models.base_model import BaseModel


class State(BaseModel):
    """ State class """
    name = ""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)