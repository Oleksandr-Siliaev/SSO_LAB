import tkinter as tk
import datetime

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")
        self.root.geometry("300x500")
        self.expression = ""
        self.history = []

        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack()

        self.input_field = tk.Entry(self.input_frame, font=('Arial', 18), textvariable=self.input_text, justify='right')
        self.input_field.grid(row=0, column=0, ipadx=8, ipady=20)
        self.input_field.pack(ipady=10, fill='both')

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack()

        self.create_buttons()

        self.history_frame = tk.Frame(self.root)
        self.history_frame.pack(fill='both', expand=True)

        self.history_label = tk.Label(self.history_frame, text="Історія обчислень:", anchor='w')
        self.history_label.pack(fill='x')

        self.history_listbox = tk.Listbox(self.history_frame, height=5)
        self.history_listbox.pack(fill='both', expand=True)

    def press(self, item):
        self.expression += str(item)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def equal(self):
        try:
            result = str(eval(self.expression))
            record = f"{self.expression} = {result}"
            self.input_text.set(result)
            self.expression = result

            self.add_to_history(record)
            self.save_to_file(record)

        except Exception:
            self.input_text.set("Помилка")
            self.expression = ""

    def add_to_history(self, record):
        self.history.append(record)
        self.history_listbox.insert(tk.END, record)

    def save_to_file(self, record):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("history.txt", "a", encoding='utf-8') as file:
            file.write(f"[{timestamp}] {record}\n")

    def create_buttons(self):
        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('0', '.', '=', '+'),
        ]

        for row_index, row in enumerate(buttons):
            for col_index, button_text in enumerate(row):
                if button_text == "=":
                    button = tk.Button(self.buttons_frame, text=button_text, width=10, height=3,
                                       command=self.equal)
                else:
                    button = tk.Button(self.buttons_frame, text=button_text, width=10, height=3,
                                       command=lambda x=button_text: self.press(x))
                button.grid(row=row_index, column=col_index, padx=5, pady=5)

        clear_button = tk.Button(self.root, text="C", width=42, height=3, command=self.clear)
        clear_button.pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()
