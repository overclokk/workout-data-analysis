import os

# Strong CSV columns
DATE: str = 'Date'
WORKOUT_NAME: str = "Workout Name"
EXERCISE_NAME: str = "Exercise Name"
SET_ORDER: str = "Set Order"
WEIGHT: str = "Weight"
WEIGHT_UNIT = 'Weight Unit'
REPS: str = "Reps"
RPE: str = "RPE"
DISTANCE: str = "Distance"
DISTANCE_UNIT: str = "Distance Unit"
SECONDS: str = "Seconds"
NOTES: str = "Notes"
WORKOUT_NOTES: str = "Workout Notes"
WORKOUT_DURATION: str = "Workout Duration"

# Strong CSV columns that are not in the original CSV
TIME: str = 'Time'
LIFTED: str = 'Lifted'
REPS_WITH_LOAD: str = 'Reps with load'
REPS_BW: str = 'Reps BW'
DAY_NAME: str = 'Weekday'
MONTH_NAME: str = 'Month'
MONTH: str = 'Month'
YEAR: str = 'Year'
WEEK_NUMBER: str = 'Week_Number'
YEAR_WEEK_NUMBER: str = YEAR + "-" + WEEK_NUMBER

ALL_KEYS: list[str] = [
    DATE,  # 0
    WORKOUT_NAME,  # 1
    EXERCISE_NAME,  # 2
    SET_ORDER,  # 3
    WEIGHT,  # 4
    WEIGHT_UNIT,  # 5
    REPS,  # 6
    RPE,  # 7
    DISTANCE,  # 8
    DISTANCE_UNIT,  # 9
    SECONDS,  # 10
    NOTES,  # 11
    WORKOUT_NOTES,  # 12
    WORKOUT_DURATION,  # 13
]

# Get the pwd of the project
PWD = os.getcwd()
# Data folder relative to the project
DATA_FOLDER = os.path.join(PWD, 'data')
# CSV data file
DATA_CSV = os.path.join(DATA_FOLDER, 'data.csv')
# Strong CSV data file
STRONG_CSV = os.path.join(DATA_FOLDER, 'strong*.csv')