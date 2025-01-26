from tkinter import *
from ctypes import windll
#import DB_controller
windll.shcore.SetProcessDpiAwareness(1)

class main_window(Frame):
    def __init__(self, master): 
        Frame.__init__(self, master)  
        self.pack(expand=True, fill='both') 
        self.create_widgets()  # Метод для создания элементов интерфейса

    def create_widgets(self):
        self.label = Label(self, text="Добро пожаловать в приложение!")
        self.label.pack()

        # Создаем footer_bar для нижней панели
        self.footer_bar = Label(self, bg='gray')
        self.footer_bar.pack(side='bottom', fill='x')

         # Создаем область для заметок с прокруткой
        self.notes_frame = Frame(self)
        self.notes_frame.pack(fill='both', expand=True)

        self.canvas = Canvas(self.notes_frame)
        self.canvas.pack(side=LEFT, fill='both', expand=True)
        
        self.scrollbar = Scrollbar(self.notes_frame, command=self.canvas.yview, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=self.scrollbar.set)

        # Создаем фрейм для размещения карточек
        self.cards_frame = Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.cards_frame, anchor='nw')

        # Добавляем 36 карточек
        for i in range(36):
            card = Frame(self.cards_frame, width=200, height=100, bg='lightblue', relief='raised', bd=2)
            card.pack(pady=5)  # Отступ между карточками
            label = Label(card, text=f'Заметка {i+1}', bg='lightblue')
            label.pack(expand=True)


        # Создаем тестовую кнопку "Выход" в footer_bar
        self.quit_button = Button(self.footer_bar, text="Выход", command=self.quit)
        self.quit_button.pack(side='right', padx=10, pady=5) 

# Создание основного окна
root = Tk()
root.title("MyNotes")
root.geometry("1280x720")  # Задаем размер окна
# Инициализация и отображение окна
app = main_window(master=root)
app.mainloop()