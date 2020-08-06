import tkinter

class StatusApp:
    def __init__(self, data):
        self.data = data
        self.main_window = tkinter.Tk()
        self.main_window.title('status')
        self.main_window.resizable(False, False)
        self.lbl_category = []
        self.lbl_category_usage = []
        self.lbl_title1 = tkinter.Label(self.main_window, text = 'Category usages', width = 60, height = 3, fg = 'red')
        self.lbl_title1.grid(column = 0, row = 0, columnspan = 2)
        for i in range(len(self.data)):
            lbl_category_temp = tkinter.Label(self.main_window, text = self.data[i][0], width = 30)
            lbl_category_temp.grid(column = 0, row = i + 1)
            self.lbl_category.append(lbl_category_temp)
            lbl_usage_temp = tkinter.Label(self.main_window, text=str(self.data[i][2]) + ' KB', width=30)
            lbl_usage_temp.grid(column=1, row=i + 1)
            self.lbl_category_usage.append(lbl_usage_temp)

        self.lbl_title2 = tkinter.Label(self.main_window, text='Website usages', width=60, height=3, fg='red')
        self.lbl_title2.grid(column = 0, row=1 + len(data), columnspan = 2)

        self.lbl_websites = []
        self.lbl_websites_usage = []
        counter = 0
        for i in range(len(self.data)):
            for j in range(len(self.data[i][1])):
                lbl_website_temp = tkinter.Label(self.main_window, text=self.data[i][1][j][0], width=30)
                lbl_website_temp.grid(column=0, row=2 + len(data) + counter)
                self.lbl_websites.append(lbl_website_temp)
                lbl_usage_temp = tkinter.Label(self.main_window, text=str(self.data[i][1][j][1]) + ' KB', width=30)
                lbl_usage_temp.grid(column=1, row=2 + len(data) + counter)
                self.lbl_websites_usage.append(lbl_usage_temp)
                counter += 1

        self.main_window.mainloop()
