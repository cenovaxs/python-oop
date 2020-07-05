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


k001 = karyawan('Wendah','-',2250000,24)
k002 = karyawan("Djubi",'Mawar',2000000,48)

class boss(karyawan):
    def __init__(self,namadepan,namabelakang,gaji,umur,pegawai=None):
        super().__init__(namadepan,namabelakang,gaji,umur)
        if pegawai is None:
            self.pegawai = []
        else:
            self.pegawai = pegawai

    def add_emp(self, emp):
        if emp not in self.pegawai:
            self.pegawai.append(emp)

    def remove_emp(self, emp):
        if emp in self.pegawai:
            self.pegawai.remove(emp)

    def print_emps(self):
        for emp in self.pegawai:
            print('-->', emp.fullname())

boss01 = boss('Pujastanto','-', 4000000, 34, [k001])


print(boss01.gaji)
boss01.add_emp(k002)
boss01.print_emps()
print(issubclass(boss, karyawan))
print(isinstance(boss01, karyawan))
# print(karyawan.persentasinaikgaji)
#
# k001.cls_naikgaji(100)
# karyawan.cls_naikgaji(karyawan.persentasinaikgaji)
# print(karyawan.persentasinaikgaji)
# print(k001.persentasinaikgaji)
# print(k002.persentasinaikgaji)
