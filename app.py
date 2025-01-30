from tkinter import *
from ctypes import windll
import properties # type: ignore
#import DB_controller
windll.shcore.SetProcessDpiAwareness(1)

class Card(Frame):
    def __init__(self, master=None, title="", description=""):

        card_width = properties.CARD_WIDTH  # Ширина карточки
        card_height = properties.CARD_HEIGHT  # Высота карточки
        self.card_bg = properties.CARD_BG_COLOR
        card_bd = properties.CARD_BORDER_WIDTH
        card_relief = properties.CARD_RELIEF

        super().__init__(master, width=card_width, height=card_height, bg=self.card_bg, bd=card_bd, relief=card_relief)
        self.title = title
        self.description = description
        self.create_widgets()
        
    def create_widgets(self):
        # Заголовок
        self.title_label = Label(self, text=self.title, font=("Arial", 12, "bold"), bg = self.card_bg)
        self.title_label.pack(anchor="nw", padx=10, pady=5)

        # Описание
        self.desc_label = Label(self, text=self.description, wraplength=340 ,bg=self.card_bg)
        self.desc_label.pack(anchor="nw", padx=10)

        # Дата и время создания заметки
        now = 'now'
        self.date_label = Label(self, text=f"Создано: {now}", font=("Arial", 8), bg=self.card_bg)
        self.date_label.pack(side="bottom", anchor="se", padx=10, pady=5)

class main_window(Frame):
    def __init__(self, master): 
        Frame.__init__(self, master)  
        self.pack(expand=True, fill='both') 
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
        self.quit_button = Button(self.footer_bar, text="Выход", command=self.quit)
        self.quit_button.pack(side='right', padx=10, pady=5) 

    def update_cards(self):
        # Очищаем предыдущие карточки из cards_frame
        #for widget in self.cards_frame.winfo_children():
        #    widget.destroy()

        card_width = properties.CARD_WIDTH  # Ширина карточки
        card_height = properties.CARD_HEIGHT  # Высота карточки
        columns = properties.CARD_COLUMNS  # Количество карточек в ряд
        card_padx = properties.CARD_PADX
        card_pady = properties.CARD_PADY
        row = 0

        for i in range(36):
            if i==10:
                card = Card(self.cards_frame, title=f'Заметка {i+1}', description="Это описание для карточки. бяяббябябябябябябябябябяяббябябябябя")
            else:
                card = Card(self.cards_frame, title=f'Заметка {i+1}', description="Это описание для карточки. ")
            #card = Frame(self.cards_frame, width=card_width, height=card_height, bg='lightblue', relief='raised', bd=2)
            card.grid(row=row, column=i % columns, padx=card_padx, pady=card_pady, sticky=E)  # Используем grid для размещения
            card.pack_propagate(False)
            #label = Label(card, text=f'Заметка {i+1}', bg='lightblue')
            #label.place(relx=0.5, rely=0.5, anchor='center')

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