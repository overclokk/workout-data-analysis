import json

from src.Exercises import Exercises


with open('data/exercises.json', 'w') as json_file:
    json.dump(Exercises, json_file, indent=4)
