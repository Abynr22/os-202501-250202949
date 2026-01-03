
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock 
---

## Identitas
- **Nama**  : M. Habibi Nur Ramadhan
- **NIM**   : 250202949 
- **Kelas** : 1IKRB

---

## Tujuan
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme deteksi deadlock** dalam sistem operasi.  
Berbeda dengan Minggu 7 yang berfokus pada *pencegahan dan penghindaran deadlock*, pada minggu ini mahasiswa diarahkan untuk **mendeteksi deadlock yang telah terjadi** menggunakan pendekatan algoritmik.

Mahasiswa akan membuat **program simulasi sederhana deteksi deadlock**, menjalankan dataset uji, serta menyajikan hasil analisis dalam bentuk tabel dan interpretasi logis.

Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan. 

---

## Dasar Teori
1. **Deadlock** adalah kondisi dimana dua atau lebih proses yang saling tunggu untuk melepaskan sumberdaya yang sedang digunakan oleh proses lain, sehingga semua proses akan terjebak pada siklus saling tunggu tanpa ada yang bisa maju. Biasanya ini sering di sebut dengan kebuntuan.

Ada beberapa karakteristik terjadinya deadlock:
* **Mutual Exclusion:** Sumber daya yang hanya dapat digunakan satu proses untuk satu waktu.
* **Hold and Wait:** Suatu proses yang sudah memegang sumber daya tapi masih menunggu sumberdaya yang digunakan oleh proses lain.
* **No Preemption:** Kondisi dimana sumber daya yang sedang digunakan proses tidak bisa diambil secara paksa oleh sistem operasi.
* **Circular Wait:** siklus tak berujung yang membuat semua proses terblokir permanen.

2. **Deteksi deadlock** adalah proses mengidentifikasi kondisi jalan buntu di sistem dengan menggunakan algoritma Deteksi Deadlock 

3. Metode dalam mencegah deadlock :
* **Deadlock Prevention**
mencegah deadlock sejak awal dengan cara menghilangkan salah satu dari empat kondisi Coffman (mutual exclusion, hold and wait, no preemption, circular wait).

* **Deadlock Avoidance**
menghindari deadlock secara dinamis dengan cara mengevaluasi setiap permintaan proses yang membawa kepada kondisi yang tidak aman.

* **Deadlock Detection**
membiarkan deadlock terjadi, kemudian mendeteksi dan menangani deadlock tersebut.
---

## Langkah Praktikum dan Ketentuan Teknis

- Bahasa pemrograman **bebas** (Python / C / Java / lainnya).  
- Program berbasis **terminal**, tidak memerlukan GUI.  
- Fokus penilaian pada **logika algoritma deteksi deadlock**, bukan kompleksitas bahasa.

Struktur folder (sesuaikan dengan template repo):
```
praktikum/week11-deadlock-detection/
├─ code/
│  ├─ deadlock_detection.*
│  └─ dataset_deadlock.csv
├─ screenshots/
│  └─ hasil_deteksi.png
└─ laporan.md
```
**Langkah Pengerjaan**
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah

```bash
import csv
import os

def print_table(data):
    if not data:
        print("[!] Tabel Kosong. Periksa format CSV Anda.")
        return
    
    headers = ["Process", "Allocation", "Request"]
    col_width = 12
    
    line = "+" + ("-" * (col_width + 2) + "+") * len(headers)
    print(line)
    print("| " + " | ".join(h.ljust(col_width) for h in headers) + " |")
    print(line)
    
    for row in data:
        print("| " + " | ".join(row.get(h, "").ljust(col_width) for h in headers) + " |")
    print(line)

def detect_deadlock(file_path):
    adj = {}
    raw_data = []
    
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} tidak ditemukan.")
        return

    try:
        # Menggunakan utf-8-sig untuk membuang karakter aneh di awal file
        with open(file_path, mode='r', encoding='utf-8-sig') as file:
            # Membaca mentah dulu untuk deteksi delimiter
            content = file.read()
            dialect = csv.Sniffer().sniff(content)
            file.seek(0)
            
            # Membaca CSV
            reader = csv.DictReader(file, delimiter=dialect.delimiter)
            
            # NORMALISASI: Bersihkan spasi dari nama kolom (header)
            reader.fieldnames = [name.strip() for name in reader.fieldnames]
            
            for row in reader:
                # NORMALISASI: Bersihkan spasi dari setiap nilai di dalam sel
                p = row.get('Process', '').strip()
                alloc = row.get('Allocation', '').strip()
                req = row.get('Request', '').strip()
                
                if p and alloc and req:
                    raw_data.append({'Process': p, 'Allocation': alloc, 'Request': req})
                    
                    # RAG: Resource -> Process (Holding)
                    if alloc not in adj: adj[alloc] = []
                    adj[alloc].append(p)
                    
                    # RAG: Process -> Resource (Requesting)
                    if p not in adj: adj[p] = []
                    adj[p].append(req)
                
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        return

    print("\n--- DATASET DEADLOCK ---")
    print_table(raw_data)

    # Algoritma DFS untuk mencari Cycle
    visited = set()
    rec_stack = []

    def find_cycle(v):
        visited.add(v)
        rec_stack.append(v)
        
        for neighbor in adj.get(v, []):
            if neighbor not in visited:
                if find_cycle(neighbor): return True
            elif neighbor in rec_stack:
                start_idx = rec_stack.index(neighbor)
                cycle = rec_stack[start_idx:]
                print("\n[!] STATUS: TERDETEKSI DEADLOCK!")
                print(f"[!] Jalur Siklus: {' -> '.join(cycle)} -> {neighbor}")
                return True
        
        rec_stack.pop()
        return False

    print("\n--- Menganalisis Resource Allocation Graph ---")
    found = False
    for node in list(adj.keys()):
        if node not in visited:
            if find_cycle(node):
                found = True
                break
    
    if not found:
        print("\n[V] STATUS: AMAN (Sistem bebas dari deadlock)")

if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)
    csv_path = os.path.join(current_dir, "dataset_deadlock.csv")
    detect_deadlock(csv_path)
```

---

## Hasil Eksekusi
Berdasarkan dataset yang saya buat:

| Process | Allocation | Request |
|--------|----------|-------|
|P1|R1|R2|
|P2|R2|R3|
|P3|R3|R4|
|P4|R4|R1|

![Screenshot hasil](screenshots/deadlock%20simulation.png)

---

## Analisis


| **Process** | **Allocation (Resource yang Dipegang)** | **Request (Resource yang Diminta)** | **Penjelasan**                                                                                          |
| ----------- | --------------------------------------- | ----------------------------------- | ------------------------------------------------------------------------------------------------------- |
| **P1**      | R1                                      | R2                                  | Proses P1 sedang memegang resource R1 dan menunggu resource R2 agar dapat melanjutkan prosesnya.        |
| **P2**      | R2                                      | R3                                  | Proses P2 memegang resource R2 dan meminta resource R3 yang saat ini sedang digunakan oleh proses lain. |
| **P3**      | R3                                      | R4                                  | Proses P3 memegang resource R3 dan menunggu resource R4 untuk melanjutkan eksekusi.                     |
| **P4**      | R4                                      | R1                                  | Proses P4 memegang resource R4 dan meminta resource R1 yang sedang dipegang oleh P1.                    |

Analisis Deadlock

 Pada tabel tersebut, terlihat adanya circular wait dengan pola berikut:

P1 → P2 → P3 → P4 → P1

Setiap proses memegang satu resource dan menunggu resource lain yang sedang digunakan oleh proses berikutnya. Tidak ada proses yang dapat melepaskan resource secara paksa (no preemption), sehingga semua proses saling menunggu tanpa akhir.
Kondisi anasisis praktikum menunjukkan bahwa sistem mengalami deadlock, karena seluruh proses berada dalam keadaan menunggu resource yang tidak akan pernah tersedia. Deadlock terjadi akibat terpenuhinya kondisi mutual exclusion, hold and wait, no preemption, dan circular wait.

---

## Kesimpulan
1. Deadlock akan terjadi saat beberapa proses saling menunggu resource secara permanen karena adanya kondisi mutual exclusion, hold and wait, no preemption, dan circular wait.

2. Sistem operasi menangani deadlock melalui tiga metode , yaitu deadlock prevention, deadlock avoidance, dan deadlock detection, yang masing-masing memiliki kelebihan dan kekurangan.

3. Pendekatan deadlock detection memberikan fleksibilitas dan pemanfaatan resource yang tinggi, namun memerlukan mekanisme deteksi dan pemulihan untuk mengatasi deadlock yang terjadi. 

---

## Quiz
1. Apa perbedaan antara *deadlock prevention*, *avoidance*, dan *detection*?  
**Jawaban**: ketiga metode ini berbeda. 
* Dimana **Deadlock Provention** mencegah deadlock sejak awal sehingga deadlock tidak mungkin terjadi dikarenakan metode ini menghilangkan minimal satu dari empat kondisi Coffman.
* **Deadlock Avoidance** menghindari deadlock secara dinamis tentunya metode ini menggunakan algoritma khusus yang mengevaluasi setiap permintaan resource, dan memiliki ultisasi proses yang lebih baik dari provention.
* **Deadlock Detection** metode yang digunakan membiarkan deadlock terjadi kemudian, mendeteksi dan menangani deadlock tersebut, metode ini memiliki ultilisasi proses yang tinggi dan sistem lebih fleksible.

2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
**Jawaban**: Deadlock detection sangat diperlukan untuk memberikan keseimbangan antara fleksibilitas dan efisiensi sistem. Metode ini memungkinkan sistem operasi mencapai utilisasi resource yang tinggi, meskipun harus menanggung risiko deadlock yang kemudian ditangani melalui mekanisme deteksi dan pemulihan.

3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?
**Jawaban**:
Kelebihan dari deadlock detection yaitu:
* Memiliki **Utilisasi resource tinggi** dimana sistem tidak membatasi cara proses meminta resource.
* **Lebih fleksibel** Proses dapat meminta resource kapan saja.
* **Cocok untuk sistem dinamis** Sangat sesuai untuk sistem dengan banyak proses dan permintaan resource yang berubah-ubah.
* **Overhead awal rendah** 
* **Efisien jika deadlock jarang terjadi**

Di satu sisi ini juga memiliki kekurangan
* **Deadlock tetap bisa terjadi**, kondisi ini hanya sementara dan akan ditangani.
* **Membutuhkan mekanisme pemulihan (recovery)**
* **Overhead saat proses deteksi**
* **Risiko kehilangan data**
* **Penentuan korban (victim selection) sulit**

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  bagian yang menantang bagaimana cara mengaplikasikan program untuk membuat kodisi algoritma pendeteksi deadlock yang masih sangat sulit saya pahami jika belajar sendiri tentunya ada beberapa bantuan ai untuk mempelajari materi ini.
- Bagaimana cara Anda mengatasinya?  belajar untuk mencari solusi.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
