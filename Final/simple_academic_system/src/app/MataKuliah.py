from app.User import User

class MataKuliah(object):
  # constructor
  def __init__(self, kodeMatkul, namaMatkul, dosenPengajar, sks, kuota):
    self.__kodeMatkul = kodeMatkul
    self.__namaMatkul = namaMatkul
    self.__dosenPengajar = dosenPengajar
    self.__sks = sks
    self.__kuota = kuota
    self.__mahasiswaTerdaftar = []

  # getter
  def getKodeMatkul(self):
    return self.__kodeMatkul

  def getNamaMatkul(self):
    return self.__namaMatkul

  def getDosenPengajar(self):
    return self.__dosenPengajar

  def getSks(self):
    return self.__sks

  def getKuota(self):
    return self.__kuota

  # menambahkan mahasiswa ke dalam daftar mahasiswa yang mendaftar matkul ini
  def setMahasiswaTerdaftar(self, userMahasiswa):
    self.__mahasiswaTerdaftar.append(userMahasiswa)
    self.__kuota += 1

  # menghapus mahasiswa yang terdaftar dalam matkul ini
  def mahasiswaBatalMendaftar(self, userMahasiswa):
    self.__mahasiswaTerdaftar.remove(userMahasiswa)
    self.__kuota -= 1
