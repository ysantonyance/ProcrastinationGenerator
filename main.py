import tkinter as tk
import random

class ProcrastinationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Генератор отмазок")
        self.root.geometry("450x360")
        self.root.resizable(False, False)
        self.root.configure(bg="#282c34")

        self.excuses = [
            "Мой кот лег на клавиатуру и случайно скомпилировал ядро линукса. Мне нельзя его беспокоить.",
            "Длина волны звездного света сегодня не подходит для написания кода.",
            "Если я сейчас сделаю домашнее задание, мировой баланс сил нарушится, и кофе превратится в чай.",
            "Я жду, пока Марс перейдёт в другой дом, потому что сейчас он находится в ретроградном положении питона.",
            "Мой компьютер слишком сильно нагрелся от моих гениальных мыслей, ему нужен психотерапевт.",
            "Закон квантовой неопределённости гласит: если не открывать репозиторий, задача одновременно и выполнена, и не выполнена.",
            "Я случайно отключил интернет через консоль. Теперь жду, пока он снова загрузится из облака.",
            "Мой код работает слишком идеально, я боюсь его трогать, чтобы он не стал умнее меня."
        ]

        self.count = 0

        # Заголовок
        title = tk.Label(root, text="Владыка прокрастинации", font=("Arial", 16, "bold"), bg="#282c34", fg="#98c379")
        title.pack(pady=20)

        # Поле для відмазки
        self.excuse_var = tk.StringVar(value="Нажмите кнопку ниже, чтобы найти оправдание своей лени...")
        self.label_excuse = tk.Label(
            root, textvariable=self.excuse_var, 
            font=("Arial", 11), bg="#3e4451", fg="#abb2bf", 
            wraplength=400, justify="center", padx=15, pady=15, relief="groove"
        )
        self.label_excuse.pack(pady=10, padx=20)

        # Кнопка
        self.btn = tk.Button(
            root, text="Придумать отмазку",
            font=("Arial", 11, "bold"), bg="#e06c75", fg="white", 
            activebackground="#be5046", activeforeground="white",
            padx=15, pady=8, command=self.generate_excuse
        )
        self.btn.pack(pady=15)

        # Лічильник
        self.counter_label = tk.Label(root, text="Сгенерированно отмазок: 0", font=("Arial", 9), bg="#282c34", fg="#5c6370")
        self.counter_label.pack(pady=5)

    def generate_excuse(self):
        excuse = random.choice(self.excuses)
        self.excuse_var.set(excuse)
        self.count += 1
        self.counter_label.config(text=f"Сгенерированно отмазок: {self.count}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ProcrastinationApp(root)
    root.mainloop()