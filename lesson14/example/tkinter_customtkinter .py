import customtkinter as ctk
from tkinter import messagebox, Button

# ctk.set_appearance_mode("System")  # Следует за Windows темой
ctk.set_default_color_theme("dark-blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Мой Windows App")
        self.geometry("400x300")
        
        # old_style
        self.button = Button(self, text="Клик!", command=self.click)
        self.button.pack(pady=20)
        
        # Современные элементы
        self.button = ctk.CTkButton(self, text="Клик!", command=self.click)
        self.button.pack(pady=20)
        self.slider = ctk.CTkSlider(self, from_=0, to=100)
        self.slider.pack(pady=20)
    
    def click(self):
        messagebox.showinfo("Успех!", f"Значение: {self.slider.get()}")

if __name__ == "__main__":
    app = App()
    app.mainloop()
