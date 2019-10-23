import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import numpy as np
import cv2 as cv

root = tk.Tk()
caminho_imagem = filedialog.askopenfilename(initialdir = "/", title = "Selecione uma imagem PNG", filetypes = (("png files","*.png"),("all files","*.*")))

def main():		
	root.title("Atividade de Computação Gráfica")
	root.geometry("1280x720")
	
	frame = tk.Frame(root)
	frame.pack()

	carregar_imagem_no(frame)
	label = tk.Label(frame, text="Clique na imagem para obter a coordenada e a cor", fg="black")	
	label.pack()
	
	tk.mainloop()

def carregar_imagem_no(frame):
	if caminho_imagem != "":
		imagem = tk.PhotoImage(file=caminho_imagem)	
		label = tk.Label(frame, image=imagem)
		label.imagem = imagem
		label.pack()
		label.bind('<Button-1>', mostra_coordenada_e_rgb)
	else:
		messagebox.showerror("Erro", "Imagem não selecionada!")
		root.destroy()	


def mostra_coordenada_e_rgb(event):
	imagemCv = cv.imread(caminho_imagem)
	(b, g, r) = imagemCv[event.y, event.x] # Retorna um array com o RGB, sendo que no opencv fica o contrário -> BGR. Assim como as coordenadas.
	resultado = "<X:{}, Y:{}, RGB:{}>".format(event.x, event.y, (r,g,b))
	messagebox.showinfo("Info", resultado)
	rgb_hex = "#%02x%02x%02x" % (r, g, b) # Converte o rgb em hexadecimal 
	root.configure(background=rgb_hex)



main()