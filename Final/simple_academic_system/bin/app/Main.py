from app.Login import Login
from app.MataKuliah import MataKuliah

class Main:

  if __name__ == "__main__":
    login = Login()

    # Mata Kuliah
    MatDas = MataKuliah("619", "Matematika Dasar", "Dosen Matematika", 3, 10)
    Bindo = MataKuliah("101", "Bahasa Indonesia", "Dosen Bahasa Indoensia", 2, 5)
    English = MataKuliah("202", "Bahasa Inggris", "Dosen Bahasa Inggris", 2, 3)
    PendAgama = MataKuliah("666", "Pendidikan Agama", "Dosen Agama", 3, 1)
    Wipteks = MataKuliah("123", "Wawasan IPTEKS", "Dosen IPTEKS", 2, 3)
    Pkn = MataKuliah("555", "Kewarganegaraan", "Dosen Kewarganegaraan", 3, 1)