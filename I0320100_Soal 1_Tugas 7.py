# Soal 1 Tugas 7

x = True
while x == True:
    password = input('Masukkan password anda : ' )
    # Password harus mengandung huruf / angka / huruf dan angka serta minimal 8 karakter
    if password.isalnum() == True and len(password) >= 8:
        print('Password anda : ', password)
        x = False
    else:
        print('Masukkan ulang password anda')