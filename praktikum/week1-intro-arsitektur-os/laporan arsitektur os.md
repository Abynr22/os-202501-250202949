
# Laporan Praktikum Minggu [1]
Topik: "Laporan Arsitektur OS"

---

## Identitas
- **Nama**  : M. Habibi Nur Ramadhan
- **NIM**   : 250202949
- **Kelas** : 1IKRB

---

## Tujuan
Tujuan pembelajaran pada minggu ini mahasiswa mampu mengidentifikasi microkernel, monolitik, hybird kernel, dan cara mengoperasikan linux pada perangkat.

---

## Dasar Teori
Jadi sistem operasi atau (OS) adalah sebuah konsep awal yang perlu di pelajari untuk mahasiswa ilmu komputer di mana sistem operasi adalah sebuah perangkat lunak yang menghubungkan antara user dan perangkat keras, mengelola seluruh sumber daya komputer. Ada beberapa point yang akan di pelajari untuk mengenal konsep awal pada komputer:
* Model sebuah arsitektur OS seperti **monolithic kernel, microkernel , hybird kernel dan layered approach**
* Mekanisme dari **system call**
* Mode eksekusi **kernel mode** dan **user mode**
* 

---

## Langkah Praktikum
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi. 
   **Jawaban:**  
2. Jelaskan perbedaan antara kernel mode dan user mode.
   **Jawaban:**  
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? **semua bagian dari minggu ini menantang karena baru mempelajari basic pada komputer, mulai dari memperkenalkan bagian-bagian komputer sampai dengan pengoperasian aplikasi seperti vscode, git bash, github , draw.io dan lain-lain.**
- Bagaimana cara Anda mengatasinya? **Saya mempelajari ini secara otodidak dan dengan berdiskusi dengan teman.**

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
