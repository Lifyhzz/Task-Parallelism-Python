import multiprocessing
import time
import random
import hashlib

# ==============================================================================
# TUGAS 1: Komputasi Matematika Berat (Menghitung jumlah kuadrat)
# Kategori: CPU-Bound Task
# ==============================================================================
def task_math_computation(limit):
    waktu_mulai = time.strftime('%H:%M:%S')
    print(f"[{waktu_mulai}] TASK 1 (Math): Memulai perhitungan jumlah kuadrat hingga {limit}...")
    
    total = sum(i * i for i in range(1, limit + 1))
    time.sleep(1.2) # Simulasi agar proses terlihat berjalan beriringan
    
    waktu_selesai = time.strftime('%H:%M:%S')
    print(f"[{waktu_selesai}] TASK 1 SELESAI: Total jumlah kuadrat adalah {total}")

# ==============================================================================
# TUGAS 2: Simulasi Pemrosesan Data (Membuat dan mengurutkan array acak)
# Kategori: Memory-Bound & CPU-Bound Task
# ==============================================================================
def task_data_sorting(array_size):
    waktu_mulai = time.strftime('%H:%M:%S')
    print(f"[{waktu_mulai}] TASK 2 (Sorting): Membuat dan mengurutkan {array_size} angka acak...")
    
    # Membuat list angka acak dan mengurutkannya
    random_list = [random.randint(1, 100000) for _ in range(array_size)]
    random_list.sort()
    time.sleep(1.5) # Waktu tunggu simulasi
    
    waktu_selesai = time.strftime('%H:%M:%S')
    print(f"[{waktu_selesai}] TASK 2 SELESAI: {array_size} angka berhasil diurutkan. Angka terbesar: {random_list[-1]}")

# ==============================================================================
# TUGAS 3: Keamanan Data (Melakukan Hashing SHA-256 berulang kali)
# Kategori: Cryptography Task
# ==============================================================================
def task_encryption_hashing(text, iterations):
    waktu_mulai = time.strftime('%H:%M:%S')
    print(f"[{waktu_mulai}] TASK 3 (Hashing): Mengenkripsi teks '{text}' sebanyak {iterations} kali...")
    
    current_hash = text.encode()
    for _ in range(iterations):
        current_hash = hashlib.sha256(current_hash).digest()
    
    time.sleep(0.8) # Proses ini dibuat sedikit lebih cepat dari yang lain
    final_hex = current_hash.hex()
    
    waktu_selesai = time.strftime('%H:%M:%S')
    print(f"[{waktu_selesai}] TASK 3 SELESAI: Hasil akhir hash -> {final_hex[:15]}...")

# ==============================================================================
# BLOK UTAMA: Menjalankan Task Parallelism
# ==============================================================================
if __name__ == "__main__":
    print("=" * 60)
    print(" IMPLEMENTASI TASK PARALLELISM - Lifyana (NRP: 107)")
    print("=" * 60 + "\n")
    
    start_time = time.time()

    # Inisialisasi proses. Terlihat jelas bahwa KETIGA TUGAS INI BERBEDA (Task Parallelism)
    p1 = multiprocessing.Process(target=task_math_computation, args=(5000000,))
    p2 = multiprocessing.Process(target=task_data_sorting, args=(3000000,))
    p3 = multiprocessing.Process(target=task_encryption_hashing, args=("Informatika107", 2000000))

    # .start() digunakan untuk memicu ketiga proses berjalan pada WAKTU YANG SAMA di core CPU berbeda
    p1.start()
    p2.start()
    p3.start()

    # .join() menahan program utama agar tidak selesai sebelum ketiga task pembantu selesai
    p1.join()
    p2.join()
    p3.join()

    end_time = time.time()
    print("\n" + "=" * 60)
    print(f" SEMUA TASK PARALEL SELESAI DALAM {end_time - start_time:.4f} DETIK")
    print("=" * 60)