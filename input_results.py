import requests
import json

import pandas as pd
from pandas.io.json import json_normalize

raw_results = requests.get("https://results.elections.virginia.gov/vaelections/2019%20November%20General/Json/GeneralAssembly.json").content
results = json.loads(raw_results)

races = json_normalize(results['Races'], 'Candidates', ['RaceName'])
for b in ["House", "Senate"]:
    r = races[races['RaceName'].str.contains(b)]
    total = r.Votes.sum()
    d_r = r[r.PoliticalParty == 'Democratic']['Votes'].sum()
    r_r = r[r.PoliticalParty == 'Republican']['Votes'].sum()
    print(b, round(d_r/total * 100, 3), round(r_r/total * 100))
