import json

from src.Exercises import Exercises

json_string = json.dumps(Exercises, indent=4)

with open('data/exercise_categories.json', 'w') as json_file:
    json.dump(Exercises, json_file, indent=4)
