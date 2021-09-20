#assignment 1 tast 2
import sys
import json
import requests
from datetime import *

for line in sys.stdin:

    line= json.loads(line)

    data = {
        "latitude":line["Start_Lat"],
        "longitude":  line["Start_Lng"]}

    res = requests.post('http://20.185.44.219:5000/', json=data)
    

    print(res.text)
