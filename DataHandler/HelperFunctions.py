import pandas as pd
import numpy as np


def gini_value(yes, no):
    yn_sum = yes + no
    p_yes = yes / yn_sum
    p_no = no / yn_sum
    return 1 - p_yes ** 2 - p_no ** 2


def bootstrap_dataset(data: pd.DataFrame):
    new_set = data.sample(n=data.shape[0])
    return new_set
