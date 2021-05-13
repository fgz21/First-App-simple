import tkinter as tk
from PIL import ImageTk, Image



#ventana

windows = tk.Tk()
windows.title("First App Fran")
windows.geometry("500x300")


#incono

windows.iconbitmap("incono.ico")



#imagenes

imagen = ImageTk.PhotoImage(Image.open("panas.jpg").resize((300,300)))
label = tk.Label(image=imagen)
label.pack()

#botton






windows.mainloop()
