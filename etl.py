"""
Python E-T-L Example
"""

import requests
import pandas as pd
from sqlalchemy import create_engine

def extract() -> dict:
    API_URL = "https://www.yelp.com/search?find_desc=Thai+food&find_loc=San+Francisco%2C+CA"
    data = requests.get(API_URL).json()
    return data

extract()