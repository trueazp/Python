# file for User's object

from app.Dosen import Advisor
import random

class Users:
  # constructor for user
  def __init__(self, id, userName, password):
    self.id = id
    self.userName = userName
    self.password = password

  # getter
  def getId(self):
    return self.id

  def getUserName(self):
    return self.userName

  def getPassword(self):
    return self.password

  def checkPass(self, password):
    return password == self.password


class UserMahasiswa(Users):
  # constructor for user mahasiswa
  def __init__(self, id, userName, password, Student):
    super().__init__(id, userName, password)
    self.mahasiswa = Student
    self.dosenPa = Advisor
    self.matkul = []
    self.listMatkul = set([])
    self.matkuls = ["Matematika Dasar (3 SKS)", "Pengantar Pemrograman (3 SKS)", "WSBM (2 SKS)", "Fisika Dasar (2 SKS)", "Kimia Dasar (2 SKS)", "Biologi Dasar (2 SKS)", "Pancasila (2 SKS)"]
    self.sksTerdaftar = 0
    self.ipk = random.uniform(2.75, 4.00)

    for i in range(0, len(self.matkuls)):
      self.listMatkul.add(self.matkuls[random.randrange(0, len(self.matkuls), 1)])

  # getter
  def getId(self):
    return self.id

  def getUserName(self):
    return self.userName

  def getPassword(self):
    return self.password

  def getMahasiswa(self):
    return self.mahasiswa

  def getSksTerdaftar(self):
    return  self.sksTerdaftar

  # checking password
  def checkPass(self, password):
    return password == self.password

  # add matkul
  def addMatkul(self, Course):
    try:
      if not Course in self.matkul:
        if Course.getKuota() > 0:
          self.sksTerdaftar += Course.getSks()
          if self.sksTerdaftar < 11:
            self.matkul.append(Course)
            Course.setMahasiswaTerdaftar(self)
            print("Mata kuliah", Course.getNamaMatkul(), "berhasil ditambahkan")
            print("Kuota tersisa untuk mata kuliah", Course.getNamaMatkul(), "sebanyak", Course.getKuota())
            print("-------------------------")
          else:
            print("Melewati batas total SKS yang diberikan...")
            print("-------------------------")
        else:
          print("Kuota tidak mencukupi...")
          print("-------------------------")
      else:
        print("Telah terdaftar dalam mata kuliah ini...")
    except:
      print("Error...")

  # remove mata kuliah
  def removeMatkul(self, Course):
    try:
      if self.sksTerdaftar == 0:
        print("Tidak ada mata kuliah yang diprogramkan...")
        print("-------------------------")
      else:
        if Course in self.matkul:
          self.matkul.remove(Course)
          Course.removeMahasiswaTerdaftar(self)
          self.sksTerdaftar -= Course.getSks()
          print("Mata kuliah", Course.getNamaMatkul(), "telah dihapus dari program...")
          print("Kuota tersisa untuk mata kuliah", Course.getNamaMatkul(), "sebanyak", Course.getKuota())
          print("-------------------------")
        else:
          print("Tidak dapat menghapus mata kuliah ini...")
          print("Anda belum terdaftar dalam mata kuliah ini...")
          print("-------------------------")
    except:
      print("Error...")

  # show mata kuliah yang diprogramkan
  def showMatkul(self):
    if self.sksTerdaftar == 0:
      print("Tidak ada mata kuliah yang diprogramkan...")
    else:
      print("Berikut adalah daftar mata kuliah yang diprogramkan oleh", self.userName)
      for matkul in self.matkul:
        print("Nama mata kuliah\t:", matkul.getNamaMatkul())
        print("Kode mata kuliah\t:", matkul.getKodeMatkul())
        print("Dosen pengajar\t\t:", matkul.getDosenPengajar())
        print("Jumlah satuan kredit:", matkul.getSks())
        print("-------------------------")

  # show IPS
  def showIps(self):
    print("Berikut adalah IPS semester lalu dari user", self.userName)
    for matkul in self.listMatkul:
      print(matkul)
    print("IPK :", "%.2f" %self.ipk)
    print("-------------------------")


class UserDosen(Users):
  # constructor for user dosen
  def __init__(self, id, userName, password, Advisor):
    super().__init__(id, userName, password)
    self.dosenPa = Advisor

# getter
  def getId(self):
    return self.id

  def getUserName(self):
    return self.userName

  def getPassword(self):
    return self.password

  def getDosenPa(self):
    return self.dosenPa

  # check password
  def checkPass(self, password):
    return password == self.password