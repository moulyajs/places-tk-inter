from tkinter import *
from PIL import Image, ImageTk

def FOODS():
    def display_foods(city):
        city_foods = {
            "Bangalore": [
                "Masala Dosa", "Idli Vada", "Bisi Bele Bath", "Ragi Mudde", "Mysore Pak",
                "Puliyogare", "Ragi Dosa", "Obbattu/Holige", "Akki Roti", "Kesari Bath"
            ],
            "Kolkata": [
                "Kathi Roll", "Macher Jhol", "Rosogolla", "Phuchka", "Mishti Doi",
                "Chingri Macher Malai Curry", "Sondesh", "Macher Chop", "Aloo Posto"
            ],
            "Delhi": [
                "Chole Bhature", "Butter Chicken", "Aloo Chaat", "Paranthas", "Dahi Bhalla",
                "Kebabs", "Rajma Chawal", "Nihari", "Samosa", "Kulfi"
            ],
            "Kochi": [
                "Appam with Stew", "Malabar Parotta with Kerala Beef Fry", "Karimeen Pollichathu",
                "Puttu and Kadala Curry", "Fish Molee", "Thalassery Biryani", "Kappa and Meen Curry",
                "Erachi Varutharacha Curry", "Idiyappam with Egg Curry", "Ada Pradhaman"
            ],
            "Chennai": [
                "Dosa", "Idli Sambar", "Chettinad Chicken", "Pongal", "Filter Coffee",
                "Masala Vada", "Kothu Parotta", "Upma", "Nelloor Biryani", "Murukku"
            ]
        }

        foods = city_foods.get(city, [])
        food_list = "\n".join(foods)
        display[city]["label"].config(text=food_list)

    root = Tk()
    root.title("Best Foods in Cities")
    root.geometry("700x400")  # Adjusted window size for better layout
    root.configure(bg="beige")  # Background color

    # Updated city_info with image paths and position for food display
    city_info = {
        "Bangalore": {"position": (0, 0), "image": "blr.png.", "food_col": 3},
        "Kolkata": {"position": (0, 1), "image": "kol.jpg", "food_col": 3},
        "Delhi": {"position": (0, 2), "image": "delhi.jpg", "food_col": 3},
        "Kochi": {"position": (0, 3), "image": "kochi.jpeg", "food_col": 3},
        "Chennai": {"position": (0, 4), "image": "chennai.jpg", "food_col":3}
    }

    cities = ["Bangalore", "Kolkata", "Delhi", "Kochi", "Chennai"]
    selected_city = StringVar(root)
    selected_city.set("Choose the city")


    display = {}
    for city in cities:
        info = city_info[city]
        row, col = info["position"]

        # Load and resize images
        img = Image.open(info["image"])
        img = img.resize((100, 100))
        img = ImageTk.PhotoImage(img)

        # Create a label to display the image
        img_label = Label(root, image=img)
        img_label.image = img
        img_label.grid(row=row, column=col)  # Image on top

        # Button for city name
        button = Button(root, text=city, compound=TOP, command=lambda c=city: city_button_click(c))
        button.config(bg="#FFD700", fg="brown", font=("Arial", 10), width=7, height=1)
        button.grid(row=row+1, column=col)  # Button below the image

        # Display label for food items
        food_display = Label(root, text="", justify="right", bg="beige", font=("Arial", 10))
        food_display.grid(row=info["food_col"], column=col, padx=10, pady=10)  # Food items on the side

        # Store each city's display label in the dictionary
        display[city] = {"label": food_display}

    # Updated function to handle city button clicks
    def city_button_click(city_name):
        selected_city.set(city_name)
        display_foods(city_name)

    root.mainloop()

FOODS()  # Calling the function to execute the code
