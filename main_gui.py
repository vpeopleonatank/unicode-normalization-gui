import sys
import unicodedata
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
    QLabel,
    QComboBox,
)


class DiacriticConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Layout
        layout = QVBoxLayout(self)

        # Text Edit for input
        self.input_text_edit = QTextEdit(self)
        self.input_text_edit.setPlaceholderText("Enter text here...")
        layout.addWidget(self.input_text_edit)

        # 'To' Label
        to_label = QLabel("To:", self)
        layout.addWidget(to_label)

        # Combo Box for selecting normalization form
        self.to_normalization_form_combo = QComboBox(self)
        self.to_normalization_form_combo.addItems(["NFC", "NFKC", "NFD", "NFKD"])
        layout.addWidget(self.to_normalization_form_combo)

        # Text Edit for output
        self.output_text_edit = QTextEdit(self)
        self.output_text_edit.setPlaceholderText("Converted text will appear here...")
        self.output_text_edit.setReadOnly(True)
        layout.addWidget(self.output_text_edit)

        # Button for converting
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.clicked.connect(self.convert_text)
        layout.addWidget(self.convert_button)

        # 'Copy to Clipboard' Button
        self.copy_button = QPushButton("Copy Output to Clipboard", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        layout.addWidget(self.copy_button)

        # Set the layout on the application's window
        self.setLayout(layout)
        self.setWindowTitle("Diacritic Converter")

    def copy_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_text_edit.toPlainText())

    def convert_text(self):
        # Get input text
        input_text = self.input_text_edit.toPlainText()
        print(input_text)

        # Get selected normalization form
        selected_form = self.to_normalization_form_combo.currentText()

        # Convert text
        converted_text = unicodedata.normalize(selected_form, input_text)

        # Display in output text edit
        self.output_text_edit.setPlainText(converted_text)


def main():
    app = QApplication(sys.argv)
    ex = DiacriticConverterApp()
    ex.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
