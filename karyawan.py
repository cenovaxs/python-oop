class karyawan:
    jumlahkaryawan = 0
    persentasinaikgaji = 4
    naikgajipertahun = persentasinaikgaji/100+1
    def __init__(self,namadepan,namabelakang,gaji,umur):
        self.namadepan=namadepan
        self.namabelakang=namabelakang
        self.gaji=gaji
        self.umur=umur
        karyawan.jumlahkaryawan += 1
    def fullname(self):
        return f'{self.namadepan} {self.namabelakang}'
    def naikgaji(self):
        self.gaji = int(self.gaji * Karyawan.naikgajipertahun)
    def pertambahangaji(self):
        return int(self.gaji * Karyawan.persentasinaikgaji/100)
    @classmethod
    def cls_naikgaji(cls, nominal):
        cls.persentasinaikgaji = nominal


weri = karyawan('weri','-',2250000,24)
ros = karyawan("Tante",'Ros',2000000,48)


print(karyawan.persentasinaikgaji)

weri.cls_naikgaji(100)
karyawan.cls_naikgaji(karyawan.persentasinaikgaji)
print(karyawan.persentasinaikgaji)
print(weri.persentasinaikgaji)
print(ros.persentasinaikgaji)
