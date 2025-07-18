import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_maturity_date():
    selected_date = cal.get_date()
    maturity_date = selected_date + relativedelta(months=3)
    result_label.config(text=f"Maturity Date: {maturity_date.strftime('%Y-%m-%d')}")

# Create main window
root = tk.Tk()
root.title("Maturity Date Calculator")
root.geometry("300x200")

# Calendar label and control
ttk.Label(root, text="Select Start Date:").pack(pady=5)
cal = DateEntry(root, width=12, background='darkblue',
                foreground='white', borderwidth=2, date_pattern='y-mm-dd')
cal.pack(pady=5)

# Button to trigger calculation
calc_btn = ttk.Button(root, text="Calculate Maturity Date", command=calculate_maturity_date)
calc_btn.pack(pady=10)

# Label to show result
result_label = ttk.Label(root, text="Maturity Date: ")
result_label.pack(pady=10)

# Start the event loop
root.mainloop()
