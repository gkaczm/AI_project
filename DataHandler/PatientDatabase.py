import pandas as pd


class PatientDatabase:
    def __init__(self, data_path):
        self.all_patient_data = pd.read_csv(data_path)

        self.mandatory_columns = ['QRSduration', 'PRinterval', 'Q-Tinterval', 'Tinterval', 'Pinterval',
                                  'J']  # Kolumny które są wymagane do zaakceptowania danych

        self.discard_empty()

    def discard_empty(self):
        self.all_patient_data.dropna(subset=self.mandatory_columns,
                                     inplace=True,
                                     how='any')

    def print_first_n(self, n):
        print(self.all_patient_data.head(n).to_string())
