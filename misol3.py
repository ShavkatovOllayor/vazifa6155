class Avtomobil:
    def __init__(self, model):
        self.model = model
        self.__eshik_ochiq = False

    def eshikni_och(self):
        self.__eshik_ochiq = True
        print("Eshik ochildi")

    def eshikni_yop(self):
        self.__eshik_ochiq = False
        print("Eshik yopildi")

    def holat(self):
        if self.__eshik_ochiq:
            print("Eshik ochiq")
            return "ochiq"

        print("Eshik yopiq")
        return "yopiq"


mashina = Avtomobil("Chevrolet Cobalt")
mashina.eshikni_och()
mashina.holat()
mashina.eshikni_yop()
mashina.holat()