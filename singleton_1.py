class Singleton:
    __instance = None
    def __init__(self):
        if not Singleton.__instance:
            print("init method called..")
        else:
            print("Instance already created:", self.getInstance())
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s1 = Singleton() ## class initialized, but object not created
print("Object created", Singleton.getInstance())
s2 = Singleton() ## instance already created