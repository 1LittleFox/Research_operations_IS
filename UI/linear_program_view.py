from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtGui import QColor
from PyQt5 import QtCore, QtGui, QtWidgets
from scipy.optimize import linprog


class Linear:
    def __init__(self, root):
        # Шрифты
        self.font_16 = QtGui.QFont()
        self.font_14 = QtGui.QFont()
        self.font_12 = QtGui.QFont()

        self.central_widget = QtWidgets.QWidget(root)                       # Главный виджет
        self.central_layout = QtWidgets.QVBoxLayout(self.central_widget)    # Главный компоновщик
        self.title = QtWidgets.QLabel()                                     # Заголовок
        self.validator = QtGui.QIntValidator()                              # Ограничение на ввод букв
        self.label_col = QtWidgets.QLabel()                                 # Текстовое поле столбцов таблицы
        self.label_row = QtWidgets.QLabel()                                 # Текстовое поле строк таблицы
        self.columns = QtWidgets.QLineEdit()                                # Поле ввода числа столбцов
        self.rows = QtWidgets.QLineEdit()                                   # Поле ввода числа строк
        self.btn_create = QtWidgets.QPushButton()                           # Кнопка создания таблицы
        self.table = QtWidgets.QTableWidget()                               # Таблица
        self.table_2 = QtWidgets.QTableWidget()                             # Таблица
        self.table_3 = QtWidgets.QTableWidget()                             # Таблица
        self.btn_result = QtWidgets.QPushButton()                           # Кнопка вычисления
        self.result = QtWidgets.QTextEdit()                                 # Результат вычислений
        self.horizontal_result_layout = QtWidgets.QHBoxLayout()             # Горизонтальный компоновщик кнопки вычислений
        self.horizontal_input_layout = QtWidgets.QHBoxLayout()              # Горизонтальный компоновщик вводимых данных
        self.horizontal_table_layout = QtWidgets.QHBoxLayout()              # Горизонтальный компоновщик кнопки назад
        self.horizontal_textEdit_layout = QtWidgets.QHBoxLayout()           # Горизонтальный компоновщик поля результата
        self.horizontal_back_layout = QtWidgets.QHBoxLayout()               # Горизонтальный компоновщик кнопки назад
        self.button_back = QtWidgets.QPushButton()                          # Кнопка возврата на главное меню

        self.btn_create.clicked.connect(lambda: self.create_table())
        self.btn_result.clicked.connect(self.function_result)

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

        # # Добавление заполнителя
        # spacer_item = QtWidgets.QSpacerItem(100, 100, QtWidgets.QSizePolicy.Fixed)
        # self.central_layout.addItem(spacer_item)

        # Необходимо для центрирования виджетов
        self.horizontal_input_layout.addStretch()

        # Настройка текстового поля столбцов
        self.label_col.setFont(self.font_16)
        self.horizontal_input_layout.addWidget(self.label_col)

        # Настройка поля ввода столбцов
        self.columns.setFont(self.font_12)
        self.columns.setValidator(self.validator)
        self.columns.setMaximumSize(QtCore.QSize(53, 37))
        self.horizontal_input_layout.addWidget(self.columns)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(50, 100, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_input_layout.addItem(spacer_item)

        # Настройка текстового поля строк
        self.label_row.setFont(self.font_16)
        self.horizontal_input_layout.addWidget(self.label_row)

        # Настройка поля ввода строк
        self.rows.setFont(self.font_12)
        self.rows.setValidator(self.validator)
        self.rows.setMaximumSize(QtCore.QSize(53, 37))
        self.horizontal_input_layout.addWidget(self.rows)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(50, 100, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_input_layout.addItem(spacer_item)

        # Настройка кнопки построения таблицы
        self.btn_create.setFont(self.font_14)
        self.horizontal_input_layout.addWidget(self.btn_create)

        # Необходимо для центрирования виджетов
        self.horizontal_input_layout.addStretch()

        # Настройка таблицы 1
        self.table.setMaximumSize(QtCore.QSize(500, 300))
        #self.table.setStyleSheet("border: 0px")
        self.horizontal_table_layout.addWidget(self.table)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(30, 100, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_table_layout.addItem(spacer_item)

        # Настройка таблицы 2
        self.table_2.setMaximumSize(QtCore.QSize(500, 300))
        #self.table_2.setStyleSheet("border: 0px")
        self.horizontal_table_layout.addWidget(self.table_2)

        # Добавление заполнителя
        spacer_item = QtWidgets.QSpacerItem(30, 100, QtWidgets.QSizePolicy.Fixed)
        self.horizontal_table_layout.addItem(spacer_item)

        # Настройка таблицы 3
        self.table_3.setMaximumSize(QtCore.QSize(500, 300))
        #self.table_3.setStyleSheet("border: 0px")
        self.horizontal_table_layout.addWidget(self.table_3)

        # Настройка кнопки рассчета
        self.btn_result.setFont(self.font_14)
        self.btn_result.setMaximumSize(QtCore.QSize(200, 60))
        self.horizontal_result_layout.addWidget(self.btn_result)

        # Настройка кнопки возврата на главную
        self.button_back.setMaximumSize(QtCore.QSize(200, 60))
        self.button_back.setFont(self.font_14)
        self.horizontal_back_layout.addWidget(self.button_back)

        # Настройка отображения результата
        self.result.setMaximumSize(QtCore.QSize(1000, 300))
        self.result.setTextColor(QColor("white"))
        self.result.setEnabled(True)
        self.result.setFont(self.font_14)
        self.result.setUndoRedoEnabled(True)
        self.result.setReadOnly(True)
        self.horizontal_textEdit_layout.addWidget(self.result)

        # Финальная компоновка
        self.central_layout.addLayout(self.horizontal_input_layout)
        self.central_layout.addLayout(self.horizontal_table_layout)
        self.central_layout.addLayout(self.horizontal_result_layout)
        self.central_layout.addLayout(self.horizontal_textEdit_layout)
        self.central_layout.addLayout(self.horizontal_back_layout)

        root.setCentralWidget(self.central_widget)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Решение задачи линейного программирования')
        self.label_col.setText('Введите количество столбцов:')
        self.label_row.setText('Введите количество строк:')
        self.btn_create.setText('Построить таблицу')
        self.btn_result.setText('Вычислить')
        self.result.setText('Здесь будет ответ...')
        self.button_back.setText('На главную')

    # Создание таблиц
    def create_table(self):
        if len(self.columns.text()) > 0 and len(self.rows.text()) > 0:
            self.table.setColumnCount(int(self.columns.text()))
            self.table.setRowCount(int(self.rows.text()))
            self.table.setFont(self.font_12)
            self.table.resizeColumnsToContents()

            self.table_2.setColumnCount(int(self.rows.text()))
            self.table_2.setRowCount(1)
            self.table_2.setFont(self.font_12)
            self.table_2.resizeColumnsToContents()

            self.table_3.setColumnCount(int(self.columns.text()))
            self.table_3.setRowCount(1)
            self.table_3.setFont(self.font_12)
            self.table_3.resizeColumnsToContents()

    # Функция решения задачи
    def function_result(self):
        if len(self.columns.text()) > 0 and len(self.rows.text()) > 0:
            # Считывание данных с 1 таблицы
            rows = self.table.rowCount()
            cols = self.table.columnCount()
            data = []
            for row in range(rows):
                tmp = []
                for col in range(cols):
                    try:
                        tmp.append(self.table.item(row, col).text())
                    except:
                        tmp.append(0)
                data.append(tmp)

            # Считывание данных со 2 таблицы
            rows2 = self.table_2.rowCount()
            cols2 = self.table_2.columnCount()
            data2 = []
            for row2 in range(rows2):
                tmp2 = []
                for col2 in range(cols2):
                    try:
                        tmp2.append(self.table_2.item(row2, col2).text())
                    except:
                        tmp2.append(0)
                data2.append(tmp2)

            # Считывание данных с 3 таблицы
            rows3 = self.table_3.rowCount()
            cols3 = self.table_3.columnCount()
            data3 = []
            for row3 in range(rows3):
                tmp3 = []
                for col3 in range(cols3):
                    try:
                        tmp3.append(self.table_3.item(row3, col3).text())
                    except:
                        tmp3.append(0)
                data3.append(tmp3)

            #obj = [-20, -12, -40, -25]
            obj = data3
            lhs_ineq = data

            #
            # [[1, 1, 1, 1],  # Рабочая сила
            # [3, 2, 1, 0],  # Материал A
            # [0, 1, 2, 3]]  # Материал B

            #rhs_ineq = [50,  # Рабочая сила
                        #100,  # Материал A
                        #90]  # Материал B

            rhs_ineq = data2

            #print(data)
            #print(data2)
            #print(data3)

            opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, method="highs")
            self.result.setText(format(opt))


