import tkinter as tk
from tkinter import filedialog
from MarkovTextGenerator import MarkovTextGenerator

class MarkovTextGeneratorApp:
    def __init__(self, master, order=2, text_length=50):
        self.master = master
        self.master.title("Markov Text Generator")

        self.generator = None
        self.current_order = order

        # default input text
        with open("./assets/defaultTrainingData.txt") as f:
            self.input_text = f.read().replace("\n", " ")

        # set up te UI
        self._order_label = tk.Label(master, text="Order:")
        self._order_label.grid(row=0, column=0, padx=5, pady=5)
        self._order_entry = tk.Entry(master)
        self._order_entry.grid(row=0, column=1, padx=5, pady=5)
        self._order_entry.insert(tk.END, str(order))

        self._length_label = tk.Label(master, text="Max Output Length:")
        self._length_label.grid(row=1, column=0, padx=5, pady=5)
        self._length_entry = tk.Entry(master)
        self._length_entry.grid(row=1, column=1, padx=5, pady=5)
        self._length_entry.insert(tk.END, str(text_length))

        self._upload_button = tk.Button(master, text="Upload .txt File", command=self._upload_file)
        self._upload_button.grid(row=2, column=0, padx=5, pady=5)

        self._generate_button = tk.Button(master, text="Generate", command=self._generate_text)
        self._generate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.start_with_capital_var = tk.BooleanVar()
        self.start_with_capital_var.set(True)
        self._start_with_capital_checkbox = tk.Checkbutton(master, text="Start with Capital", variable=self.start_with_capital_var)
        self._start_with_capital_checkbox.grid(row=2, column=1, columnspan=2, padx=5, pady=5)


        self.output_text = tk.Text(master, height=10, width=50, state=tk.DISABLED, wrap=tk.WORD)
        self.output_text.grid(row=4, column=0, columnspan=2, padx=5, pady=5)


    def _upload_file(self):
        # only allow .txt files
        file_path = filedialog.askopenfilename()
        if file_path.endswith(".txt"):
            with open(file_path, "r") as file:
                self.input_text = file.read().replace("\n", " ")
        else:
            self.output_text.config(state=tk.NORMAL)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Invalid input file. Using last known input file instead.", "red")
            self.output_text.tag_configure("red", foreground="red")
            self.output_text.config(state=tk.DISABLED)

    def _generate_text(self):
        order = int(self._order_entry.get())
        max_length = int(self._length_entry.get())
        start_with_capital = self.start_with_capital_var.get()

        # only update the generator if some of values related to the model
        # was changed since the last execution
        self.generator = MarkovTextGenerator(self.input_text, order)
        if order != self.current_order:
            self.generator.build_markov_model(order)

        output_phrase = self.generator.generate_text(order, max_length, start_with_capital)

        self.output_text.config(state=tk.NORMAL)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, output_phrase)
        self.output_text.config(state=tk.DISABLED)