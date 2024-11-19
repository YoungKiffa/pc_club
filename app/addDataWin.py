from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QComboBox, QLineEdit, QTextEdit, QMessageBox, QLabel



class AddDataWin(QWidget):
    def __init__(self, data=None):
        super().__init__()
        self.data = data
        self.initUI()
        if data:
            self.upload_editable_data()
        self.show()

    def initUI(self):
        self.setWindowIcon(QIcon('resources/gg.ico'))
        self.setWindowTitle("Добавить нового пользователя")
        self.setGeometry(100, 100, 400, 300)

        self.name_label = QLabel("Имя:")
        self.name_input = QLineEdit()

        self.surname_label = QLabel("Фамилия:")
        self.surname_input = QLineEdit()

        self.id_pc_label = QLabel("Компьютер:")
        self.id_pc_input = QComboBox()
        self.load_id_pc()

        self.time_label = QLabel("Время:")
        self.time_input = QLineEdit()

        self.add_button = QPushButton("Добавить пользователя")
        self.cls_1 = QPushButton("Выйти")

        self.add_button.clicked.connect(self.add_user)
        self.cls_1.clicked.connect(self.close)

        layout = QVBoxLayout()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)
        layout.addWidget(self.surname_label)
        layout.addWidget(self.surname_input)
        layout.addWidget(self.id_pc_label)
        layout.addWidget(self.id_pc_input)
        layout.addWidget(self.time_label)
        layout.addWidget(self.time_input)
        layout.addWidget(self.add_button)
        layout.addWidget(self.cls_1)
        self.setLayout(layout)

    def load_id_pc(self):
        pc_types = ["Asus", "Msi", "ArdorGaming", "Mac"]
        self.id_pc_input.addItems(pc_types)

    def upload_editable_data(self):
        if self.data:
            self.name_input.setText(self.data[0])
            self.surname_input.setText(self.data[1])
            self.id_pc_input.setCurrentText(self.data[2])  # Изменено на setCurrentText для QComboBox
            self.time_input.setText(self.data[3])

    def add_user(self):
        user_data = {
            "name": self.name_input.text(),
            "surname": self.surname_input.text(),
            "id_pc": self.id_pc_input.currentText(),
            "time": self.time_input.text()
        }
        print("Новый пользователь добавлен:", user_data)

        QMessageBox.information(self, "Информация", "Пользователь добавлен успешно!")
        self.close()
