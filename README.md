🚗 Data Showroom Mobil Console App
Aplikasi berbasis console sederhana yang dikembangkan dengan Python untuk mengelola data kendaraan dalam sebuah showroom. Aplikasi ini memanfaatkan konsep Pemrograman Berorientasi Objek (OOP), termasuk penggunaan class methods dan static methods, serta menerapkan validasi input dasar.
⚙️ Cara MenjalankanPastikan Python Terinstal:Bashpython --version
Kloning Repositori:Bashgit clone https://github.com/rifqiArdiansyah1/pemrograman_berorientasi_objek
cd [NAMA_FOLDER_REPO]
Jalankan Aplikasi:python showroom.py)
📝 Penggunaan Aplikasi
Setelah aplikasi berjalan, Anda akan diminta untuk memasukkan data mobil baru.
Format InputData mobil harus dimasukkan dengan format:MERK|MODEL|TAHUN|HARGA
Contoh Input:Honda|Brio|2027|100000000
Mengakhiri InputUntuk menyelesaikan proses input data mobil, ketik:selesai
Validasi InputAplikasi memiliki validasi dasar untuk mencegah input data yang tidak valid:Pengecekan Format: Memastikan input memiliki tiga pemisah (|).
Pengecekan Tipe Data: Memastikan nilai untuk TAHUN dan HARGA adalah angka. 
Jika gagal, akan muncul pesan Nilai tahun atau harga tidak valid....
🛠️ Detail Teknis 
(Struktur Kode)Aplikasi ini dibangun di sekitar satu kelas utama, Metode/Atribut,Tipe,Deskripsi
__init__,Konstruktor,"Menginisialisasi atribut merk, model, tahun, dan harga untuk setiap objek mobil."
info(),Metode Instansi,"Menampilkan detail lengkap mobil (Merk, Model, Tahun, Harga, Jenis) dengan format yang rapi."
jenis_kendaraan(),@staticmethod,"Mengembalikan nilai ""Transportasi Darat"". Terikat pada kelas, tidak memerlukan akses ke data instansi (self)."
"from_string(cls, data_string)",@classmethod,Konstruktor Alternatif. Digunakan untuk membuat objek Mobil dari string input (`merk
Digunakan untuk membuat objek Mobil dari string input (`merkAlur Program UtamaInisialisasi daftar_mobil (list kosong).Memuat data mobil awal yang telah didefinisikan ke dalam daftar_mobil menggunakan Mobil.from_string().Memasuki loop interaktif untuk menerima input dari pengguna.Validasi input dan penambahan objek mobil baru ke daftar_mobil.Setelah pengguna mengetik selesai, program akan mengiterasi seluruh daftar_mobil dan memanggil mobil.info() untuk menampilkan data semua mobil.
