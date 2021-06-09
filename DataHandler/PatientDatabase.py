import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.impute import SimpleImputer
from sklearn.impute import KNNImputer
from sklearn.ensemble import GradientBoostingClassifier
from IPython.display import display
from sklearn.svm import NuSVC


class PatientDatabase:

    def __init__(self, data_path):
        self.all_patient_data = pd.read_csv(data_path, skipinitialspace=True)
        self.personal_info_column_names = ['age', 'sex', 'height', 'weight']

        # Dataframe containing age, sex etc. info
        self.personal_info_data = self.all_patient_data[self.personal_info_column_names]
        classes = self.all_patient_data['class']
        print(set(classes))
        # Dataframe containing all ECG results + binary classification
        self.all_cardio_data = self.all_patient_data.copy().drop(self.personal_info_column_names, axis='columns')
        self.all_cardio_data = self.all_cardio_data.drop(self.all_cardio_data[self.all_cardio_data['class'] == 16].index)
        classes = self.all_cardio_data['class']
        print(set(classes))
        self.all_cardio_data.loc[self.all_cardio_data['class'] > 1, 'class'] = 0

        self.X = self.all_cardio_data.iloc[:, 0:len(self.all_cardio_data.columns) - 1].values
        # Zastąpienie nanów wartosciami usrednionymi
        # define imputer
        imp = SimpleImputer(missing_values=np.nan, strategy='mean')
        self.X = pd.DataFrame(imp.fit_transform(self.X),
                              columns=self.all_cardio_data.iloc[:, 0:len(self.all_cardio_data.columns) - 1].columns)

        self.y = self.all_cardio_data.iloc[:, len(self.all_cardio_data.columns) - 1].values
        self.X.to_html('X.html')        # Zredukowanie danych X do najważniejszych kolumn, wartoscią poniżej można sie bawić
        corrMatrix = self.X.corr()
        ax = sns.heatmap(
            corrMatrix.iloc[35:56, 175:196],
            vmin=-1, vmax=1, center=0,
            cmap=sns.diverging_palette(20, 220, n=200),
            square=True
        )
        ax.set_xticklabels(
            ax.get_xticklabels(),
            rotation=45,
            horizontalalignment='right'
        )
        plt.xlabel('Attribute 1')
        plt.ylabel('Attribute 2')
        plt.title('Example attribute correlation heatmap')
        plt.show()
        corrMatrix.to_html('temp.html')        # Zredukowanie danych X do najważniejszych kolumn, wartoscią poniżej można sie bawić

        iters = range(len(corrMatrix.columns) - 1)
        drop_cols = []
        threshold = 0.7
        print("Df args: " + str(len(self.X.columns)))
        # Iterate through the correlation matrix and compare correlations
        for i in iters:
            for j in range(i + 1):
                item = corrMatrix.iloc[j:(j + 1), (i + 1):(i + 2)]
                col = item.columns
                row = item.index
                val = abs(item.values)
                # If correlation exceeds the threshold
                if val >= threshold:
                    # Print the correlated features and the correlation value
                    print(col.values[0], "|", row.values[0], "|", round(val[0][0], 2))
                    drop_cols.append(col.values[0])

        # Drop one of each pair of correlated columns
        drops = set(drop_cols)
        self.X = self.X.drop(columns=drops)
        print("Df args: " + str(len(self.X.columns)))

        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2,
                                                                                random_state=0)
        self.importance_cutoff = 0.005
        best_attributes = self.get_best_attributes()
        self.X_train = self.X_train[best_attributes]
        self.X_test = self.X_test[best_attributes]

        self.classify_using_gbc(self.X_train, self.y_train, self.X_test, self.y_test)
        self.classify_using_rf()

    def get_best_attributes(self):
        print("Calculating most meaningful attributes out of :", len(self.X.columns))
        classifier = RandomForestClassifier(n_estimators=100)
        classifier.fit(self.X_train, self.y_train)
        feature_imp = pd.Series(classifier.feature_importances_, index=self.X.columns).sort_values(ascending=False)

        sns.barplot(x=feature_imp, y=feature_imp.index)
        plt.xlabel('Feature Importance Score')
        plt.ylabel('Features')
        plt.title("Visualization of feature importance")
        plt.legend()
        plt.show()

        best_attributes = feature_imp.loc[feature_imp > self.importance_cutoff].index
        print("Reduced ", len(self.X.columns), " attributes to ", len(best_attributes))
        print("Printing best attributes :")
        print(best_attributes)
        return best_attributes

    def classify_using_gbc(self, X_train, y_train, X_test, y_test):
        print("\nStarting GBC classification")
        a = 0
        for i in range(10):
            gb_clf = GradientBoostingClassifier(n_estimators=100)
            gb_clf.fit(X_train, y_train)
            a += gb_clf.score(X_test, y_test) * 100
        print("\n GBC classification finished with score :")
        print(a / 100, "%")

    def classify_using_rf(self):
        print("\nStarting Random Forest classification")
        b = 0
        for i in range(100):
            rf = RandomForestClassifier(n_estimators=100)
            rf.fit(self.X_train, self.y_train)
            b += rf.score(self.X_test, self.y_test) * 100
        print("\n Random Forest classification finished with score :")
        print(b / 100, "%")
