class Foydalanuvchi:
    def __init__(self, ism, username, parol):
        self.ism = ism
        self.username = username
        self.__parol = parol

    def parolni_ozgartir(self, eski_parol, yangi_parol):
        if self.__parol != eski_parol:
            print("Eski parol notogri!")
            return False

        self.__parol = yangi_parol
        print("Parol muvaffaqiyatli ozgartirildi.")
        return True

    def tekshir(self, parol):
        return self.__parol == parol

user = Foydalanuvchi("Ali", "ali_01", "abc123")
user2 = Foydalanuvchi("Malika", "malika_02", "123xyz")

print(user.tekshir("abc123"))
print(user.parolni_ozgartir("abc123", "new456"))
print(user.tekshir("new456"))
