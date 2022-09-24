from jproperties import Properties

propfile = Properties()

def readProp(Key):
    with open("config.properties", "rb") as configfile:
        propfile.load(configfile)
        return propfile.get(Key).data

print(readProp("username"))
# print all the values
# propitems = propfile.items()
# for prop in propitems:
#     print(prop[1].data)