import tkinter

class WebsitesApp:
    def __init__(self, category_name):
        self.main_window = tkinter.Tk()
        self.main_window.title(category_name)
        self.main_window.resizable(False, False)
        self.websites_list = []
        self.lbl_title = tkinter.Label(self.main_window, text='Websites of ' + category_name, width=50)
        self.lbl_title.grid(row=0, column=0)
        self.lst_websites = tkinter.Listbox(self.main_window, width=50)
        self.lst_websites.grid(row=1, column=0)
        self.lbl_entry = tkinter.Label(self.main_window, text='Please Enter Your Website(like \'senario.net\')', width=50)
        self.lbl_entry.grid(row=2, column=0)
        self.ent_websites = tkinter.Entry(self.main_window, width=50)
        self.ent_websites.grid(row=3, column=0)
        self.btn_add = tkinter.Button(self.main_window, text='Add', width=50,
                                           command=self.add_btn_action)
        self.btn_add.grid(row=4, column=0)
        self.btn_done = tkinter.Button(self.main_window, text='Done', width=50, command=self.quit)
        self.btn_done.grid(row=5, column=0)
        self.main_window.mainloop()

    def add_btn_action(self):
        self.websites_list.append(self.ent_websites.get())
        self.ent_websites.delete(0, 'end')
        self.lst_websites.insert(len(self.websites_list), self.websites_list[-1])

    def quit(self):
        self.main_window.destroy()
