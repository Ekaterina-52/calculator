import tkinter as tk

def convert_temperature():
    try:
        input_value = float(entry_input.get())
        from_unit = var_from.get()
        to_unit = var_to.get()

        if from_unit == to_unit:
            result = input_value
        elif from_unit == "Цельсий":
            if to_unit == "Фаренгейт":
                result = (input_value * 9/5) + 32
            elif to_unit == "Кельвин":
                result = input_value + 273.15
        elif from_unit == "Фаренгейт":
            if to_unit == "Цельсий":
                result = (input_value - 32) * 5/9
            elif to_unit == "Кельвин":
                result = (input_value - 32) * 5/9 + 273.15
        elif from_unit == "Кельвин":
            if to_unit == "Цельсий":
                result = input_value - 273.15
            elif to_unit == "Фаренгейт":
                result = (input_value - 273.15) * 9/5 + 32

        label_result.config(text=f"{result:.2f} {to_unit}")
    except ValueError:
        label_result.config(text="Ошибка: введите число")

root = tk.Tk()
root.title("Конвертер температур")

var_from = tk.StringVar(value="Цельсий")
var_to = tk.StringVar(value="Фаренгейт")

label_input = tk.Label(root, text="Введите температуру:")
entry_input = tk.Entry(root)
label_from = tk.Label(root, text="Из:")
option_from = tk.OptionMenu(root, var_from, "Цельсий", "Фаренгейт", "Кельвин")
label_to = tk.Label(root, text="В:")
option_to = tk.OptionMenu(root, var_to, "Цельсий", "Фаренгейт", "Кельвин")
button_convert = tk.Button(root, text="Конвертировать", command=convert_temperature)
label_result = tk.Label(root, text="")

label_input.grid(row=0, column=0, padx=5, pady=5)
entry_input.grid(row=0, column=1, padx=5, pady=5)
label_from.grid(row=1, column=0, padx=5, pady=5)
option_from.grid(row=1, column=1, padx=5, pady=5)
label_to.grid(row=2, column=0, padx=5, pady=5)
option_to.grid(row=2, column=1, padx=5, pady=5)
button_convert.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
label_result.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
