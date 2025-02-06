from tkinter import *
from ctypes import windll
import properties # type: ignore

from card import Card # type: ignore
from CardCreationWindow import card_creation_window # type: ignore
#import DB_controller
windll.shcore.SetProcessDpiAwareness(1)

class main_window(Frame):
    def __init__(self, master): 
        Frame.__init__(self, master)  
        self.pack(expand=True, fill='both') 
        self.master.title("MyNotes")
        self.master.geometry("1120x1080") 
        self.create_widgets()  # Метод для создания элементов интерфейса

    def create_widgets(self):
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
        self.update_cards()
        
        # Создаем тестовую кнопку "Выход" в footer_bar
        self.quit_button = Button(self.footer_bar, text="Создать", command=self.open_card_creation_window)
        self.quit_button.pack(side='right', padx=10, pady=5) 
    
    def open_card_creation_window(self):
        # Создаем новое окно для создания карточки
        self.master.withdraw()  # Скрываем главное окно
        creation_window = card_creation_window(self.master, self)  # Создаем экземпляр класса CardCreationWindow

        # Обработчик события закрытия окна создания карточки
        creation_window.protocol("WM_DELETE_WINDOW", lambda: self.show_main_window(creation_window))

    def show_main_window(self, creation_window):
        # Возвращаемся к основному окну и закрываем побочное
        self.master.deiconify()
        self.update_cards()
        creation_window.destroy()

    def update_cards(self):
        # Очищаем предыдущие карточки из cards_frame
        #for widget in self.cards_frame.winfo_children():
        #    widget.destroy()

        columns = properties.CARD_COLUMNS  # Количество карточек в ряд
        card_padx = properties.CARD_PADX
        card_pady = properties.CARD_PADY
        row = 0

        for i in range(36):
            if i==5:
                card = Card(master=self.cards_frame, id=i, title=f'Заметка заметка заметка заметка заметка {i+1}', description="Это описание для карточки. бяяббябябябябябябябябябяяббябябябябя")
            else:
                card = Card(master=self.cards_frame, id=i, title=f'Заметка {i+1}', description="Это описание для карточки. ")
            card.grid(row=row, column=i % columns, padx=card_padx, pady=card_pady, sticky=E) 
            card.pack_propagate(False) #Оставляем фиксированный размер

            if (i + 1) % columns == 0:  # Переход на новую строку
                row += 1

        # Обновляем размеры и scrollregion после добавления карточек
            self.update_scrollregion()

    def update_scrollregion(self):
        # Устанавливаем scrollregion для canvas
        self.cards_frame.update_idletasks()  # Обновляем размеры
        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Устанавливаем scrollregion для canvas


# Создание основного окна
root = Tk()
root.title("MyNotes")
root.geometry("1120x1080")  # Задаем размер окна
# Инициализация и отображение окна
app = main_window(master=root)
app.mainloop()