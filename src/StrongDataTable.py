from typing import Dict

import numpy as np
import pandas as pd
from pandas import DataFrame

from constants import DATE, TIME, WEIGHT, REPS, LIFTED, REPS_WITH_LOAD, REPS_BW, DAY_NAME, MONTH_NAME, MONTH, YEAR, \
    WEEK_NUMBER, YEAR_WEEK_NUMBER, EXERCISE_NAME


class StrongDataTable:
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
    LIFTED: str = 'Total wight lifted'
    REPS_WITH_LOAD: str = 'Reps with load'
    REPS_BW: str = 'Reps BW'
    DAY_NAME: str = 'Weekday'
    MONTH_NAME: str = 'Month'
    MONTH: str = 'Month'
    YEAR: str = 'Year'
    WEEK_NUMBER: str = 'Week_Number'
    YEAR_WEEK_NUMBER: str = YEAR + "-" + WEEK_NUMBER

    def __init__(self, csv_file_path: str, exercises: Dict[str, Dict[str, str]]):
        self.options = None
        self.csv_file_path = csv_file_path
        self.exercises = exercises

    def with_options(self, options: Dict[str, any]):
        self.options: Dict[str, any] = options
        return self

    def build(self) -> DataFrame:
        # Set pd with options if self.options is not None
        if self.options is not None:
            # create loop to set options
            for key, value in self.options.items():
                pd.set_option(key, value)

        df: DataFrame = pd.read_csv(self.csv_file_path, sep=';')
        # Split the date to have date and time separated
        df[[DATE, TIME]] = df.Date.str.split(" ", expand=True)
        # Convert date to dateTime
        df[DATE] = pd.to_datetime(df[DATE])
        # Convert Weight values to float
        df[WEIGHT] = pd.to_numeric(df[WEIGHT], errors='coerce')
        # Remove NaN
        df = df.replace(np.nan, 0, regex=True)
        # Convert REPS to int and add new column
        df[REPS] = df[REPS].astype(int)
        # Get the total lifted for every set and add it to new column
        df[LIFTED] = (df[WEIGHT] * df[REPS])
        # Reps with weight
        df[REPS_WITH_LOAD] = np.where(df[LIFTED] != 0, df[REPS], 0)
        # Reps with body weight
        df[REPS_BW] = np.where(df[LIFTED] == 0, df[REPS], 0)
        # Add new columns based on the date
        df[DAY_NAME] = df[DATE].dt.day_name()
        df[MONTH_NAME] = df[DATE].dt.month_name()
        df[MONTH] = df[DATE].dt.month
        df[YEAR] = df[DATE].dt.year
        df[WEEK_NUMBER] = df[DATE].dt.isocalendar().week
        # df with year and week number as index
        df[YEAR_WEEK_NUMBER] = df[YEAR].astype(str) + "-" + df[WEEK_NUMBER].astype(str)

        self.__update_columns_with_exercises(df)

        return df

    def __update_columns_with_exercises(self, df):
        # Get all unique keys from the exercises dictionary
        all_keys = set(key for exercise in self.exercises.values() for key in exercise.keys())
        # Add new columns based on the exercises dictionary
        for column_name in all_keys:
            df[column_name] = df.apply(lambda row: self.__get_exercise_value(row, column_name), axis=1)

    def __get_exercise_value(self, row: DataFrame, column_name: str) -> object:
        exercise_name = row[EXERCISE_NAME]
        if exercise_name in self.exercises:
            return self.exercises[exercise_name].get(column_name, "")
        return ""
