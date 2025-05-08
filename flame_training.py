import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.model_selection import train_test_split


df = pd.read_csv("flame_data.csv")  
X = df[["flame_val"]]
y = df["label"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


print(" Accuracy:", accuracy_score(y_test, y_pred))
print("\n Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\n Classification Report:\n", classification_report(y_test, y_pred))


weight = model.coef_[0][0]
bias = model.intercept_[0]

print(f"\n Use in Arduino:\nfloat weight = {weight:.6f}f;")
print(f"float bias = {bias:.6f}f;")


with open("arduino_model_params.txt", "w") as f:
    f.write(f"float weight = {weight:.6f}f;\n")
    f.write(f"float bias = {bias:.6f}f;\n")
