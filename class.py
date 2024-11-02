class Car:
    yakıt = "elektrik"

    def __init__(self, marka):
        self.marka = marka

bmw = Car("BMW")
print(bmw.marka)
print(bmw.yakıt)

bmw.yakıt = "benzin"  # burada aslında init fonksiyonu içinde bir yakıt değişkeni tanımladık.
bmw.vites = "manuel"  # burada da vites diye bir değişken tanımladık.
print(bmw.yakıt)
print(bmw.vites)

# yani class içindeki yakıt değişkenini değiştirmiş olmadık.

# class içindeki değişkenlere erişmek için:
Car.yakıt = "benzin"
print(Car.yakıt)
