# Password Generator

# Cetak header // String Function 1 : center()
welcome = " Selamat Datang "
header = welcome.center(50, '-')
print('\n', header, '\n')

x = True

while x == True:
    username = input("Username : ")

    # Cek apakah username memiliki panjang lebih dari 7 karakter
    # String Function 2 : len()
    if len(username) > 7:

        # Cek username apakah terdapat spasi atau simbol selain underscore 
        # dan juga memastikan username tidak diawali dengan angka
        # // String Function 3 & 4 : isalnum() & isidentifier()
        if not username.isalnum() and not username.isidentifier() :
            print("\n -- Mohon maaf, username anda tidak dapat diproses -- \n")
            
        else :
            # Mengganti huruf vokal (A) dan (I) didalam String dengan huruf acak
            # // String Function 5 : replace()
            password = username.replace('a', 'fcv').replace('i', 'ldc').replace('_', '271')
            password = password[::-1][0:12]
            x = False
    else :
        if not username.isalnum() and not username.isidentifier() :
            print("\n -- Mohon maaf, username anda tidak dapat diproses -- \n")
        else :
            password = username.replace('a', 'pty').replace('i', 'cqm').replace('_', '649')
            password = password[::-1] * 2
            password = password[0:12]
            x = False

print("Password anda adalah : ", password)

sayonara = " Terima Kasih "
tail = sayonara.center(50, '-')
print('\n', tail, '\n')