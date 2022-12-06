from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QSizePolicy


class HomeView:
    def __init__(self, root):
        self.lbl_font = QtGui.QFont()  # Шрифт надписей
        self.btn_font = QtGui.QFont()  # Шрифт кнопок

        self.centralWidget    = QtWidgets.QWidget(root)                   # Главный виджет
        self.centralLayout    = QtWidgets.QVBoxLayout(self.centralWidget) # Главный компоновщик
        self.gridlayout       = QtWidgets.QGridLayout()                   # Сетка
        self.horizontalLayout = QtWidgets.QHBoxLayout()                   # Горизонтальный компоновщик

        self.title = QtWidgets.QLabel()  # Заголовок

        # Кнопки меню
        self.button_1 = QtWidgets.QPushButton()
        self.button_2 = QtWidgets.QPushButton()
        self.button_3 = QtWidgets.QPushButton()
        self.button_4 = QtWidgets.QPushButton()
        self.button_5 = QtWidgets.QPushButton()
        self.button_6 = QtWidgets.QPushButton()

        self.status_bar = QtWidgets.QStatusBar(root) # Статусбар

        self.setupUi(root)

    def setupUi(self, root):
        # Выставление размеров шрифтов
        self.lbl_font.setPointSize(24)
        self.btn_font.setPointSize(24)

        # Определение размера окна и центрирование
        self.centralWidget.setMinimumSize(QtCore.QSize(1200, 850))
        self.gridlayout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignTop)
        self.horizontalLayout.setAlignment(QtCore.Qt.AlignHCenter)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 250, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка заголовка
        self.title.setFont(self.lbl_font)
        self.title.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed))
        self.title.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom)
        self.centralLayout.addWidget(self.title)

        # Добавление заполнителя
        spacerItem = QtWidgets.QSpacerItem(0, 20, QtWidgets.QSizePolicy.Ignored)
        self.centralLayout.addItem(spacerItem)

        # Настройка кнопки меню 1
        self.button_1.setMinimumSize(QtCore.QSize(380, 60))
        self.button_1.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_1, 0, 0)

        # Настройка кнопки меню 2
        self.button_2.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_2, 1, 0)

        # # Настройка кнопки меню 3
        self.button_3.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_3, 2, 0)
        #
        # Настройка кнопки меню 4
        self.button_4.setMinimumSize(QtCore.QSize(380, 60))
        self.button_4.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_4, 3, 0)
        #
        # Настройка кнопки меню 5
        self.button_5.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_5, 4, 0)
        #
        # Настройка кнопки меню 6
        self.button_6.setFont(self.btn_font)
        self.gridlayout.addWidget(self.button_6, 5, 0)

        # Финальная компоновка
        self.centralLayout.addLayout(self.gridlayout)
        self.centralLayout.addLayout(self.horizontalLayout)
        root.setCentralWidget(self.centralWidget)
        root.setStatusBar(self.status_bar)

        self.setTextUi()

    def setTextUi(self):
        # Наполнение виджетов текстом
        self.title.setText('Выберите категорию:')
        self.button_1.setText('Построение графика')
        self.button_2.setText('Решение задачи оптимизации')
        self.button_3.setText('Оптимизация методом равномерного поиска')
        self.button_4.setText("Многомерная оптимизация | метод симплекса")
        self.button_5.setText("Решение задачи линейного программирования")
        self.button_6.setText("Метод множителей Лагранжа")
        # self.button_8.setText("Кнопка 7")