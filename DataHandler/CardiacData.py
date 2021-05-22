import pandas as pd
import numpy as np
import os


class CardiacData:

    def __init__(self, data_path):
        cardiac_data = pd.read_csv(data_path)
        print(cardiac_data)

dir = os.path.realpath(os.path.dirname(__file__))  # Directory of your Python file
file_path = os.path.join(dir, "resources", "arrhythmia.csv")  # Create the path of the file
test = CardiacData(file_path)