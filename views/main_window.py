from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QPushButton, QTableWidget, QLabel, QHeaderView)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Elektronik - Zainul Majdi F1D02310028")
        self.resize(1000, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Identitas Mahasiswa (Read-Only)
        self.lbl_id = QLabel("APLIKASI INVENTARIS ELEKTRONIK\nZainul Majdi | NIM: F1D02310028")
        self.lbl_id.setObjectName("identitasLabel")
        self.lbl_id.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.lbl_id)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(["ID", "Nama Alat", "Kategori", "Kondisi", "Tanggal", "Harga"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.layout.addWidget(self.table)

        # Controls
        self.btn_layout = QHBoxLayout()
        self.btn_add = QPushButton("Tambah Barang")
        self.btn_delete = QPushButton("Hapus Barang")
        self.btn_refresh = QPushButton("Refresh Data")
        
        self.btn_layout.addWidget(self.btn_add)
        self.btn_layout.addWidget(self.btn_delete)
        self.btn_layout.addWidget(self.btn_refresh)
        self.layout.addLayout(self.btn_layout)