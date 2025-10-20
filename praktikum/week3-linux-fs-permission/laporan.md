
# Laporan Praktikum Minggu [3]
Topik: Manajemen File dan Permission di Linux

---

## Identitas
- **Nama**  : M. Habibi Nur Ramadhan
- **NIM**   : 250202949
- **Kelas** : 1 IKRB

---

## Tujuan
Tuliskan tujuan praktikum minggu ini.  
Menggunakan perintah ls, pwd, cd, cat untuk navigasi file dan direktori.
Menggunakan chmod dan chown untuk manajemen hak akses file.
Menjelaskan hasil output dari perintah Linux dasar.
Menyusun laporan praktikum dengan struktur yang benar.
Mengunggah dokumentasi hasil ke Git Repository tepat waktu.

---

## Dasar Teori
Saat kita menggunakan linux, akan sangat penting kamu memahami dan bisa mengatur hal perizinan file yang ada di linux. Dan apa itu perizinan File atau permission?
Linux punya aturan yang ketat mengenai hak akses, tidak bisa mengakses file menggunakan user biasa(bukan root) karena belum diatur hak aksesnya.
Hak akses file bisa kita lihat dengan mengecek attribut file tersebut menggunakan perintah linux.
Setiap file dan folder di linux punya atribut yang menentukan akses untuk user ataupun group di sistem tersebut.
Inilah alasan mengapa linux sangat aman,karena sebuah file bisa diset agar hanya bisa diakses /dimodifikasi oleh user dan group tertentu.
3 Atribut Akses pada File dan Folder
Setiap file pada linux mempunyai 3 attribute yang menjelaskan hak akses user dan group terhadap file tersebut, yaitu:
owner/user (pemilik file)
group (user yang berada di group tertentu)
dan other/world (semua user yang ada di sistem).
Hak akses disini berupa hak akses untuk :
Membaca data (Read)
Memodifikasi data (Write)
dan Mengeksekusi/menjalankan file aplikasi(eXecutable)
Hak akses ini sering dikenal dengan atribut R-W-X


## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan folder kerja berada di dalam direktori repositori Git praktikum:
     ```
     praktikum/week3-linux-fs-permission/
     ```

2. **Eksperimen 1 – Navigasi Sistem File**
   Jalankan perintah berikut:
   ```bash
   pwd
   ls -l
   cd /tmp
   ls -a
   ```
   - Jelaskan hasil tiap perintah.
   - Catat direktori aktif, isi folder, dan file tersembunyi (jika ada).

3. **Eksperimen 2 – Membaca File**
   Jalankan perintah:
   ```bash
   cat /etc/passwd | head -n 5
   ```
   - Jelaskan isi file dan struktur barisnya (user, UID, GID, home, shell).

4. **Eksperimen 3 – Permission & Ownership**
   Buat file baru:
   ```bash
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   ```
   - Analisis perbedaan sebelum dan sesudah chmod.  
   - Ubah pemilik file (jika memiliki izin sudo):
   ```bash
   sudo chown root percobaan.txt
   ls -l percobaan.txt
   ```
   - Catat hasilnya.

5. **Eksperimen 4 – Dokumentasi**
   - Ambil screenshot hasil terminal dan simpan di:
     ```
     praktikum/week3-linux-fs-permission/screenshots/
     ```
   - Tambahkan analisis hasil pada `laporan.md`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 3 - Linux File System & Permission"
   git push origin main
   ```

---

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
pwd
   ls -l
   cd /tmp
   ls -a
   cat /etc/passwd | head -n 5
   echo "Hello <NAME><NIM>" > percobaan.txt
   ls -l percobaan.txt
   chmod 600 percobaan.txt
   ls -l percobaan.txt
   sudo chown root percobaan.txt
   ls -l percobaan.txt
```
---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](Screenshotlinuxweek3.png)


---
 ### Hasil eksekusi Kode perintah,pwd , ls, ls -a, cd/tmp, ls -a.
| Perintah | Output | Keterangan |
| :--- | :--- | :--- |
| `mkdir week3-linux-fs-permission` | (no output) | Membuat folder praktikum |
| `ls` | `week3-linux-fs-permission` | Menampilkan direktori yang ada |
| `pwd` | `/home/habibinurramadhan123` | Menampilkan direktori progressing saat ini, hasilnya direktori home dari user `habibinurramadhan123`. |
| `ls -l` | `drwxrwxr-x 2 habibinurramadhan123 habibinurramadhan123 4096 oct 20 12:39 week3-linux-fs-permission ` | Menampilkan isi direktori . Terlihat direktori `week3-linux-fs-permission` dan tanggal akses. |
| `cd /tmp` | (Tidak ada output) | Mengubah direktori aktif. |
| `ls -a` | (Menampilkan daftar file `minikube_delete`dll.) | Menunjukan seluruh isi dari direktori `/tmp`, termasuk file-file service dan file tersembunyi. |

 ### Hasil eksekusi kode perintah echo "Hello <NAME><NIM>" > percobaan.txt, ls -l percobaan.txt, chmod 600 percobaan.txt, ls -l percobaan.txt
   
| Perintah | Output | Keterangan |
| :--- | :--- | :--- |
| `echo "Hello <Habibi><250202949>" > percobaan.txt` | (no output) | perintah untuk mencetak teks|
| `ls -l percobaan.txt` | -rw-rw-r-- 1 habibinurramadhan123... | Menampilkan permission (izin akses) |
| `chmod 600 percobaan.txt` | no output | mengatur permission percobaan.txt|
| `ls -l percobaan.txt` | -rw------ | membaca dan menulis file |

 ### Hasil eksekusi kode perintah sudo chown root percobaan.txt, ls -l percobaan.txt dan cat /etc/passwd head -n 5
   
| Perintah | Output | Keterangan |
| :--- | :--- | :--- |
| `sudo chown root percobaan.txt`| (no output) | mengubah kepemilikan owner file percobaan.txt |
| `ls -l percobaan.txt` | -rw----- 1 root habibinurramadhan123... | Menampilkan permission (izin akses) membaca dan menulis |
| `cat /etc/passwd head -n 5`| root:x:0:0:root:/root:/bin/bash.....| menampilkan 5 baris pertama dari file|


## Analisis
- Jelaskan makna hasil percobaan.
Analisis hasil eksekusi perintah `pwd`, `ls -1`, `cd/tmp` , dan `ls -a` kode perintah ini digunakan untuk menampilkan lokasi kerja saat ini  melihat isi direktori dengan format berbeda , berpindah ke direktori/tmp , yang dapat menampilkan semua file termasuk file yang tersembunyi.

Analisis untuk perintah `cat /etc/passwd | head -n 5` pada perintah ini menampilkan sebuah username, paswword, UID / GID user id dan group id, GECOS (informasi user) , home directory, dan shell.
Pada perintah `echo "Hello <Habibi><250202949>" > percobaan.txt` ini menampilkan hasil print teks `<Habibi><250202949>`
Dan pada perintah `ls -l percobaan.txt` terdapat output seperti `-rw-rw-r-- 1 habibinurramadhan123... ` rw atau read & write artinya saya hanya memiliki hak untuk membaca dan mengubah.
Dan pada `chmod` hasil analisis menunjukan sebuah permission atau izin akses ke file. sedangkan pada perintah `chown root` ini mengubah kepemilikan atau owner pada sebuah file.


---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
 * Pada kesimpulannya Permission atau izin akses linux berperan mengatur keamaanan file dan direktori, menentukan siapa saja yang dapat mengakses , seperti membaca , menulis , dan menjalankan.
 * perintah penting yang digunakan pada permission linux : `ls -l` melihat izin dan pemilik file , `chmod` mengubah izin akses , `chown` mengubah pemilik file.
 * Dan izin akses ditampilkan dalam bentuk simbolik (rwxr-xr--) atau numerik (chmod 755 file.txt)


---

## Quiz
1. Apa fungsi dari perintah `chmod`?  
   **Jawaban:**  Fungsi dari perintah chmod digunakan untuk mengubah izin akses (permission) pada file ataupun direktori OS pada Linux. Fungsi utamanya ialah untuk membaca (read) file atau direktori > r ,menulis (write) mengubah isi file > w, dan menjalankan (execute) > x, di kenal dengan istilah R W X.
2. Apa arti dari kode permission `rwxr-xr--`?  
   **Jawaban:**  ini adalah sebuah simbolik yang menunjukan izin (permission) pada sebuah file ataupun direktori , pada rwx atau read,write, execute hanya pemilik file yang bisa membaca, mengubah dan menjalankan file. pada r-x anggota pada grup bisa membaca dan menjalankan tetapi tidak bisa mengubah isi file. dan  untuk r-- read only , pengguna lain hanya bisa membaca tetapi tidak bisa menjalankan dan mengubah.
3. Jelaskan perbedaan antara `chown` dan `chmod`.  
   **Jawaban:** Kedua perintah ini mengatur hak akses file , tetapi kedua perintah ini memiliki fungsi dasarnya yang berbeda. Pada chmod atau change mode , mengubah izin akses (permission) file atau direktori siapa yang boleh membaca, menulis , dan menjalankan. pada chown atau change owner Mengubah kepemilikan (owner) file atau direktori siapa pemilik dan grup dari file.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  Bagian yang menantang pada minggu ini semua sangat menantang dalam mengoperasikan linux, dan karena pada minggu ini daring otomatis kita belajar sendiri dirumah.
- Bagaimana cara Anda mengatasinya?  belajar dan terus belajar. 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
