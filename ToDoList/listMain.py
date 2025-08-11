import tkinter as tk
from _ast import Lambda
from tkinter import ttk, font, messagebox
from tkinter import PhotoImage
from types import LambdaType

#criando janela
janela = tk.Tk()
janela.title("Meu app de Tarefas")
janela.configure(bg="#F0F0F0")
janela.geometry("500x600")

fonte_cabecalho = font.Font(family="Garamond", size=24, weight="bold")
rotulo_cabecalho = tk.Label(janela,text="Meu app de tarefas", font= fonte_cabecalho, bg="#F0F0F0", fg ="#333").pack(pady=20)


frame = tk.Frame(janela, bg="#F0F0F0")


frame.pack(pady=10)
entrada_tarefa = tk.Entry(frame, font=("Garamond",14),relief=tk.FLAT, bg="white", fg="grey", width=30)
entrada_tarefa.pack(side=tk.LEFT, padx=10)

botao_adicionar= tk.Button(frame, text="Adicionar tarefa", bg="#4CAF50", fg="white", height=1, width=15, font=("Roboto", 11),relief=tk.FLAT)
botao_adicionar.pack(side=tk.LEFT, padx=10)

#Criar um frame para a lista de tarefas com scroll
frame_lista_tarefas = tk.Frame(janela, bg="white")
frame_lista_tarefas.pack(fill=tk.BOTH, expand=True,padx=10,pady=10)

canvas= tk.Canvas(frame_lista_tarefas, bg="white")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_lista_tarefas, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)
canvas_interior = tk.Frame(canvas, bg="white")
canvas.create_window((0,0), window=canvas_interior, anchor="nw")
canvas_interior.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

























janela.mainloop()
