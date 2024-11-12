import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox, QWidget, QVBoxLayout
from main import DocProcessing  # Импортируем класс обработки документа

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Document Processor")
        self.setGeometry(100, 100, 400, 300)

        self.processor = None

        # UI элементы
        self.layout = QVBoxLayout()

        # Кнопка для загрузки документа
        self.file_button = QPushButton("Загрузить документ")
        self.file_button.clicked.connect(self.load_document)
        self.layout.addWidget(self.file_button)

        # Подсказка и поле ввода
        self.hint_label = QLabel("Подсказка:")
        self.input_field = QLineEdit()
        self.layout.addWidget(self.hint_label)
        self.layout.addWidget(self.input_field)

        # Кнопки Вперёд и Назад для перемещения по ячейкам и таблицам
        self.next_button = QPushButton("Вперёд")
        self.next_button.clicked.connect(self.move_forward)
        self.back_button = QPushButton("Назад")
        self.back_button.clicked.connect(self.move_backward)
        self.layout.addWidget(self.next_button)
        self.layout.addWidget(self.back_button)

        # Кнопка для сохранения документа
        self.process_button = QPushButton("Сохранить изменения")
        self.process_button.clicked.connect(self.save_document)
        self.layout.addWidget(self.process_button)

        # Основной виджет
        container = QWidget()
        container.setLayout(self.layout)
        self.setCentralWidget(container)

    def load_document(self):
        """Загрузка файла документа"""
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(self, "Выберите документ Word", "", "Word Files (*.docx)")
        if file_path:
            self.processor = DocProcessing(file_path)
            QMessageBox.information(self, "Файл загружен", f"Документ загружен: {file_path}")
            self.update_hint()  # Показываем подсказку для первой ячейки первой таблицы

    def move_forward(self):
        """Перемещение вперёд по ячейкам или таблицам"""
        if self.processor:
            user_input = self.input_field.text()
            if user_input:
                self.processor.table_fill(user_input)  # Заполнение текущей ячейки
                self.input_field.clear()  # Очищаем поле ввода
            self.processor.move_forward()  # Переход вперёд
            self.update_hint()

    def move_backward(self):
        """Перемещение назад по ячейкам или таблицам"""
        if self.processor:
            self.processor.move_backward()  # Переход назад
            self.update_hint()

    def update_hint(self):
        """Обновление подсказки для текущей позиции"""
        if self.processor:
            hint = self.processor.get_hint()
            self.hint_label.setText(f"{hint}")

    def save_document(self):
        """Сохранение документа с выбором пути и имени файла"""
        if self.processor:
            # Открываем диалог сохранения
            file_path, _ = QFileDialog.getSaveFileName(self, "Сохранить документ как", "", "Word Files (*.docx)")
            if file_path:
                # Сохраняем документ по указанному пути
                self.processor.save_document(file_path)
                QMessageBox.information(self, "Успех", f"Документ успешно сохранен как: {file_path}")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()