class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif
        self.__ijarada = False

    def ijaraga_ber(self):
        if self.__ijarada:
            print("Bu kitob allaqachon ijarada.")
            return False

        self.__ijarada = True
        print("Kitob ijaraga berildi.")
        return True

    def qaytarish(self):
        if not self.__ijarada:
            print("Bu kitob kutubxonada turibdi.")
            return False

        self.__ijarada = False
        print("Kitob kutubxonaga qaytarildi.")
        return True

    def holat(self):
        holat = "Ijarada" if self.__ijarada else "Kutubxonada"
        print(holat)
        return holat


kitob = Kitob("Otkan kunlar", "Abdulla Qodiriy")
kitob.ijaraga_ber()
kitob.holat()
kitob.qaytarish()
kitob.holat()