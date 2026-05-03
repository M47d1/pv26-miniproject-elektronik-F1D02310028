import os

import sys
import os
from PySide6.QtWidgets import QApplication
from database.db_handler import DatabaseHandler
from views.main_window import MainWindow
from controllers.app_controller import AppController

def load_stylesheet(app):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    qss_path = os.path.join(script_dir, "assets", "style.qss")
    
    if os.path.exists(qss_path):
        with open(qss_path, "r") as f:
            app.setStyleSheet(f.read())
            print("--- Style.qss Berhasil Dimuat ---")
    else:
        print(f"--- PERINGATAN: Style.qss tidak ditemukan di {qss_path} ---")

if __name__ == "__main__":
    print("--- Memulai Aplikasi ---")
    app = QApplication(sys.argv)
    
    # 1. Inisialisasi Database
    db = DatabaseHandler()
    print("--- Database Siap ---")
    
    # 2. Inisialisasi Tampilan
    view = MainWindow()
    print("--- Window Siap ---")
    
    # 3. Inisialisasi Controller (Penting: harus disimpan di variabel)
    controller = AppController(view, db)
    print("--- Controller Terhubung ---")
    
    # 4. Load Style
    load_stylesheet(app)
    
    # 5. Tampilkan Jendela
    view.show()
    print("--- Menjalankan Event Loop ---")
    
    sys.exit(app.exec())