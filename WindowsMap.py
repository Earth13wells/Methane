import tkinter

main = tkinter.Tk()

selection1 = tkinter.StringVar(main)
selection1.set("thing")

dropdown = tkinter.OptionMenu(main, selection1, "stuff")
dropdown.pack()

main.mainloop()

#yello
