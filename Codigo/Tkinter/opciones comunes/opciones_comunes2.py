from tkinter import Tk, Entry

root = Tk()

campo1 = Entry(bg="yellow", fg="blue", font=("Times New Roman", "24", "bold italic"), highlightcolor="red", highlightthickness=2)
campo2 = Entry(bg="yellow", fg="blue", font=("Times New Roman", "24", "bold italic"), highlightcolor="red", highlightthickness=2)
campo3 = Entry(bg="yellow", fg="blue", font=("Times New Roman", "24", "bold italic"), highlightcolor="red", highlightthickness=2, takefocus=False)
campo4 = Entry(bg="yellow", fg="blue", font=("Times New Roman", "24", "bold italic"), highlightcolor="red", highlightthickness=2)

campo1.pack(padx=10, pady=5)
campo2.pack(padx=10, pady=5)
campo3.pack(padx=10, pady=5)
campo4.pack(padx=10, pady=5)
