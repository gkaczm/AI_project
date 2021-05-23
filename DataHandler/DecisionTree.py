import pandas as pd


class DecisionTree:
    # data = dataframe with all attributes + class column with binary classification
    def __init__(self, data: pd.DataFrame):
        self.dataset = data.copy()
        pass

    # Generates the split values for each attribute in the decision tree
    def generate_splits(self):
        for col in self.dataset:
            col_values = self.dataset[col].copy().sort_values()
            for value in col_values:



