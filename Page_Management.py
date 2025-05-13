import customtkinter as ctk
from tkinter import * # We still need to use plain tkinter

app = ctk.CTk()

# Full screen as usual
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
app.geometry(f"{screen_width}x{screen_height}+0+0")
app.update()
app.state("zoomed")

app.title("Sample Page Management")

def set_page(page):
    
    # Clears all the frame first
    Page1.pack_forget()
    Page2.pack_forget()
    
    if page == "page1":
        Page1.pack(expand = True, fill = BOTH)
    elif page == "page2":
        Page2.pack(expand = True, fill = BOTH)

# Pages
Page1 = ctk.CTkFrame(app)
Page2 = ctk.CTkFrame(app)

# Page 1 Content
ctk.CTkLabel(Page1, text = "This is page 1", font = ("Arial", 24)).pack(pady=(100, 0))
ctk.CTkButton(Page1, text = "Go to Page 2", font = ("Arial", 24), command = lambda: set_page("page2")).pack()

# Page 2 Content
ctk.CTkLabel(Page2, text = "This is page 2", font = ("Arial", 24)).pack(pady=(100, 0))
ctk.CTkButton(Page2, text = "Go to Page 1", font = ("Arial", 24), command = lambda: set_page("page1")).pack()

Page1.pack(expand = True, fill = BOTH)

app.mainloop()