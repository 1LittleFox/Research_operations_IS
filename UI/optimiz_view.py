from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
import math as m


class optimiz:
    def __init__(self, root):
        # Шрифты
        self.font_16 = QtGui.QFont()
        self.font_14 = QtGui.QFont()
        self.font_12 = QtGui.QFont()

        self.central_widget = QtWidgets.QWidget(root)                    # Главный виджет
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) # Главный компоновщик

        self.title             = QtWidgets.QLabel()                      # Заголовок
        self.page_h_layout     = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик страницы

        self.function_h_layout = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик функции
        self.label_f           = QtWidgets.QLabel()                      # Надпись функции F
        self.f_edit            = QtWidgets.QLabel()                      # Текстовое F
        self.f_edit.setText("0.09*xi^2-0.6*xi+1")

        self.label_n = QtWidgets.QLabel()                                # Надпись n
        self.n_edit = QtWidgets.QLineEdit()                              # Поле ввода количества вычислений функции

        self.interval_h_layout = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик интервала
        self.label_a           = QtWidgets.QLabel()                      # Надпись граница интервала А
        self.a_edit            = QtWidgets.QLineEdit()                   # Текстовое поле А

        self.label_b           = QtWidgets.QLabel()                      # Надпись граница интервала B
        self.b_edit            = QtWidgets.QLineEdit()                   # Текстовое поле B

        self.find_h_layout     = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик кнопки поиска
        self.golden_v_layout   = QtWidgets.QVBoxLayout()                 # Вертикальный компоновщик страницы
        self.button_calc       = QtWidgets.QPushButton()                 # Кнопка поиска минимума
        self.result            = QtWidgets.QTextEdit()                   # Результат вычислений
        self.back_h_layout     = QtWidgets.QHBoxLayout()                 # Горизонтальный компоновщик кнопки назад
        self.button_back       = QtWidgets.QPushButton()                 # Кнопка возврата на главное меню

        # Бинд кнопки поиска минимума
        self.button_calc.clicked.connect(lambda: self.find_minimum())

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

        # --------------------------------------------------------------------------------------------------------------

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 150, QtWidgets.QSizePolicy.Fixed)
        self.central_layout.addItem(spacer_item)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(550, 20, QtWidgets.QSizePolicy.Fixed)
        self.function_h_layout.addItem(spacer_item)

        # Настройка надписи ввода
        self.label_f.setMinimumSize(QtCore.QSize(50, 70))
        self.label_f.setFont(self.font_16)
        self.function_h_layout.addWidget(self.label_f)

        # Настройка поля ввода
        self.f_edit.setFont(self.font_16)
        self.function_h_layout.addWidget(self.f_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(500, 20, QtWidgets.QSizePolicy.Fixed)
        self.function_h_layout.addItem(spacer_item)

        self.central_layout.addLayout(self.function_h_layout)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed)
        self.interval_h_layout.addItem(spacer_item)

        # Настройка надписи ввода
        self.label_a.setMinimumSize(QtCore.QSize(30, 70))
        self.label_a.setFont(self.font_16)
        self.interval_h_layout.addWidget(self.label_a)

        # Настройка поля ввода
        self.a_edit.setFont(self.font_12)
        self.a_edit.setMinimumSize(150, 30)
        self.interval_h_layout.addWidget(self.a_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed)
        self.interval_h_layout.addItem(spacer_item)

        # Настройка надписи ввода
        self.label_b.setMinimumSize(QtCore.QSize(30, 70))
        self.label_b.setFont(self.font_16)
        self.interval_h_layout.addWidget(self.label_b)

        # Настройка поля ввода
        self.b_edit.setFont(self.font_12)
        self.b_edit.setMinimumSize(150, 30)
        self.interval_h_layout.addWidget(self.b_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Fixed)
        self.interval_h_layout.addItem(spacer_item)

        # Настройка надписи ввода
        self.label_n.setMinimumSize(QtCore.QSize(30, 70))
        self.label_n.setFont(self.font_16)
        self.interval_h_layout.addWidget(self.label_n)

        # Настройка поля ввода
        self.n_edit.setFont(self.font_12)
        self.n_edit.setMinimumSize(150, 30)
        self.interval_h_layout.addWidget(self.n_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed)
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

        # --------------------------------------------------------------------------------------------------------------

        # Настройка кнопки возврата на главную
        self.button_back.setMaximumSize(QtCore.QSize(200, 60))
        self.button_back.setFont(self.font_14)
        self.back_h_layout.addWidget(self.button_back)
        self.central_layout.addLayout(self.back_h_layout)

        root.setCentralWidget(self.central_widget)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Оптимизация методом равномерного поиска.')
        self.label_f.setText('f(x) =')
        self.label_a.setText('а =')
        self.label_b.setText('b =')
        self.label_n.setText('n =')
        self.button_calc.setText('Найти минимум')
        self.result.setText('Здесь будет ответ...')
        self.button_back.setText('На главную')

    # Метод равномерного поиска
    def find_minimum(self):

        if len(self.a_edit.text()) > 0 and len(self.b_edit.text()) > 0 and len(self.n_edit.text()) > 0:
            # Замена запятой на точку в введённых числах
            def max_numbers(s):
                return max([float(i) for i in s.replace(',', '.').split()])

            a = max_numbers(self.a_edit.text())
            b = max_numbers(self.b_edit.text())
            n = int(self.n_edit.text())

            e = 0.1
            k = 0
            xi_dict = []
            func_dict = []
            while e < abs(a - b):
                i_min = int()
                func_min = float()
                xi_dict.clear()
                func_dict.clear()
                delta = (abs(a - b)) / n
                for i in range(0, n + 1):
                    xi = a + i * delta
                    xi_dict.append(xi)
                    function = 0.09 * xi ** 2 - 0.6 * xi + 1
                    func_dict.append(function)
                    if func_min > function or func_min == float():
                        func_min = function
                        i_min = i
                if i_min <= 1:
                    a = xi_dict[0]
                    b = xi_dict[1]
                elif i_min == n:
                    a = xi_dict[i_min - 1]
                    b = xi_dict[i_min]
                else:
                    a = xi_dict[i_min + 1]
                    b = xi_dict[i_min - 1]
                k += 1
            self.result.setText(format(xi_dict[i_min]))
