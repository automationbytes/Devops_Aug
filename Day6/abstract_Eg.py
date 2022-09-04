from abc import ABC, abstractmethod


class marrge(ABC):

    @abstractmethod
    def partnerfinding(self):
        None

    def prop(self):
        print("House")

class child(marrge):
    def partnerfinding(self):
        print("ABC")

ob = child()
ob.partnerfinding()
ob.prop()

p = marrge()
p.prop()