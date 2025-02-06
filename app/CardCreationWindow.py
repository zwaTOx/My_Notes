from tkinter import Label, Entry, Button, Toplevel

class card_creation_window(Toplevel):
    def __init__(self, master, main_window):
        super().__init__(master)
        self.main_window = main_window
        self.title("Создание карточки")
        self.geometry("400x300")

        # Добавляем элементы интерфейса
        Label(self, text="Введите данные для новой карточки").pack(pady=10)
        Entry(self).pack(pady=5)
        
    def close_window(self):
        self.master.show_main_window(self)  # Показываем главное окно
        self.destroy()  # Закрываем текущее окно