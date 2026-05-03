# Sistem Inventaris Elektronik (Electronic Inventory System)

Aplikasi manajemen aset perangkat elektronik berbasis desktop yang dikembangkan menggunakan Python dan framework PySide6. Aplikasi ini menerapkan arsitektur Separation of Concerns (SoC) untuk manajemen data yang terstruktur dan modular.

## 👤 Identitas Pengembang
*   **Nama:** Zainul Majdi
*   **NIM:** F1D02310028
*   **Program Studi:** Teknik Informasi, Universitas Mataram

---

## 📝 Deskripsi Proyek
Aplikasi ini dirancang untuk mencatat data inventaris elektronik secara sistematis. Dengan menggunakan database SQLite, setiap data yang dimasukkan akan tersimpan secara permanen (persistent data). Antarmuka aplikasi telah dikustomisasi menggunakan Qt Style Sheets (QSS) untuk memberikan pengalaman pengguna yang profesional dan modern. 

### Fitur Utama:
*   **Create (Tambah Data):** Input data melalui jendela dialog terpisah dengan validasi field.
*   **Read (Tampilkan Data):** Visualisasi data inventaris dalam bentuk tabel yang rapi.
*   **Delete (Hapus Data):** Menghapus record aset elektronik dengan dialog konfirmasi keamanan.
*   **Custom Styling:** UI yang responsif dengan tema warna gelap pada header identitas sesuai standar project.

---

## 🚀 Teknologi & Arsitektur
*   **Bahasa:** Python 3.x
*   **GUI Framework:** PySide6 (Qt for Python)
*   **Database:** SQLite3 (Serverless)
*   **Pattern:** Model-View-Controller (MVC) / Separation of Concerns (SoC)

---

## 🛠 Cara Menjalankan Aplikasi

1. **Clone Repository:**
   ```bash
   git clone https://github.com/M47d1/pv26-miniproject-elektronik-F1D02310028.git
   cd pv26-miniproject-elektronik-F1D02310028

2. **Instalasi Dependensi**
   Pastikan Anda telah menginstal library PySide6 melalui terminal:
   ```bash
   pip install PySide6

3. **Menjalankan Program
   Eksekusi file utama aplikasi
   ```bash
   python3 main.py