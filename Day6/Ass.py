#Opening Expected result

with open("C:\\Users\\Vigne\\Desktop\\expected.txt") as file_in:

    lines = []
    expecteddict = {}
    for line in file_in:
        if(line.startswith('|')):
            lines.append(line)

        for l in lines:
            expecteddict.update({l.split('|')[1].strip(): l.split('|')[2].strip()})

    print(expecteddict)

#opening actual result
with open("C:\\Users\\Vigne\\Desktop\\Actual.txt") as file_in:

    lines = []
    actualdict = {}
    for line in file_in:
        if(line.startswith('|')):
            lines.append(line)

        for l in lines:
            actualdict.update({l.split('|')[1].strip(): l.split('|')[2].strip()})

    print(actualdict)


#missing key
for key in expecteddict.keys():
    if not key in actualdict:
        print ("Missing Key",key)

#mismatched data
mismatcheddata = {"Key: "+a:"Expected: "+ expecteddict[a] + "; Actual: "+actualdict[a] for a in expecteddict if expecteddict[a] != actualdict[a]}
print("Mismatched Data")
print(mismatcheddata)

