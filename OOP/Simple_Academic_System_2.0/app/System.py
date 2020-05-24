# file for Login's object

from app.Mahasiswa import Student
from app.Dosen import Advisor
from app.User import UserDosen, UserMahasiswa
from app.DataSource import DataBase

class Login:
  # static variable
  login = None

  # constructor
  def __init__(self):
    self.userMahasiswa = UserMahasiswa
    self.userDosen = UserDosen
    self.mahasiswa = Student
    self.dosenPa = Advisor
    self.dataSource = DataBase.getInstance()
    self.authenticatedMahasiswa = False
    self.authenticatedDosen = False

  # instansiasi
  @classmethod
  def getInstance(cls):
    if cls.login == None:
      cls.login = Login()
    return cls.login

  # getter
  def getUserMahasiswa(self):
    return self.userMahasiswa

  def getUserDosen(self):
    return self.userDosen

  def getDosenPa(self):
    return self.dosenPa

  def getAuthMahasiswa(self):
    return self.authenticatedMahasiswa

  def getAuthDosen(self):
    return self.authenticatedDosen

  # login mahasiswa
  def authMahasiswa(self, userName, password):
    self.userMahasiswa = self.dataSource.getUserMahasiswa(userName)
    try:
      if self.userMahasiswa.checkPass(password):
        self.mahasiswa = self.userMahasiswa.getMahasiswa()
        self.authenticatedMahasiswa = True
        return True
      else:
        print("Wrong Password...")
        return False
    except:
      print("Username", userName, "not found")

  # login dosen
  def authDosen(self, userName, password):
    self.userDosen = self.dataSource.getUserDosen(userName)
    try:
      if self.userDosen.checkPass(password):
        self.dosenPa = self.userDosen.getDosenPa()
        self.authenticatedDosen = True
        return True
      else:
        print("Wrong password...")
        return False
    except:
      print("Username", userName, "not found")

  # menampilkan detail user mahasiswa
  def statusMahasiswa(self):
    if self.authenticatedMahasiswa:
      print("-------------------------")
      print("Berikut adalah profil dari", self.userMahasiswa.getUserName())
      print("Nama\t\t:", self.mahasiswa.getNama())
      print("Email\t\t:", self.mahasiswa.getEmail())
      print("Dosen Pa\t:", self.mahasiswa.getNamaDosenPa())
      print("Username\t:", self.userMahasiswa.getUserName())
      print("Password\t:", self.userMahasiswa.getPassword(), "\n")
      self.getUserMahasiswa().showMatkul()
      print("JUMLAH TOTAL SKS :", self.userMahasiswa.getSksTerdaftar())
      print("-------------------------")
    else:
      print("Not authenticated...")

  # menampilkan detail user dosen
  def statusDosen(self):
    if self.authenticatedDosen:
      print("Berikut adalah profil dari dosen", self.userDosen.getUserName())
      print("Nama\t\t\t:", self.dosenPa.getNamaDosen())
      print("Nomor Telepon\t:", self.dosenPa.getNoTelp())
      print("Email\t\t\t:", self.dosenPa.getEmail())
      print("-------------------------")
    else:
      print("Not authenticated...")

  # logout
  def logout(self):
    self.userMahasiswa = None
    self.userDosen = None