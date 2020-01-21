from pathlib import Path

if Path('a.out').is_file():
    print ("File exists")
else:
    print ("File not exists")
    saveFile = open('a.out', 'a+')
    TS = "First Name, Last Name, Title, Location, Email, Phone Number, Carrier \n"
    saveFile.write(TS)
    saveFile.close