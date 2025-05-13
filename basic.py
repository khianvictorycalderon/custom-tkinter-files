import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.update()
app.state("zoomed")
app.title("Sample Maxmized Window")

app.mainloop()