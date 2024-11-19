from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, \
    QMessageBox, QLineEdit, QHBoxLayout, QComboBox
from PyQt6.QtGui import QIcon


class ViewDataWin(QWidget):
    def __init__(self):
        super().__init__()
        self.data = self.get_sample_data()  # Получение образцов данных
        self.initUI()
        self.load_data()

    def initUI(self):
        self.setWindowTitle("Выборки из базы данных")
        self.setGeometry(100, 100, 1500, 500)
        self.setWindowIcon(QIcon('resources/gg.ico'))
        self.query_label = QLabel("Выберите выборку:")

        self.query_combo = QComboBox()
        self.query_combo.addItem("Все пользователи", "all_user")
        self.query_combo.addItem("Статус пк", "status")
        self.query_combo.addItem("ПК", "name_pc")
        self.filter = QLineEdit()
        self.filter.setPlaceholderText('Здесь нужно ввести фильтр')
        self.table = QTableWidget()
        self.back_button = QPushButton("Выйти")
        self.del_entry = QPushButton("Удалить")
        self.edit_entry = QPushButton("Изменить")
        main_l = QVBoxLayout()
        h_l1 = QHBoxLayout()
        main_l.addWidget(self.query_label)
        main_l.addWidget(self.query_combo)
        main_l.addWidget(self.filter)
        main_l.addWidget(self.table)
        h_l1.addWidget(self.edit_entry)
        h_l1.addWidget(self.del_entry)
        h_l1.addWidget(self.back_button)
        main_l.addLayout(h_l1)
        self.setLayout(main_l)
        self.filter.textChanged.connect(self.load_data)
        self.query_combo.currentIndexChanged.connect(self.load_data)
        self.back_button.clicked.connect(self.back)
        self.edit_entry.clicked.connect(self.edit_order)
        self.del_entry.clicked.connect(self.delete_order)

    def get_sample_data(self):

        return []

    def load_data(self):
        query_type = self.query_combo.currentData()
        self.table.clear()
        self.table.setRowCount(0)
        self.table.setColumnCount(0)

        filtered_data = self.filter_data(query_type)
        if filtered_data:
            self.table.setColumnCount(5)
            self.table.setHorizontalHeaderLabels(
                ['ID Пользователя', 'Имя', 'Фамилия', 'ПК', 'Время'])
            self.table.setRowCount(len(filtered_data))
            for row_idx, row_data in enumerate(filtered_data):
                for col_idx, col_data in enumerate(row_data):
                    self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось загрузить данные")

    def filter_data(self, query_type):
        filter_text = self.filter.text().strip().lower()
        filtered_data = self.data

        if query_type == "status":
            # Здесь можно добавить логика фильтрации по статусу
            pass
        elif query_type == "name_pc":
            filtered_data = [row for row in self.data if filter_text in row[3].lower()]
        else:
            filtered_data = [row for row in self.data if any(filter_text in str(col).lower() for col in row)]

        return filtered_data

    def delete_order(self):
        if self.table.selectedItems():
            confirmation_dialog = QMessageBox()
            confirmation_dialog.setWindowTitle("Подтверждение удаления")
            confirmation_dialog.setText(f"Вы уверены?:\n{self.table.item(self.table.currentRow(), 2).text()}?")
            confirmation_dialog.setIcon(QMessageBox.Icon.Warning)
            confirmation_dialog.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            confirmation_dialog.setDefaultButton(QMessageBox.StandardButton.No)
            user_response = confirmation_dialog.exec()
            if user_response == QMessageBox.StandardButton.Yes:
                # Удаляем элемент из списка данных
                row_to_delete = self.table.currentRow()
                if row_to_delete >= 0:
                    del self.data[row_to_delete]
                    self.load_data()  # Обновляем таблицу

    def back(self):
        self.close()

    def edit_order(self):
        QMessageBox.information(self, "Редактирование", "Функция редактирования еще не реализована.")

