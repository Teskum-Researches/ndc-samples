#! /usr/bin/env python3
from http.cookies import SimpleCookie
from datetime import datetime, timedelta, UTC
import sys

from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, 
                            QLineEdit, QListWidget, QLabel, QProgressBar, 
                            QHBoxLayout, QCheckBox, QMainWindow)
from PyQt6.QtGui import QAction

def log(message):
    window.list.addItem(message)
    window.list.scrollToBottom()



class MyApplication(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NDC PyQt6 Sample')
        self.setGeometry(100, 100, 600, 480)
        self.setFixedSize(600, 480)

        # Создание центрального виджета и установка компоновки
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Создание виджетов
        self.label = QLabel("Кликни на кнопку")
        self.button = QPushButton("Нажми меня")
        self.checkbox = QCheckBox("Пример чекбокса")
        self.list = QListWidget()
        self.progress = QProgressBar()
        self.statusbar = self.statusBar()
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.showMessage("Готово", 5000)

        # Подключение обработчиков событий
        self.button.clicked.connect(self.on_button_click)
        self.checkbox.stateChanged.connect(lambda: log("Чекбокс изменен"))
        
        # горизонтальный layout
        hbox = QHBoxLayout()
        hbox.addWidget(self.button)
        hbox.addWidget(self.checkbox)

        layout.addWidget(self.label)
        layout.addLayout(hbox)          # Вот тут добавляем layout
        layout.addWidget(self.list)
        layout.addWidget(self.progress)
        layout.addWidget(self.statusbar)
        

    def on_button_click(self):
        self.label.setText("Кнопка была нажата!")
        self.progress.setValue(self.progress.value() + 1)
        self.statusbar.showMessage("Кнопка нажата", 2000)

        

def main():
    global window
    app = QApplication(sys.argv)
    window = MyApplication()
    window.show()
    sys.exit(app.exec())
    


if __name__ == '__main__':
    main()