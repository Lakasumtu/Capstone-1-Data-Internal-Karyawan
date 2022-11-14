#nama, umur, jabatan, pendidikan terakhir, gender, gaji, lembur

listdatakaryawan = {
    'Marko': [29, 'Manager', 'S2', 'M', 50000000, 5],
    'Polo': [24, 'Histaff', 'S1', 'M', 25000000, 3],
    'Bolak':[37, 'Lostaff', 'S1', 'M', 12000000, 10],
    'Balik':[21, 'Operator','SMA', 'F', 10000000, 15] 
    }

##tampil seluruh data karyawan

def tampildata():
    print('--------------------------Data Karyawan--------------------------')
    print('Nama  \t\t\t [Umur\t Jabatan\t|Pendidikan|   |Gender|   |Gaji|     |Lembur|')   
    for i in listdatakaryawan:
        print(i,'\t\t\t', listdatakaryawan[i][0], '\t',listdatakaryawan[i][1],'\t',listdatakaryawan[i][2],'\t\t ',listdatakaryawan[i][3],'\t',listdatakaryawan[i][4],'\t  ',listdatakaryawan[i][5])


def panggildata():
    x = True
    while x == True:
        inputpanggil = input('Masukkan nama karyawan yang datanya ingin ditampilkan:').capitalize()
        if inputpanggil not in listdatakaryawan:
            print('Tidak ada karyawan dengan nama tersebut')
            input9 = input('apakah anda ingin mencari data karyawan kembali?(Y/N)').capitalize()
            if input9 == 'Y':
                continue
            elif input9 == 'N':
                x = False
            else:
                print('Input yang anda masukkan tidak sesuai')
        else:
            print('--------------------------Data Karyawan--------------------------')
            print('Nama  \t\t\t [Umur\t Jabatan\t|Pendidikan|   |Gender|   |Gaji|\t|Lembur|')
            print(inputpanggil,'\t\t\t', listdatakaryawan[inputpanggil][0], '\t',listdatakaryawan[inputpanggil][1],'\t',listdatakaryawan[inputpanggil][2],'\t\t ',listdatakaryawan[inputpanggil][3],'\t',listdatakaryawan[inputpanggil][4],'\t  ',listdatakaryawan[inputpanggil][5])
            x = False

# tambah data karyawan baru
def tambahdata():
    x = True
    y = True
    while y == True:
        userinput = input('Masukkan nama karyawan baru:').capitalize()
        userinput0 = input('Masukkan umur:')
        userinput1 = input('Masukkan jabatan:').capitalize()
        userinput2 = input('Masukkan pendidikan terakhir:').upper()
        userinput3 = input('Masukkan jenis kelamin(M/F):').capitalize()
        userinput4 = input('Masukkan gaji:')
        userinput5 = input('Masukkan lembur pada bulan ini, input 0 jika belum ada:')
        print(userinput, 'dengan informasi sebagai berikut', userinput0 ,' tahun ',userinput1,userinput2,userinput3,userinput4,userinput5)
        input89 = input('apakah anda yakin ingin mengupdate data sesuai dengan info diatas?(Y/N)').capitalize()
        while x == True:
            if input89 == 'Y':
                listdatakaryawan.update({userinput:[userinput0, userinput1,userinput2,userinput3,userinput4,userinput5]})
                tampildata()
                print('Data telah di tambahkan')
                x = False
            elif input89 == 'N':
                x = False
            else:
                print('Input yang anda masukkan tidak sesuai')
                x = False
        inputlagi = input('Ingin menambah data karyawan lagi?(Y/N)').capitalize()
        if inputlagi == 'Y':
            x = True
            continue
        elif inputlagi == 'N':
            y = False
        else:
            print('input tidak sesuai')
            y = False

##update data karyawan
def updatedata():
    x = True
    while x == True:
        userinputu = input('Masukkan nama karyawan yang akan di update:').capitalize()
        if userinputu not in listdatakaryawan:
            print ('Tidak ada data karyawan dengan nama tersebut, silahkan input di menu karyawan baru')
            input1 = input('Apakah ingin tetap update data karyawan? (Y/N)').capitalize()
            if input1 == 'Y':
                continue
            else:
                tampildata()
                x = False
        else:
            break
    while x == True:
            userinputu1 = input('Masukkan informasi yang ingin di update(Jabatan, Pendidikan, Gaji, Lembur):').lower()
            userinputu2 = input('Masukkan informasi terbaru:').capitalize()
            if userinputu1 ==  'jabatan':
                listdatakaryawan[userinputu][1] = userinputu2
                print('data terupdate')
                tampildata()
                break
            elif userinputu1 ==  'pendidikan':
                listdatakaryawan[userinputu][2] = userinputu2
                print('data terupdate')
                tampildata()
                break
            elif userinputu1 ==  'gaji':
                listdatakaryawan[userinputu][4] = userinputu2
                print('data terupdate')
                tampildata()
                break
            elif userinputu1 ==  'lembur':
                listdatakaryawan[userinputu][5] = userinputu2
                print('data terupdate')
                tampildata()
                break
            else:
                print ('input tidak sesuai, silahkan masukkan kembali')
                continue

##hapus data karyawan
def hapusdata():
    x = True
    while x == True:
        userinputd = input('Masukkan nama karyawan yang akan di delete:').capitalize()
        if userinputd not in listdatakaryawan:
            print ('Tidak ada data karyawan dengan nama tersebut.')
            input1 = input('Apakah ingin tetap hapus data karyawan? (Y/N)').capitalize()
            if input1 == 'Y':
                continue
            else:
                tampildata()
                x = False
        else:
            print (userinputd,listdatakaryawan[userinputd])
            input7 = input('Apakah anda yakin menghapus data?(Y/N)').capitalize()
            if input7 == 'Y':
                del listdatakaryawan[userinputd]
                print('data telah dihapus')
                tampildata()
            else:
                break
            x = False

#tampilanmenu

def tampilmenu():
    x = True
    while x == True:
        print ('Menu data karyawan: \n 1. Tampil data karyawan \n 2. Tambah data karyawan \n 3. Update data karyawan \n 4. Hapus data karyawan \n 5. Keluar program')
        menu = str(input('Masukkan pilihan menu:'))
        if menu == '1':
            tampildata()
            panggildata()
        elif menu == '2':
            tambahdata()
        elif menu == '3':
            updatedata()
        elif menu == '4':
            hapusdata()
        elif menu == '5':
            x = False
        else:
            print ('Input anda belum sesuai')
            continue

tampilmenu()


