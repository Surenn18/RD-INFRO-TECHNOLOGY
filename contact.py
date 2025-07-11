import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store contacts
FILENAME = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return {}

# Save contacts to file
def save_contacts():
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

# Add or Update contact
def save_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if not name or not phone:
        messagebox.showwarning("Missing Info", "Name and Phone are required.")
        return

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address
    }
    save_contacts()
    messagebox.showinfo("Success", "Contact saved successfully!")
    clear_entries()
    refresh_listbox()

# Display selected contact
def view_contact(event):
    selected = contact_listbox.curselection()
    if selected:
        name = contact_listbox.get(selected[0])
        contact = contacts.get(name)
        name_entry.delete(0, tk.END)
        name_entry.insert(0, name)
        phone_entry.delete(0, tk.END)
        phone_entry.insert(0, contact["phone"])
        email_entry.delete(0, tk.END)
        email_entry.insert(0, contact["email"])
        address_entry.delete(0, tk.END)
        address_entry.insert(0, contact["address"])

# Delete contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        confirm = messagebox.askyesno("Confirm", f"Delete contact: {name}?")
        if confirm:
            contacts.pop(name)
            save_contacts()
            clear_entries()
            refresh_listbox()
    else:
        messagebox.showerror("Not Found", "Contact not found.")

# Search contact
def search_contact():
    query = search_entry.get().lower()
    contact_listbox.delete(0, tk.END)
    for name in contacts:
        if query in name.lower() or query in contacts[name]["phone"]:
            contact_listbox.insert(tk.END, name)

# Clear entries
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Refresh listbox
def refresh_listbox():
    contact_listbox.delete(0, tk.END)
    for name in sorted(contacts):
        contact_listbox.insert(tk.END, name)

# Main Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("500x450")
root.configure(bg="lightyellow")

contacts = load_contacts()

# Labels and Entries
tk.Label(root, text="Name:", bg="lightyellow").place(x=20, y=20)
name_entry = tk.Entry(root, width=40)
name_entry.place(x=100, y=20)

tk.Label(root, text="Phone:", bg="lightyellow").place(x=20, y=60)
phone_entry = tk.Entry(root, width=40)
phone_entry.place(x=100, y=60)

tk.Label(root, text="Email:", bg="lightyellow").place(x=20, y=100)
email_entry = tk.Entry(root, width=40)
email_entry.place(x=100, y=100)

tk.Label(root, text="Address:", bg="lightyellow").place(x=20, y=140)
address_entry = tk.Entry(root, width=40)
address_entry.place(x=100, y=140)

# Buttons
tk.Button(root, text="Save Contact", command=save_contact, width=15, bg="lightgreen").place(x=100, y=180)
tk.Button(root, text="Delete Contact", command=delete_contact, width=15, bg="red").place(x=250, y=180)

# Search Bar
tk.Label(root, text="Search:", bg="lightyellow").place(x=20, y=230)
search_entry = tk.Entry(root, width=25)
search_entry.place(x=100, y=230)
tk.Button(root, text="Search", command=search_contact, width=10).place(x=300, y=226)

# Contact Listbox
contact_listbox = tk.Listbox(root, width=50)
contact_listbox.place(x=100, y=270)
contact_listbox.bind("<<ListboxSelect>>", view_contact)

refresh_listbox()

root.mainloop()
