"""
本代码由[Tkinter布局助手]生成
当前版本:3.1.2
官网:https://www.pytk.net/tkinter-helper
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *

"""
全局通用函数
"""
# 自动隐藏滚动条
def scrollbar_autohide(bar,widget):
    def show():
        bar.lift(widget)
    def hide():
        bar.lower(widget)
    hide()
    widget.bind("<Enter>", lambda e: show())
    bar.bind("<Enter>", lambda e: show())
    widget.bind("<Leave>", lambda e: hide())
    bar.bind("<Leave>", lambda e: hide())
    
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_input_le2nwgvj = self.__tk_input_le2nwgvj()
        self.tk_label_le2nx6o6 = self.__tk_label_le2nx6o6()
        self.tk_button_le2nxpmc = self.__tk_button_le2nxpmc()
        self.tk_table_le2nxvkf = self.__tk_table_le2nxvkf()
        self.tk_label_le2nypho = self.__tk_label_le2nypho()

    def __win(self):
        self.title("排序")
        # 设置窗口大小、居中
        width = 600
        height = 400
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        self.resizable(width=False, height=False)

    def __tk_input_le2nwgvj(self):
        ipt = Entry(self)
        ipt.place(x=100, y=60, width=400, height=53)
        return ipt

    def __tk_label_le2nx6o6(self):
        label = Label(self,text="Label",anchor="center")
        label.place(x=200, y=0, width=200, height=48)
        return label

    def __tk_button_le2nxpmc(self):
        btn = Button(self, text="排序")
        btn.place(x=390, y=120, width=118, height=44)
        return btn

    def __tk_table_le2nxvkf(self):
        # 表头字段 表头宽度
        columns = {"ID":120,"字段#1":180,"字段#2":300}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=0, y=170, width=602, height=231)
        
        return tk_table

    def __tk_label_le2nypho(self):
        label = Label(self,text="时间",anchor="center")
        label.place(x=0, y=140, width=205, height=24)
        return label

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
