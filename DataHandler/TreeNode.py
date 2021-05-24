import pandas as pd
import numpy as np
from collections import Counter


class TreeNode:
    def __init__(self,
                 data: pd.DataFrame,
                 depth=0,
                 node_type=None):
        self.X = data.drop(['class'], axis='columns').copy()
        self.Y = data['class'].values

        self.depth = depth
        self.features = list(self.X.columns)

        self.node_type = node_type if node_type else 'root'
        self.counts = Counter(self.Y)
        self.left = None
        self.Right = None


    def generate_gini(self):
        # Create the dataframe for splitting our values
        split_base = self.X.copy()
        split_base['Y'] = self.Y

        max_gain = 0



