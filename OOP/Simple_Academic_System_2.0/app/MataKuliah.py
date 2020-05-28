# file for course's object

class Course:
  # constructor
  def __init__(self, kodeMatkul, namaMatkul, dosenPengajar, sks, kuota):
    self.kodeMatkul = kodeMatkul
    self.namaMatkul = namaMatkul
    self.dosenPengajar = dosenPengajar
    self.sks = sks
    self.kuota = kuota
    self.mahasiswaTerdaftar = []

  # getter
  def getKodeMatkul(self):
    return self.kodeMatkul

  def getNamaMatkul(self):
    return self.namaMatkul

  def getDosenPengajar(self):
    return self.dosenPengajar

  def getSks(self):
    return self.sks

  def getKuota(self):
    return self.kuota

  # menambahkan mahasiswa ke dalam list mahasiswaTerdaftar
  def setMahasiswaTerdaftar(self, UserMahasiswa):
    self.mahasiswaTerdaftar.append(UserMahasiswa)
    self.kuota -= 1

  # menghapus mahasiswa yang terdapat dalam list mahasiswaTerdaftar
  def removeMahasiswaTerdaftar(self, UserMahasiswa):
    self.mahasiswaTerdaftar.remove(UserMahasiswa)
    self.kuota += 1