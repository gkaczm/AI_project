import pandas as pd
from DataHandler.HelperFunctions import *
from DataHandler.DecisionTree import DecisionTree


class PatientDatabase:
    def __init__(self, data_path):
        self.all_patient_data = pd.read_csv(data_path, skipinitialspace=True)

        # Columns which must not be NaN or the corresponding row will be removed from database
        # TODO Generate using decision tree
        self.mandatory_columns = ['QRSduration', 'PRinterval', 'Q-Tinterval', 'Tinterval', 'Pinterval', 'QRS', 'T', 'P',
                                  'QRST', 'heartrate', 'J']
        print(self.all_patient_data.columns.tolist())
        self.prune_database_nan()
        self.personal_info_column_names = ['age', 'sex', 'height', 'weight']

        # Dataframe containing age,sex etc. info
        self.personal_info_data = self.all_patient_data[self.personal_info_column_names]

        # Dataframe containing all ECG results + binary classification
        self.all_cardio_data = self.all_patient_data.copy().drop(self.personal_info_column_names, axis='columns')
        self.all_cardio_data.loc[self.all_cardio_data['class'] > 1, 'class'] = 0

        # List of leading attributes
        self.best_attributes = self.get_best_attributes()
        # Dataframe with only the useful ECG results + bin class
        self.cardio_data = self.all_patient_data[self.mandatory_columns]

    # prune the database from incomplete data
    def prune_database_nan(self):
        print("Patient count before pruning : ", len(self.all_patient_data.index))

        self.all_patient_data.dropna(subset=self.mandatory_columns,
                                     inplace=True,
                                     how='any')

        print("Patient count after pruning : ", len(self.all_patient_data.index))

    def get_best_attributes(self):
        dt = DecisionTree(self.all_cardio_data)
        dt.generate_splits()
        return "placeholder"  # placeholder
