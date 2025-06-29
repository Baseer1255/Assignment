import tkinter as tk
from PIL import Image, ImageTk

# Create main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x500")
root.configure(bg="lightblue")
root.resizable(False, False)
try:
    # Correct way to load image using raw string (no escape errors)
    img = Image.open(r"D:\Rainmeter\convert.png")
    img = img.resize((150, 150))
    logo = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=logo, bg="white")
    label.image = logo  # Keep reference to avoid garbage collection
    label.pack(pady=20)

except Exception as e:
    print("Image load failed:", e)
    tk.Label(root, text="Image not found", fg="red").pack(pady=20)


# ===== Currency Data =====
currencies = [
    "USD to INR", "USD to EUR", "USD to GBP", "USD to JPY",
    "USD to AUD", "USD to CAD", "USD to CHF", "USD to CNY",
    "USD to NZD", "USD to SEK", "USD to KRW", "USD to SGD",
    "USD to NOK", "USD to MXN", "USD to RUB", "USD to ZAR",
    "USD to TRY", "USD to AED", "USD to BRL", "USD to ARS",
    "USD to CLP", "USD to COP", "USD to PHP", "USD to MYR",
    "USD to IDR", "USD to THB", "USD to VND", "USD to PKR",
    "USD to BDT", "USD to LKR", "USD to EGP", "USD to MAD",
    "USD to DZD", "USD to TND", "USD to QAR", "USD to KWD",
    "USD to OMR", "USD to SAR", "USD to JOD", "USD to BHD",
    "USD to KZT", "USD to UAH", "USD to BYN", "USD to AZN",
    "USD to GEL", "USD to MDL", "USD to RON", "USD to HUF",
    "USD to CZK", "USD to PLN", "USD to ILS"
]

rates = [
    82.74, 0.93, 0.82, 110.57, 1.35, 1.25, 0.92, 6.45, 1.50,
    10.30, 1182.00, 1.36, 9.50, 20.00, 75.00, 14.50, 18.00, 3.67,
    5.20, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
    0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01
]

# ===== Currency Dropdown =====
tk.Label(root, text="Select Currency", bg="lightblue", font=("Arial", 12)).pack(pady=5)
selected_currency = tk.StringVar()
selected_currency.set(currencies[0])
dropdown = tk.OptionMenu(root, selected_currency, *currencies)
dropdown.pack(pady=5)

# ===== Amount Entry =====
tk.Label(root, text="Enter amount in USD:", bg="lightblue", font=("Arial", 12)).pack(pady=5)
amount_entry = tk.Entry(root)
amount_entry.pack(pady=5)

# ===== Result Display =====
result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 12))
result_label.pack(pady=10)

# ===== Conversion Function =====
def perform_conversion():
    try:
        amount = float(amount_entry.get())
        index = currencies.index(selected_currency.get())
        rate = rates[index]
        converted = amount * rate
        result_label.config(text=f"Converted Amount: {converted:.2f}")
    except:
        result_label.config(text="Please enter a valid number.")

# ===== Convert Button =====
convert_button = tk.Button(root, text="Convert", command=perform_conversion)
convert_button.pack(pady=10)
convert_button.config(bg="lightgreen", font=("Arial", 12))
convert_button.bind("<Enter>", lambda e: convert_button.config(bg="green"))
convert_button.bind("<Leave>", lambda e: convert_button.config(bg="lightgreen"))
root.bind("<Return>", lambda e: perform_conversion())

# ===== Live Input Validation =====
def validate_input(*args):
    value = amount_entry.get()
    try:
        float(value)
        result_label.config(text="")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

amount_entry.bind("<KeyRelease>", validate_input)

# ===== Run the App =====
root.mainloop()

