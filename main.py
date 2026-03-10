import tkinter as tk
from tkinter import filedialog, messagebox

class VectorCASTConverter:
    def __init__(self, master):
        self.master = master
        master.title("VectorCAST Excel Converter")

        self.label = tk.Label(master, text="Select VectorCAST Excel File:")
        self.label.pack()

        self.file_path_entry = tk.Entry(master, width=50)
        self.file_path_entry.pack()

        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack()

        self.convert_button = tk.Button(master, text="Convert", command=self.convert_file)
        self.convert_button.pack()

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        self.file_path_entry.insert(0, file_path)

    def convert_file(self):
        file_path = self.file_path_entry.get()
        if file_path:
            # Placeholder for conversion logic
            messagebox.showinfo("Conversion", f"Converted: {file_path}")
        else:
            messagebox.showwarning("No File", "Please select an Excel file to convert.")

if __name__ == '__main__':
    root = tk.Tk()
    app = VectorCASTConverter(root)
    root.mainloop()