#get_commits

import requests
import pandas as pd
import re
import json
import math


def get_commits(base_url, key, owner, repo, commits, pull, username, api_token):
    r_commits = requests.get(base_url + key + owner + repo + commits.format(pull),
                             auth=(username, api_token)).json()
    df_commits = pd.json_normalize(r_commits)
    list_commits = list(df_commits['commit.message'])
    commit = list(set([commit if commit == 'lab-finished' else 'lab-started' for commit in list_commits]))
    if 'lab-finished' in commit:
        return 'lab-finished'
    else:
        return 'lab-started'