import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QVBoxLayout, QMessageBox, QRadioButton
from PIL import Image
import imageio

def convert_dds_to_png(dds_directory, png_directory):
    if not os.path.exists(png_directory):
        os.makedirs(png_directory)
    
    for filename in os.listdir(dds_directory):
        if filename.endswith('.dds'):
            dds_path = os.path.join(dds_directory, filename)
            png_filename = os.path.splitext(filename)[0] + '.png'
            png_path = os.path.join(png_directory, png_filename)

            image = imageio.imread(dds_path)
            imageio.imwrite(png_path, image)

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Conversion Mode Selection (Only DDS to PNG now)
        self.dds_to_png_radio = QRadioButton("DDS to PNG")
        self.dds_to_png_radio.setChecked(True)  # Default selection

        layout.addWidget(self.dds_to_png_radio)

        # DDS Directory
        self.dds_dir_label = QLabel("DDS Directory:")
        self.dds_dir_button = QPushButton("Browse")
        self.dds_dir_button.clicked.connect(self.select_dds_directory)
        layout.addWidget(self.dds_dir_label)
        layout.addWidget(self.dds_dir_button)

        # Output PNG Directory
        self.png_out_dir_label = QLabel("Output PNG Directory:")
        self.png_out_dir_button = QPushButton("Browse")
        self.png_out_dir_button.clicked.connect(self.select_png_out_directory)
        layout.addWidget(self.png_out_dir_label)
        layout.addWidget(self.png_out_dir_button)

        # Start Conversion Button
        self.start_button = QPushButton("Start Conversion")
        self.start_button.clicked.connect(self.start_conversion)
        layout.addWidget(self.start_button)

        self.setLayout(layout)
        self.setWindowTitle('DDS to PNG Converter')
        self.setGeometry(300, 300, 400, 300)

    def select_dds_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select DDS Directory")
        if directory:
            self.dds_dir_label.setText(f"DDS Directory: {directory}")
    
    def select_png_out_directory(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Output PNG Directory")
        if directory:
            self.png_out_dir_label.setText(f"Output PNG Directory: {directory}")

    def start_conversion(self):
        dds_dir = self.dds_dir_label.text().replace("DDS Directory: ", "")
        png_out_dir = self.png_out_dir_label.text().replace("Output PNG Directory: ", "")

        if "Select" in dds_dir or "Select" in png_out_dir:
            QMessageBox.warning(self, "Input Error", "Please select the DDS and Output PNG directories.")
            return

        try:
            convert_dds_to_png(dds_dir, png_out_dir)
            QMessageBox.information(self, "Success", "DDS to PNG conversion completed successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ConverterApp()
    ex.show()
    sys.exit(app.exec_())
