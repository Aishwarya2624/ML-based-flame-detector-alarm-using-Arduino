import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Load your real dataset
df = pd.read_csv("flame_data.csv")   # ← change to the correct path

# 2. Prepare features and labels
X = df[["flame_val"]]
y = df["label"]

# 3. Train the logistic regression model
model = LogisticRegression()
model.fit(X, y)

# 4. Generate a smooth range of sensor values for plotting
x_vals = np.linspace(df["flame_val"].min(),
                     df["flame_val"].max(), 300).reshape(-1, 1)

# 5. Compute predicted probabilities for those values
y_prob = model.predict_proba(x_vals)[:, 1]

# 6. Plot data and logistic curve
plt.figure(figsize=(6, 4))
plt.scatter(df["flame_val"], df["label"], edgecolor='k', label="Data points")
plt.plot(x_vals, y_prob, linewidth=2, label="Logistic fit")
plt.xlabel("Flame Sensor Value (raw ADC)")
plt.ylabel("Predicted Probability of Flame")
plt.title("Logistic Regression on Your Flame Data")
plt.legend()
plt.grid(True)
plt.show()
