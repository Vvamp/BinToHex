import sys, getopt
from operator import truediv
from printers import HexPrinter,BinaryPrinter

def readFile(fileName):
    ddd_file = open(f"{fileName}.DDD", "rb")
    ddd_data = ddd_file.read()
    ddd_file.close()
    return ddd_data

def generateFile(importFilename : str, printHex: bool, printBinary : bool, exportFilename = ""):
    if exportFilename == "": 
        exportFilename = importFilename + ".txt"

    types = [printHex, printBinary]
    multipleTypes =  types.count(True) > 1
    
    importFile = open(f"{importFilename}.DDD", "rb")
    ddd_data = importFile.read()
    importFile.close()

    exportFile = open(f"{exportFilename}", "w+")
    output = []
    printers = []
    if printHex:  
        printers.append(HexPrinter(ddd_data))
    if printBinary:
        printers.append(BinaryPrinter(ddd_data))
    
    for printer in printers:
        if multipleTypes and len(output) >= 1:
            data = printer.process()
            for i in range(0, len(output)):
                output[i] += " | " + data[i]
        else:
            output = printer.process()

    for line in output:
        try:
            exportFile.write(line + "\n")
        except:
            print("An error occured while trying to write to the output file.")
            return
    try:
        exportFile.close()
    except:
        print("An error occured while trying to write to close the output file.")
        return
    finally:
        print("Successfully wrote to outputfile " + exportFilename)



def main(argv : list[str]):
    inputfile = ""
    outputfile = ""
    printHex = False
    printBinary = False
    helpString = "Usage: main.py -i <inputfile> -o (outputfile) -hex -binary"

    try:
        opts, args = getopt.getopt(argv,"hi:oxb",["ifile=","ofile=", "hex", "binary"])
    except getopt.GetoptError:
        print(helpString)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(helpString)
            sys.exit()
        elif opt in ("-x", "--hex"):
            printHex = True
        elif opt in ("-b", "--binary"):
            printBinary = True
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    if inputfile == "":
        print("Error. Not all required arguments were given.\n" + helpString)
        return

    if inputfile.lower().endswith(".ddd") == True:
        inputfiles = inputfile.split(".")[0:-1] 
        inputfile = ""
        for item in inputfiles:
            inputfile += item

    generateFile(inputfile, printHex, printBinary, outputfile)
    return




if __name__ == "__main__":
   main(sys.argv[1:])