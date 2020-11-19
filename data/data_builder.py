import json
import pandas as pd
from pathlib import Path
"""This script builds a pandas dataframe out of the already-scraped fighter's json file."""

fighter_stats_path = Path(__file__).parent.joinpath('extraction/fighters.json')
fighter_fights_path = Path(__file__).parent.joinpath('extraction/fights.json')

def build_fighters_statistics():
    fighters = pd.DataFrame([json.loads(line) for line in open(fighter_stats_path)])
    return fighters

def build_fighters_match_histories():
    fights = pd.DataFrame([json.loads(line) for line in open(fighter_fights_path)])
    return fights

if __name__ == '__main__':
	#build_fighters_statistics()