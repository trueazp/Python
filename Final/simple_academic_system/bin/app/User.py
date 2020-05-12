from app.Mahasiswa import Mahasiswa
from app.DosenPa import DosenPa
from app.MataKuliah import MataKuliah
import random

class User(object):
  # constructor for user mahasiswa
  def __init__(self, id, userName, password, mahasiswa):
    self.__id = id
    self.__userName = userName
    self.__password = password
    self.__mahasiswa = mahasiswa
    self.__dosenPa = DosenPa()
    self.__sksTerdaftar
    self.__matkul = []
    self.__matkuls = ["Matematika Dasar (3 SKS)", "Pengantar Pemrograman (3 SKS)", "WSBM (2 SKS)", "Fisika Dasar (2 SKS)", "Kimia Dasar (2 SKS)", "Biologi Dasar (2 SKS)", "Pancasila (2 SKS)"]
    self.__listMatkul = set([])
    self.__ipk = random.uniform(2.75, 4.00)

    for i in range(0, len(self.__matkuls)):
      self.__listMatkul.add(self.__matkuls[random.randrange(0, len(self.__matkuls), 1)])

  # constructor for user dosen
  def __init__(self, id, userName, password, dosenPa):
    self.__id = id
    self.__userName = userName
    self.__password = password
    self.__dosenPa = dosenPa
    
  # getter
  def getId(self):
    return self.__id

  def getUserName(self):
    return self.__userName

  def getPassword(self):
    return self.__password

  def getMahasiswa(self):
    return self.__mahasiswa

  def getDosenPa(self):
    return self.__dosenPa

  def getSksTerdaftar(self):
    return self.__sksTerdaftar

  # checking password
  def checkPass(self, password):
    return password == self.__password

  # add mata kuliah
  def addMataKuliah(self, matkul):
    try:
      if not matkul in self.__matkul:
        if matkul.getKuota() > 0:
          self.__sksTerdaftar += matkul.getSks()
          if self.__sksTerdaftar < 11:
            self.__matkul.append(matkul)
            matkul.setMahasiswaTerdaftar(self)
            print("Mata kuliah", matkul.getNamaMatkul(), "berhasil ditambahkan")
            print("Kuota tersisa untuk mata kuliah", matkul.getNamaMatkul(), "sebanyak", matkul.getKuota())
            print("-------------------------")
          else:
            print("Melewati batas total SKS yang diberikan...")
            print("-------------------------")
            self.__sksTerdaftar -= matkul.getSks()
        else:
          print("Kupta tidak mencukupi...")
          print("-------------------------")
      else:
        print("Telah terdaftar dalam mata kuliah ini...")
    except:
      print("Error...")

  # remove mata kuliah
  def removeMataKuliah(self, matkul):
    try:
      if self.__sksTerdaftar == 0:
        print("Tidak ada mata kuliah yang diprogramkan...")
        print("-------------------------")
      else:
        if matkul in self.__matkul:
          self.__matkul.remove(matkul)
          matkul.mahasiswaBatalMendaftar(self)
          self.__sksTerdaftar -= matkul.getSks()
          print("Mata kuliah", matkul.getNamaMatkul(), "telah dihapus dari program...")
          print("Kuota tersisa untuk mata kuliah", matkul.getNamaMatkul(), "sebanyak", matkul.getKuota())
          print("-------------------------")
        else:
          print("Tidak dapat menghapus mata kuliah ini...")
          print("Anda belum terdaftar dalam mata kuliah ini...")
          print("-------------------------")
    except:
      print("Error")

  # show mata kuliah yang diprogramkan
  def showMatkul(self):
    if self.__sksTerdaftar == 0:
      print("Tidak ada mata kuliah yang diprogramkan...")
    else:
      print("Berikut adalah daftar mata kuliah yang diprogramkan oleh", self.__userName)
      for mataKuliah in self.__matkul:
        print("Nama mata kuliah\t:", mataKuliah.getNamaMatkul())
        print("Kode mata kuliah\t:", mataKuliah.getKodeMatkul())
        print("Dosen pengajar\t\t:", mataKuliah.getDosenPengajar())
        print("Jumlah satuan kredit\t:", mataKuliah.getSks())
        print("-------------------------")
  
  # show IPS
  def showIps(self):
    print("Berikut adalah IPS semester lalu dari user", self.__userName)
    for element in self.__listMatkul:
      print(element)
    print("IPK :", "%.2f" %self.__ipk)
    print("-------------------------")