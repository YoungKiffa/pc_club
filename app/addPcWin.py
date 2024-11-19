from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLineEdit, QMessageBox, QLabel


class AddPcWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.data = data
        self.initUI()
        if data:
            self.upload_editable_data()
        self.show()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/gg.ico'))
        self.setWindowTitle("Добавить новый компьютер")
        self.setGeometry(100, 100, 300, 100)

        self.name_pc_label = QLabel("Имя:")
        self.name_pc_input = QLineEdit()

        self.add_button = QPushButton("Добавить компьютер")
        self.cls_1 = QPushButton("Выйти")

        self.add_button.clicked.connect(self.add_pc)
        self.cls_1.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.name_pc_label)
        layout.addWidget(self.name_pc_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.cls_1)
        self.setLayout(layout)

    def upload_editable_data(self):
        if self.data:
            self.name_pc_input.setText(self.data[0])

    def add_pc(self):
        pc_data = {
            "name_pc": self.name_pc_input.text(),
        }
        print("Новый компьютер добавлен:", pc_data)

        QMessageBox.information(self, "Информация", "Компьютер добавлен успешно!")
        self.close()

