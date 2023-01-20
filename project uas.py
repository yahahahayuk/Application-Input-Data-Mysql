import mysql.connector
import os

db = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="db_rumahsakit"
)

if db.is_connected():
  print("Berhasil terhubung ke database")

def insert_data(db):
  nama = input("Masukan nama: ")
  tanggal_lahir = input("Masukan tanggal lahir: ")
  alamat = input("Masukan alamat: ")
  diagnosa = input("Masukan diagnosa: ")
  val = (nama, tanggal_lahir, alamat, diagnosa)
  cursor = db.cursor()
  sql = "INSERT INTO tbl_pasien (nama, tanggal_lahir, alamat, diagnosa) VALUES (%s, %s, %s, %s)"
  cursor.execute(sql, val)
  db.commit()
  print("DATA PASIEN BERHASIL DISIMPAN".format(cursor.rowcount))

def show_data(db):
  cursor = db.cursor()
  sql = "SELECT * FROM tbl_pasien"
  cursor.execute(sql)
  results = cursor.fetchall()
  
  if cursor.rowcount < 0:
    print("TIDAK TERDAPAT DATA PASIEN")
  else:
    for data in results:
      print(data)

def update_data(db):
  cursor = db.cursor()
  show_data(db)
  id_pasien = input("pilih id pasien: ")
  nama = input("Perbarui Nama: ")
  tanggal_lahir = input("Perbarui tanggal lahir: ")
  alamat = input("Perbarui alamat: ")
  diagnosa = input("Perbarui Diagnosa: ")

  sql = "UPDATE tbl_pasien SET nama=%s, tanggal_lahir=%s, alamat=%s, diagnosa=%s WHERE id_pasien=%s"
  val = (nama, tanggal_lahir, alamat, diagnosa, id_pasien)
  cursor.execute(sql, val)
  db.commit()
  print("DATA PASIEN BERHASIL DIUBAH".format(cursor.rowcount))

def delete_data(db):
  cursor = db.cursor()
  show_data(db)
  id_pasien = input("pilih id pasien: ")
  sql = "DELETE FROM tbl_pasien WHERE id_pasien=%s"
  val = (id_pasien,)
  cursor.execute(sql, val)
  db.commit()
  print("DATA PASIEN BERHASIL DIHAPUS".format(cursor.rowcount))

def search_data(db):
  cursor = db.cursor()
  keyword = input("cari berdasarkan nama atau alamat: ")
  sql = "SELECT * FROM tbl_pasien WHERE nama LIKE %s OR alamat LIKE %s"
  val = ("%{}%".format(keyword), "%{}%".format(keyword))
  cursor.execute(sql, val)
  results = cursor.fetchall()

  if cursor.rowcount < 0:
    print("TIDAK DITEMUKAN DATA PASIEN")
  else:
    for data in results:
      print(data)


def show_menu(db):
  print("=== DATA PASIEN RS AMIKOM ===")
  print("1. Insert Data Pasien")
  print("2. Tampilkan Data Pasien")
  print("3. Update Data Pasien")
  print("4. Hapus Data Pasien")
  print("5. Cari Data Pasien")
  print("0. Keluar")
  print("------------------")
  menu = input("Pilih menu> ")

  os.system("clear")

  if menu == "1":
    insert_data(db)
  elif menu == "2":
    show_data(db)
  elif menu == "3":
    update_data(db)
  elif menu == "4":
    delete_data(db)
  elif menu == "5":
    search_data(db)
  elif menu == "0":
    exit()
  else:
    print("Menu salah!")


if __name__ == "__main__":
  while(True):
    show_menu(db)