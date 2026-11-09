import pandas as pd
import joblib
from pathlib import Path
from urllib.request import urlretrieve
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
DATA = Path("wine_quality.csv")
MODEL = Path("wine_model.pkl")

def main():
    if not DATA.exists():
        print("Downloading UCI red wine dataset...")
        urlretrieve(URL, DATA)
    df = pd.read_csv(DATA, sep=";")
    df["quality_category"] = (df["quality"] >= 6).map(
        {True: "GOOD QUALITY", False: "NEEDS IMPROVEMENT"})
    X = df.drop(columns=["quality", "quality_category"])  # quality is target only
    y = df["quality_category"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y)
    model = Pipeline([
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(
            n_estimators=150, random_state=42, class_weight="balanced"))
    ])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    print("Accuracy:", round(accuracy_score(y_test, pred), 4))
    print("Confusion matrix:\\n", confusion_matrix(y_test, pred))
    print("Classification report:\\n", classification_report(y_test, pred))
    joblib.dump(model, MODEL)
    print("Saved model:", MODEL)

if __name__ == "__main__":
    main()
