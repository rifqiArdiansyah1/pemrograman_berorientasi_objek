class Mobil:
    def __init__(self, merk, model, tahun, harga):
        self.merk = merk
        self._model = model
        self.tahun = tahun
        self.__harga = harga
    
    def info(self):
        title = "DATA MOBIL SHOWROOM"
        print("="*80)
        print(title.center(80))
        print("="*80)
        print(f"Merk    : {self.merk}")
        print(f"Model   : {self._model}")
        print(f"Harga   : {self.__harga}")
        print(f"Tahun   : Rp.{self.tahun}")
        print(f"Jenis   : {self.jenis_kendaraan()}")
        print("="*80)
    
    @staticmethod
    def jenis_kendaraan():
        return "Transportasi Darat"
    
    @classmethod
    def from_string(cls,data_string):
        merk, model, harga, tahun = data_string.split("|")
        return cls(merk, model, int(tahun), int(harga))

data = ["Toyota|innova|2020|350000000",
        "Mitsubishi|Pajero|2022|600000000"]

if __name__ == "__main__":
    daftar_mobil = []

    print("Tambah data mobil baru ke dalam showroom")
    print("contoh input: Honda|Civic|2023|550000000")
    while True:
        user_input = input("Masukkan data mobil (merk|model|tahun|harga): ")
        if user_input.lower() == 'selesai':
            break
        elif user_input.count("|") != 3:
            print("Format input salah. Silakan coba lagi.")
            continue
        else:
            try:
                new_mobil = Mobil.from_string(user_input)
            except ValueError:
                print("Nilai tahun atau harga tidak valid. Gunakan angka untuk tahun dan harga.")
                continue
            daftar_mobil.append(new_mobil)
            print("Data mobil berhasil ditambahkan.")
        
        
    for item in data:
        mobil = Mobil.from_string(item)
        daftar_mobil.append(mobil)
    
    for mobil in daftar_mobil:
        mobil.info()