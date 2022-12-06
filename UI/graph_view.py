from PyQt5.QtWidgets import QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np


class GraphView:
    def __init__(self, root):
        # Шрифты
        self.font_16 = QtGui.QFont()
        self.font_14 = QtGui.QFont()
        self.font_12 = QtGui.QFont()

        self.central_widget = QtWidgets.QWidget(root)                    # Главный виджет
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) # Главный компоновщик

        self.title = QtWidgets.QLabel()                                   # Heading
        self.horizontal_formula_layout = QtWidgets.QHBoxLayout()         # Horizontal Formula Builder
        self.layout = QtWidgets.QHBoxLayout()                            # Горизонтальный компоновщик интервалов
        self.label_enter_formula = QtWidgets.QLabel()                     # Надпись ввода формулы
        self.formula_edit = QtWidgets.QLineEdit()                         # Текстовое поле формулы
        self.button_build = QtWidgets.QPushButton()                       # Кнопка построения графика
        self.horizontal_back_layout = QtWidgets.QHBoxLayout()             # Горизонтальный компоновщик кнопки назад
        self.button_back = QtWidgets.QPushButton()                       # Кнопка возврата на главное меню

        self.x1_label = QtWidgets.QLabel()                               # Надпись ввода начального значения интервала х
        self.x1_edit = QtWidgets.QLineEdit()                             # Текстовое поле начального значения интервала х
        self.x2_label = QtWidgets.QLabel()                               # Надпись ввода конечного значения интервала х
        self.x2_edit = QtWidgets.QLineEdit()                             # Текстовое поле конечного значения интервала х

        self.step_x_label = QtWidgets.QLabel()                           # Надпись ввода шага х
        self.step_x_edit = QtWidgets.QLineEdit()                         # Текстовое поле шага х

        self.y1_label = QtWidgets.QLabel()                               # Надпись ввода начального значения интервала y
        self.y1_edit = QtWidgets.QLineEdit()                             # Текстовое поле начального значения интервала y
        self.y2_label = QtWidgets.QLabel()                               # Надпись ввода конечного значения интервала y
        self.y2_edit = QtWidgets.QLineEdit()                             # Текстовое поле конечного значения интервала y

        self.step_y_label = QtWidgets.QLabel()                           # Надпись ввода шага y
        self.step_y_edit = QtWidgets.QLineEdit()                         # Текстовое поле шага х

        # Создание системы координат
        self.canvas = FigureCanvas(Figure())
        self.axes   = self.canvas.figure.add_subplot(111, projection='3d')

        # Бинд кнопки построения графика
        self.button_build.clicked.connect(lambda: self.build_plot())

        self.setupUi(root)

    def setupUi(self, root):
        # Настройка компонентов интерфейса
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

        # Настройка надписи ввода
        self.label_enter_formula.setMinimumSize(QtCore.QSize(60, 70))
        self.label_enter_formula.setFont(self.font_16)
        self.horizontal_formula_layout.addWidget(self.label_enter_formula)

        # Настройка поля ввода
        self.formula_edit.setFont(self.font_12)
        self.horizontal_formula_layout.addWidget(self.formula_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_formula_layout.addItem(spacer_item)

        # Настройка кнопки построения графика
        self.button_build.setMinimumSize(QtCore.QSize(200, 60))
        self.button_build.setFont(self.font_14)
        self.horizontal_formula_layout.addWidget(self.button_build)
        self.central_layout.addLayout(self.horizontal_formula_layout)

        # Настройка интервала X
        self.x1_label.setMaximumSize(QtCore.QSize(250, 60))
        self.x1_label.setFont(self.font_14)
        self.x1_label.setText("Введите интервал для x, от:")
        self.layout.addWidget(self.x1_label)

        self.x1_edit.setMaximumSize(QtCore.QSize(100, 40))
        self.x1_edit.setFont(self.font_14)
        self.layout.addWidget(self.x1_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed)
        self.layout.addItem(spacer_item)

        self.x2_label.setMaximumSize(QtCore.QSize(50, 40))
        self.x2_label.setFont(self.font_14)
        self.x2_label.setText("до:")
        self.layout.addWidget(self.x2_label)

        self.x2_edit.setMaximumSize(QtCore.QSize(100, 40))
        self.x2_edit.setFont(self.font_14)
        self.layout.addWidget(self.x2_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed)
        self.layout.addItem(spacer_item)

        self.step_x_label.setMaximumSize(QtCore.QSize(50, 50))
        self.step_x_label.setFont(self.font_14)
        self.step_x_label.setText("Шаг:")
        self.layout.addWidget(self.step_x_label)

        self.step_x_edit.setMaximumSize(QtCore.QSize(100, 40))
        self.step_x_edit.setFont(self.font_14)
        self.layout.addWidget(self.step_x_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Fixed)
        self.layout.addItem(spacer_item)

        # Настройка интервала Y
        self.y1_label.setMaximumSize(QtCore.QSize(250, 60))
        self.y1_label.setFont(self.font_14)
        self.y1_label.setText("Введите интервал для y, от:")
        self.layout.addWidget(self.y1_label)

        self.y1_edit.setMaximumSize(QtCore.QSize(100, 40))
        self.y1_edit.setFont(self.font_14)
        self.layout.addWidget(self.y1_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(5, 20, QtWidgets.QSizePolicy.Fixed)
        self.layout.addItem(spacer_item)

        self.y2_label.setMaximumSize(QtCore.QSize(50, 40))
        self.y2_label.setFont(self.font_14)
        self.y2_label.setText("до:")
        self.layout.addWidget(self.y2_label)

        self.y2_edit.setMaximumSize(QtCore.QSize(100, 40))
        self.y2_edit.setFont(self.font_14)
        self.layout.addWidget(self.y2_edit)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed)
        self.layout.addItem(spacer_item)

        self.step_y_label.setMaximumSize(QtCore.QSize(50, 50))
        self.step_y_label.setFont(self.font_14)
        self.step_y_label.setText("Шаг:")
        self.layout.addWidget(self.step_y_label)

        self.step_y_edit.setMaximumSize(QtCore.QSize(100, 40))
        self.step_y_edit.setFont(self.font_14)
        self.layout.addWidget(self.step_y_edit)

        # Настройка расположения лайаута
        self.layout.addStretch()

        self.central_layout.addLayout(self.layout)
        self.central_layout.addWidget(self.canvas)

        # --------------------------------------------------------------------------------------------------------------

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed)
        self.central_layout.addItem(spacer_item)

        # Настройка кнопки возврата на главную
        self.button_back.setMaximumSize(QtCore.QSize(200, 60))
        self.button_back.setFont(self.font_14)
        self.horizontal_back_layout.addWidget(self.button_back)
        self.central_layout.addLayout(self.horizontal_back_layout)

        root.setCentralWidget(self.central_widget)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Построение графика')
        self.label_enter_formula.setText('F(x,y) =')
        self.formula_edit.setPlaceholderText('Введите формулу')
        self.button_build.setText('Построить')
        self.button_back.setText('На главную')

    def build_plot(self):
        self.formula_edit.setPlaceholderText('Введите формулу')

        def max_numbers(s):
            return max([float(i) for i in s.replace(',', '.').split()])

        try:
            formula = self.formula_edit.text() # Ввод формулы
            # Ввод интервалов и шагов
            a = max_numbers(self.x1_edit.text())
            b = max_numbers(self.x2_edit.text())
            c = max_numbers(self.step_x_edit.text())
            d = max_numbers(self.y1_edit.text())
            e = max_numbers(self.y2_edit.text())
            f = max_numbers(self.step_y_edit.text())

            # Адаптация формулы
            formula = formula.replace('^', '**')
            formula = formula.replace('sqrt', 'np.sqrt')
            formula = formula.replace('sin', 'np.sin')
            formula = formula.replace('cos', 'np.cos')
            formula = formula.replace('tan', 'np.tan')
            formula = formula.replace('exp', 'np.exp')
            formula = formula.replace('log', 'np.log')

            if formula and a and b and c and d and e and f: # если все значения введены
                # область отрисовки графика
                x = np.arange(a, b, c)
                y = np.arange(d, e, f)
                x, y = np.meshgrid(x, y)
                z = eval(formula)  # Вычисление высот в точках

                # Примеры формул
                # z = sqrt(x)*sin(x)*exp(cos(y))
                # z = x^3 + y^3 - 3 * x * y

                self.axes.cla()                               # очистка графика
                self.axes.plot_surface(x, y, z, cmap='inferno') # построение поверхности
                self.canvas.draw()                            # отрисовка графика
        except Exception:
            self.formula_edit.setPlaceholderText('Некорректная формула! Введите новую')
            self.formula_edit.setText('')