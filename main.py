import tkinter as tk
from MarkovTextGeneratorApp import MarkovTextGeneratorApp

def main():
    root = tk.Tk()
    app = MarkovTextGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
