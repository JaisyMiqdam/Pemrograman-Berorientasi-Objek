class Mahasiswa:
    def __init__(self, nama, umur, jurusan):
        self.nama = nama
        self.umur = umur
        self.jurusan = jurusan

    def get_info(self):
        print(
            f'Biodata anda :\n    Nama    : {self.nama}\n    Umur    : {self.umur}\n    Jurusan : {self.jurusan}')

    def set_nama(self, ubah_nama):
        self.nama = ubah_nama

    def set_umur(self, ubah_umur):
        self.umur = ubah_umur


mahasiswa = Mahasiswa('Jaisy Muhammad Al Miqdam', 19,
                      'Pendidikan Teknik Informatika')
mahasiswa.get_info()
mahasiswa.set_nama('Jaisy Al Miqdam')
mahasiswa.set_umur(20)
mahasiswa.get_info()
