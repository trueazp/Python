from interface import implements
from app.Dosen import Dosen
from app.DataSource import DataSource
from app.Mahasiswa import Mahasiswa

class DosenPa(implements(Dosen)):
  # constructor
  def __init__(self, id, namaDosen, noTelp, email):
    self.__id = id
    self.__namaDosen = namaDosen
    self.__noTelp = noTelp
    self.__email = email
    self.__dataSource = DataSource()
    self.__mahasiswaBimbingan = []

  # getter
  def getId(self):
    return self.__id

  def getNamaDosen(self):
    return self.__namaDosen

  def getNoTelp(self):
    return self.__noTelp

  def getEmail(self):
    return self.__email

  # overriding
  def setMahasiswaBimbingan(self):
    for bimbingan in self.__dataSource.getBimbinganDosen():
      self.__mahasiswaBimbingan.append(bimbingan)

  def showMahasiswaBimbingan(self):
    print("Berikut adalah mahasiswa bimbingan dari", self.__namaDosen)
    if not self.__mahasiswaBimbingan:
      print("Tidak memiliki mahasiswa bimbingan...")
    else:
      for mahasiswa in self.__mahasiswaBimbingan:
        print("Nama\t\t:", mahasiswa.getNama())
        print("Email\t\t:", mahasiswa.getEmail())
        print("-------------------------")