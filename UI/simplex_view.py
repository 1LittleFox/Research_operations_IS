from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import math
import scipy.optimize as opt


class Simplex:
    def __init__(self, root):
        # Шрифты
        self.font_16 = QtGui.QFont()
        self.font_14 = QtGui.QFont()
        self.font_12 = QtGui.QFont()

        self.central_widget = QtWidgets.QWidget(root)                    # Главный виджет
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) # Главный компоновщик

        self.page_v_layout = QtWidgets.QVBoxLayout()                     # Вертикальный компоновщик страницы

        self.title = QtWidgets.QLabel()                                  # Заголовок
        self.label_enter_formula = QtWidgets.QLabel()                    # Формула
        self.validator = QtGui.QDoubleValidator()                        # Ограничение на ввод букв
        self.label_x0 = QtWidgets.QLabel()                               # Надпись ввода Х0
        self.x0_edit = QtWidgets.QLineEdit()                             # Текстовое поле X0
        self.x0_edit_2 = QtWidgets.QLineEdit()                           # Текстовое поле X0
        self.label_alpha = QtWidgets.QLabel()                            # Надпись ввода альфа
        self.alpha_edit = QtWidgets.QLineEdit()                          # Текстовое поле альфа
        self.button_extremum = QtWidgets.QPushButton()                   # Кнопка вычисления экстремума функции
        self.result = QtWidgets.QTextEdit()                              # Результат вычислений
        self.horizontal_formula_layout = QtWidgets.QHBoxLayout()         # Горизонтальный компоновщик формулы
        self.horizontal_back_layout = QtWidgets.QHBoxLayout()            # Горизонтальный компоновщик кнопки назад
        self.horizontal_btn_ext_layout = QtWidgets.QHBoxLayout()         # Горизонтальный компоновщик кнопки вычисления
        self.horizontal_textEdit_layout = QtWidgets.QHBoxLayout()        # Горизонтальный компоновщик поля результата
        self.button_back = QtWidgets.QPushButton()                       # Кнопка возврата на главное меню

        self.button_extremum.clicked.connect(lambda: self.search())

        self.setupUi(root)

    def setupUi(self, root):
        # Настройка компонентов интерфейса
        self.font_16.setPointSize(16)
        self.font_14.setPointSize(14)
        self.font_12.setPointSize(12)

        self.central_widget.setMinimumSize(QtCore.QSize(1000, 700))  # Определение минимального размера окна

        # Настройка заголовка
        self.title.setFont(self.font_16)
        self.title.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.central_layout.addWidget(self.title)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Fixed)
        self.central_layout.addItem(spacer_item)

        # --------------------------------------------------------------------------------------------------------------
        # Необходимо для центрирования виджетов
        self.horizontal_formula_layout.addStretch()

        # Настройка надписи ввода формулы
        self.label_enter_formula.setMinimumSize(QtCore.QSize(60, 70))
        self.label_enter_formula.setFont(self.font_16)
        self.horizontal_formula_layout.addWidget(self.label_enter_formula)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_formula_layout.addItem(spacer_item)

        # Настройка надписи ввода Х0
        self.label_x0.setMinimumSize(QtCore.QSize(40, 50))
        self.label_x0.setFont(self.font_16)
        self.horizontal_formula_layout.addWidget(self.label_x0)

        # Настройка поля ввода Х0
        self.x0_edit.setFont(self.font_12)
        self.x0_edit.setMaximumSize(QtCore.QSize(53, 37))
        self.x0_edit.setValidator(self.validator)
        self.horizontal_formula_layout.addWidget(self.x0_edit)

        # Настройка поля ввода Х0
        self.x0_edit_2.setFont(self.font_12)
        self.x0_edit_2.setMaximumSize(QtCore.QSize(53, 37))
        self.x0_edit_2.setValidator(self.validator)
        self.horizontal_formula_layout.addWidget(self.x0_edit_2)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_formula_layout.addItem(spacer_item)

        # Настройка надписи ввода альфа
        self.label_alpha.setMinimumSize(QtCore.QSize(30, 50))
        self.label_alpha.setFont(self.font_16)
        self.horizontal_formula_layout.addWidget(self.label_alpha)

        # Настройка поля ввода альфа
        self.alpha_edit.setFont(self.font_12)
        self.alpha_edit.setMaximumSize(QtCore.QSize(70, 37))
        self.alpha_edit.setValidator(self.validator)
        self.horizontal_formula_layout.addWidget(self.alpha_edit)

        # Необходимо для центрирования виджетов
        self.horizontal_formula_layout.addStretch()

        # Настройка кнопки рассчёта экстремума
        self.button_extremum.setMaximumSize(QtCore.QSize(300, 60))
        self.button_extremum.setFont(self.font_14)
        self.horizontal_btn_ext_layout.addWidget(self.button_extremum)

        # Настройка отображения результата
        self.result.setMaximumSize(QtCore.QSize(1000, 300))
        self.result.setTextColor(QColor("white"))
        self.result.setEnabled(True)
        self.result.setFont(self.font_14)
        self.result.setUndoRedoEnabled(True)
        self.result.setReadOnly(True)
        self.horizontal_textEdit_layout.addWidget(self.result)

        self.page_v_layout.addLayout(self.horizontal_formula_layout)
        self.page_v_layout.addLayout(self.horizontal_btn_ext_layout)
        self.page_v_layout.addLayout(self.horizontal_textEdit_layout)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Fixed)
        self.page_v_layout.addItem(spacer_item)

        self.central_layout.addLayout(self.page_v_layout)

        # Настройка кнопки возврата на главную
        self.button_back.setMaximumSize(QtCore.QSize(200, 60))
        self.button_back.setFont(self.font_14)
        self.horizontal_back_layout.addWidget(self.button_back)
        self.central_layout.addLayout(self.horizontal_back_layout)

        root.setCentralWidget(self.central_widget)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Многомерная оптимизация методом симплекса')
        self.button_back.setText('На главную')
        self.label_enter_formula.setText('F(x,y) = 3x**2+xy+2y**2-x-4y')
        self.label_x0.setText("x0 = ")
        self.label_alpha.setText("α = ")
        self.button_extremum.setText("Вычислить экстремум")
        self.result.setText('Здесь будет ответ...')

    def simplex_func(self, X):
        return (3 * X[0] ** 2 + X[0] * X[1] + 2 * X[1] ** 2 - X[0] - 4 * X[1])

    # Процедура формирования начального симплекса
    def makeInitialSimplex(self, X, L, n, initialSimplex):
        qn = math.sqrt(1.0 + n) - 1.0
        q2 = L / math.sqrt(2.0) * n
        r1 = q2 * (qn + n)
        r2 = q2 * qn
        initialSimplex[0, :] = X
        for j in range(n):
            initialSimplex[j + 1, :] = X + r2
        for i in range(n):
            initialSimplex[i + 1, i] += (r1 - r2)

    def search(self):
        if len(self.x0_edit.text()) > 0 and len(self.x0_edit_2.text()) > 0 and len(self.alpha_edit.text()) > 0:
            # Замена запятой на точку в введённых числах
            def max_numbers(s):
                return max([float(i) for i in s.replace(',', '.').split()])
            n = 2
            x0 = np.zeros(2, dtype=float)  # Вектор с двумя элементами типа float
            # Начальная точка поиска минимума функции
            x0[0] = max_numbers(self.x0_edit.text())
            x0[1] = max_numbers(self.x0_edit_2.text())
            xtol = 1.0e-5  # Точность поиска экстремума
            # Начальная симплекс поиска минимума функции
            initialSimplex = np.zeros((n + 1, n), dtype=float)
            L = max_numbers(self.alpha_edit.text())  # Длина ребра начального симплекса
            # Формируем начальный симплекс
            self.makeInitialSimplex(x0, L, n, initialSimplex)
            # Находим минимум функции
            res = opt.minimize(self.simplex_func, x0, method='Nelder-Mead',
                        options={'xtol': xtol, 'disp': True, 'initial_simplex': initialSimplex})
            self.result.setText(format(res))
