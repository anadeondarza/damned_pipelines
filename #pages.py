#pages

import requests
import pandas as pd
import re
import json
import math

def pages(base_url, search, state, username, api_token):
    pages = requests.get(base_url + search.format(state), auth=(username,api_token)).json()['total_count']
    if STATE == 'open':
        pages = math.ceil(pages/100)
        return pages
    elif STATE == 'closed':
        pages = math.ceil(pages/100)
        return pages