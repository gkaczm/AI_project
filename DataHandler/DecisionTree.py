import pandas as pd


class DecisionTree:
    # data = dataframe with all attributes + class column with binary classification
    def __init__(self, data: pd.DataFrame):
        self.dataset = data.copy()
        self.split_values = data.copy()  # Temporary, will be set to proper values on generate_splits function call

        pass

    # Generates the split values for each attribute in the decision tree

    def generate_splits(self):
        # 1 Policz wszystkie 1 w kolumnach gdzie dana wartość jest mniejsza od zadanej
        # Poniższy początek i próba jest ogólnie chujowa
        # Co chcemy żeby to robiło :
        # Chcemy znaleźć wartość "split" która najlepiej podzieli nam zbiór na pół
        #
        # Czyli chcemy policzyć ile osób które np. mają puls szybszy od tego w pierwszym rzędzie ma arytmie a ile nie i
        # z tych dwóch liczebności policzyć "impurity value" za pomocą funkcji z HelperFunctions.py, wydaje mi sie że
        # niepotrzebuje ona wytłumaczenia

        # Liczymy to "impurity value" dla każdej komórki i potem dla każdej kolumny nasz "split" to będzie najniższa
        # wartość impurity

        # Czyli na koniec mamy jeden rząd poprostu z naszymi splitami które bedą potrzebne dla drzewa żeby mogło
        # sobie podejmować decyzje binarnie (Czy ten pacjent ma QRST niższe niż split dla QRST ? TAK | NIE)
        # I na tej podstawie zbudujemy drzewo :)

        

        for col in self.dataset.columns:
            for index, row in self.dataset[col].iteritems():
                print(self.dataset.loc[(self.dataset[col] < row)].groupby('class').count())
