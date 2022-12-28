def hi():
    print('Merhaba!')
    print('Nasılsın?')

# hi()

# def hi(name):
#     if name == 'Ayşe':
#         print('Merhaba Ayşe!')
#     elif name == 'Zeynep':
#         print('Merhaba Zeynep!')
#     else:
#         print('Merhaba yabancı!')

# hi("Enes")

# def hi(name):
#     print('Merhaba ' + name + '!')

# names = ['Seda', 'Ahmet', 'Pınar', 'Nejdet', 'Yasemin']
# for x in names:
#     hi(x)
#     print('Sıradaki:')

#return ifadesi 
# def hi(name):
#     yanit = 'Merhaba ' + name + '!'
#     return yanit 

# names = ['Seda', 'Ahmet', 'Pınar', 'Nejdet', 'Yasemin']

# for name in names:
#     hi(name)


# #return ile gelen değeri yazdır 
# def hi(name):
#     yanit = 'Merhaba ' + name + '!'
#     return yanit 

# names = ['Seda', 'Ahmet', 'Pınar', 'Nejdet', 'Yasemin']

# for name in names:
#     yazdir = hi(name)
#     print(yazdir)


#argümanlarla deneme
# def onay_sor(sor, deneme=4, hatirlatma='Lütfen tekrar deneyin!'):
#     while True:
#         ok = input(sor)
#         if ok in ('e', 'evet', 'y'):
#             return True
#         if ok in ('h', 'hayir', 'n'):
#             return False
#         deneme = deneme - 1
#         if deneme < 0:
#             raise ValueError('Geçerli olmayan kullanıcı yanıtı')
#         print(hatirlatma)
    

# # onay_sor()
# onay_sor('Dosyanın üzerine yazılsın mı?', 2, 'Olamaz! Yalnızca evet ya da hayır!')
# # onay_sor('Ekranı kapatmak istiyor musunuz?')

# # onay_sor('Dosyanın üzerine yazılsın mı?', 2)

#sınırsız isimsiz parametre alabilen fonksiyon 
def fonksiyon(*parametreler):
    print(parametreler)

# fonksiyon('Ahmet', 'Ankara', 6, hi())
x = fonksiyon(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(x))

# #sınırsız isimli parametre alabilen fonksiyon 
def fonksiyon(**parametreler):
    print(parametreler)

x=fonksiyon(isim="Ayşe", yas= 19, soyisim="Gül", meslek="Mühendis", şehir="Bitlis")
# fonksiyon(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(type(x))