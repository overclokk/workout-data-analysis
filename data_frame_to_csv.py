from constants import DATA_CSV, STRONG_CSV
from src.StrongDataTable import StrongDataTable
from src.Exercises import Exercises
from src.utils import latest_strong_file

StrongDataTable(latest_strong_file(), Exercises).build().to_csv(DATA_CSV, index=False)
