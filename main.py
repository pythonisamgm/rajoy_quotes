from tkinter import *
import random
import json



def get_quote():
    with open("frases.json", "r", encoding="utf-8") as data_file:
        data = json.load(data_file)

        lista = data["sounds"]
        quote_list = []
        for diccionario in lista:
            frase = diccionario["tags"]
            quote_list.append(frase)

        quote = random.choice(quote_list)
    canvas.itemconfig(quote_text, text=quote)

window = Tk()
window.title("Rajoy Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="../rajoy_frases/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(
    150,
    207,
    width= 250,
    text="Que comience el festival del humor",
    font=("Arial", 25, "bold"),
    fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="rajoy_cara.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()




    #print(quotes)

get_quote()
#diccionarioGrande["sounds"]