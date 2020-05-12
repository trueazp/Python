class DataSource(object):
  # static variable
  __dataSource = None
  # constructor
  def __init__(self):
    self.__userMapMahasiswa = {}
    self.__userMapDosen = {}
    self.__mahasiswaMap = {}
    self.__dosenPaMap = {}
    self.__bimbinganDosen = {}

    try:
      putDosen()
    except:
      print("Error...")
  
  # instansiasi
  def getInstance(self):
    if self.__dataSource == None:
      self.__dataSource = DataSource()
    return self.__dataSource
  
  # getter
  def getUser(self, key):
    return self.__userMapMahasiswa.get(key)
  
  def getMahasiswa(self, key):
    return self.__mahasiswaMap.get(key)

  def getUserDosen(self, key):
    return self.__userMapDosen.get(key)

  def getDosenPa(self, key):
    return self.__dosenPaMap.get(key)

  def getBimbinganDosen(self):
    return self.__bimbinganDosen

  # checking String apakah merupakan integer
  def isInt(str):
    isInt = False
    try:
      int(str)
      isInt = True
    except:
      print("Cannot parse...")
    return isInt

  # baca tulis file untuk data user mahasiswa
  def putUserMahasiswa(self):
    pass

  # baca tulis file untuk data user dosen pembimbing
  def putUserDosen(self):
    pass

  # baca tulis file untuk data mahasiswa
  def putMahasiswa(self):
    pass

  def putDosen(self):
    pass
