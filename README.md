Aplikasi ini dibuat menggunakan bahasa pemrograman Python dengan memanfaatkan Pemrograman Berorientasi Objek (OOP) melalui sebuah kelas bernama Mobil. Tujuannya adalah untuk mengelola dan menampilkan data mobil di sebuah showroom.
1. Struktur Kelas Mobil
Kelas Mobil adalah cetak biru untuk setiap objek mobil yang akan dibuat.
•	__init__(self, merk, model, tahun, harga):
o	Ini adalah konstruktor kelas. Setiap kali objek Mobil baru dibuat, metode ini akan dipanggil.
o	Ia menerima empat argumen: merk, model, tahun, dan harga.
o	Argumen-argumen ini disimpan sebagai atribut instansi (self.merk, self.model, self.tahun, self.harga), yang merupakan data spesifik untuk setiap objek mobil.
•	info(self):
o	Ini adalah metode instansi yang digunakan untuk menampilkan informasi lengkap dari objek mobil.
o	Outputnya diformat dengan header dan separator yang rapi.
o	Ia memanggil self.jenis_kendaraan() untuk mendapatkan jenis kendaraan yang akan ditampilkan.
•	@staticmethod jenis_kendaraan():
o	Ini adalah metode statis. Metode ini terikat pada kelas, bukan pada instansi, dan tidak memerlukan akses ke data instansi (self).
o	Fungsinya hanya mengembalikan nilai string tetap: "Transportasi Darat".
•	@classmethod from_string(cls, data_string):
o	Ini adalah metode kelas. Metode ini terikat pada kelas dan menerima kelas itu sendiri sebagai argumen pertama (cls).
o	Fungsinya adalah sebagai konstruktor alternatif untuk membuat objek Mobil dari string dengan format tertentu (merk|model|tahun|harga).
o	Prosesnya:
1.	Memecah string input (data_string.split('|')).
2.	Mengonversi tahun dan harga menjadi tipe data integer (int()).
3.	Memanggil konstruktor utama (cls(merk, model, tahun, harga)) untuk membuat dan mengembalikan objek Mobil baru.
________________________________________
2. Alur Eksekusi Program Utama
Bagian ini dimulai di bawah blok if __name__ == "__main__":, yang memastikan kode berjalan hanya ketika file ini dieksekusi secara langsung.
A. Inisialisasi Data Awal
•	Sebuah list kosong bernama daftar_mobil dibuat untuk menyimpan semua objek mobil.
•	Data awal yang sudah ada (data) berupa list string diolah menggunakan loop:
1.	Setiap string di dalam data diproses oleh Mobil.from_string(item) untuk membuat objek Mobil.
2.	Objek Mobil yang baru dibuat ditambahkan ke daftar_mobil.
B. Input Data Baru dari Pengguna (Loop Interaktif)
•	Program meminta pengguna untuk memasukkan data mobil baru dalam format merk|model|tahun|harga.
•	Loop while True berjalan hingga pengguna mengetik selesai.
•	Pengecekan dan Validasi Input:
o	Pengecekan Break: Jika input adalah selesai (tidak sensitif huruf besar/kecil), loop dihentikan.
o	Pengecekan Format (Jumlah Pemisah |): Program mengecek apakah jumlah pemisah | adalah 3 (menunjukkan 4 bagian data). Jika tidak, pesan error ditampilkan, dan loop berlanjut ke iterasi berikutnya.
o	Pengecekan Tipe Data (Harga/Tahun):
	Kode mencoba memanggil Mobil.from_string(user_input).
	Jika tahun atau harga yang dimasukkan bukan angka, ValueError akan muncul (karena fungsi int() gagal).
	Blok try...except ValueError menangkap error ini, menampilkan pesan "Nilai tahun atau harga tidak valid...", dan loop berlanjut ke iterasi berikutnya.
o	Penyimpanan Data Berhasil: Jika semua pengecekan lolos, objek Mobil baru disimpan ke daftar_mobil, dan pesan konfirmasi ditampilkan.
C. Tampilan Data Akhir
•	Setelah loop input selesai, program melakukan iterasi pada setiap objek mobil di dalam daftar_mobil.
•	Untuk setiap objek, metode mobil.info() dipanggil, yang akan menampilkan semua data mobil yang ada di showroom (data awal + data yang diinput pengguna).
________________________________________
3. Hasil Tampilan Aplikasi
Tampilan menunjukkan hasil dari eksekusi kode:
•	Tampilan Input ():
o	Input pertama (Honda|Brio|2027|100000000) berhasil ditambahkan.
o	Input kedua (Supra|X|200p|1000R) gagal dan menampilkan error "Nilai tahun atau harga tidak valid..." karena 200p dan 1000R bukan angka.
o	Input ketiga (Yamaha|2026|100000000) gagal dan menampilkan error "Format input salah..." karena hanya memiliki dua pemisah | (data merk|tahun|harga), bukan tiga.
•	Tampilan Output Akhir ():
o	Menampilkan data mobil yang berhasil diinisialisasi (Toyota Innova, Mitsubishi Pajero).
o	Menampilkan data mobil yang berhasil diinput oleh pengguna (Honda Brio).
o	Setiap data ditampilkan menggunakan format yang dihasilkan oleh metode info().
