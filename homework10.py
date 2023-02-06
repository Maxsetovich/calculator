'''1) 2ta QLabel va 2ta QLineEdit va 2ta QPushButton e'lon qiling.
1-Qlabel va 1-QLineEdit Login uchun
2-Qlabel va 2-QLineEdit Parol uchun
1-QPushButton SignIn uchun ya'ni foydalanuvchini sistemaga kiritadi va 
"Siz tizimga kirdingiz" MessageBox orqali qilinishi kerak
2-QPushButton esa SignUp uchun ya'ni sizda faylda kamida 10ta Login va parol
yozilgan ro'yhatni ichida mavjud bo'lmasa ushbu login va parolni fayl
ro'yhatiga qo'shib qo'ysin.'''
#1-task
'''
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtWidgets import QLabel,QPushButton,QLineEdit,QMessageBox
from PyQt5.QtGui import QFont
import sys
ls=["Abdulaziz,3477","Mahmud,1234","Jaxa,7777","Umida,8697","Messi,1010"]
print(ls)
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("1-task")
        self.setFixedSize(600,600)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",18))
        obj.move(x,y)
    def start(self):
        login=QLabel("Login:",self)
        self.font(login,50,50)
        self.loginline=QLineEdit(self)
        self.loginline.setPlaceholderText("Username")
        self.font(self.loginline,150,50)
        parol=QLabel("Parol:",self)
        self.font(parol,50,100)
        self.parolline=QLineEdit(self)
        self.parolline.setPlaceholderText("Password")
        self.font(self.parolline,150,100)
        
        self.button1=QPushButton("SignIn",self)
        self.font(self.button1,190,200)
        self.button1.clicked.connect(self.run1)
        self.button2=QPushButton("SignUp",self)
        self.font(self.button2,310,200)
        self.button2.clicked.connect(self.run2)
    def run1(self):
        miniwindow=QMessageBox(self)
        miniwindow.setText("You have successfully signed in!!!")
        miniwindow.show()
    def run2(self):
        a=self.loginline.text()+","+self.parolline.text()
        ls.append(a)
      
oyna=Window()
oyna.show()
app.exec_()
ls=set(ls)
ls=list(ls)
print(ls)
'''
#2-task Tetris
'''
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("2-task")
        self.setFixedSize(700,600)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)
    def font2(self,obj,x,y):
        obj.setFont(QFont("Times",24))
        obj.move(x,y)
        obj.setFixedSize(50,50)
    def start(self):
        b1=QPushButton("1",self)
        self.font(b1,140,400)
        b1.clicked.connect(self.run1)
        b2=QPushButton("2",self)
        self.font(b2,240,400)
        b2.clicked.connect(self.run2)
        b3=QPushButton("3",self)
        self.font(b3,340,400)
        b3.clicked.connect(self.run3)
        b4=QPushButton("4",self)
        self.font(b4,440,400)
        b4.clicked.connect(self.run4)

        self.b11=QPushButton(self); self.b11.hide()
        self.b12=QPushButton(self); self.b12.hide()
        self.b13=QPushButton(self); self.b13.hide()
        self.b14=QPushButton(self); self.b14.hide()
    def run1(self):
        self.font2(self.b11,300,100)
        self.font2(self.b12,300,150)
        self.font2(self.b13,300,200)
        self.font2(self.b14,350,100)
        self.b11.show()
        self.b12.show()
        self.b13.show()
        self.b14.show()
    def run2(self):
        self.font2(self.b11,300,100)
        self.font2(self.b12,300,150)
        self.font2(self.b13,350,100)
        self.font2(self.b14,350,150)
        self.b11.show()
        self.b12.show()
        self.b13.show()
        self.b14.show()
    def run3(self):
        self.font2(self.b11,230,100)
        self.font2(self.b12,280,100)
        self.font2(self.b13,330,100)
        self.font2(self.b14,380,100)
        self.b11.show()
        self.b12.show()
        self.b13.show()
        self.b14.show()
    def run4(self):
        self.font2(self.b11,350,100)
        self.font2(self.b12,300,150)
        self.font2(self.b13,350,150)
        self.font2(self.b14,300,200)
        self.b11.show()
        self.b12.show()
        self.b13.show()
        self.b14.show()            
oyna=Window()
oyna.show()
app.exec_()
'''

#3-task
'''
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLineEdit
from PyQt5.QtGui import QFont
import sys
app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("3-task")
        self.setFixedSize(700,600)
        self.start()
    def font(self,obj,x,y):
        obj.setFont(QFont("Times",20))
        obj.move(x,y)
    def start(self):
        self.line=QLineEdit(self)
        self.line.setPlaceholderText("Enter a number between 1 and 1000")
        self.font(self.line,50,50)
        self.line.setFixedSize(600,50)
        ok=QPushButton("ok",self)
        self.font(ok,310,150)
        ok.clicked.connect(self.run1)
        
        self.b1=QPushButton(self)
        self.font(self.b1,200,400)
        self.b2=QPushButton(self)
        self.font(self.b2,300,400)
        self.b3=QPushButton(self)
        self.font(self.b3,400,400)
        self.b1.hide()
        self.b2.hide()
        self.b3.hide()
    def run1(self):
        a=self.line.text()
        if len(a)==1:
            self.b1.setText(a[0])
            self.b1.show()
        elif len(a)==2:
            self.b1.setText(a[0])
            self.b2.setText(a[1])
            self.b1.show()
            self.b2.show()
        else:
            self.b1.setText(a[0])
            self.b2.setText(a[1])
            self.b3.setText(a[2])
            self.b1.show()
            self.b2.show()
            self.b3.show()
oyna=Window()
oyna.show()
app.exec_()
'''