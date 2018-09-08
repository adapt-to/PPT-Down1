#coding:utf-8
import requests
import bs4
import sys
import html5lib
import math
import time
import os

from qt4_article import *
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class slot_con(QtGui.QWidget, Ui_Form): # 定义槽函数
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.calibration_status = False
		self.parameter_status = False
		self.return1 = return_text()
		self.ppt = down_ppt()

	def con_serial(self, message): #槽函数
		starttime = time.strftime("%H:%M:%S - ", time.localtime(time.time()))

		self.textBrowser_1.append(starttime + str(message))
		textcursor = QtGui.QTextCursor(self.textBrowser_1.textCursor())
		self.textBrowser_1.moveCursor(textcursor.atStart())

		text1 = self.return1.request1(str(message))
		if text1 == 1: #开始下载标志

			list1 = self.ppt.pages(self.ppt.target, self.ppt.nums)
			#print(self.ppt.target, self.ppt.nums)
			#print(list1)
			t = 0
			for i in list1:
				list2 = self.ppt.down_url(i)
				#print("i=",i)
				#print(list2)
				for n in list2:
					t += 1
					self.ppt.down(n, t)
					self.con_serial(float(t))
					if t >= self.ppt.nums:
						break
			#print("下载完成！")
			self.con_serial("下载完成！！！")

			return  1

		text2 = str(text1)
		endtime = time.strftime("%H:%M:%S - ", time.localtime(time.time()))
		self.textBrowser_1.append(endtime + str(message) + text2)
		textcursor = QtGui.QTextCursor(self.textBrowser_1.textCursor()) #自动滚屏
		self.textBrowser_1.moveCursor(textcursor.atStart())

	@QtCore.pyqtSignature("")
	def on_pushButton_1_clicked(self):
		self.ppt.target = self.lineEdit_1.text()
		if self.ppt.target:  # 不为空进入
			self.con_serial(self.ppt.target)  # 调用con_serial函数

	# self.textBrowser_1.append("保存成功\n")

	@QtCore.pyqtSignature("")
	def on_pushButton_2_clicked(self):
		self.ppt.path = self.lineEdit_2.text()
		if not self.ppt.path:
			self.ppt.path = "D:\\优品PPT模板" + time.strftime("-%Y-%m-%d %H %M %S", time.localtime()) + "\\"
		if self.ppt.path:
			self.con_serial(self.ppt.path)

	@QtCore.pyqtSignature("")
	def on_pushButton_3_clicked(self):
		self.ppt.nums = int(self.lineEdit_3.text())  # 填写的下载数减1
		if self.ppt.nums:
			self.con_serial(str(self.ppt.nums))

	@QtCore.pyqtSignature("")
	def on_pushButton_4_clicked(self):
		a = self.con_serial("开始下载ppt......")

class return_text():
	def __init__(self):
		pass
	def request1(self, message):
		if message == "开始下载ppt......":
			return 1

		elif type(message) == float:
			return "已下载" + str(message) + "个"

		elif message == "下载完成！！！":
			return  "下载完成！！！"

		else:
			return "保存成功"



class down_ppt():
	def __init__ (self):
		self.target = ""
		self.nums = 0
		self.path = ""
		#self.urls_list = []
	def pages(self,urls_1,number):
		dijige  = urls_1[-6]
		pp = 0
		try:
			if type(eval(dijige)) == int:
				pp = eval(dijige)
		except:
			pass
		urls_list = []
		urls_list.append(urls_1)
		page = math.ceil(number / 20)
		if page >= 2:
			req = requests.get(url = urls_1)
			html = req.text
			bf = bs4.BeautifulSoup(html,features="html5lib")
			texts = bf.find_all("div", class_ = "page-navi")
			page_urls = texts[0].find_all("a")
			#fo i in page_urls
			for i in range(int(page)-1):
				if pp:
					for n in page_urls:
						if str(pp+1+i) in n.get("href") and str(pp+1+i) == n.text:
							pt = urls_1.split( '/')
							pt[-1] = n.get("href")
							urls_list.append("/".join(pt))
					#urls_list.append(urls_1 + page_urls[i + pp].get("href"))
				else:
					urls_list.append( urls_1 + page_urls[i].get("href"))
		return urls_list #返回包含几页的网址

	def down_url(self, target): # 专门根据 url 获取文章的url
		list_url = []
		req = requests.get(url = target)
		html = req.text
		bf = bs4.BeautifulSoup(html,features="html5lib")
		texts = bf.find_all("a", class_ = "img_preview")
		for i in texts: 
			list_url.append("http://www.ypppt.com/"+str(i.get("href"))) #存放url
		return list_url

	def down(self,ppt_url,num): # 根据ppt的url获得每个ppt的下载链接
		req = requests.get(url = ppt_url)
		html = req.text
		bf = bs4.BeautifulSoup(html,features="html5lib")
		texts = bf.find_all("a", class_ = "down-button")
		rar = texts[0].get("href")
		if not "http" in rar:
			rar = "http://www.ypppt.com/" + rar
		r =  requests.get(rar)
		if not os.path.exists(self.path):
			os.mkdir(self.path)

		with open(self.path+str(num)+".rar","wb") as code:
			code.write(r.content)

class slot(QtGui.QMainWindow):
	def __init__(self,ui,tab):
		QtGui.QMainWindow.__init__(self)
		self.tab = tab

	def graphical_intf(self):
		self.con = slot_con(self.tab)
		self.con.setGeometry(QtCore.QRect(0, 0, 740, 480))

if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv)

	widget = QtGui.QTabWidget()
	widget.resize(750, 500)
	a = QtGui.QFrame(widget)
	a.setGeometry(QtCore.QRect(0, 0, 740, 480))
	w = slot(widget, a)
	w.graphical_intf()
	widget.show()
	sys.exit(app.exec_())
