from tkinter import *
from ctypes import windll
import DB_controller
windll.shcore.SetProcessDpiAwareness(1)

class main_window(Frame):
    def __init__(self, master): 
        Frame.__init__(self, master)  
        self.pack()
        self.create_widgets()  # Метод для создания элементов интерфейса

    def create_widgets(self):
        self.label = Label(self, text="Добро пожаловать в приложение!")
        self.label.pack()

        self.tool_bar = Label(self, bg='gray', text="toolbar")
        #self.quit_button = Button(self, text="Выход", command=self.quit)
        #self.quit_button.pack()

# Создание основного окна
root = Tk()
root.title("Приложение")
root.geometry("800x600")  # Задаем размер окна

# Инициализация и отображение окна
app = main_window(master=root)
app.mainloop()