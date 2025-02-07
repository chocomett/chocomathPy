import libs 
from datetime import date

def start(tahun_lahir, bulan_lahir, tanggal_lahir):
  hari_ini = date.today()
  tanggal_lahir = date(tahun_lahir, bulan_lahir, tanggal_lahir)
  umur = hari_ini.year - tanggal_lahir.year - ((hari_ini.month, hari_ini.day) < (tanggal_lahir.month, tanggal_lahir.day))
  return umur

# Contoh penggunaan
tahun_lahir = 1990
bulan_lahir = 5
tanggal_lahir = 15

umur = start(tahun_lahir, bulan_lahir, tanggal_lahir)
print(f"Umur Anda adalah {umur} tahun.")

if __name__ == "__main__":
    start()
    libs.wellcome_message()   
    libs.menu()