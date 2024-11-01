import tkinter as tk
import math

class Equacao2Grau:
    def __init__(self, entry_a, entry_b, entry_c, label):
        self.entry_a = entry_a
        self.entry_b = entry_b
        self.entry_c = entry_c

        self.result = label

    def calcular(self):

        if any(entry.get() == "" for entry in [self.entry_a, self.entry_b, self.entry_c]):
            return self.result.config(text = "Campos não totalmente preenchidos", font = ("Arial", 18))

        a = float(self.entry_a.get())
        b = float(self.entry_b.get())
        c = float(self.entry_c.get())

        delta = math.pow(b, 2) - (4 * a * c)

        if delta < 0:
            resultado = "Não existem raízes reais."
        else:
            raiz_delta = math.sqrt(delta)
            r1 = (-b + raiz_delta) / (2 * a)
            r2 = (-b - raiz_delta) / (2 * a)
            resultado = f"As raízes são:\nR1 = {r1}\nR2 = {r2}"

        self.result.config(text = resultado, font = ("Arial", 24))

view = tk.Tk()

frame_width = 500
frame_height = 300

frame = tk.Frame(view, width = frame_width, height = frame_height, background = "gray")
frame.pack_propagate(False)
frame.pack()

higher_section = tk.Frame(frame, width = (frame_width * 0.95), height = (frame_height * 0.45), background = "light gray")
higher_section.pack_propagate(False)
higher_section.pack(pady = ((frame_height * 0.05) / 2))

title = tk.Label(higher_section, text="Calcule a raízes de uma Equação do 2º Grau", font=("Arial", 16), background = "light gray")
title.pack(pady = (10, 0))

subtitle = tk.Label(higher_section, text="Insira os valores de a, b e c:", font=("Arial", 12), background = "light gray")
subtitle.pack(pady = (5, 0))

higher_section_grid = tk.Frame(higher_section, width = (frame_width * 0.95), background = "light gray")
higher_section_grid.pack_propagate(False)
higher_section_grid.pack(pady = 5)

label_a = tk.Label(higher_section_grid, text="a:", font=("Arial", 12), background = "light gray")
label_a.grid(row = 1, column = 0, padx=5)
entry_a = tk.Entry(higher_section_grid, width=10)
entry_a.grid(row = 1, column = 1, padx=5)

label_b = tk.Label(higher_section_grid, text="b:", font=("Arial", 12), background = "light gray")
label_b.grid(row = 1, column = 2, padx=5)
entry_b = tk.Entry(higher_section_grid, width=10)
entry_b.grid(row = 1, column = 3, padx=5)

label_c = tk.Label(higher_section_grid, text="c:", font=("Arial", 12), background = "light gray")
label_c.grid(row = 1, column = 4, padx=5)
entry_c = tk.Entry(higher_section_grid, width=10)
entry_c.grid(row = 1, column = 5, padx=5)

lower_section = tk.Frame(frame, width = (frame_width * 0.95), height = (frame_height * 0.45), background = "light gray")
lower_section.pack_propagate(False)
lower_section.pack(pady = ((frame_height * 0.05) / 2))

resut_label = tk.Label(lower_section, text = "", font = ("Arial", 24), background = "light gray")
resut_label.pack(expand = True)

eq2grau = Equacao2Grau(entry_a, entry_b, entry_c, resut_label)

button = tk.Button(higher_section, text = "Calcular", font = ("Arial", 12), command = eq2grau.calcular)
button.pack(pady = 5)


view.mainloop()