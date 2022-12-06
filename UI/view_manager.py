from PyQt5.QtWidgets import QMainWindow
from UI.home_view import HomeView
from UI.graph_view import GraphView
from UI.hessian_view import HessianView
from UI.optimiz_view import optimiz
from UI.simplex_view import Simplex
from UI.linear_program_view import Linear
from UI.lagranj_view import Lagranj


class ViewManager(QMainWindow):
    def __init__(self):
        super(ViewManager, self).__init__()
        self.setWindowTitle('Исследование операций в ИС')
        self.move(350, 100)
        self.show_home()

    def show_home(self):
        home_view = HomeView(self)

        # Бинд кнопок выбора категорий
        home_view.button_1.clicked.connect(self.show_graph)
        home_view.button_2.clicked.connect(self.show_hessian)
        home_view.button_3.clicked.connect(self.show_optimiz)
        home_view.button_4.clicked.connect(self.show_simplex)
        home_view.button_5.clicked.connect(self.show_linear)
        home_view.button_6.clicked.connect(self.show_lagranj)

    def show_graph(self):
        grath_view = GraphView(self)
        grath_view.button_back.clicked.connect(self.show_home)

    def show_optimiz(self):
        optimiz_view = optimiz(self)
        optimiz_view.button_back.clicked.connect(self.show_home)

    def show_hessian(self):
        hessian_view = HessianView(self)
        hessian_view.button_back.clicked.connect(self.show_home)

    def show_simplex(self):
        simplex_view = Simplex(self)
        simplex_view.button_back.clicked.connect(self.show_home)

    def show_linear(self):
        linear_view = Linear(self)
        linear_view.button_back.clicked.connect(self.show_home)

    def show_lagranj(self):
        lagranj_view = Lagranj(self)
        lagranj_view.button_back.clicked.connect(self.show_home)
