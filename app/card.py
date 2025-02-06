import properties # type: ignore
from tkinter import Label, Frame

class Card(Frame):
    def __init__(self, id, title, master=None, description=""):
        #Настройки карточки
        self.card_width = properties.CARD_WIDTH 
        card_height = properties.CARD_HEIGHT  
        self.card_bg = properties.CARD_BG_COLOR
        card_bd = properties.CARD_BORDER_WIDTH
        card_relief = properties.CARD_RELIEF

        super().__init__(master, width=self.card_width, height=card_height, 
        bg=self.card_bg, bd=card_bd, relief=card_relief)
        self.id = id
        self.title = title
        self.description = description
        self.create_widgets()

        self.bind("<Button-1>", self.on_click)

    def create_widgets(self):
        # Заголовок
        self.title_label = Label(self, text=self.title, 
            font=("Arial", 12, "bold"), 
            wraplength=self.card_width-20, 
            bg = self.card_bg,
            justify="left")
        self.title_label.pack(anchor="nw", padx=10, pady=5)

        # Описание
        self.desc_label = Label(self, text=self.description, 
            font=("Arial", 8), 
            wraplength=self.card_width-20, 
            bg=self.card_bg, 
            justify="left")
        self.desc_label.pack(anchor="nw", padx=10, pady=5)

        # Дата и время создания заметки
        now = 'now'
        self.date_label = Label(self, text=f"Создано: {now}", font=("Arial", 8), bg=self.card_bg)
        self.date_label.pack(side="bottom", anchor="se", padx=10, pady=5)

        # Регистация нажатия
        self.title_label.bind("<Button-1>", self.on_click)
        self.desc_label.bind("<Button-1>", self.on_click)
        self.date_label.bind("<Button-1>", self.on_click)

    def on_click(self, event):
        print(f'card: id={self.id}')