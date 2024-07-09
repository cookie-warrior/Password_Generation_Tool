import sys
import string
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QCheckBox, QPushButton, QGridLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QColor, QPalette

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Strong Password Generator")
        self.setGeometry(300, 300, 400, 300)

        # Main vertical layout
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Title label
        self.title_label = QLabel("Strong Password Generator")
        title_font = QFont("Arial", 20, QFont.Bold)
        self.title_label.setFont(title_font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.title_label)

        # Settings section (vertical layout)
        self.settings_layout = QVBoxLayout()
        self.settings_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.addLayout(self.settings_layout)

        # Password length section (horizontal layout)
        self.length_layout = QHBoxLayout()
        self.settings_layout.addLayout(self.length_layout)

        self.length_label = QLabel("Password Length:")
        length_font = QFont("Arial", 12)
        self.length_label.setFont(length_font)
        self.length_layout.addWidget(self.length_label)

        self.length_entry = QLineEdit()
        self.length_entry.setText("12")
        self.length_entry.setFixedWidth(50)
        self.length_layout.addWidget(self.length_entry)

        # Character type checkboxes (grid layout)
        self.char_type_layout = QGridLayout()
        self.char_type_layout.setSpacing(10)
        self.settings_layout.addLayout(self.char_type_layout)

        self.uppercase_checkbox = QCheckBox("Include Uppercase")
        self.uppercase_checkbox.setChecked(True)
        self.char_type_layout.addWidget(self.uppercase_checkbox, 0, 0)

        self.lowercase_checkbox = QCheckBox("Include Lowercase")
        self.lowercase_checkbox.setChecked(True)
        self.char_type_layout.addWidget(self.lowercase_checkbox, 1, 0)

        self.numbers_checkbox = QCheckBox("Include Numbers")
        self.numbers_checkbox.setChecked(True)
        self.char_type_layout.addWidget(self.numbers_checkbox, 0, 1)

        self.symbols_checkbox = QCheckBox("Include Symbols")
        self.symbols_checkbox.setChecked(True)
        self.char_type_layout.addWidget(self.symbols_checkbox, 1, 1)

        # Generate button
        self.generate_button = QPushButton("Generate Password")
        button_font = QFont("Arial", 14)
        self.generate_button.setFont(button_font)
        self.generate_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 10px 20px;")
        self.generate_button.clicked.connect(self.generate_password)
        self.settings_layout.addWidget(self.generate_button, alignment=Qt.AlignCenter)

        # Password display area
        self.password_label = QLabel("Generated Password:")
        self.password_label.setFont(length_font)
        self.password_label.setAlignment(Qt.AlignLeft)
        self.settings_layout.addWidget(self.password_label)

        self.password_display = QLabel("")
        self.password_display.setFont(QFont("Arial", 16))
        self.password_display.setAlignment(Qt.AlignCenter)
        self.settings_layout.addWidget(self.password_display, alignment=Qt.AlignCenter)

        # Set application palette for overall aesthetic
        palette = QPalette()
        palette.setColor(QPalette.Window, QColor("#f0f0f0"))  # Light gray background
        palette.setColor(QPalette.WindowText, QColor("#333333"))  # Dark gray text
        self.setPalette(palette)

        # Show the window
        self.show()

    def generate_password(self):
        try:
            length = int(self.length_entry.text())
            include_uppercase = self.uppercase_checkbox.isChecked()
            include_lowercase = self.lowercase_checkbox.isChecked()
            include_numbers = self.numbers_checkbox.isChecked()
            include_symbols = self.symbols_checkbox.isChecked()

            char_set = ""
            if include_uppercase:
                char_set += string.ascii_uppercase
            if include_lowercase:
                char_set += string.ascii_lowercase
            if include_numbers:
                char_set += string.digits
            if include_symbols:
                char_set += string.punctuation

            if not char_set:
                self.password_display.setText("Error: Please select at least one character type.")
                return

            password = ''.join(random.choice(char_set) for _ in range(length))
            self.password_display.setText(password)

        except ValueError:
            self.password_display.setText("Error: Invalid password length.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    sys.exit(app.exec_())
