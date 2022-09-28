import json
from textwrap import indent
from unicodedata import category

with open("categoryPath.json","r") as new:
    data = json.load(new)
    
with open(data["category1"]["location"]) as new:
    newdata = json.load(new)
    
print(newdata)

