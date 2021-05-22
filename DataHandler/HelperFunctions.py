import pandas as pd
import numpy as np


def generate_gini_values():
    pass


def bootstrap_dataset(data: pd.DataFrame):
    new_set = data.sample(n=data.shape[0])
    print(data)
    print(new_set)
