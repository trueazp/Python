class Mahasiswa(object):
  # constructor
  def __init__(self, id, nama, email, namaDosenPa):
    self.__id = id
    self.__nama = nama
    self.__email = email
    self.__namaDosenPa = namaDosenPa

  # getter
  def getId(self):
    return self.__id

  def getNama(self):
    return self.__nama

  def getEmail(self):
    return self.__email

  def getNamaDosenPa(self):
    return self.__namaDosenPa