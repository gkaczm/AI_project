import pandas as pd


class PatientDatabase:
    def __init__(self, data_path):
        self.all_patient_data = pd.read_csv(data_path)

        # Columns which must not be NaN or the corresponding row will be removed from database
        self.mandatory_columns = ['QRSduration', 'PRinterval', 'Q-Tinterval', 'Tinterval', 'Pinterval',
                                  'J']
        self.discard_empty()

    def discard_empty(self):
        print("Patient count before pruning : ", len(self.all_patient_data.index))

        self.all_patient_data.dropna(subset=self.mandatory_columns,
                                     inplace=True,
                                     how='any')

        print("Patient count after pruning : ", len(self.all_patient_data.index))

    def print_first_n(self, n):
        print(self.all_patient_data.head(n).to_string())
