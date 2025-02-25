import os
import csv
import tkinter as tk
from tkinter import ttk

FILE_NAME = "RegisteredUsers.txt"

class User:
    def __init__(self, name, user_id, phone, email):
        self.name = name
        self.user_id = user_id
        self.phone = phone
        self.email = email

    def to_list(self):
        return [self.name, self.user_id, self.phone, self.email]


class FileHandler:

    @staticmethod
    def read_users():
        users = []
        if not os.path.exists(FILE_NAME):
            return users

        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.reader(file, delimiter="-")
            for row in reader:
                if len(row) == 4:
                    users.append(User(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip()))
        return users

    @staticmethod
    def write_users(users):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file, delimiter="-")
            for user in users:
                writer.writerow(user.to_list())


class UserManager:

    @staticmethod
    def is_numeric(value):
        return value.isdigit()

    @staticmethod
    def is_valid_email(email):
        return "@" in email and email.endswith(".com")

    @staticmethod
    def create_user(new_user):
        users = FileHandler.read_users()

        if not UserManager.is_numeric(new_user.user_id):
            return "Error: ID must contain only numbers."
        if not UserManager.is_numeric(new_user.phone):
            return "Error: Phone Number must contain only numbers."
        if not UserManager.is_valid_email(new_user.email):
            return "Error: Invalid email format. Email must contain '@' and end with '.com'."

        for user in users:
            if user.user_id == new_user.user_id:
                return "Error: ID already exists."

        users.append(new_user)
        FileHandler.write_users(users)
        return "User created successfully."

    @staticmethod
    def read_users():
        return FileHandler.read_users()

    @staticmethod
    def update_user(updated_user):
        users = FileHandler.read_users()
        found = False

        for i in range(len(users)):
            if users[i].user_id == updated_user.user_id:
                users[i] = updated_user
                found = True
                break

        if found:
            FileHandler.write_users(users)
            return "User updated successfully."
        else:
            return "Error: User ID not found."

    @staticmethod
    def clear_users():
        FileHandler.write_users([])
        return "All users have been deleted."


class UserWindow(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("User Management")
        self.geometry("600x450")

        tk.Label(self, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self, text="ID:").grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.id_entry = tk.Entry(self, width=30)
        self.id_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self, text="Phone Number:").grid(row=2, column=0, padx=10, pady=5, sticky="w")
        self.phone_entry = tk.Entry(self, width=30)
        self.phone_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(self, text="Email:").grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.email_entry = tk.Entry(self, width=30)
        self.email_entry.grid(row=3, column=1, padx=10, pady=5)

        self.output_area = tk.Text(self, height=10, width=60)
        self.output_area.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        tk.Button(self, text="Create", command=self.create_user).grid(row=5, column=0, padx=10, pady=5)
        tk.Button(self, text="Read", command=self.read_users).grid(row=5, column=1, padx=10, pady=5)
        tk.Button(self, text="Update", command=self.update_user).grid(row=6, column=0, padx=10, pady=5)
        tk.Button(self, text="Delete All", command=self.delete_all_users).grid(row=6, column=1, padx=10, pady=5)
        tk.Button(self, text="Search by ID", command=self.search_user_by_id).grid(row=7, column=0, padx=10, pady=5)
        tk.Button(self, text="Clear Fields", command=self.clear_fields).grid(row=7, column=1, padx=10, pady=5)

    def show_large_message(self, title, message):
        """Muestra una ventana emergente más grande con un diseño mejorado."""
        popup = tk.Toplevel(self)
        popup.title(title)
        popup.geometry("400x200")  # Tamaño más grande

        frame = ttk.Frame(popup, padding=20)
        frame.pack(fill="both", expand=True)

        label = ttk.Label(frame, text=message, font=("Arial", 12), wraplength=350, justify="center")
        label.pack(pady=20)

        close_button = ttk.Button(frame, text="Aceptar", command=popup.destroy)
        close_button.pack(pady=10)

        popup.transient(self)
        popup.grab_set()

    def create_user(self):
        user = User(self.name_entry.get(), self.id_entry.get(), self.phone_entry.get(), self.email_entry.get())
        result = UserManager.create_user(user)
        self.show_large_message("Create User", result)

    def read_users(self):
        users = UserManager.read_users()
        self.output_area.delete("1.0", tk.END)
        if users:
            for user in users:
                self.output_area.insert(tk.END, f"Name: {user.name}\nID: {user.user_id}\nPhone: {user.phone}\nEmail: {user.email}\n\n")
        else:
            self.output_area.insert(tk.END, "No users found.")

    def update_user(self):
        user = User(self.name_entry.get(), self.id_entry.get(), self.phone_entry.get(), self.email_entry.get())
        result = UserManager.update_user(user)
        self.show_large_message("Update User", result)

    def delete_all_users(self):
        result = UserManager.clear_users()
        self.show_large_message("Delete Users", result)

    def search_user_by_id(self):
        user_id = self.id_entry.get().strip()
        if not user_id:
            self.show_large_message("Search Error", "Please enter an ID to search.")
            return

        users = UserManager.read_users()
        for user in users:
            if user.user_id == user_id:
                self.output_area.delete("1.0", tk.END)
                self.output_area.insert(tk.END, f"User Found:\nName: {user.name}\nID: {user.user_id}\nPhone: {user.phone}\nEmail: {user.email}")
                return

        self.show_large_message("Search Result", "User not found.")

    def clear_fields(self):
        self.name_entry.delete(0, tk.END)
        self.id_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.output_area.delete("1.0", tk.END)
        self.show_large_message("Clear Fields", "Fields cleared.")


if __name__ == "__main__":
    app = UserWindow()
    app.mainloop()
