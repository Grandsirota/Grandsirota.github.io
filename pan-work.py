import tkinter as tk
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Sample training data for 100+ League of Legends characters with 5 features:
# [Attack Damage, Armor, Movement Speed, Ability Power, Health]
# Labels could be 'fighter', 'mage', 'tank', etc.
train_data = np.array([
    [60, 30, 325, 0, 570], [65, 35, 340, 20, 620], [50, 20, 330, 50, 500], 
    [70, 40, 350, 10, 650], [55, 25, 345, 40, 600], [62, 32, 330, 5, 580], 
    [58, 28, 320, 45, 560], [66, 34, 355, 0, 630], [53, 22, 340, 60, 540], 
    [67, 37, 360, 15, 660], [54, 23, 345, 50, 570], [63, 33, 325, 20, 610], 
    [52, 21, 330, 60, 530], [68, 38, 350, 10, 670], [56, 26, 335, 40, 590], 
    # Add more data points (total > 100)
])

# Labels for the characters
train_labels = np.array([
    'fighter', 'tank', 'mage', 'tank', 'fighter', 'fighter', 
    'mage', 'tank', 'mage', 'tank', 'fighter', 'fighter', 
    'mage', 'tank', 'fighter', 
    # Add more labels (total > 100)
])

# KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_data, train_labels)

# Function to predict based on user input
def predict_body():
    attack_damage = int(attack_damage_entry.get())
    armor = int(armor_entry.get())
    movement_speed = int(movement_speed_entry.get())
    ability_power = int(ability_power_entry.get())
    health = int(health_entry.get())

    # Predict using the model
    prediction = knn.predict([[attack_damage, armor, movement_speed, ability_power, health]])
    result_label.config(text=f'Prediction: {prediction[0]}')

# Function to show training data
def show_training_data():
    for i, (data, label) in enumerate(zip(train_data, train_labels)):
        tree.insert("", "end", values=(data[0], data[1], data[2], data[3], data[4], label))

# Create main window
root = tk.Tk()
root.title("League of Legends Role Prediction")
root.geometry("1200x800")
root.configure(bg="#1C1C1C")  # Dark theme background

# Treeview for showing training data
tree = ttk.Treeview(root, columns=("Attack Damage", "Armor", "Movement Speed", "Ability Power", "Health", "Class"), show='headings', height=10)
tree.heading('Attack Damage', text='ATTACK DAMAGE')
tree.heading('Armor', text='ARMOR')
tree.heading('Movement Speed', text='MOVEMENT SPEED')
tree.heading('Ability Power', text='ABILITY POWER')
tree.heading('Health', text='HEALTH')
tree.heading('Class', text='CLASS')
tree.configure(style="Treeview")

# Styling for Treeview
style = ttk.Style()
style.configure("Treeview", background="#2A2A2A", foreground="white", fieldbackground="#2A2A2A")
style.configure("Treeview.Heading", background="#3C3C3C", foreground="white", font=("Arial", 12, "bold"))

tree.pack(padx=10, pady=10)

# Button to show training data
show_button = tk.Button(root, text="Show Training Data", command=show_training_data, font=("Arial", 12), bg="#3C3C3C", fg="white", relief="raised", borderwidth=2)
show_button.pack(pady=10)

# Frame for input fields
input_frame = tk.Frame(root, bg="#1C1C1C")
input_frame.pack(padx=10, pady=10)

# Input labels and fields
tk.Label(input_frame, text="ATTACK DAMAGE", bg="#1C1C1C", fg="white", font=("Arial", 12)).grid(row=0, column=0, pady=5)
tk.Label(input_frame, text="ARMOR", bg="#1C1C1C", fg="white", font=("Arial", 12)).grid(row=1, column=0, pady=5)
tk.Label(input_frame, text="MOVEMENT SPEED", bg="#1C1C1C", fg="white", font=("Arial", 12)).grid(row=2, column=0, pady=5)
tk.Label(input_frame, text="ABILITY POWER", bg="#1C1C1C", fg="white", font=("Arial", 12)).grid(row=3, column=0, pady=5)
tk.Label(input_frame, text="HEALTH", bg="#1C1C1C", fg="white", font=("Arial", 12)).grid(row=4, column=0, pady=5)

attack_damage_entry = tk.Entry(input_frame, font=("Arial", 12))
armor_entry = tk.Entry(input_frame, font=("Arial", 12))
movement_speed_entry = tk.Entry(input_frame, font=("Arial", 12))
ability_power_entry = tk.Entry(input_frame, font=("Arial", 12))
health_entry = tk.Entry(input_frame, font=("Arial", 12))

attack_damage_entry.grid(row=0, column=1, padx=10, pady=5)
armor_entry.grid(row=1, column=1, padx=10, pady=5)
movement_speed_entry.grid(row=2, column=1, padx=10, pady=5)
ability_power_entry.grid(row=3, column=1, padx=10, pady=5)
health_entry.grid(row=4, column=1, padx=10, pady=5)

# Button to predict
predict_button = tk.Button(root, text="Predict", command=predict_body, font=("Arial", 14), bg="#4A90E2", fg="white", relief="raised", borderwidth=2)
predict_button.pack(pady=10)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#1C1C1C", fg="white")
result_label.pack(pady=10)

# Run main loop
root.mainloop()
