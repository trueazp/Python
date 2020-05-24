# file for database activity
# read and write from database
# performed here
from app.Dosen import Advisor
from app.Mahasiswa import Student
from app.User import UserMahasiswa, UserDosen
import random

class DataBase:
  # static variable
  dataSource = None

  # constructor
  def __init__(self):
    self.userMapMahasiswa = {}
    self.userMapDosen = {}
    self.mahasiswaMap = {}
    self.dosenPaMap = {}
    self.bimbinganDosen = []

    # self.exDict = {}
    # self.testing()

    self.putDosen()
    self.putMahasiswa()
    self.putUserDosen()
    self.putUserMahasiswa()
    self.addBimbinganDosen()

    # try:
    #
    # except:
    #   print("Error in writing database")

  # instansiasi
  @classmethod
  def getInstance(cls):
    if cls.dataSource == None:
      cls.dataSource = DataBase()
    return cls.dataSource

  # # getter for testing
  # def getUserMahasiswa(self, key):
  #   return self.exDict.get(key)
  #
  # # testing
  # def testing(self):
  #   data = []
  #   with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\Mahasiswa.txt") as rf:
  #     contents = rf.readlines()
  #
  #     for line in contents:
  #       if not line in data:
  #         data.append(line.split(";"))
  #
  #   for datum in data:
  #     self.exDict.update({
  #       datum[1] : Student(datum[0], datum[1], datum[2], "DosenPa")
  #     })

  # getter
  def getUserMahasiswa(self, key):
    return self.userMapMahasiswa.get(key)

  def getMahasiswa(self, key):
    return self.mahasiswaMap.get(key)

  def getUserDosen(self, key):
    return self.userMapDosen.get(key)

  def getDosenPa(self, key):
    return self.dosenPaMap.get(key)

  def getBimbinganDosen(self):
    return self.bimbinganDosen

  # baca tulis file untuk data user mahasiswa
  def putUserMahasiswa(self):
    data = []
    with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\User.txt") as readFile:
      contents = readFile.readlines()

      for line in contents:
        data.append(line.split(";"))

      for datum in data:
        self.userMapMahasiswa.update({
          datum[1]: UserMahasiswa(datum[0], datum[1], datum[2], self.mahasiswaMap.get(datum[0]))
        })

  # baca tulis file untuk data user dosen pa
  def putUserDosen(self):
    data = []
    with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\DosenPaUser.txt") as readFile:
      contents = readFile.readlines()

      for line in contents:
        if not line in data:
          data.append(line.split(";"))

      for datum in data:
        self.userMapDosen.update({
          datum[1]: UserDosen(datum[0], datum[1], datum[2], self.dosenPaMap.get(datum[0]))
        })

  # baca tulis file untuk data mahasiswa
  def putMahasiswa(self):
    data = []
    data2 = []
    names = []
    with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\Mahasiswa.txt") as readFile:
      contents = readFile.readlines()

      for line in contents:
        if not line in data:
          data.append(line.split(";"))

    with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\DosenPa.txt") as readFile:
      contents = readFile.readlines()

      for line in contents:
        if not line in data:
          data2.append(line.split(";"))

    for datum in data2:
      names.append(datum[1])

    for datum in data:
      self.mahasiswaMap.update({
        datum[0]: Student(datum[0], datum[1], datum[2], random.choice(names))
      })

  # baca tulis file untuk data dosen pembimbing
  def putDosen(self):
    data = []
    with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\DosenPa.txt") as readFile:
      contents = readFile.readlines()

      for line in contents:
        data.append(line.split(";"))

      for datum in data:
        self.dosenPaMap.update({
          datum[0]: Advisor(datum[0], datum[1], datum[2], datum[3])
        })

  # baca tulis file untuk data bimbingan dosen
  def addBimbinganDosen(self):
    data = []
    with open("D:\\Programming\\Python\\Simple_Academic_System_2.0\\database\\BimbinganDosen.txt") as readFile:
      contents = readFile.readlines()

      for line in contents:
        data.append(line.split(";"))

      for datum in data:
        self.bimbinganDosen.append(datum)