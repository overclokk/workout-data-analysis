import pandas as pd

from constants import EXERCISE_NAME
from src.Exercises import Exercises, category_generator_config
from src.utils import latest_strong_file

data = pd.read_csv(latest_strong_file(), sep=';')
exercises = data[EXERCISE_NAME].unique()

print('-------------------')

not_in_exercises_dictionary = []
exercises_with_less_category = []
for exercise in exercises:
    if exercise not in Exercises:
        not_in_exercises_dictionary.append(exercise)
        continue

    count = len(Exercises[exercise].values()) - list(Exercises[exercise].values()).count('')
    print(exercise + ': ' + str(count))
    if count < len(category_generator_config):
        exercises_with_less_category.append(exercise)


print('-------------------')
print('Not in Exercises dictionary: ' + str(len(not_in_exercises_dictionary)))
print('-------------------')
print('\n'.join(not_in_exercises_dictionary))

print('-------------------')
count_categories = len(category_generator_config)
print(f"Exercises with less then {count_categories} category: " + str(len(exercises_with_less_category)))
print('-------------------')
print('\n'.join(exercises_with_less_category))