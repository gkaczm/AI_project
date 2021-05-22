import pandas as pd


class PatientDatabase:
    def __init__(self, data_path):


        self.all_patient_data = pd.read_csv(data_path)

        # Columns which must not be NaN or the corresponding row will be removed from database
        # <feels good might delete later> only those columns will be used for classification
        self.mandatory_columns = ['QRSduration', 'PRinterval', 'Q-Tinterval', 'Tinterval', 'Pinterval', 'QRS', 'T', 'P',
                                  'QRST', 'heartrate']

        self.personal_info_column_names = ['age', 'sex', 'height', 'weight']

        # define acceptable tolerance(relative) for classification of data f.e. 0.05 means the data will be categorised
        # into 5% step increments
        self.relative_tolerance = 0.05

        # Dataframe containing age,sex etc. info
        self.personal_info_data = self.all_patient_data[self.personal_info_column_names]

        # Dataframe with only the useful ECG results
        self.cardio_data = self.all_patient_data[self.mandatory_columns]

        # Class distribution
        self.class_names = ["Normal", "Coronary Artery Disease", "Old Anterior Myocardial Infarction",
                            "Old Inferior Myocardial Infarction", "Sinus tachycardy", "Sinus bradycardy",
                            "Ventricular Premature Contraction",
                            "Supraventricular Premature Contraction", "Left bundle branch block", "Right bundle branch block", ]

        # lowest and highest value of each column
        self.min_max = self.all_patient_data.min()
        print(self.min_max.to_string())

    def prepare_data(self):
        self.all_patient_data.drop('J', axis='columns', inplace=True)  # Delete the J column cause its almost fully NaN
        self.prune_database_nan()  # pruning before dividing data into parts

    # prune the database from incomplete data
    def prune_database_nan(self):
        print("Patient count before pruning : ", len(self.all_patient_data.index))

        self.all_patient_data.dropna(subset=self.mandatory_columns,
                                     inplace=True,
                                     how='any')

        print("Patient count after pruning : ", len(self.all_patient_data.index))

    def print_first_n(self, n):
        print(self.all_patient_data.head(n).to_string())
