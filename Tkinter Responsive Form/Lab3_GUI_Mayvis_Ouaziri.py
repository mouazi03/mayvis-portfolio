import tkinter as tk
from tkinter import ttk, messagebox

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window Properties
        self.title("User Information Form")
        self.geometry("400x350")
        self.resizable(True, True)
        self.configure(bg="lightblue")

        # Frame creation for widgets
        self.frame = ttk.Frame(self, padding=10, relief="ridge")
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Grid configuration for resizing
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # Initialize variables
        self.full_name_var = tk.StringVar()
        self.residency_var = tk.StringVar()
        self.program_var = tk.StringVar()
        self.comp100_var = tk.StringVar()
        self.comp213_var = tk.StringVar()
        self.comp120_var = tk.StringVar()

        # Create widgets
        self.create_widgets()

        # Reset form to default state
        self.reset_form()

    def create_widgets(self):
        # Title Label
        ttk.Label(self.frame, text="User Information Form", font=("Times New Roman", 14, "bold")).grid(
            row=0, column=0, columnspan=2, pady=5, sticky="w"
        )

        # Full Name
        ttk.Label(self.frame, text="Full Name:").grid(row=1, column=0, sticky="w")
        self.full_name_entry = ttk.Entry(self.frame, textvariable=self.full_name_var)
        self.full_name_entry.grid(row=1, column=1, sticky="w")

        # Residency (Radiobuttons)
        ttk.Label(self.frame, text="Residency:").grid(row=2, column=0, sticky="w")
        self.residency_dom = ttk.Radiobutton(self.frame, text="Domestic", variable=self.residency_var, value="dom")
        self.residency_int = ttk.Radiobutton(self.frame, text="International", variable=self.residency_var, value="intl")
        self.residency_dom.grid(row=2, column=1, sticky="w")
        self.residency_int.grid(row=3, column=1, sticky="w")

        # Program (Combobox)
        ttk.Label(self.frame, text="Program:").grid(row=4, column=0, sticky="w")
        self.program_combobox = ttk.Combobox(self.frame, textvariable=self.program_var)
        self.program_combobox["values"] = ("AI", "Gaming", "Health", "Software")
        self.program_combobox.grid(row=4, column=1, sticky="w")

        # Courses (Checkboxes)
        ttk.Label(self.frame, text="Courses:").grid(row=5, column=0, sticky="w")
        self.check_comp100 = ttk.Checkbutton(
            self.frame, text="Programming I", variable=self.comp100_var, onvalue="COMP100", offvalue=""
        )
        self.check_comp213 = ttk.Checkbutton(
            self.frame, text="Web Page Design", variable=self.comp213_var, onvalue="COMP213", offvalue=""
        )
        self.check_comp120 = ttk.Checkbutton(
            self.frame, text="Software Engineering", variable=self.comp120_var, onvalue="COMP120", offvalue=""
        )
        self.check_comp100.grid(row=5, column=1, sticky="w")
        self.check_comp213.grid(row=6, column=1, sticky="w")
        self.check_comp120.grid(row=7, column=1, sticky="w")

        # Buttons
        self.reset_button = ttk.Button(self.frame, text="Reset", command=self.reset_form)
        self.ok_button = ttk.Button(self.frame, text="OK", command=self.show_message)
        self.exit_button = ttk.Button(self.frame, text="Exit", command=self.quit)
        self.reset_button.grid(row=8, column=0, pady=5, sticky="w")
        self.ok_button.grid(row=8, column=1, pady=5, sticky="w")
        self.exit_button.grid(row=8, column=2, pady=5, sticky="w")

    def reset_form(self):
        # Resets the form fields to their default values.
        self.full_name_var.set("Enter your name")
        self.residency_var.set("dom")  # Default to Domestic
        self.program_var.set("AI")     # Default to AI program
        self.comp100_var.set("")
        self.comp213_var.set("")
        self.comp120_var.set("")

    def show_message(self):
        messagebox.showinfo(
            "Form Information",
            f"Full Name: {self.full_name_var.get()}\n"
            f"Program: {self.program_var.get()}\n"
            f"Residency: {self.residency_var.get()}\n"
            f"Courses: {self.comp100_var.get()} {self.comp213_var.get()} {self.comp120_var.get()}\n",
        )

if __name__ == "__main__":
    app = Application()
    app.mainloop()
