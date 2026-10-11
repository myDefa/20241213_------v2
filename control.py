"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:905019785
在线反馈:https://support.qq.com/product/618914
"""
# 示例下载 https://www.pytk.net/blog/1702564569.html
from tkinter import filedialog
import tkinter as tk
from ui_v2 import Win
import re
import chardet

class Controller:
    # 导入UI类后，替换以下的 object 类型，将获得 IDE 属性提示功能
    ui_v2: Win  # 建立IDE链接, 方便索引
    def __init__(self):
        self.file_path = ""
        self.location, self.name, self.command = "", "", ""
        self.KEYWORD = "光芒"

    def init(self, Win):
        """
        得到UI实例，对组件进行初始化配置
        """
        self.ui_v2 = Win
        self.ui_v2.tk_text_show_filepath.insert(tk.END, f"未选择文件")

    # TODO 组件初始化 赋值操作
    def search1_1(self, evt):
        print("<search1_1-2>事件未处理:", evt)
    def Search2_2(self,evt):
        print("<Return>事件未处理:",evt)
    def GetResult(self,evt):
        print("<Button-123>事件未处理:",evt)
    def Search3_3(self,evt):
        print("<Return>事件未处理:",evt)
    def Search4_4(self,evt):
        print("<Return>事件未处理:",evt)

    def upload_file(self,evt):
        self.file_path = filedialog.askopenfilename(title="选择文件")
        self.ui_v2.tk_text_show_filepath.delete(1.0, tk.END)
        # 将文件路径显示在标签上
        if self.file_path:
            self.ui_v2.tk_text_show_filepath.insert(tk.END, f"{self.file_path}")
        else:
            self.ui_v2.tk_text_show_filepath.insert(tk.END, f"未选择文件")
        self.location, self.name, self.command = self.GetMessageFromText(
            self.GetTextFromFile(self.file_path))

    def return_menu(self, evt):
        print("<Button-1>事件未处理:", evt)

    def GetMessageFromText(self, content):
        location = []
        Name = []
        command = []
        for line in content:
            if line != "\n":
                try:
                    PinDao = re.findall("\(.*?\)", line)[0]
                    Wanjia = re.findall("\[.*?\]", line)[0]
                except IndexError:
                    print(f'IndexError Occur, The Current Message "{line.strip()}" has been bypassed')

                Pinglun = line.replace(PinDao, "").replace(Wanjia, "")
                location.append(PinDao)
                Name.append(Wanjia)
                command.append(Pinglun.rstrip())
        return location, Name, command  # 待整理成message数组

    def GetTextFromFile(self, path: str):
        with open(path, "rb") as f:  # 检测编码格式
            content = f.read()

            result = chardet.detect(content)
            encoding = result['encoding']

        with open(path, "r", encoding=encoding) as f:
            next(f)
            content = f.readlines()
            for index, line in enumerate(content):
                if "2024-10" in content[index]:
                    content.pop(index)
        return content

    def SearchFromMessage(self, evt):
        result = ""
        Name_filtered = []
        _kw = self.ui_v2.tk_input_keyword1.get().strip()
        if _kw:
            self.KEYWORD = _kw
        for i in range(0, len(self.command)):
            if self.KEYWORD in self.command[i]:  # 锁定关键词评论
                if self.name[i] not in Name_filtered:  # 过滤重复玩家
                    Name_filtered.append(self.name[i])
                    # location = Command[i].find(KEYWORD)
                    # fp_print.write(Name[i] + Command[i].replace(KEYWORD, f"\033[91m" + KEYWORD + "\033[0m").rstrip())
                    str1 = self.name[i]
                    # str2 = self.command[i].replace(self.KEYWORD, f"\033[91m" + self.KEYWORD + "\033[0m").rstrip()
                    str2 = self.command[i]
                    result += str1 + ":    " + str2 + "\n"
                    # print(str1, end=":    ")
                    # print(str2)
                    # fp_print.write(str1 + ":    " + str2 + "\n")  # txt文本无法输出颜色
        self.ui_v2.tk_text_Result.insert(1.0, result, 'white')
        # return result
