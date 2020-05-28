# file for runner

from app.System import Login
from app.MataKuliah import Course

class Main:
  if __name__ == '__main__':
    login = Login.getInstance()

    # mata kuliah
    matDas = Course("619", "Matematika Dasar", "Dosen Matematika", 3, 10)
    bindo = Course("101", "Bahasa Indonesia", "Dosen Bahasa Indoensia", 2, 5)
    english = Course("202", "Bahasa Inggris", "Dosen Bahasa Inggris", 2, 3)
    pendAgama = Course("666", "Pendidikan Agama", "Dosen Agama", 3, 1)
    wipteks = Course("123", "Wawasan IPTEKS", "Dosen IPTEKS", 2, 3)
    pkn = Course("555", "Kewarganegaraan", "Dosen Kewarganegaraan", 3, 1)

    # main loop
    while True:
      print("--MENU--")
      print("1. Login")
      print("2. Exit")
      mainMenu_input = int(input("Masukkan pilihan ::> "))

      # login
      if mainMenu_input == 1:
        print("--USER MENU--")
        print("1. Login Mahasiswa")
        print("2. Login Dosen")
        userMenu_input = int(input("Masukkan pilihan ::> "))

        # login mahasiswa
        if userMenu_input == 1:
          print("--Input your username & password below--")
          userName = str(input("Username ::> "))
          password = str(input("Password ::> "))

          # user mahasiswa loop
          while login.authMahasiswa(userName, password):
            print("--WELCOME MAHASISWA--")
            print("1. Lihat Profil")
            print("2. Tambah Mata Kuliah")
            print("3. Hapus Mata Kuliah")
            print("4. Informasi IPS")
            print("5. Logout")
            mahasiswaMenu_input = int(input("Masukkan pilihan ::> "))

            # menampilkan profil mahasiswa
            if mahasiswaMenu_input == 1:
              login.statusMahasiswa()
            # tambah mata kuliah
            elif mahasiswaMenu_input == 2:
              print("--DAFTAR MATA KULIAH--")
              print("1. Matematika Dasar")
              print("2. Bahasa Indonesia")
              print("3. Bahasa Inggris")
              print("4. Pendidikan Agama")
              print("5. Wawasan IPTEKS")
              print("6. Kewarganegaraan")
              matkul_input = int(input("Masukkan pilihan ::> "))

              if matkul_input == 1:
                login.getUserMahasiswa().addMatkul(matDas)
              elif matkul_input == 2:
                login.getUserMahasiswa().addMatkul(bindo)
              elif matkul_input == 3:
                login.getUserMahasiswa().addMatkul(english)
              elif matkul_input == 4:
                login.getUserMahasiswa().addMatkul(pendAgama)
              elif matkul_input == 5:
                login.getUserMahasiswa().addMatkul(wipteks)
              elif matkul_input == 6:
                login.getUserMahasiswa().addMatkul(pkn)
              else:
                print("Opsi tidak ada...")

            # hapus mata kuliah
            elif mahasiswaMenu_input == 3:
              login.getUserMahasiswa().showMatkul()
              print("Silahkan memilih mata kuliah yang akan dihapus")
              kode_matkul = str(input("Masukkan kode mata kuliah ::> "))

              if kode_matkul == matDas.getKodeMatkul():
                login.getUserMahasiswa().removeMatkul(matDas)
              elif kode_matkul == bindo.getKodeMatkul():
                login.getUserMahasiswa().removeMatkul(bindo)
              elif kode_matkul == english.getKodeMatkul():
                login.getUserMahasiswa().removeMatkul(english)
              elif kode_matkul == pendAgama.getKodeMatkul():
                login.getUserMahasiswa().removeMatkul(pendAgama)
              elif kode_matkul == wipteks.getKodeMatkul():
                login.getUserMahasiswa().removeMatkul(wipteks)
              elif kode_matkul == pkn.getKodeMatkul():
                login.getUserMahasiswa().removeMatkul(pkn)
              else:
                print("Mata kuliah tidak tersedia")

            # menampilkan infromasi IPS
            elif mahasiswaMenu_input == 4:
              login.getUserMahasiswa().showIps()
            # logout
            else:
              login.logout()
              break

        # login dosen
        else:
          print("--Input your username & password below--")
          userName = str(input("Username ::> "))
          password = str(input("Password ::> "))

          # user dosen loop
          while login.authDosen(userName, password):
            print("--WELCOME DOSEN--")
            print("1. Lihat Profil")
            print("2. Lihat Mahasiswa Bimbingan")
            print("3. Logout")
            dosenMenu_input = int(input("Masukkan pilihan ::> "))

            # meanmpilkan profil dosen
            if dosenMenu_input == 1:
              login.statusDosen()

            # menampilkan mahasiswa  bimbingan dosen
            elif dosenMenu_input == 2:
              login.getDosenPa().showMahasiswaBimbingan()

            # logout
            else:
              login.logout()
              break

      # exit
      else:
        break