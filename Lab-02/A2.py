import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

def data(file_path):
    df = pd.read_excel(file_path, sheet_name="Purchase data")
    return df

def create_matrices(df):
    X = df[["Candies (#)", "Mangoes (Kg)", "Milk Packets (#)"]]
    y = df["Payment (Rs)"].apply( lambda payment: "RICH" if payment > 200 else "POOR" )

    return X,y
    
def train_classifier(X, y):
    classifier = KNeighborsClassifier(n_neighbors=3)
    classifier.fit(X, y)
    return classifier


file_path = "lab2data.xlsx"
df = data(file_path)
X, y = create_matrices(df)
classifier = train_classifier(X, y)

predictions = classifier.predict(X)

print("Predicted Classes:")
print(predictions)