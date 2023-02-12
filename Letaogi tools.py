from tkinter import *
from tkinter.ttk import *
import requests,re,json,datetime

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
        self.tk_tabs_ldv3hjab = Frame_ldv3hjab(self)

    def __win(self):
        self.title("Letaogi tools")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # self.configure(background='white')
        self.config(bg='white')
        self.geometry(geometry)
        self.resizable(width=False, height=False)

class Frame_ldv3hjab(Notebook):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        
    def __frame(self):
        self.tk_tabs_ldv3hjab_0 = Frame_ldv3hjab_0(self)
        self.add(self.tk_tabs_ldv3hjab_0, text="Info")

        self.tk_tabs_ldv3hjab_1 = Frame_ldv3hjab_1(self)
        self.add(self.tk_tabs_ldv3hjab_1, text="挂店")

        self.tk_tabs_ldv3hjab_2 = Frame_ldv3hjab_2(self)
        self.add(self.tk_tabs_ldv3hjab_2, text="公海")

        self.tk_tabs_ldv3hjab_3 = Frame_ldv3hjab_3(self)
        self.add(self.tk_tabs_ldv3hjab_3, text="快捷出售")

        self.tk_tabs_ldv3hjab_4 = Frame_ldv3hjab_4(self)
        self.add(self.tk_tabs_ldv3hjab_4, text="网店估价")

        self.tk_tabs_ldv3hjab_5 = Frame_ldv3hjab_5(self)
        self.add(self.tk_tabs_ldv3hjab_5, text="排序")

        self.tk_tabs_ldv3hjab_6 = Frame_ldv3hjab_6(self)
        self.add(self.tk_tabs_ldv3hjab_6, text="Garbage request")

        self.tk_tabs_ldv3hjab_7 = Frame_ldv3hjab_7(self)
        self.add(self.tk_tabs_ldv3hjab_7, text="店铺信息")

        self.tk_tabs_ldv3hjab_8 = Frame_ldv3hjab_8(self)
        self.add(self.tk_tabs_ldv3hjab_8, text="Help")

        self.place(x=0, y=0, width=600, height=500)

class Frame_ldv3hjab_0(Frame):
    
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_ldv43rvf = self.__tk_label_ldv43rvf()
        self.tk_label_ldv4te4l = self.__tk_label_ldv4te4l()
        self.tk_label_ldv4tyms = self.__tk_label_ldv4tyms()
        self.tk_text_ldv4wo77 = self.__tk_text_ldv4wo77()
        self.tk_input_ldv4xo0c = self.__tk_input_ldv4xo0c()
        self.tk_button_ldv4xyzv = self.__tk_button_ldv4xyzv()
        self.tk_button_ldv4xyzvv = self.__tk_button_ldv4xyzvv()
        self.tk_label_ldv4zs56 = self.__tk_label_ldv4zs56()
        self.tk_input_ldv5066a = self.__tk_input_ldv5066a()

    def __frame(self):
        self.place(x=0, y=0, width=650, height=500)

    def __tk_label_ldv43rvf(self):
        label = Label(self,text="Ver 0.1 demo by xiaoc0519",anchor="center")
        label.place(x=380, y=440, width=176, height=24)
        return label

    def __tk_label_ldv4te4l(self):
        label = Label(self,text="企业微信群机器人推送Token",anchor="center")
        label.place(x=20, y=160, width=188, height=24)
        return label

    def __tk_label_ldv4tyms(self):
        label = Label(self,text="cookie",anchor="center")
        label.place(x=20, y=60, width=120, height=24)
        return label

    def __tk_text_ldv4wo77(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=360, y=10, width=220, height=424)
        text.config(state=DISABLED)
        return text

    def __tk_input_ldv4xo0c(self):
        ipt = Entry(self)
        ipt.place(x=20, y=100, width=294, height=24)
        return ipt

    def __tk_button_ldv4xyzv(self):
        btn = Button(self, text="User")
        btn.place(x=20, y=250, width=110, height=40)
        return btn

    def __tk_button_ldv4xyzvv(self):
        btn = Button(self, text="Post")
        btn.place(x=150, y=250, width=110, height=40)
        return btn

    def __tk_label_ldv4zs56(self):
        label = Label(self,text="* 这里是注意事项",anchor="center")
        label.place(x=20, y=310, width=330, height=120)
        return label

    def __tk_input_ldv5066a(self):
        ipt = Entry(self)
        ipt.place(x=20, y=200, width=300, height=24)
        return ipt

class Frame_ldv3hjab_1(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_ldv7d1x7 = self.__tk_label_ldv7d1x7()
        self.tk_label_ldv7d9me = self.__tk_label_ldv7d9me()
        self.tk_input_ldv7dgph = self.__tk_input_ldv7dgph()
        self.tk_input_ldv7dl5w = self.__tk_input_ldv7dl5w()
        self.tk_button_ldv7dock = self.__tk_button_ldv7dock()
        self.tk_text_ldv7dw4e = self.__tk_text_ldv7dw4e()
        self.tk_label_ldvolgae = self.__tk_label_ldvolgae()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_label_ldv7d1x7(self):
        label = Label(self,text="旺旺",anchor="center")
        label.place(x=20, y=60, width=120, height=24)
        return label

    def __tk_label_ldv7d9me(self):
        label = Label(self,text="手机号",anchor="center")
        label.place(x=20, y=160, width=120, height=24)
        return label

    def __tk_input_ldv7dgph(self):
        ipt = Entry(self)
        ipt.place(x=20, y=200, width=300, height=24)
        return ipt

    def __tk_input_ldv7dl5w(self):
        ipt = Entry(self)
        ipt.place(x=20, y=100, width=300, height=24)
        return ipt

    def __tk_button_ldv7dock(self):
        btn = Button(self, text="提交")
        btn.place(x=20, y=250, width=110, height=40)
        return btn

    def __tk_text_ldv7dw4e(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=360, y=10, width=220, height=424)
        text.config(state=DISABLED)
        return text

    def __tk_label_ldvolgae(self):
        label = Label(self,text="* 这里是注意事项",anchor="center")
        label.place(x=20, y=310, width=330, height=120)
        return label

class Frame_ldv3hjab_2(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_ldv7f4sz = self.__tk_label_ldv7f4sz()
        self.tk_text_ldv7fnvf = self.__tk_text_ldv7fnvf()
        self.tk_select_box_ldvot2gm = self.__tk_select_box_ldvot2gm()
        self.tk_button_ldvp14cz = self.__tk_button_ldvp14cz()
        self.tk_label_ldvp2atq = self.__tk_label_ldvp2atq()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_label_ldv7f4sz(self):
        label = Label(self,text="最低",anchor="center")
        label.place(x=20, y=100, width=120, height=24)
        return label

    def __tk_text_ldv7fnvf(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=360, y=10, width=220, height=424)
        text.config(state=DISABLED)
        
        return text

    def __tk_select_box_ldvot2gm(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("zuanshi-3","zuanshi-4","zuanshi-5")
        cb.place(x=20, y=160, width=120, height=24)
        return cb

    def __tk_button_ldvp14cz(self):
        btn = Button(self, text="commonsea")
        btn.place(x=20, y=220, width=120, height=40)
        return btn

    def __tk_label_ldvp2atq(self):
        label = Label(self,text="* common sea",anchor="center")
        label.place(x=20, y=310, width=330, height=120)
        return label

class Frame_ldv3hjab_3(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_text_ldv7hi3u = self.__tk_text_ldv7hi3u()
        self.tk_button_ldv7i1wc = self.__tk_button_ldv7i1wc()
        self.tk_select_box_ldvp47af = self.__tk_select_box_ldvp47af()
        self.tk_label_ldvp4adt = self.__tk_label_ldvp4adt()
        self.tk_label_ldvp5qdx = self.__tk_label_ldvp5qdx()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_text_ldv7hi3u(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=360, y=10, width=220, height=424)
        text.config(state=DISABLED)
        
        return text

    def __tk_button_ldv7i1wc(self):
        btn = Button(self, text="按钮")
        btn.place(x=160, y=180, width=130, height=49)
        return btn

    def __tk_select_box_ldvp47af(self):
        cb = Combobox(self, state="readonly")
        cb['values'] = ("30s","Python","Tkinter Helper")
        cb.place(x=1250, y=200, width=150, height=24)
        return cb

    def __tk_label_ldvp4adt(self):
        label = Label(self,text="sleep",anchor="center")
        label.place(x=120, y=100, width=50, height=24)
        return label

    def __tk_label_ldvp5qdx(self):
        label = Label(self,text="Writting !",anchor="center")
        label.place(x=20, y=310, width=330, height=120)
        return label

class Frame_ldv3hjab_4(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_text_ldv7iie9 = self.__tk_text_ldv7iie9()
        self.tk_label_ldvp7gxv = self.__tk_label_ldvp7gxv()
        self.tk_button_ldvp7mff = self.__tk_button_ldvp7mff()
        self.tk_label_ldvp83od = self.__tk_label_ldvp83od()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_text_ldv7iie9(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=360, y=10, width=220, height=424)
        text.config(state=DISABLED)
        
        return text

    def __tk_label_ldvp7gxv(self):
        label = Label(self,text="sleep",anchor="center")
        label.place(x=80, y=90, width=50, height=24)
        return label

    def __tk_button_ldvp7mff(self):
        btn = Button(self, text="按钮")
        btn.place(x=80, y=160, width=136, height=77)
        return btn

    def __tk_label_ldvp83od(self):
        label = Label(self,text="writting",anchor="center")
        label.place(x=20, y=310, width=330, height=120)
        return label

class Frame_ldv3hjab_5(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_table_ldv7iw6p = self.__tk_table_ldv7iw6p()
        self.tk_label_ldv7j3z5 = self.__tk_label_ldv7j3z5()
        self.tk_input_ldv7jn0o = self.__tk_input_ldv7jn0o()
        self.tk_label_ldv7jy7k = self.__tk_label_ldv7jy7k()
        self.tk_button_ldv7kfgx = self.__tk_button_ldv7kfgx()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_table_ldv7iw6p(self):
        # 表头字段 表头宽度
        columns = {"组名":113,"成交":170,"小组人数":83,"人均成交":200}
        # 初始化表格 表格是基于Treeview，tkinter本身没有表格。show="headings" 为隐藏首列。
        tk_table = Treeview(self, show="headings", columns=list(columns))
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=False)  # stretch 不自动拉伸
        
        tk_table.place(x=10, y=265, width=568, height=193)
        
        return tk_table

    def __tk_label_ldv7j3z5(self):
        label = Label(self,text=datetime.datetime.now(),anchor="center")
        label.place(x=10, y=230, width=185, height=24)
        return label

    def __tk_input_ldv7jn0o(self):
        ipt = Entry(self)
        ipt.insert(0, '钢铁组,1,A组,1,星梦,1,腾飞,1,皇族,1')
        ipt.place(x=100, y=120, width=397, height=49)
        return ipt

    def __tk_label_ldv7jy7k(self):
        label = Label(self,text="组",anchor="center")
        label.place(x=100, y=10, width=396, height=92)
        return label

    def __tk_button_ldv7kfgx(self):
        btn = Button(self, text="get_sort")
        btn.place(x=410, y=180, width=120, height=40)
        return btn

class Frame_ldv3hjab_6(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_button_ldv7kroz = self.__tk_button_ldv7kroz()
        self.tk_text_ldv7laai = self.__tk_text_ldv7laai()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_button_ldv7kroz(self):
        btn = Button(self, text="One_punch")
        btn.place(x=110, y=180, width=143, height=63)
        return btn

    def __tk_text_ldv7laai(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=360, y=10, width=220, height=424)
        text.config(state=DISABLED)
        
        return text

class Frame_ldv3hjab_7(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_ldv7lhtb = self.__tk_label_ldv7lhtb()
        self.tk_input_ldv7lp3c = self.__tk_input_ldv7lp3c()
        self.tk_button_ldv7m1jj = self.__tk_button_ldv7m1jj()
        self.tk_label_ldv7mc5j = self.__tk_label_ldv7mc5j()
        self.tk_label_ldv7mevf = self.__tk_label_ldv7mevf()
        self.tk_label_ldv7qo7p = self.__tk_label_ldv7qo7p()
        self.tk_label_ldv7r0at = self.__tk_label_ldv7r0at()
        self.tk_label_ldv7rkbh = self.__tk_label_ldv7rkbh()
        self.tk_frame_ldv7ry0d = Frame_ldv7ry0d(self)
        self.tk_label_ldvpgl8w = self.__tk_label_ldvpgl8w()
        self.tk_input_ldvph0bo = self.__tk_input_ldvph0bo()
        self.tk_label_ldvphjq7 = self.__tk_label_ldvphjq7()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_label_ldv7lhtb(self):
        label = Label(self,text="旺旺:",anchor="center")
        label.place(x=30, y=40, width=50, height=24)
        return label

    def __tk_input_ldv7lp3c(self):
        ipt = Entry(self)
        ipt.place(x=100, y=40, width=198, height=24)
        return ipt

    def __tk_button_ldv7m1jj(self):
        btn = Button(self, text="信息请求")
        btn.place(x=320, y=40, width=98, height=46)
        return btn

    def __tk_label_ldv7mc5j(self):
        label = Label(self,text="店铺名",anchor="center")
        label.place(x=30, y=90, width=226, height=24)
        return label

    def __tk_label_ldv7mevf(self):
        label = Label(self,text="信用等级",anchor="center")
        label.place(x=30, y=140, width=227, height=24)
        return label

    def __tk_label_ldv7qo7p(self):
        label = Label(self,text="创店时间",anchor="center")
        label.place(x=30, y=190, width=229, height=24)
        return label

    def __tk_label_ldv7r0at(self):
        label = Label(self,text="老店标",anchor="center")
        label.place(x=30, y=240, width=229, height=24)
        return label

    def __tk_label_ldv7rkbh(self):
        label = Label(self,text="店铺订阅",anchor="center")
        label.place(x=30, y=290, width=228, height=24)
        return label

    def __tk_label_ldvpgl8w(self):
        label = Label(self,text="cookie:",anchor="center")
        label.place(x=30, y=10, width=50, height=24)
        return label

    def __tk_input_ldvph0bo(self):
        ipt = Entry(self)
        ipt.place(x=100, y=10, width=462, height=24)
        return ipt

    def __tk_label_ldvphjq7(self):
        label = Label(self,text="标签",anchor="center")
        label.place(x=30, y=340, width=529, height=106)
        return label

class Frame_ldv3hjab_8(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_text_ldv5ddcv = self.__tk_text_ldv5ddcv()
    def __frame(self):
        self.place(x=0, y=0, width=600, height=500)

    def __tk_text_ldv5ddcv(self):
        text = Text(self,borderwidth=0,background='#f0f0f0',highlightcolor='#f0f0f0',highlightbackground='#f0f0f0')
        text.place(x=150, y=30, width=300, height=424)
        text.config(state=DISABLED)
        
        return text

class Frame_ldv7ry0d(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.__frame()
        self.tk_label_ldv7s4hp = self.__tk_label_ldv7s4hp()
    
    def __frame(self):
        self.place(x=310, y=90, width=247, height=222)

    def __tk_label_ldv7s4hp(self):
        label = Label(self,text="这里是店铺头像",anchor="center")
        label.place(x=50, y=60, width=164, height=24)
        return label

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def post(self,webhook):
        bo = {
            'msgtype': 'markdown',
            'markdown': {
                "content": f'webhook post sucessful'
            }
        }
        requests.post(webhook,headers={'Content-Type': 'application/json'},
                 data=json.dumps(bo))

    def inertT(self,entryv,t):
        entryv.config(state=NORMAL)
        entryv.insert(END,t+'\n')
        entryv.see(END)
        entryv.config(state=DISABLED)


    def submit0(self,evt):
        print("info",evt)
        '''
            请求我的客户资源 
            用re提取登记人名
        '''
        self.cookie = self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_input_ldv4xo0c.get()
        self.cookie = self.cookie if self.cookie != '' else '未输入cookie'
        if self.cookie == '':return 0
        self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_text_ldv4wo77,self.cookie)
        url = 'https://letaojiabackstage.letaojiashop.com/Member/GetMeunData?page=1&limit=20'
        headers ={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.23',
            'Cookie': self.cookie,
            'Content-Type': 'application/json'}
        try:
            req = requests.get(url=url,headers=headers)
        except:
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_text_ldv4wo77,'cookie 出错')
            return 0
        reqq = json.loads(req.text)
        if reqq['count'] == 0:
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_text_ldv4wo77,'请先在会员列表创建一个会员')
            return 0
        reqqq = reqq.get('data')
        id = reqqq[0]['userid']
        url2 = f'https://letaojiabackstage.letaojiashop.com/Member/MemberEdit?id={int(id)}'
        print(url2)
        req2 = requests.get(url=url2,headers=headers)
        html = req2.text
        # print(html)
        self.name = re.findall(r'<option value="(.*?)" selected>(.*?)</option>',html)
        self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_text_ldv4wo77,f'你好：{self.name[1][1].strip()}')
        return self.name

    
    def submit00(self,evt):
        print("post later",evt)
        '''
        test post link
        '''
        self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_text_ldv4wo77,self.name[1][1].strip())
        # webhook = self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_input_ldv5066a.get()

        # self.post(webhook)
        
    def submit1(self,evt):
        print("guadian writting",evt)
        self.wangwang = self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_input_ldv7dgph.get()
        self.phone = self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_input_ldv7dl5w.get()
        if self.wangwang == '':
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_text_ldv7dw4e,'输入旺旺')
            return 0
        elif self.phone == '':
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_text_ldv7dw4e,'输入手机号')
            return 0
        headers ={
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.23',
            'Cookie': self.cookie,
            'Content-Type': 'application/json'}
        body = {
            'itemid': 0,
            'title': '西南地区1皇冠珠宝首饰淘宝网店',
            'areaid': 23,
            'catid': 9,
            'credit': 11,
            'typeid': 46,
            'titleTips':'', 
            'fuwuguwen': int(self.name[1][0]),
            'price': 10000,
            'lowPrice': 10000,
            'renzhengleixing': '个人',
            'creattime': 2023,
            'goodpercent': 99,
            'bail': 0,
            'bailreturn': 0,
            'jishunianfei': 0,
            'nianfeiReturn': 0,
            'flowers': 0,
            'fans': 0,
            'xuni': 0,
            'sellType': '协议变更,',
            'mobile': self.phone,
            'memberid': '9ac50857d48418b0',
            'qq': self.phone,
            'ali':'', 
            'shopurl': self.wangwang, 
            'shopkeeper': self.wangwang,
            'newTmall': 0,
            'tmalltype': '',
            'otherTypes':'', 
            'select':'', 
            'erjileimu':'', 
            'tradeMark':'', 
            'angleMark': 0,
            'pasteCard': 0,
            'zhucezijin': 0,
            'jiaonazizhi':'', 
            'xufeijiezhi':'', 
            'score2': 0,
            'score1bi': '高',
            'score3':0, 
            'score2bi':'高',
            'score1': 0,
            'score3bi':'高',
            'yibankoufen': 0,
            'yanzhongkoufen': 0,
            'jiamaokoufen': 0,
            'jignyingzhuangtai':'', 
            'creditScore': '',
            'huoyuan':0,
            'malltag':'', 
            'introduce': '西南地区,1皇冠珠宝首饰淘宝网店,好评99%，动态全红！强烈推荐！',
            'file':'', 
            'thumb':'', 
            'pointsScreen':'', 
        }
        url = 'https://letaojiabackstage.letaojiashop.com/Mall/MallEdit'
        try:
            req = requests.post(url=url,headers=headers,data=json.dumps(body))
        except:
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_text_ldv7dw4e,'旺旺或手机号出错，或者已存在相同旺旺')
            return 0
        req = json.loads(req.text)
        print(req)
        try:
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_text_ldv7dw4e,req['msg'])
        except:
            self.inertT(self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_text_ldv7dw4e,req['message'])

    
    def submit2(self,evt):
        print("<Button-1>事件未处理",evt)

    def submit3(self,evt):
        print("<Button-1>事件未处理",evt)

    def submit4(self,evt):
        print("<Button-1>事件未处理",evt)

    def submit5(self,evt):
        print("sort",evt)
        items = self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_5.tk_table_ldv7iw6p.get_children()
        [self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_5.tk_table_ldv7iw6p.delete(item) for item in items]
        self.data = self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_5.tk_input_ldv7jn0o.get().split(',')
        self.teams = self.data[::2]
        '''
        此处 获取 各组的 放款金额
        '''
        headers = {
        'cookie' : 'USER-AGENTLTJ=FDF5Zp1BZwus4mdt2vhDi26PQA+cx91yN0ZHxsW6H2kS0Dgx2scihw//jn3Lgzz1Kz6TJwagloy/oTnMBLZpz/Q+RpbSK87LImBDwd1MDJ8N5PBAmUiMsMyIBmpZj+eqjZ7qRmuvDNz8AsWuAcAIQcSUKWTW/yKfuBA+ZtshQYs=',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.23',
        'Connection': 'close'
    }

        url_count = 'https://letaojiabackstage.letaojiashop.com/Common/GroupsRank?ssTime={}&eeTime={}'.format(\
    datetime.datetime.now().strftime('%Y-%m-%d'),datetime.datetime.now().strftime('%Y-%m-%d'))
        req = requests.get(url = url_count,headers=headers)
        html = req.text
        top3d = re.findall('<h6>(.*?)</h6>.*?<p>(\d+)</p>\n<span>已成交</span>',html,re.S)
        top3d = top3d[:3]
        # other data
        odata = re.findall(r'<td class="color">(.*?)</td.*?<span.*?<td.*?<td.*?<td>(\d+)</',html,re.S) 
        odata = odata[:21]
        cd = []
        for i in top3d+odata:
            for g in self.teams:
                if g in i:
                    cd.append(i)
        print(cd)
        acd = []
        for i in cd:
            i = list(i)
            i.append(self.data[self.data.index(i[0])+1])
            i.append(float(i[1])/int(self.data[self.data.index(i[0])+1]))
            acd.append(i)
        acd.sort(key=lambda acd:acd[3],reverse=True)
        print(acd)
        '''
        打印到表上
        '''
        for i in range(len(cd)):
            self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_5.tk_table_ldv7iw6p.insert('',i,
            values = (acd[i][0],acd[i][1],acd[i][2],acd[i][3]))


    def submit6(self,evt):
        print("<Button-1>事件未处理",evt)

    def submit7(self,evt):
        print("<Button-1>事件未处理",evt)
        
    def __event_bind(self):
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_button_ldv4xyzv.bind('<Button-1>',self.submit0)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_0.tk_button_ldv4xyzvv.bind('<Button-1>',self.submit00)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_1.tk_button_ldv7dock.bind('<Button-1>',self.submit1)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_2.tk_button_ldvp14cz.bind('<Button-1>',self.submit2)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_3.tk_button_ldv7i1wc.bind('<Button-1>',self.submit3)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_4.tk_button_ldvp7mff.bind('<Button-1>',self.submit4)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_5.tk_button_ldv7kfgx.bind('<Button-1>',self.submit5)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_6.tk_button_ldv7kroz.bind('<Button-1>',self.submit6)
        self.tk_tabs_ldv3hjab.tk_tabs_ldv3hjab_7.tk_button_ldv7m1jj.bind('<Button-1>',self.submit7)
        
if __name__ == "__main__":
    win = Win()
    win.mainloop()
