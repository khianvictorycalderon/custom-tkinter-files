import customtkinter as ctk
import tkinter as tk  # Needed for screen dimensions
from tkinter import BOTH

currentTheme = "dark"
ctk.set_appearance_mode(currentTheme)
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Simple Theme Changer")

screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")

app.update()
app.state("zoomed")

container = ctk.CTkFrame(app)
container.pack(expand=True, fill=BOTH)

def ChangeTheme():
    global currentTheme
    if currentTheme == "dark" : currentTheme = "light"
    elif currentTheme == "light" : currentTheme = "dark"
    ctk.set_appearance_mode(currentTheme)
    toggle_button.configure(text=f"{currentTheme}")

ctk.CTkLabel(container, text="Toggle Theme: ", font=("Arial", 24)).pack(pady=(150, 0))
toggle_button = ctk.CTkButton(container, text=currentTheme, font=("Arial", 24), command=ChangeTheme)
toggle_button.pack(padx=20, pady=20)

app.mainloop()
