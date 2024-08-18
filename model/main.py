import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import  accuracy_score, classification_report
import pickle as pickle

bcancer = None


def get_data():
    global bcancer
    bcancer = pd.read_csv('data/data.csv')
    print(bcancer.head(15))
    return bcancer


def clean_data():
    global bcancer
    bcancer = bcancer.drop(['Unnamed: 32', 'id'], axis=1)   # deleting unnamed col and id because its not req
    bcancer['diagnosis'] = bcancer['diagnosis'].map({'M': 1, 'B': 0}) # mapping diagnosis values to 1 and 0
    print(bcancer.head())
    return bcancer


def create_model(data):
    X = data.drop(['diagnosis'], axis=1)    # return dataframe without dropped column, if inplace=True, returns None and modifies original df
    y = data['diagnosis']

    # scaling the data since values in diff cols vary like one is in 1000 and other is single digit
    scaler = StandardScaler()
    X = scaler.fit_transform(X) # except the diagnosis col we will scale every other col

    # split the data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # train
    model = LogisticRegression()
    model.fit(X_train, y_train) # training data using LR on X and y training data

    # predictions
    y_pred = model.predict(X_test)

    #accuracy
    print(f'accuracy: {accuracy_score(y_test, y_pred)}')  # we will test the score against the predicted value and y_test data
    print(f'Classification report: \n{classification_report(y_test, y_pred)}')
    return model, scaler


def main():
    get_data()
    data = clean_data()
    model, scaler = create_model(data)
    with open('model/model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('model/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)


if __name__ == "__main__":
    main()