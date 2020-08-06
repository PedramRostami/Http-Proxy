import tkinter

class CategoryApp:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('category')
        self.main_window.resizable(False, False)
        self.category_items_list = []
        self.category_title = tkinter.Label(self.main_window, text='Category List', width=30)
        self.category_title.grid(row=0, column=0)
        self.category_list = tkinter.Listbox(self.main_window, width=30)
        self.category_list.grid(row=1, column=0)
        self.category_label = tkinter.Label(self.main_window, text='Please Enter Your Category', width=30)
        self.category_label.grid(row=2, column=0)
        self.category_entry = tkinter.Entry(self.main_window, width=30)
        self.category_entry.grid(row=3, column=0)
        self.category_add = tkinter.Button(self.main_window, text='Add', width=30,
                                      command=self.add_btn_action)
        self.category_add.grid(row=4, column=0)
        self.category_done = tkinter.Button(self.main_window, text='Done', width=30, command = self.quit)
        self.category_done.grid(row=5, column=0)
        self.main_window.mainloop()

    def add_btn_action(self):
        self.category_items_list.append(self.category_entry.get())
        self.category_entry.delete(0, 'end')
        self.category_list.insert(len(self.category_items_list), self.category_items_list[-1])

    def quit(self):
        self.main_window.destroy()
