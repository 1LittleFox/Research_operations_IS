from PyQt5.QtWidgets import QApplication
from qt_material import apply_stylesheet
from UI.view_manager import ViewManager
from sys import argv, exit


def main():
    # Инициализация окна и запуск приложения
    app = QApplication(argv)
    apply_stylesheet(app, theme='my_theme.xml')  # Установка темы приложения
    vm = ViewManager() # Сохраняется в переменную чтобы экземпляр не удалился
    vm.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
