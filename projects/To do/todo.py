from tkinter import *
from tkinter import ttk

class todo:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do-List")
        self.root.geometry("650x410+300+150")

        self.label = Label(self.root, text="To-Do-List-App", 
              font="ariel, 25 bold", width=10, bd=5, bg="White", fg="black")
        self.label.pack(side="top", fill=BOTH)

        self.label2 = Label(self.root, text="Add Task", 
              font="ariel, 18 bold", width=10, bd=5, bg="orange", fg="black")
        self.label2.place(x=40, y=54)

        self.label3 = Label(self.root, text="Tasks", 
              font="ariel, 18 bold", width=10, bd=5, bg="orange", fg="black")
        self.label3.place(x=320, y=54)

        self.main_text = Listbox(self.root, height=9, bd=5, width=23, font="ariel, 20 italic bold")
        self.main_text.place(x=200, y=100)

        self.text = Text(self.root, bd=5, height=2, width=20, font="ariel, 10 bold")
        self.text.place(x=20, y=120)

        def add():
            content = self.text.get(1.0, END).strip()
            if content:  # Ensure that empty content is not added
                self.main_text.insert(END, content)
                with open("data.txt", "a") as file:
                    file.write(content + "\n")
                self.text.delete(1.0, END)

        def delete():
            selected_indices = self.main_text.curselection()
            if selected_indices:
                index = selected_indices[0]
                look = self.main_text.get(index)
                with open("data.txt", "r+") as f:
                    new_f = f.readlines()
                    f.seek(0)
                    for line in new_f:
                        if line.strip() != look:
                            f.write(line)
                    f.truncate()
                self.main_text.delete(index)

        with open("data.txt", "r") as file:
            read = file.readlines()
            for i in read:
                ready = i.strip()
                if ready:
                    self.main_text.insert(END, ready)

        self.button = Button(self.root, text="Add", font="ariel, 16 bold italic",
                   width=10, bd=5, bg="orange", fg="black", command=add)
        self.button.place(x=30, y=180)

        self.button2 = Button(self.root, text="Delete", font="ariel, 16 bold italic",
                   width=10, bd=5, bg="orange", fg="black", command=delete)
        self.button2.place(x=30, y=250)
        
def main():
    root = Tk()
    ui = todo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
