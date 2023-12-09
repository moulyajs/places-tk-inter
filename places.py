import tkinter as tk
from tkinter import ttk


class TravelApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Travel and Tourism Management System")

        # Sample data for places to visit
        self.places_data = [
            {"name": "Paris", "description": "City of Love", "rating": 5},
            {"name": "Tokyo", "description": "Vibrant Metropolis", "rating": 4},
            {"name": "New York", "description": "The Big Apple", "rating": 4.5},
            # Add more places as needed
        ]

        # Create and set up the GUI
        self.create_widgets()

    def create_widgets(self):
        # Label to display the title
        title_label = tk.Label(
            self.root, text="Places to Visit", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=10)

        # Treeview widget to display places data
        columns = ("Name", "Description", "Rating")
        self.tree = ttk.Treeview(
            self.root, columns=columns, show="headings", height=10)

        # Set column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100, anchor="center")

        # Insert data into the treeview
        for place in self.places_data:
            self.tree.insert("", "end", values=(
                place["name"], place["description"], place["rating"]))

        # Pack the treeview
        self.tree.pack(padx=20, pady=10)

        # Button to view more details
        view_button = tk.Button(
            self.root, text="View Details", command=self.view_details)
        view_button.pack(pady=10)

    def view_details(self):
        # Get the selected item from the treeview
        selected_item = self.tree.selection()

        if not selected_item:
            tk.messagebox.showwarning(
                "No Selection", "Please select a place to view details.")
            return

        # Retrieve data from the selected item
        item = self.tree.item(selected_item, "values")
        name, description, rating = item[0], item[1], item[2]

        # Display a messagebox with details
        details_message = f"Name: {name}\nDescription: {description}\nRating: {rating}"
        tk.messagebox.showinfo("Place Details", details_message)


if __name__ == "__main__":
    root = tk.Tk()
    app = TravelApp(root)
    root.mainloop()
