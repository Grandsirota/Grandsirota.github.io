import tkinter as tk
from tkinter import ttk
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

train_data = np.array([
    [1, 27, 60, 170], [1, 18, 70, 180], [0, 19, 64, 174], [1, 40, 56, 172], [0, 32, 45, 156],
    [1, 24, 52, 170], [0, 25, 45, 160], [1, 20, 120, 165], [0, 27, 50, 155], [1, 30, 55, 168],
    [0, 35, 58, 165], [1, 22, 80, 175], [1, 29, 77, 170], [0, 41, 46, 160], [1, 38, 100, 180],
    [0, 28, 70, 164], [1, 33, 65, 170], [0, 24, 49, 150], [1, 26, 85, 185], [0, 29, 62, 158],
    [1, 34, 90, 172], [0, 23, 55, 165], [1, 31, 58, 175], [0, 37, 72, 160], [1, 21, 75, 178],
    [0, 26, 67, 164], [1, 29, 80, 170], [0, 32, 64, 156], [1, 27, 85, 174], [0, 36, 45, 162],
    [1, 24, 60, 169], [0, 31, 55, 160], [1, 35, 88, 175], [0, 23, 62, 154], [1, 39, 92, 172],
    [0, 28, 49, 150], [1, 26, 82, 180], [0, 33, 70, 158], [1, 30, 87, 170], [0, 27, 60, 156],
    [1, 34, 72, 176], [0, 25, 50, 152], [1, 32, 90, 178], [0, 21, 55, 154], [1, 36, 88, 180],
    [0, 29, 64, 160], [1, 37, 92, 174], [0, 30, 50, 150], [1, 22, 75, 170], [0, 26, 53, 160],
    [1, 33, 85, 176], [0, 35, 62, 158], [1, 38, 95, 180], [0, 28, 65, 152], [1, 27, 70, 168],
    [0, 24, 49, 155], [1, 40, 100, 185], [0, 32, 55, 162], [1, 23, 72, 170], [0, 31, 58, 160],
    [1, 25, 80, 178], [0, 29, 64, 150], [1, 28, 77, 175], [0, 30, 50, 160], [1, 26, 85, 180],
    [0, 33, 48, 154], [1, 37, 90, 172], [0, 34, 60, 158], [1, 39, 95, 175], [0, 27, 56, 152],
    [1, 31, 82, 170], [0, 29, 68, 160], [1, 36, 78, 180], [0, 35, 53, 155], [1, 22, 85, 178],
    [0, 24, 60, 162], [1, 32, 88, 176], [0, 26, 49, 150], [1, 34, 92, 172], [0, 28, 55, 158],
    [1, 25, 80, 175], [0, 30, 60, 156], [1, 21, 78, 180], [0, 27, 54, 150], [1, 33, 85, 178],
    [0, 32, 62, 164], [1, 31, 90, 170], [0, 36, 58, 160], [1, 29, 80, 175], [0, 26, 55, 152],
    [1, 38, 92, 180], [0, 34, 66, 158], [1, 30, 88, 174], [0, 25, 50, 154], [1, 37, 95, 176],
    [0, 33, 52, 150], [0, 22, 75, 168], [1, 26, 55, 169], [1, 32, 95, 180], [1, 27, 59, 170]
])


train_labels = np.array([
    'slim', 'fat', 'fat', 'slim', 'thin', 'thin', 'thin', 'fat', 'slim', 'slim',
    'fat', 'slim', 'slim', 'thin', 'fat', 'slim', 'slim', 'thin', 'fat', 'thin',
    'slim', 'thin', 'slim', 'thin', 'fat', 'thin', 'slim', 'fat', 'thin', 'slim',
    'slim', 'thin', 'fat', 'thin', 'fat', 'thin', 'fat', 'slim', 'thin', 'slim',
    'fat', 'thin', 'fat', 'thin', 'fat', 'slim', 'fat', 'slim', 'thin', 'fat',
    'slim', 'thin', 'slim', 'slim', 'thin', 'fat', 'slim', 'thin', 'fat', 'slim',
    'thin', 'fat', 'slim', 'thin', 'slim', 'fat', 'thin', 'slim', 'fat', 'thin',
    'fat', 'slim', 'thin', 'fat', 'slim', 'slim', 'thin', 'fat', 'slim', 'thin',
    'fat', 'thin', 'slim', 'thin', 'slim', 'fat', 'slim', 'slim', 'fat', 'thin',
    'fat', 'slim', 'thin', 'fat', 'slim', 'thin', 'slim', 'slim', 'fat', 'thin'
])


# สร้าง KNN Model
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(train_data, train_labels)

# ฟังก์ชันสำหรับการทำนาย
def predict_body():
    sex = int(sex_entry.get())
    age = int(age_entry.get())
    weight = int(weight_entry.get())
    height = int(height_entry.get())

    # นำข้อมูลที่ผู้ใช้ป้อนเข้าไปทำนาย
    prediction = knn.predict([[sex, age, weight, height]])
    result_label.config(text=prediction[0])

# ฟังก์ชันสำหรับแสดงข้อมูลที่ใช้ฝึกฝน
def show_training_data():
    for i, (data, label) in enumerate(zip(train_data, train_labels)):
        tree.insert("", "end", values=(data[0], data[1], data[2], data[3], label))

# สร้างหน้าจอหลัก
root = tk.Tk()
root.title("KNN APP")
root.geometry("1200x800")
root.configure(bg="#D0D6F0") 

tree = ttk.Treeview(root, columns=("Sex", "Age", "Weight", "Height", "Body"), show='headings', height=10)
tree.heading('Sex', text='SEX')
tree.heading('Age', text='AGE')
tree.heading('Weight', text='WEIGHT')
tree.heading('Height', text='HEIGHT')
tree.heading('Body', text='BODY')

tree.pack(padx=10, pady=10)

# ปุ่มสำหรับแสดงข้อมูลการฝึกฝน
show_button = tk.Button(root, text="Show Training Data", command=show_training_data, font=("Arial", 12), bg="#ACB6E5")
show_button.pack(pady=10)

# ส่วนของการนำเข้าข้อมูล
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

# ปุ่ม Predict
predict_button = tk.Button(root, text="Predict", command=predict_body, font=("Arial", 14), bg="#98FB98", fg="black", relief="raised")
predict_button.pack(pady=10)

# ผลลัพธ์ของการทำนาย
result_label = tk.Label(root, text="", font=("Arial", 16), bg="#D0D6F0", fg="black")
result_label.pack(pady=10)

# รันโปรแกรมหลัก
root.mainloop()