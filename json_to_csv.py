import json
import pandas as pd
from pandas.io.json import json_normalize

with open('chrome_h2.json','r') as f:
    data = json.loads(f.read())

df = pd.io.json.json_normalize(data)

df.to_csv('cloudflare_1mb_h2_cwnd.csv', index=False)