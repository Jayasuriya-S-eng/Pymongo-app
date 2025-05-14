import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import webbrowser
import pymongo

# Initialize Tkinter window
root = tk.Tk()
root.title("JAYASURIYA.S")
root.state("zoomed")  # Maximize the window
root.configure(bg="white")

# MongoDB Connection
try:
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["UserDB"]
    collection = db["users"]
    messagebox.showinfo("Success", "Connected to MongoDB Database!")
except pymongo.errors.ConnectionFailure as e:
    messagebox.showerror("Error", f"Database connection failed: {e}")

# Function to load and resize image
def load_image(path, width, height):
    img = Image.open(path)
    img = img.resize((width, height))
    return ImageTk.PhotoImage(img.copy())  # Avoid garbage collection issues

# Insert data into MongoDB
def insert():
    data = {
        "Name": tb1.get(),
        "Gender": tb2.get(),
        "D_O_B": tb3.get(),
        "Father_name": tb4.get(),
        "Phone_no": tb5.get(),
        "Sslc": tb6.get(),
        "Hall_ticket_no": tb7.get(),
        "Hsc": tb8.get(),
        "Cutoff": tb9.get(),
        "College_name": tb10.get(),
    }
    
    if all(data.values()):
        collection.insert_one(data)
        messagebox.showinfo("Success", "Data saved to MongoDB!")
        clear()  # Optional: clear after insert
    else:
        messagebox.showerror("Error", "Please enter all details")

# Clear all fields
def clear():
    for tb in entries:
        tb.delete(0, "end")

# Exit application
def cancel():
    root.destroy()

# Frame for form
frame1 = tk.Frame(root, bg="white")
frame1.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.75)

# Frame for image
frame2 = tk.Frame(root, bg="white")
frame2.place(relx=0.4, rely=0.02, relwidth=0.4, relheight=0.2)

# Load and display image
bg2_img = load_image("tnea-2022.jpg", 400, 220)  # Make sure this image exists
bgp2 = tk.Label(frame2, image=bg2_img, bd=0)
bgp2.image = bg2_img
bgp2.place(relx=0, rely=0)

# Labels and textboxes
labels = [
    ("Name", 0.01, 0.1), ("Gender", 0.01, 0.2), ("D_O_B", 0.01, 0.3),
    ("Father_name", 0.01, 0.4), ("Phone_no", 0.01, 0.5), ("Sslc", 0.50, 0.1),
    ("Hall_ticket_no", 0.50, 0.2), ("Hsc", 0.50, 0.3), ("Cutoff", 0.50, 0.4),
    ("College_name", 0.50, 0.5)
]

entries = []

for text, x, y in labels:
    tk.Label(frame1, text=text, font=("Dubai", 20), fg="black", bg="white").place(relx=x, rely=y)
    tb = tk.Entry(frame1, font=("Times New Roman", 20, "italic"), fg="black", bg="white")
    tb.place(relx=x + 0.19, rely=y)
    entries.append(tb)

# Assigning entries for use in `insert` function
tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, tb9, tb10 = entries

# Buttons
tk.Button(frame1, text="Submit", font=("Arial", 25), bg="skyblue", command=insert).place(relx=0.1, rely=0.8)
tk.Button(frame1, text="Clear", font=("Arial", 25), bg="skyblue", command=clear).place(relx=0.3, rely=0.8)
tk.Button(frame1, text="Exit", font=("Arial", 25), bg="skyblue", command=cancel).place(relx=0.5, rely=0.8)

# Web links
frame4 = tk.Frame(root, bg="white")
frame4.place(relx=0.83, rely=0.78, relwidth=0.15, relheight=0.2)

links = [
    ("TNEA>>>", "https://www.tneaonline.org", 0.0, 0.1),
    ("Rank list>>>", "https://www.bgsbuniversity.org", 0.0, 0.4),
    ("Topcolleges>>>", "https://engineering.careers360.com", 0.0, 0.7)
]

for text, url, x, y in links:
    lbl = tk.Label(frame4, text=text, font=("Arial", 20, "underline"), fg="blue", cursor="hand2", bg="white")
    lbl.place(relx=x, rely=y)
    lbl.bind("<Button-1>", lambda e, url=url: webbrowser.open_new(url))

# Run the app
root.mainloop()
