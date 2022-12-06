from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QInputDialog, QSizePolicy
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np


class HessianView:
    def __init__(self, root):
        # Шрифты
        self.font_16 = QtGui.QFont()
        self.font_14 = QtGui.QFont()
        self.font_12 = QtGui.QFont()

        self.central_widget = QtWidgets.QWidget(root)                    # Главный виджет
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget) # Главный компоновщик

        self.title                     = QtWidgets.QLabel()              # Заголовок
        self.horizontal_hessian_layout = QtWidgets.QHBoxLayout()         # Горизонтальный компоновщик страницы
        self.horizontal_calc_layout    = QtWidgets.QHBoxLayout()         # Горизонтальный компоновщик кнопки вычисления
        self.vertical_hessian_layout   = QtWidgets.QVBoxLayout()         # Вертикальный компоновщик страницы
        self.button_calc               = QtWidgets.QPushButton()         # Кнопка вычисления гессиана
        self.result                    = QtWidgets.QTextEdit()           # Результат вычислений
        self.horizontal_back_layout    = QtWidgets.QHBoxLayout()         # Горизонтальный компоновщик кнопки назад
        self.button_back               = QtWidgets.QPushButton()         # Кнопка возврата на главное меню

        # Бинд кнопки вычисления гессиана
        self.button_calc.clicked.connect(lambda: self.find_optimum(root))

        self.setupUi(root)

    def setupUi(self, root):
        # Настройка шрифтоф
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

        # Настройка кнопки вычисления
        self.button_calc.setMaximumSize(QtCore.QSize(300, 60))
        self.button_calc.setFont(self.font_14)
        self.horizontal_calc_layout.addWidget(self.button_calc)
        self.vertical_hessian_layout.addLayout(self.horizontal_calc_layout)

        # Настройка отображения результата
        self.result.setMaximumSize(QtCore.QSize(1000, 300))
        self.result.setTextColor(QColor("white"))
        self.result.setEnabled(True)
        self.result.setFont(self.font_14)
        self.result.setUndoRedoEnabled(True)
        self.result.setReadOnly(True)
        self.vertical_hessian_layout.addWidget(self.result)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Fixed)
        self.vertical_hessian_layout.addItem(spacer_item)

        # Компоновка
        self.horizontal_hessian_layout.addLayout(self.vertical_hessian_layout)
        self.central_layout.addLayout(self.horizontal_hessian_layout)

        # --------------------------------------------------------------------------------------------------------------

        # Настройка кнопки возврата на главную
        self.button_back.setMaximumSize(QtCore.QSize(200, 60))
        self.button_back.setFont(self.font_14)
        self.horizontal_back_layout.addWidget(self.button_back)
        self.central_layout.addLayout(self.horizontal_back_layout)

        root.setCentralWidget(self.central_widget)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Решение задачи оптимизации')
        self.button_calc.setText('Вычислить гессиан')
        self.result.setText('Здесь будет ответ...')
        self.button_back.setText('На главную')

    def find_optimum(self, root):
        try:
            output = ''
            # СОСТАВЛЕНИЕ ГЕССЕАНА #####################################################################################
            n = int(InputDialog(root, 'Количество переменных функции', 'n =').exec())  # количество переменных
            output += f'Количество переменных функции | n = {n}\n'
            # n = 2 # данные для теста
            h = []  # Гессеан
            for i in range(n * n):
                inp = InputDialog(root, f'Смешанные производные {i+1}/{n * n}', f'f"x{int(i // n) + 1}x{int(i % n) + 1} = ').exec()
                if not inp:
                    raise Exception
                h.append(inp)
                output += f'f"x{int(i // n) + 1}x{int(i % n) + 1} = {inp}\n'
            # h = ['6*x1', '-3', '-3', '6*x2'] # данные для теста
            h = np.array(h).reshape(n, n)

            # ОПРЕДЕЛЕНИЕ ТОЧЕК ЭКСТРЕМУМА #############################################################################
            k = int(InputDialog(root, 'Количестов точек экстремума', 'k =').exec())  # Количество корней
            output += f'Количество точек экстремума | k = {k}\n'
            # k = 2 # данные для теста
            d = []  # Корни
            for i in range(k):
                cd = []
                for j in range(n):
                    cd.append(float(InputDialog(root, f'Точка {i + 1}', f'x{j + 1} =').exec()))
                d.append(cd)
            # d = [[0, 0], [1, 1]] # данные для теста

            # ВЫЧИСЛЕНИЕ ГЕССЕАНА ДЛЯ КАЖДОЙ ТОЧКИ ЭКСТРЕМУМА ##########################################################
            output += f'\nРезультат вычислений:\n'
            for i in range(k):
                # ПОДСТАНОВКА ЗНАЧЕНИЙ В МАТРИЦУ
                hk = h.copy()  # Гессиан для точки
                for j in range(n):
                    for l in range(n):
                        e = hk[j, l]  # Выражение производной
                        for m in range(n):
                            e = e.replace(f'x{m + 1}', str(d[i][m]))  # Подстановка значений точки
                        hk[j, l] = eval(e)  # Вычисление выражения
                hk = hk.astype(float)

                # ВЫЧИСЛЕНИЕ УГЛОВЫХ МИНОРОВ ###########################################################################
                m = []
                for j in range(n):
                    m.append(np.linalg.det(hk[:j + 1, :j + 1]))

                # ОПРЕДЕЛЕНИЕ MIN/MAX ##################################################################################
                miin = True
                maax = True
                for j in range(len(m)):
                    if miin and (m[j] < 0):
                        miin = False
                    elif maax:
                        if ((j % 2) == 0) and m[j] >= 0:
                            maax = False
                        elif ((j % 2) != 0) and m[j] <= 0:
                            maax = False
                if miin:
                    output += f'Точка {tuple(d[i])} = min\n'
                elif maax:
                    output += f'Точка {tuple(d[i])} = max\n'
                else:
                    output += f'Точка {tuple(d[i])} = неизвестно\n'
                self.result.setText(output)
        except Exception:
            self.result.setText('Что-то пошло не так. Вероятно вы ввели некорректное значение. Попробуйте еще раз.')


class InputDialog(object):
    def __init__(self, root, title='input', label='input double'):
        self.dialog = QInputDialog(root)
        self.dialog.resize(400, 300)
        self.dialog.setStyleSheet("* { font-size: 13pt; }" ) # Увеличенный шрифт
        self.dialog.setInputMode(QInputDialog.TextInput)
        self.dialog.setWindowTitle(title)
        self.dialog.setLabelText(label)

    def exec(self):
        if self.dialog.exec():
            return self.dialog.textValue()