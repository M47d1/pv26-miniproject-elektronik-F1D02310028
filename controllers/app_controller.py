from PySide6.QtWidgets import QMessageBox, QTableWidgetItem
from views.form_dialog import InventoryDialog

class AppController:
    def __init__(self, view, db):
        self.view = view
        self.db = db
        self.init_connections()
        self.load_data()

    def init_connections(self):
        self.view.btn_add.clicked.connect(self.handle_add)
        self.view.btn_refresh.clicked.connect(self.load_data)
        self.view.btn_delete.clicked.connect(self.handle_delete)

    def load_data(self):
        data = self.db.fetch_all()
        self.view.table.setRowCount(0)
        for row_idx, row_data in enumerate(data):
            self.view.table.insertRow(row_idx)
            for col_idx, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.view.table.setItem(row_idx, col_idx, item)

    def handle_add(self):
        dialog = InventoryDialog(self.view)
        dialog.btn_save.clicked.connect(dialog.accept)
        
        if dialog.exec():
            new_data = dialog.get_data()
            if new_data[0].strip() == "":
                QMessageBox.warning(self.view, "Error", "Nama alat tidak boleh kosong!")
                return
            self.db.insert_peralatan(new_data)
            self.load_data()
            QMessageBox.information(self.view, "Sukses", "Data berhasil ditambahkan!")

    def handle_delete(self):
        curr_row = self.view.table.currentRow()
        if curr_row < 0:
            QMessageBox.warning(self.view, "Peringatan", "Pilih data yang ingin dihapus!")
            return
        
        item_id = self.view.table.item(curr_row, 0).text()
        confirm = QMessageBox.question(self.view, "Konfirmasi", f"Hapus ID {item_id}?", 
                                    QMessageBox.Yes | QMessageBox.No)
        
        if confirm == QMessageBox.Yes:
            self.db.delete_peralatan(item_id)
            self.load_data()