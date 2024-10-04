import tkinter as tk
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd

# Load Genshin Impact Characters Dataset
dataset_path = "path_to_your_dataset/genshin_impact_characters.csv"
data = pd.read_csv(dataset_path)

# Extract useful columns from dataset (assuming you have columns like 'Sex', 'Age', 'Weight', 'Height')
# Modify the column names according to the actual dataset
train_data = data[['Sex', 'Age', 'Weight', 'Height']].values
train_labels = data['BodyType'].values  # Assuming 'BodyType' is the label, modify according to the dataset

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_data, train_labels)

# Prediction function
def predict_body():
    sex = int(sex_entry.get())
    age = int(age_entry.get())
    weight = int(weight_entry.get())
    height = int(height_entry.get())

    # Use user input to make a prediction
    prediction = knn.predict([[sex, age, weight, height]])
    result_label.config(text=prediction[0])

# Show training data in Treeview
def show_training_data():
    for i, (data_row, label) in enumerate(zip(train_data, train_labels)):
        tree.insert("", "end", values=(data_row[0], data_row[1], data_row[2], data_row[3], label))

# Create the main window
root = tk.Tk()
root.title("KNN APP")
root.geometry("1200x800")
root.configure(bg="#D0D6F0")

# Treeview for displaying training data
tree = ttk.Treeview(root, columns=("Sex", "Age", "Weight", "Height", "Body"), show='headings', height=10)
tree.heading('Sex', text='SEX')
tree.heading('Age', text='AGE')
tree.heading('Weight', text='WEIGHT')
tree.heading('Height', text='HEIGHT')
tree.heading('Body', text='BODY')
tree.pack(padx=10, pady=10)

# Button to show training data
show_button = tk.Button(root, text="Show Training Data", command=show_training_data, font=("Arial", 12), bg="#ACB6E5")
show_button.pack(pady=10)

# Input fields for user data
input_frame = tk.Frame(root, bg="#D0D6F0")
input_frame.pack(padx=10, pady=10)

tk.Label(input_frame, text="SEX", bg="#D0D6F0", font=("Arial", 12)).grid(row=0, column=0, pady=5)
tk.Label(input_frame, text="AGE", bg="#D0D6F0", font=("Arial", 12)).grid(row=1, column=0, pady=5)
tk.Label(input_frame, text="WEIGHT", bg="#D0D6F0", font=("Arial", 12)).grid(row=2, column=0, pady=5)
tk.Label(input_frame, text="HEIGHT", bg="#D0D6F0", font=("Arial", 12)).grid(row=3, column=0, pady=5)

sex_entry = tk.Entry(input_frame, font=("Arial", 12))
age_entry = tk.Entry(input_frame, font=("Arial", 12))
weight_entry = tk.Entry(input_frame, font=("Arial", 12))
height_entry = tk.Entry(input_frame, font=("Arial", 12))

sex_entry.grid(row=0, column=1, padx=10, pady=5)
age_entry.grid(row=1, column=1, padx=10, pady=5)
weight_entry.grid(row=2, column=1, padx=10, pady=5)
height_entry.grid(row=3, column=1, padx=10, pady=5)

# Predict button
predict_button = tk.Button(root, text="Predict", command=predict_body, font=("Arial", 14), bg="#98FB98", fg="black", relief="raised")
predict_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#D0D6F0", fg="black")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
