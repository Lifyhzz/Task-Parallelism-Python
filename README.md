# Implementasi Task Parallelism (Python)

Repository ini dibuat untuk memenuhi tugas mata kuliah Komputasi Paralel (WFA). Program ini mendemonstrasikan eksekusi asinkron menggunakan arsitektur **Task Parallelism**, di mana program menjalankan tugas (*task*) yang sepenuhnya berbeda secara serentak pada *core* CPU yang berbeda.

## 👨‍💻 Identitas Mahasiswa
- **Nama:** Lifyana Nailah Azzahra
- **NRP:** 152024107 (Ganjil)
- **Tugas:** Task Parallelism

## ⚙️ Penjelasan Task (Tugas)
Program ini menggunakan *library* `multiprocessing` bawaan Python untuk menjalankan 3 tugas berbeda secara bersamaan:
1. **Task 1 (Math Computation):** *CPU-Bound task* untuk menghitung total deret bilangan kuadrat hingga 5.000.000 iterasi.
2. **Task 2 (Data Sorting):** *Memory/CPU-Bound task* untuk membuat dan mengurutkan 3.000.000 angka acak (array) dari yang terkecil hingga terbesar.
3. **Task 3 (Hashing Cryptography):** Simulasi keamanan siber dengan mengenkripsi sebuah string teks menggunakan algoritma SHA-256 yang diulang sebanyak 2.000.000 kali.

## 🚀 Cara Menjalankan Program
Pastikan Python versi 3.x sudah terinstal di sistem Anda.

1. Clone repository ini:
   ```bash
   git clone [https://github.com/USERNAME_GITHUB_KAMU/Task-Parallelism-Python.git](https://github.com/USERNAME_GITHUB_KAMU/Task-Parallelism-Python.git)
