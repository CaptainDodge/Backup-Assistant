welcome = print("Welcome to File Backup Assistant!")

# functions:
def keyInFileName():
    global fileName
    fileName = input("Please key in the file name:\n")
    if (type(fileName) == str and len(fileName) > 0):
        backupProcess()
    else:
        print("Please key in a valid filename string!")
        keyInFileName()

def backupProcess():
    try:
        global backupName
        backupName = fileName + ".bak"
        with open(fileName,"r") as FILE:
            data = FILE.read()
            with open(backupName,"w") as newFILE:
                newFILE.write(data)
        print("Success! Backed up file as " + str(backupName))
    except:
        print("File does not exist. Try again!")
        keyInFileName()
# end of functions

keyInFileName()


