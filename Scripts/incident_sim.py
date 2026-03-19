import pandas as pd
import datetime

data = [
    {"time": datetime.datetime.now(), "event": "Unauthorized access attempt"},
    {"time": datetime.datetime.now(), "event": "Privilege escalation detected"}
]

df = pd.DataFrame(data)
print(df)
