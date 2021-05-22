import pandas as pd
from DataHandler.HelperFunctions import *


class PatientDatabase:
    def __init__(self, data_path):
        self.all_patient_data = pd.read_csv(data_path)

        # Columns which must not be NaN or the corresponding row will be removed from database
        # TODO Generate using decision tree
        self.mandatory_columns = ['QRSduration', 'PRinterval', 'Q-Tinterval', 'Tinterval', 'Pinterval', 'QRS', 'T', 'P',
                                  'QRST', 'heartrate','J']
        self.prune_database_nan()
        self.personal_info_column_names = ['age', 'sex', 'height', 'weight']

        # Dataframe containing age,sex etc. info
        self.personal_info_data = self.all_patient_data[self.personal_info_column_names]

        # Dataframe containing all ECG results + binary classification
        self.all_cardio_data = self.all_patient_data.drop(self.personal_info_column_names, axis='columns')
        self.all_cardio_data.loc[self.all_cardio_data['class'] > 1, 'class'] = 0
        print(self.all_cardio_data)

        # Dataframe with only the useful ECG results + bin class
        self.cardio_data = self.all_patient_data[self.mandatory_columns]




        # <NOT SURE IF WILL BE NEEDED> lowest and highest value of each column and
        self.min_values = self.all_patient_data.min()
        self.max_values = self.all_patient_data.max()

    # prune the database from incomplete data
    def prune_database_nan(self):
        print("Patient count before pruning : ", len(self.all_patient_data.index))

        self.all_patient_data.dropna(subset=self.mandatory_columns,
                                     inplace=True,
                                     how='any')

        print("Patient count after pruning : ", len(self.all_patient_data.index))

    def print_first_n(self, n):
        print(self.all_patient_data.head(n).to_string())
