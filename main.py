import tkinter as tk


def calculate_bmi():
    name = name_entry.get().strip().lower()
    height_text = height_entry.get()
    weight_text = weight_entry.get()
    height_unit = height_unit_var.get()
    weight_unit = weight_unit_var.get()

    try:
        height = float(height_text)
        weight = float(weight_text)
    except ValueError:
        result_label.config(text="Bruv you good? We want numbers, not letters, you silly.")
        return

    if height_unit == "Centimeters":
        height /= 100  # Convert centimeters to meters
    elif height_unit == "Inches":
        height *= 0.0254  # Convert inches to meters

    if weight_unit == "Pounds":
        weight *= 0.453592  # Convert pounds to kilograms

    bmi = weight / (height ** 2)
    result_label.config(text=f"{name.capitalize()}'s BMI is {bmi:.2f}")

    # Check for the Easter egg
    if name in ["muyin", "muyinjon"]:
        result_label.config(text=f"{name.capitalize()}'s BMI is {bmi:.2f}.\nYou are the GOAT")
    else:
        result_label.config(text=f"{name.capitalize()}'s BMI is {bmi:.2f}")


# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Name Entry
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Height Entry
height_label = tk.Label(root, text="Height:")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# Height Unit Dropdown
height_unit_var = tk.StringVar(root)
height_unit_var.set("Meters")
height_unit_label = tk.Label(root, text="Height Unit:")
height_unit_label.pack()
height_unit_dropdown = tk.OptionMenu(root, height_unit_var, "Meters", "Centimeters", "Inches")
height_unit_dropdown.pack()

# Weight Entry
weight_label = tk.Label(root, text="Weight:")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# Weight Unit Dropdown
weight_unit_var = tk.StringVar(root)
weight_unit_var.set("Kilograms")
weight_unit_label = tk.Label(root, text="Weight Unit:")
weight_unit_label.pack()
weight_unit_dropdown = tk.OptionMenu(root, weight_unit_var, "Kilograms", "Pounds")
weight_unit_dropdown.pack()

# Calculate Button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack()

# Start the GUI main loop
root.mainloop()
