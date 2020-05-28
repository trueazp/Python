# file for lecturer's and advisor's object

class Lecturer:
  def setMahasiswaBimbingan(self):
    pass
  def showMahasiswaBimbingan(self):
    pass


class Advisor(Lecturer):
  # constructor
  def __init__(self, id, namaDosen, noTelp, email):
    self.id = id
    self.namaDosen = namaDosen
    self.noTelp = noTelp
    self.email = email
    self.mahasiswaBimbingan = []

  # getter
  def getId(self):
    return self.id

  def getNamaDosen(self):
    return self.namaDosen

  def getNoTelp(self):
    return self.noTelp

  def getEmail(self):
    return self.email

  # method Override from interface Dosen
  def setMahasiswaBimbingan(self):
    for bimbingan in self.dataSource.getBimbinganDosen():
      self.mahasiswaBimbingan.append(bimbingan)

  def showMahasiswaBimbingan(self):
    print("Berikut adalah mahasiswa bimbingan dari", self.namaDosen)
    if not self.mahasiswaBimbingan:
      print("Tidak memiliki mahasiswa bimbingan...")
    else:
      for mahasiswa in self.mahasiswaBimbingan:
        print("Nama\t\t:", mahasiswa.getNama())
        print("Email\t\t:", mahasiswa.getEmail())
        print("-------------------------")