class std:
    __age = 10
    def name(self):
        print("name method - public")

    def _proname(self):
        print(self.__age,"name method - protected")

    def __privatemet(self):
        print("name method - private")

class subj(std):
    pass

o = std()
s = subj()
o.name()
s.name()
o._proname()
s._proname()
o.__privatemet()
s.__privatemet()


'''
marriageProposal
    partnerfinding
    prop - house
    
child
    partnerfinding - xyz

'''