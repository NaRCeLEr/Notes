from database import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import sys
from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtGui import QColor

app = QApplication(sys.argv)


def get(id, title, text):
    data = []
    data.append(id)
    data.append(title)
    data.append(text)
    return data


def openO(x):
    global OtherWindowa
    OtherWindowa = OtherWindow(x)
    OtherWindowa.show()
    window.close()


def openOt(x):
    OtherWindowa.close()
    global OtherWindowt
    OtherWindowt = OtherWindow(x)
    OtherWindowt.show()
    window.close()


def openMfromOthera():
    global window
    window = Window()
    window.show()
    OtherWindowa.close()


def openAdd():
    global ADD
    ADD = Add()
    ADD.show()
    window.close()


def openMfromAdd():
    global window
    window = Window()
    window.exec_()


class OtherWindow(QDialog):

    def __init__(self, arg):
        super(OtherWindow, self).__init__()

        self.setStyleSheet(
            "background-color: '#fff';"
        )
        self.setWindowTitle(arg)
        self.setGeometry(330, 330, 960, 590)
        aa = get_title(arg)

        layout = QVBoxLayout(self)

        box = QVBoxLayout(self)
        self.setLayout(box)
        scroll = QScrollArea(self)
        scroll.setStyleSheet(
            "border: none;"
        )
        box.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrolc = QWidget(scroll)
        scrolc.setGeometry(0, 20, 960, 560)
        layout = QVBoxLayout(scrolc)
        scrolc.setLayout(layout)

        scroll.setGeometry(0, 0, 960, 580)

        b = []
        a = sel_all()
        for item in a:
            eff = QGraphicsDropShadowEffect(offset=QPoint(4, 4), blurRadius=10, color=QColor("#111"))
            self.text = QPushButton(self)
            self.text.setGraphicsEffect(eff)
            self.text.setGeometry(0, 0, 130, 70)
            self.text.setText(item)
            self.text.setMaximumSize(130, 70)
            self.text.resize(10, 10)
            self.text.setStyleSheet(
                "height: 130px;" +
                "weight: 50px;" +
                "border: 1px solid '#fff';" +
                "border-radius: 10px;"
            )

            x = lambda btn=self.text.text(): btn
            s = lambda x=x(): self.text.clicked.connect(lambda c=self.x: openOt(x))
            s()
            b.append(self.text)

        for i in b:
            layout.addWidget(i)

        scroll.setWidget(scrolc)

        self.setLayout(layout)

        line = QWidget(self)
        line.setGeometry(150, 0, 2, 650)
        line.setStyleSheet(
            "background-color: grey;"
        )

        title = QLineEdit(self)
        title.setPlaceholderText("title")
        title.setGeometry(155, 2, 805, 50)
        title.setText(aa[0][1])
        title.setStyleSheet(
            "border: 2px solid grey;"
            "border-radius: 15px;"
        )

        text = QTextEdit(self)
        text.setStyleSheet(
            "border: 2px solid grey;"
            "border-radius: 15px;"
        )
        text.setPlaceholderText("Note")
        text.setGeometry(155, 55, 805, 580)
        text.setText(aa[0][2])


        btn = QPushButton(self)
        btn.setGeometry(750, 540, 50, 50)
        btn.setText('Save')

        data = lambda titles=title, texts=text: get(aa[0][0], titles.text(), texts.toPlainText())
        f = lambda: data()
        btn.clicked.connect(lambda: [update(f()), openMfromOthera()])


class Window(QDialog):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Notes")
        self.setGeometry(330, 330, 960, 580)

        box = QVBoxLayout(self)
        self.setLayout(box)
        scroll = QScrollArea(self)
        scroll.setStyleSheet(
            "border: none;"
        )
        box.addWidget(scroll)
        scroll.setWidgetResizable(True)
        scrolc = QWidget(scroll)
        scrolc.setGeometry(0, 20, 960, 560)
        scrollL = QGridLayout(scrolc)
        scrolc.setLayout(scrollL)

        scroll.setGeometry(0, 0, 960, 580)

        b = []
        c, f = 0, 0
        a = sel_all()
        for item in a:
            eff = QGraphicsDropShadowEffect(offset=QPoint(4, 4), blurRadius=10, color=QColor("#111"))
            self.text = QPushButton(self)
            self.text.setGraphicsEffect(eff)
            self.text.setText(item)
            self.text.  resize(10, 50)
            self.text.setMaximumSize(300, 200)
            self.setMinimumSize(200, 100)
            self.text.setStyleSheet(
                "height: 130px;" +
                "border: 1px solid '#fff';" +
                "border-radius: 15px;"
            )

            x = lambda btn=self.text.text(): btn
            s = lambda x=x(): self.text.clicked.connect(lambda c=self.x: openO(x))
            s()
            b.append(self.text)

        for i in b:
            if f == 5:
                c+=1
                f =0
            scrollL.addWidget(i, c, f)
            f += 1
        scroll.setWidget(scrolc)


        self.setLayout(scrollL)


        self.add = QPushButton(self)
        self.add.setText("Add Note")
        self.add.setGeometry(3, 3, 80, 40)
        self.add.setStyleSheet(
            "height: 50px;" +
            "border: 2px solid grey;" +
            "border-radius: 15px;"
        )
        self.add.clicked.connect(lambda: openAdd())



class Add(QDialog):
    def __init__(self):
        super(Add, self).__init__()

        self.setWindowTitle("AddNote")
        self.setGeometry(330, 330, 960, 590)

        id = QLineEdit(self)
        id.setGeometry(1, 1, 955, 30)
        id.setPlaceholderText('id')
        id.setStyleSheet(
            "border: 2px solid grey;" +
            "border-radius: 15px;"
        )
        title = QLineEdit(self)
        title.setGeometry(1, 35, 955, 40)
        title.setPlaceholderText('Title')
        title.setStyleSheet(
            "border: 2px solid grey;" +
            "border-radius: 15px;"
        )
        text = QTextEdit(self)
        text.setGeometry(20, 80, 900, 440)
        text.setPlaceholderText("Note")
        text.setStyleSheet(
            "border: 4px solid grey;"
        )
        btn = QPushButton(self)
        btn.setGeometry(870, 530, 50, 50)
        btn.setText("Save")

        data = lambda id=id, titles=title, texts=text: get(int(id.text()), titles.text(), texts.toPlainText())
        f = lambda: data()
        btn.clicked.connect(lambda: [add(f()), openMfromAdd()])


global window
window = Window()
window.show()

sys.exit(app.exec_())