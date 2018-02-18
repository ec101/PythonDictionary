import json
import difflib

dataFile = open("data.json")
data = json.load(dataFile)

def findDefinition(key):  
    lowerKey = key.lower()
    if lowerKey in data:
        return data[lowerKey]
    elif len(difflib.get_close_matches(lowerKey, data.keys(), n=1)) == 0:
        return "Unknown word "+key+"."
    else:
        possible = difflib.get_close_matches(lowerKey, data.keys(), n=1)
        print("Unknown word "+key+". Did you mean "+possible[0]+"?")
        decision = input("y/n? ")
        if decision.lower() == "y":
            return findDefinition(possible[0])
        else:
            return "Word not found."
    
word = input("Enter Word: ")
 
result = findDefinition(word)

if type(result) == list:
    for r in result:
        print(r)
else:
    print(result)