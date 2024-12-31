import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def miles_to_km():
	miles = float(input.get())
	km = round(miles * 1.60934) # converts to a whole number
	result_label.config(text=f"{km}")

input = tk.Entry(width=10)
input.grid(column=1, row=0)

miles_label = tk.Label(text="Miles")
miles_label.grid(column=2, row=0)

equals_label = tk.Label(text="is equal to")
equals_label.grid(column=0, row=1)

result_label = tk.Label(text="")
result_label.grid(column=1, row=1)

km_label = tk.Label(text="Km")
km_label.grid(column=2, row=1)

button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)



window.mainloop()