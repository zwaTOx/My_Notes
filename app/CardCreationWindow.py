from tkinter import Label, Entry, Button, Toplevel, Tk, Text
from DB_controller import NotesDatabase # type: ignore

class card_creation_window(Toplevel):
    def __init__(self, master, main_window):
        super().__init__(master)
        self.main_window = main_window
        self.title("Создание карточки")
        self.geometry("1120x1080")
        self.create_widgets()
    
    def create_widgets(self):
        # Заголовок
        Label(self, text="Заголовок карточки:").pack(pady=10)
        self.title_entry = Entry(self, width=50)
        self.title_entry.pack(pady=10)

        # Описание
        Label(self, text="Описание карточки:").pack(pady=10)
        self.description_text = Text(self, width=70, height=20)
        self.description_text.pack(pady=10)

        # Кнопка сохранить
        self.save_button = Button(self, text="Сохранить", command=self.save_card)
        self.save_button.pack(pady=20)
        
    def save_card(self):
        title = self.title_entry.get()
        description = self.description_text.get("1.0", "end-1c")  # Получаем текст из текстовой области
        # Здесь можно добавить код для сохранения заголовка и описания карточки
        print("Сохранено:", title, description)
        try:
           database = NotesDatabase()
           database.add_note(title, description)
           database.close()
           print("Запись успешна!")
        except Exception as e:
           print("Ошибка при записи в базу данных:", e)
        self.main_window.show_main_window(self)

    def close_window(self):
        self.master.show_main_window(self)  # Показываем главное окно
        self.destroy()  # Закрываем текущее окно

if __name__ == "__main__":
    root = Tk()
    main_window = None  # Здесь должен быть ваш основной класс окна
    card_creation = card_creation_window(root, main_window)
    root.mainloop()