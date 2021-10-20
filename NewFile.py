#Var that controls where the output file is located
import os

#Creates a new file with all the data together if the user wishes it
def newFile(output, fileout):
    setFileLocation(fileout)
    try:
        newfile = open(exportFileLocation, "w+")
        newfile.write(output)
        return "Your file is located at  " + exportFileLocation
    except PermissionError:
        return "Please eiter enter a valid path, or run this program as admin "
#Retuns the string of all number values within the given textfile
def getFullsting():
    return fullsetString
#Sets the string that will later be converted into a list
def setFullString(list):
    global fullsetString
    fullsetString = ""
    for i in list:
        fullsetString = fullsetString + ", "+ i 
#Checks if the desired file location is a valid one, and then creates a file in said location
def setFileLocation(fileout):
    global exportFileLocation
    exportFileLocation = fileout
    if fileout == "" or  fileout == "Please enter the desired location for the output text file here. If blank it wil be placed in a folder within the Program's Document File":
        exportFileLocation = "Documents/OutputFile.txt"
    else:
        exportFileLocation = "C:/" + exportFileLocation
        try:
            os.mkdir(fileout)
            print(fileout + "This is the export location")
            exportFileLocation = fileout
        except FileExistsError:
            print(fileout + "This is the export location")
            exportFileLocation = fileout+"/Output.txt"
        except OSError:
            print(exportFileLocation + "Desired location is ")
            exportFileLocation = "Please enter a valid Path location"
        except PermissionError:
            exportFileLocation = "Please enter a valid Path location"
