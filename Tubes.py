# Urutan Kerja
# start() -> pemilihan() -> pengisian() -> paymain() -> payY() or payN() -> start()
# mulai -> memilih tempat, judul film, tiket, waktu -> memilih tempat duduk -> melakukan pembayaran -> mulai

# Variabel global
kursi = [[0 for i in range (8)] for j in range (8)] # matriks untuk tempat duduk yang telah diisi
kursitemp = [[0 for i in range (8)] for j in range (8)] # matriks sementara  sebelum di transfer nilainya ke matriks kursi setelah pembayaran terkonfirmasi

balance = 200000 # jumlah uang yang dimiliki
screenwidth = 50 # perkiraan lebar layar
hargatiket = 0 # harga individual tiket menurut jenis tiket

# Variabel lokal
# k, i, j : int (variabel iterasi)
#
#[variabel fungsi draw]
#   matriks : array of array -> matriks yang akan digambarkan
#
#[variabel fungsi kirikanan]
#   kiri, kanan, tengah : str
#   nkiri, nkanan, width : int
#
#[variabel fungsi rupiah]
#   nilai : int
#
#[variabel fungsi pemilihan]
#   a -> bioskop yang dipilih
#   b -> film yang dipilih
#   c -> kelas yang dipilih
#   d -> waktu yang dipilih
#   e -> looping untuk memilih ulang apabila terjadi salah input
#
#[variabel prosedur pengisian]
#   mengisi : bool -> flag untuk menghentikan loop while
#   posisi : int -> status apakah suatu tempat duduk sudah terisi atau belum; 1 = sudah terisi, 0 = belum terisi
#
#[variabel prosedur paymain (pembayaran)]
#   hargatotal : int -> harga tiket individu dikali banyak tiket yang dipesan
#   pajak hiburan : int -> pajak dengan nilai 10% hargatotal
#   _bioskop, _judul, _jenis, _waktu : str
#   n : int -> banyak tempat duduk yang dipesan
#   k : int -> pilihan jawaban
#
#[variabel prosedur start]
#   inputting : bool -> flag untuk menghentikan loop while
#   n : int -> banyak tempat duduk yang dipesan

# utility
from os import system, name # dibutuhkan untuk membersihkan layar, fungsi clear()

def draw(matriks):
  # prosedur untuk menggambarkan matriks
  for k in range(len(matriks)):
    if k == 0:
      print(end='  ')
    elif k == 4:
      print(end='\t')
    print(f' {k+1} ', end=' ') # menuliskan label nomor untuk kolom
  print()
  for i in range(len(matriks)):
    if i == 4: # memberi jarak tiap 4 baris
      print()
    for j in range(len(matriks[i])):
      if j == 0:
        print(i+1, end=' ') # menuliskan label nomor untuk baris
      elif j == 4:
        print(end='\t') # memberi jarak tiap 4 kolom
      print(f'[{matriks[i][j]}]', end=' ') # gambarkan matriks
    print()
  print()
  print('[0] = belum terisi')
  print('[1] = sudah terisi')
  print()

def pilihan_a():
  return (print("Selamat Datang"),
    print("Silahkan pilih tempat Bioskop yang anda inginkan"), 
    print("1. Cinema XXI"), 
    print("2. CGV Cinema"), 
    print("3. Cinépolis"),
    print())
  
def pilihan_b():
  return (print(),
    print("Silahkan Pilih Judul Film yang anda inginkan:"),
    print("1. Spider-Man: No Way Home"),
    print("2. Shang-Chi and the Legend of the Ten Rings"),
    print("3. Venom: Let There Be Carnage"),
    print("4. Free Guy"),
    print())

def pilihan_c():
  return (print(),
    print("Silahkan Pilih Jenis Tiket yang anda inginkan:"),
    print("1. Reguler (35k)"),
    print("2. Deluxe  (50k)"),
    print())

def pilihan_d():
  return (print(),
    print("Silahkan Pilih Waktu tonton yang yang anda inginkan:"),
    print("1. 08.00-10.00"),
    print("2. 12.00-14.00"),
    print("3. 17.00-19.00"),
    print("4. 20.00-22.00"),
    print())

def pause():
  return input("Tekan enter untuk melanjutkan ...")

def clear():
  # prosedur untuk membersihkan layar
  if name == 'nt': # sistem adalah windows
    system('cls') # bersihkan layar
  else: # sistem selain windows
    system('cls') # bersihkan layar
  

  # header tiap tampilan
  print(kirikanan('', 'Saldo saat ini : '+ rupiah(balance), screenwidth))
  print()
  

def kirikanan(kiri, kanan, width):
  # fungsi untuk membuat 2 bagian terpisah sedemikan rupa sehingga tepat memenuhi perkiraan lebar layar
  nkiri = len(str(kiri))
  nkanan = len(str(kanan))
  
  ntengah = width - nkiri - nkanan
  tengah = ''

  for i in range(ntengah):
    tengah+=' '

  kiri = str(kiri)
  kanan = str(kanan)

  return kiri+tengah+kanan

def rupiah(nilai):
  # fungsi untuk memberikan mata uang
  return 'Rp ' + str(nilai)

def pemilihan():
  # fungsi untuk melakukan pemilihan bioskop, judul film, jenis tiket, dan waktu tayang yang diinginkan
  global hargatiket

  clear()
  e=4
  while (e==4):
      pilihan_a()
      a=str(input("Bioskop pilihan anda (masukkan angka pilihan) : "))
      print()
      if (a=="1"):
          a=str("Cinema XXI,")
          e=3
      elif (a=="2"):
          a=str("CGV Cinema,")
          e=3
      elif (a=="3"):
          a=str("Cinépolis,")
          e=3
      else:
         input("Pilihan anda tidak tersedia")
         clear()
      
  while (e==3):
      print('Pilihan bioskop anda adalah     : ' + str(a))
      
      pilihan_b()
      b=str(input("Judul Film pilihan anda (masukkan angka pilihan) : "))
      
      print()
      if (b=="1"):
        b=str("Spider-Man: No Way Home,") 
        e=2
      elif (b=="2"):
        b=str("Shang-Chi and the Legend of the Ten Rings,") 
        e=2
      elif (b=="3"):
        b=str("Venom: Let There Be Carnage,") 
        e=2
      elif (b=="4"):
        b=str("Free Guy,") 
        e=2
      else:
        input("Pilihan anda tidak tersedia")
        clear()

  while (e==2):
      print('Pilihan bioskop anda adalah     : ' + str(a))
      print('Judul Film pilihan anda adalah  : ' + str(b))

      pilihan_c()
      c=str(input("Jenis Tiket pilihan anda (masukkan angka pilihan) : "))
      
      print()
      if (c=="1"):
          c=str("Reguler,")
          hargatiket = 35000 #penyesuaian harga per tiket
          e=1
      elif (c=="2"):
          c=str("Deluxe,")
          hargatiket = 50000 #penyesuaian harga per tiket
          e=1
      else:
        input("Pilihan anda tidak tersedia")
        clear()

  while (e==1):
      print('Pilihan bioskop anda adalah     : ' + str(a))
      print('Judul Film pilihan anda adalah  : ' + str(b))
      print('Jenis Tiket pilihan anda adalah : ' + str(c))

      pilihan_d()
      d=str(input("Waktu pilihan anda (masukkan angka pilihan) : "))

      print()
      if (d=="1"):
          d=str("8.00-10.00")
          e=0
      elif (d=="2"):
          d=str("12.00-14.00")
          e=0
      elif (d=="3"):
          d=str("17.00-19.00")
          e=0
      elif (d=="4"):
          d=str("20.00-22.00")
          e=0
      else:
          input("Pilihan anda tidak tersedia")
          clear()

  return a, b, c, d

def pengisian(k) :
  # prosedur untuk melakukan pemilihan tempat duduk dalam bioskop
  global kursitemp # variabel sementara sebelum disimpan ke matriks permanen

  mengisi = True # flag yang menandakan apakah user dalam proses mengisi
  
  while(mengisi):
    draw(kursitemp)
    try :
      j = int(input(f"Nomor kolom kursi ke-{k} = "))
      i = int(input(f"Nomor baris kursi ke-{k} = "))

      if i < 1 or j < 1: # mencegah pengaksesan matriks dengan index negatif
        raise
        
      posisi = kursitemp[i-1][j-1]
      print()
    except:
      clear() # ulangi
    else:
      mengisi = False

  if posisi == 0 :
      kursitemp[i-1][j-1] = 1
      print(f"---- Kolom baris kursi anda = {i} dan kolom kursi anda = {j} ----")
  else :
      print("Kursi sudah terisi. Silahkan memilih ulang kursi.")
      pengisian(k)
  print()

def paymain(_bioskop, _judul, _jenis, _waktu, n):
  # prosedur untuk menampilkan banyak biaya yang harus dibayarkan dan melakukan konfirmasi pembayaran
  global balance

  clear()

  hargatotal = n*hargatiket # hargatotal tiket
  pajakhiburan = hargatotal//10 # pajak 10 persen dari harga total tiket

  while True:
    print('----------------------------------------')
    print('Bioskop      : '+_bioskop)
    print('Jenis Tiket  : '+_jenis)
    print('Judul Film   : '+_judul)
    print('Waktu Putar  : '+_waktu)
    print('Jumlah Pesan : '+ str(n) +' seats')
    print()
    print('----------------------------------------')
    print(kirikanan('Harga Tiket    : ', rupiah(hargatotal), screenwidth))
    print(kirikanan('PPN (10%)      :', rupiah(pajakhiburan), screenwidth))
    print(kirikanan('Total harga    : ', rupiah(hargatotal+pajakhiburan), screenwidth))
    print('Lanjutkan transaksi ?')
    print(' 1. Iya')
    print(' 2. Tidak')

    k = input('Pilihan : ')
    if k == '1':
      payY(hargatotal+pajakhiburan)
    elif k == '2':
      payN()
    else:
      print()
      print('Pilihan tidak tersedia.')
      print()
      pause()
      clear()

def payY(harga):
  # prosedur yang menangani pembayaran yang terkonfirmasi

  global kursi
  global kursitemp

  print()
  global balance
  if balance >= harga :
    #meregister nilai kursitemp ke kursi
    for i in range(len(kursi)):
      for j in range(len(kursi[i])):
        kursi[i][j] = kursitemp[i][j]

    balance -= harga
    print()
    print('Sisa saldo : '+ rupiah(balance))
  
  else:
    for i in range(len(kursitemp)):
      for j in range(len(kursitemp[i])):
        kursitemp[i][j] = kursi[i][j]
        
    print('Saldo tidak mencukupi.')

  pause()
  start()

def payN():
  # prosedur yang menangani pembayaran yang dibatalkan

  global kursitemp
  for i in range(len(kursitemp)):
      for j in range(len(kursitemp[i])):
        kursitemp[i][j] = kursi[i][j]
  start()

# mulai
def start():
  # prosedur yang menjalankan program
  a, b, c, d = pemilihan()
  
  inputting = True
  while inputting:
    print('Pilihan bioskop anda adalah     : ' + str(a))
    print('Judul Film pilihan anda adalah  : ' + str(b))
    print('Jenis Tiket pilihan anda adalah : ' + str(c))
    print('Waktu tonton pilihan anda adalah: ' + str(d))
    print()
    print(kirikanan('Harga tiket :', rupiah(hargatiket), screenwidth ))
    print(kirikanan('', '(belum termasuk pajak)', screenwidth))
    print()
    try:
      print('Kapasitas maksimum bioskop : 64 seats')
      n = int(input("Silahkan masukkan jumlah pemesanan = "))

      if n < 1 or n > 64: #minimal 1 dan maksimal 64
        raise

    except:
      clear()
    else:   
      inputting = False
   
  for k in range (1,n+1) : # melakukan pengisian sebanyak n kali
    print(f"PEMESANAN KE-{k}")
    pengisian(k) 
  draw(kursitemp)
  pause() 
  
  paymain(a, b, c, d, n)

start() #memulai pemanggilan pertama