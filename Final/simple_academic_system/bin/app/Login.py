from app.User import User
from app.Mahasiswa import Mahasiswa
from app.DosenPa import DosenPa
from app.DataSource import DataSource

class Login(object):
  # static variable
  __login = None
  # constructor
  def __init__(self):
    self.__user = User()
    self.__mahasiswa = Mahasiswa()
    self.__dosenPa = DosenPa()
    self.__dataSource = DataSource()
    self.__authenticated = False

  # instansiasi
  def getInstance(self):
    if self.__login == None:
      self.__login = Login()
    return self.__login

  # getter
  def getUser(self):
    return self.__user

  def getDosenPa(self):
    return self.__dosenPa

  def getAuth(self):
    return self.__authenticated

  # login mahasiswa
  def authDosen(self, userName, password):
    self.__user = self.__dataSource.getUserDosen(userName)
    try:
      if self.__user.checkPass(password):
        self.__dosenPa = self.__user.getDosenPa()
        self.__authenticated = True
        return True
    except:
      print("Username not found...")

  # menampilkan detail user mahasiswa
  def statusMahasiswa(self):
    if self.__authenticated:
      print("-------------------------")
      print("Berikut adalah profil dari", self.__user.getUserName())
      print("Nama\t\t:", self.__mahasiswa.getNama())
      print("Email\t\t:", self.__mahasiswa.getEmail())
      print("Dosen Pembimbing:", self.__mahasiswa.getNamaDosenPa())
      print("Username\t:", self.__user.getUserName())
      print("Password\t:", self.__user.getPassword())
      self.getUser().showMatkul()
      print("JUMLAH TOTAL SKS : ", self.__user.getSksTerdaftar())
      print("-------------------------")
    else:
      print("Not authenticated...")

    # menampilkan detail user dosen
    def statusDosen(self):
      if self.__authenticated:
        print("Berikut adalah profil dari dosen", self.__user.getUserName())
        print("Nama\t\t:", self.__dosenPa.getNamaDosenPa())
        print("Nomor Telepon\t:", self.__dosenPa.getNoTelp())
        print("Email\t\t:", self.__dosenPa.getEmail())
        print("-------------------------")
      else:
        print("Not authenticated...")

    # keluar dari akun
    def logout(self):
      self.__user = None