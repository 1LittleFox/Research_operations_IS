from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
from sympy import *


class Lagranj:
    def __init__(self, root):
        # Шрифты
        self.font_16 = QtGui.QFont()
        self.font_14 = QtGui.QFont()
        self.font_12 = QtGui.QFont()

        self.central_widget = QtWidgets.QWidget(root)                    # Главный виджет
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) # Главный компоновщик

        self.title             = QtWidgets.QLabel()                      # Заголовок
        self.page_h_layout     = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик страницы

        self.interval_h_layout = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик функции

        self.label_b           = QtWidgets.QLabel()                      # Надпись функции
        self.b_edit            = QtWidgets.QLineEdit()                   # Текстовое поле функции

        self.find_h_layout     = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик кнопки поиска
        self.golden_v_layout   = QtWidgets.QVBoxLayout()                 # Вертикальный компоновщик страницы
        self.button_calc       = QtWidgets.QPushButton()                 # Кнопка поиска минимума
        self.result            = QtWidgets.QTextEdit()                   # Результат вычислений
        self.back_h_layout     = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик кнопки назад
        self.button_back       = QtWidgets.QPushButton()                 # Кнопка возврата на главное меню

        # Бинд кнопки поиска минимума
        self.button_calc.clicked.connect(lambda: self.find_extremum())

        self.setupUi(root)

    def setupUi(self, root):
        # Настройка шрифтов
        self.font_16.setPointSize(16)
        self.font_14.setPointSize(14)
        self.font_12.setPointSize(12)

        self.central_widget.setMinimumSize(QtCore.QSize(1000, 700)) # Определение минимального размера окна

        # Настройка заголовка
        self.title.setFont(self.font_16)
        self.title.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.central_layout.addWidget(self.title)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 50, QtWidgets.QSizePolicy.Fixed)
        self.central_layout.addItem(spacer_item)

        # Настройка надписи ввода
        self.label_b.setMinimumSize(QtCore.QSize(30, 70))
        self.label_b.setFont(self.font_16)
        self.interval_h_layout.addWidget(self.label_b)

        # Настройка поля ввода
        self.b_edit.setFont(self.font_12)
        self.b_edit.setMinimumSize(150, 30)
        self.interval_h_layout.addWidget(self.b_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(0, 150, QtWidgets.QSizePolicy.Fixed)
        self.interval_h_layout.addItem(spacer_item)

        self.central_layout.addLayout(self.interval_h_layout)

        # Настройка кнопки вычисления
        self.button_calc.setMaximumSize(QtCore.QSize(300, 60))
        self.button_calc.setFont(self.font_14)
        self.find_h_layout.addWidget(self.button_calc)

        self.golden_v_layout.addLayout(self.find_h_layout)

        # Настройка отображения результата
        self.result.setMaximumSize(QtCore.QSize(1000, 500))
        self.result.setTextColor(QColor("white"))
        self.result.setEnabled(True)
        self.result.setFont(self.font_14)
        self.result.setUndoRedoEnabled(True)
        self.result.setReadOnly(True)
        self.golden_v_layout.addWidget(self.result)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 150, QtWidgets.QSizePolicy.Fixed)
        self.golden_v_layout.addItem(spacer_item)

        # Компоновка
        self.page_h_layout.addLayout(self.golden_v_layout)
        self.central_layout.addLayout(self.page_h_layout)

        # Настройка кнопки возврата на главную
        self.button_back.setMaximumSize(QtCore.QSize(200, 60))
        self.button_back.setFont(self.font_14)
        self.back_h_layout.addWidget(self.button_back)
        self.central_layout.addLayout(self.back_h_layout)

        root.setCentralWidget(self.central_widget)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Метод множителей Лагранжа')
        self.label_b.setText('Введите функцию:')
        self.button_calc.setText('Вычислить экстремум')
        self.result.setText('Здесь будет ответ...')
        self.button_back.setText('На главную')

    # Метод равномерного поиска
    def find_extremum(self):

        if (len(self.b_edit.text()) > 0):

            x, y, z = symbols(' x y z')

            f = eval(self.b_edit.text())
            # -x**2-5*y**2-3*z**2+x*y-2*x*z+ 2*y*z+11 *x+2*y+18*z+10
            # print('Анализируемая функция f  для переменных x,y,z -\n f= ', f)
            print('Необходимые условия экстремума')
            fx = f.diff(x)
            print('df/dx =', fx, '=0')
            fy = f.diff(y)
            print('df/dy =', fy, '=0')
            fz = f.diff(z)
            print('df/dz =', fz, '=0')
            try:
                sols = solve([fx, fy, fz], x, y, z)
            except:
                print(' Функция не дифференцируема')
                raise SystemExit(1)
            fxx = f.diff(x, x).subs({x: sols[x], y: sols[y], z: sols[z]})
            print('fxx=', fxx)
            fxy = f.diff(x, y).subs({x: sols[x], y: sols[y], z: sols[z]})
            print('fxy=', fxy)
            fxz = f.diff(x, z).subs({x: sols[x], y: sols[y], z: sols[z]})
            print('fxz=', fxz)
            fyy = f.diff(y, y).subs({x: sols[x], y: sols[y], z: sols[z]})
            print('fyy=', fyy)
            fzy = f.diff(z, y).subs({x: sols[x], y: sols[y], z: sols[z]})
            print('fyz=', fzy)
            fzz = f.diff(z, z).subs({x: sols[x], y: sols[y], z: sols[z]})
            print('fzz=', fzz)
            fyx = fxy;
            fzx = fxz;
            fyz = fzy  # равенства из условия симметричности матрицы Гессе
            print('Расчёт определителей матрицы Гессе \n («разрастаются» из левого верхнего угла)')
            d1 = fxx
            print('Определитель М1- d1=', d1)
            M2 = Matrix([[fxx, fxy], [fyx, fyy]])
            d2 = M2.det()
            M3 = Matrix([[fxx, fxy, fxz], [fyx, fyy, fyz], [fzx, fzy, fzz]])
            d3 = M3.det()
            print('Достаточные условия экстремума')
            if d1 > 0 and d2 > 0 and d3 > 0:
                self.result.setText('При d1=%s,>0, d2=%s>0, d3=%s>0, минимум f в точке М(%s,%s,%s)' % (
                    str(d1), str(d2), str(d3), str(sols[x]), str(sols[y]), str(sols[z])))
            elif d1 < 0 and d2 > 0 and d3 < 0:
                self.result.setText('При d1=%s,<0, d2=%s>0, d3=%s<0,максимум f в точке М(%s,%s,%s)' % (
                    str(d1), str(d2), str(d3), str(sols[x]), str(sols[y]), str(sols[z])))
            elif d3 != 0:
                self.result.setText('Седло в точке М(%s,%s,%s)' % (str(sols[x]), str(sols[y]), str(sols[z])))
            else:
                self.result.setText('Нет экстремума в точке М(%s,%s,%s)' % (str(sols[x]), str(sols[y]), str(sols[z])))
            r = f.subs({x: sols[x], y: sols[y], z: sols[z]})
            print('Значение %s функции в точке М(%s,%s,%s)' % (str(r), str(sols[x]), str(sols[y]), str(sols[z])))


            # Примеры
            # x**2+2*y**2+3*z**2-2*x*y-2*x*z
            # x**2+y**2+2*z**2-22