# file for student's object

class Student:
  # constructor
  def __init__(self, id, nama, email, dosenPa):
    self.id = id
    self.nama = nama
    self.email = email
    self.dosenPa = dosenPa

  # getter
  def getId(self):
    return self.id

  def getNama(self):
    return self.nama

  def getEmail(self):
    return self.email

  def getNamaDosenPa(self):
    return self.dosenPa