from prettytable import PrettyTable

print("""
===============Luscious Cakes================
+-------------------------------------------+
|     SELAMAT DATANG DI LUSCIOUS CAKES      |
+-------------------------------------------+
""")
# Daftar Menu Awal LUSCIOUS CAKES
daftar_menu = [
    {"No": 1, "Nama Kue": "Vanilabery Cake", "Harga": 490000, "Stok": 10},
    {"No": 2, "Nama Kue": "Cheesecake Flurry", "Harga": 380000, "Stok": 8},
    {"No": 3, "Nama Kue": "Chocolate Tiramisu", "Harga": 250000, "Stok": 12},
    {"No": 4, "Nama Kue": "Chocolate De Ville", "Harga": 395000, "Stok": 6},
    {"No": 5, "Nama Kue": "Red Velvet", "Harga": 320000, "Stok": 8},
    {"No": 6, "Nama Kue": "Pink Lemonade", "Harga": 295000, "Stok": 11},
    {"No": 7, "Nama Kue": "Black Forest", "Harga": 300000, "Stok": 7},
    {"No": 8, "Nama Kue": "Mix Fruit Cheesecake", "Harga": 375000, "Stok": 9},
    {"No": 9, "Nama Kue": "Madeline Rose", "Harga": 280000, "Stok": 13},
    {"No": 10, "Nama Kue": "Blueberry Bloom", "Harga": 360000, "Stok": 10}
]

# Inisialisasi PrettyTable untuk menampilkan daftar menu
def init_table():
    y = PrettyTable()
    y.field_names = ["No", "Nama Kue", "Harga", "Stok"]
    for kue in daftar_menu:
        y.add_row([kue["No"], kue["Nama Kue"], kue["Harga"], kue["Stok"]])
    return y

# Fungsi untuk menampilkan daftar menu
def tampilkan_daftarmenu():
    table = init_table()
    print(table)

# Fungsi untuk menambahkan kue baru
def create_menu():
    nama = input("Masukkan nama kue: ")
    harga = int(input("Masukkan harga kue: "))
    stok = int(input("Masukkan stok kue: "))
    new_no = len(daftar_menu) + 1
    daftar_menu.append({"No": new_no, "Nama Kue": nama, "Harga": harga, "Stok": stok})
    print("Kue baru berhasil ditambahkan!")
    tampilkan_daftarmenu()

# Fungsi untuk memperbarui data kue
def update_menu():
    no_kue = int(input("Masukkan Nomor kue yang akan diupdate: "))
    for kue in daftar_menu:
        if kue["No"] == no_kue:
            nama = input("Masukkan nama kue baru: ")
            harga = int(input("Masukkan harga kue baru: "))
            stok = int(input("Masukkan stok kue baru: "))
            kue["Nama Kue"] = nama
            kue["Harga"] = harga
            kue["Stok"] = stok
            print("Data kue berhasil diupdate!")
            tampilkan_daftarmenu()
            return
    print("Nomor yang anda masukkan tidak valid.")

# Fungsi untuk menghapus kue
def delete_menu():
    no_kue = int(input("Masukkan Nomor kue yang akan dihapus: "))
    for kue in daftar_menu:
        if kue["No"] == no_kue:
            daftar_menu.remove(kue)
            print("Kue berhasil dihapus!")
            tampilkan_daftarmenu()
            return
    print("Nomor yang anda masukkan tidak valid.")

# Fungsi untuk transaksi pembelian
def transaksi_pembelian():
    tampilkan_daftarmenu()
    no_kue = int(input("Masukkan Nomor kue yang akan dibeli: "))
    jumlah = int(input("Masukkan jumlah kue yang akan dibeli: "))
    
    for kue in daftar_menu:
        if kue["No"] == no_kue:
            if kue["Stok"] >= jumlah:
                total_harga = jumlah * kue["Harga"]
                print(f"Total harga: Rp. {total_harga}")
                kue["Stok"] -= jumlah
                print("Pembelian berhasil!")
            else:
                print("Maaf! Stok kue tidak mencukupi.")
            return
    print("Nomor yang anda masukkan tidak valid")

# Fungsi untuk login admin
def admin_login():
    username = input("Masukkan username admin: ")
    password = input("Masukkan password admin: ")
    if username == "athira" and password == "asahiganteng":
        print("Selamat! Anda berhasil login!")
        return True
    else:
        print("Login admin gagal. Username atau password salah.")
        start()

# Fungsi untuk pilihan customer
def customer():
        print("""
+------------------------------------+
|           Menu Customer            |
+------------------------------------+    
|    1. Tampilkan Daftar Menu        |
|    2. Transaksi Pembelian          |
|    3. Keluar                       |
+------------------------------------+
""")
        
        pilihan = input("Masukkan Nomor Pilihan (1/2/3): ")
        
        if pilihan == "1":
            tampilkan_daftarmenu()
            customer()
        elif pilihan == "2":
            transaksi_pembelian()
            customer()
        elif pilihan == "3":
            print ("""
+---------------------------------------+
|                                       |
|     TERIMA KASIH TELAH BERKUNJUNG     |
|             KE TOKO KAMI!             |
|                                       |
+------------Luscious Cakes-------------+
""")
        else:
            print("Pilihan Anda Tidak valid.")
            customer()

# Fungsi untuk pilihan admin
def admin():
    # Main program
        print("""
+-----------------------------------+
|            Menu Admin             |
+-----------------------------------+    
|    1. Tampilkan Daftar Menu       |
|    2. Create Menu                 |
|    3. Update Menu                 |
|    4. Delete Menu                 |
|    5. Keluar                      |
+-----------------------------------+
""")
        
        pilihan = input("Masukkan Nomor Pilihan (1/2/3/4/5): ")
                
        if pilihan == "1":
            tampilkan_daftarmenu()
            admin()
        elif pilihan == "2":
            create_menu()
            admin()
        elif pilihan == "3":
            update_menu()
            admin()
        elif pilihan == "4":
            delete_menu()
            admin()
        elif pilihan == "5":
            print("Anda telah keluar dari akun, silahkan login kembali jika ingin mengedit menu")
            start()
        else:
            print("Pilihan Anda Tidak Valid")
            admin()

# Main program   
def start():    
    print("""
+---------------------+
|        ROLE         |
+---------------------+    
|   1. Admin          |
|   2. Customer       |
+---------------------+
""")
    peran = input("Masukkan Peran Anda (1/2): ")
        
    if peran == "1":
        if admin_login():  # Memanggil fungsi login admin
            admin()
    elif peran == "2":
        customer()
start()