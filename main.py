from email import message
import sys, getopt
from operator import truediv
from printers import DecimalPrinter, HexPrinter,BinaryPrinter

Debug = False


def printDebug(stringToWrite : str):
    global Debug
    if(Debug):
        print(stringToWrite)

def readFile(fileName):
    ddd_file = open(f"{fileName}", "rb")
    ddd_data = ddd_file.read()
    ddd_file.close()
    return ddd_data

def generateFile(importFilename : str, printHex: bool, printBinary : bool, printDecimal : bool, exportFilename : str):
    types = [printHex, printBinary]
    multipleTypes =  types.count(True) > 1
    
    importFile = open(f"{importFilename}", "rb")
    ddd_data = importFile.read()
    importFile.close()

    exportFile = open(f"{exportFilename}", "w+")
    print("Generating output file {} for {}...".format(exportFilename, importFilename))
    output = []
    printers = []
    if printHex:  
        printDebug("Enabling HexPrinter")
        printers.append(HexPrinter(ddd_data))
    if printBinary:
        printDebug("Enabling BinaryPrinter")
        printers.append(BinaryPrinter(ddd_data))
    if printDecimal:
        printDebug("Enabling DecimalPrinter")
        printers.append(DecimalPrinter(ddd_data))
   
    if(len(printers) == 0):
        print("Error: No printers specified!")
        return 

    for printer in printers:
        printDebug("Starting write job...")
        if multipleTypes and len(output) >= 1:
            printDebug("Adding another row of data")
            data = printer.process()
            for i in range(0, len(output)):
                output[i] += " | " + data[i]
        else:
            printDebug("Adding first row of data")
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
        print("Successfully wrote to outputfile " + exportFilename + "!")



def main(argv : list[str]):
    global Debug
    inputfile = ""
    outputfile = ""
    printHex = False
    printBinary = False
    printDecimal = False 
    helpString = "Usage: main.py  (--hex) (--binary) (--decimal) (--verbose) -i <inputfile> -o <outputfile>"

    try:
        opts, args = getopt.getopt(argv,"hi:o:xbv",["ifile=","ofile=", "hex", "binary", "verbose", "decimal"])
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
        elif opt in ('-d', "--decimal"):
            printDecimal = True
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-v", "--verbose"):
            Debug = True
        else:
            print("Unknown command line argument {}".format(opt))
            return


    if inputfile == "":
        print("Error. Not all required arguments were given.\n" + helpString)
        return

    generateFile(inputfile, printHex, printBinary, printDecimal, outputfile)
    return




if __name__ == "__main__":
   main(sys.argv[1:])
