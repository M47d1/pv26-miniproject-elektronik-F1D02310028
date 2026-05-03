from PySide6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
                            QComboBox, QDateEdit, QDoubleSpinBox, 
                            QPushButton, QHBoxLayout, QRadioButton, QButtonGroup)
from PySide6.QtCore import QDate

class InventoryDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tambah Peralatan Elektronik")
        self.setMinimumWidth(350)
        
        self.layout = QVBoxLayout(self)
        self.form = QFormLayout()

        # Input Fields
        self.input_nama = QLineEdit()
        self.input_kategori = QComboBox()
        self.input_kategori.addItems(["Smartphone", "Laptop", "Kamera", "Audio", "Lainnya"])
        
        # Kondisi (Radio Buttons)
        self.radio_group = QButtonGroup(self)
        self.radio_baik = QRadioButton("Baik")
        self.radio_baik.setChecked(True)
        self.radio_rusak = QRadioButton("Rusak/Servis")
        self.radio_group.addButton(self.radio_baik)
        self.radio_group.addButton(self.radio_rusak)
        
        self.radio_layout = QHBoxLayout()
        self.radio_layout.addWidget(self.radio_baik)
        self.radio_layout.addWidget(self.radio_rusak)

        self.input_tanggal = QDateEdit(QDate.currentDate())
        self.input_tanggal.setCalendarPopup(True)
        
        self.input_harga = QDoubleSpinBox()
        self.input_harga.setRange(0, 999999999)
        self.input_harga.setPrefix("Rp ")

        # Add to Form
        self.form.addRow("Nama Alat:", self.input_nama)
        self.form.addRow("Kategori:", self.input_kategori)
        self.form.addRow("Kondisi:", self.radio_layout)
        self.form.addRow("Tgl Beli:", self.input_tanggal)
        self.form.addRow("Harga:", self.input_harga)
        
        self.layout.addLayout(self.form)

        # Buttons
        self.buttons = QHBoxLayout()
        self.btn_save = QPushButton("Simpan Data")
        self.btn_cancel = QPushButton("Batal")
        self.buttons.addWidget(self.btn_save)
        self.buttons.addWidget(self.btn_cancel)
        self.layout.addLayout(self.buttons)

        self.btn_cancel.clicked.connect(self.reject)

    def get_data(self):
        kondisi = "Baik" if self.radio_baik.isChecked() else "Rusak/Servis"
        return (
            self.input_nama.text(),
            self.input_kategori.currentText(),
            kondisi,
            self.input_tanggal.date().toString("yyyy-MM-dd"),
            self.input_harga.value()
        )