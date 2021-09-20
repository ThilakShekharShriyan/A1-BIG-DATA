#assignment 1 tast 1
import sys
import json
from datetime import datetime

for line in sys.stdin: #{"ID":1321,}
    line = line.strip()
    res = json.loads(line)
    d = res["Start_Time"]  #2017-02-07 13:32:33 2020-09-23 23:12:04
    v =d[11:13]
    

    if(res["Severity"] >= 2 and res["Sunrise_Sunset"] == "Night" and res["Visibility(mi)"] <= 10.0 and res["Precipitation(in)"] >= 0.2 and res["Weather_Condition"] == "Heavy Snow" or "Thunderstorm" or "Heavy Rain" or "Showers" or "Blowing Dust" and 'lane blocked' or 'shoulder blocked' or 'overturned vehicle' in res["Description"]):
        print(v, 1)
