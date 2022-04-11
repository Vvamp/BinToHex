'''
    File name: main.py
    Description: Converts unreadable binary files into readable binary/hex/decimal
    Author: Vincent van Setten
    Date created: 23/02/2022
    Date last modified: 11/04/2022
    Python Version: 3.10.2
    License: LICENSE.md
'''

import sys, getopt, traceback
from printers import DecimalPrinter, HexPrinter,BinaryPrinter, AsciiPrinter
from sysout import sysout

Debug = False


def printDebug(stringToWrite : str):
    global Debug
    if(Debug):
        print(stringToWrite)

def readFile(fileName):
    ddd_file = open(f"{fileName}", "rb")
    binary_data = ddd_file.read()
    ddd_file.close()
    return binary_data

def generateFile(importFilename : str, printers : list, exportFilename : str):
    """Generate a text file from a binary file, using given printers

    Args:
        importFilename (str): Import filename
        printers (list): A list of DataPrinters
        exportFilename (str): Optional output file name, or __sysout

    Returns:
        <Nothing, String>: Either returns void, or the output if '__sysout' was passed as exportname 
    """
    multipleTypes =  len(printers) > 1
     
    if(len(printers) == 0):
        print("Error: No printers specified!")
        return 

    importFile = open(f"{importFilename}", "rb")
    binary_data = importFile.read()
    importFile.close()

    if exportFilename != "__sysout":
        exportFile = open(f"{exportFilename}", "w+")
        print("Generating output file {} for {}...".format(exportFilename, importFilename))
    else:
        exportFile = sysout()

    output = []
    for printer in printers:
        printDebug("Enabling " + printer.__class__.__name__ + "...")
        printer.set_data(binary_data)  

    for printer in printers:
        printDebug("Starting write job...")
        if multipleTypes and len(output) >= 1:
            printDebug("Adding another column of data")
            data = printer.process()
            for i in range(0, len(output)):
                output[i] += " | " + data[i]
        else:
            printDebug("Adding first column of data")
            output = printer.process()

    for line in output:
        try:
            exportFile.write(line + "\n")
        except Exception as exc:
            print("An error occurred while trying to write to the output file.")
            printDebug("Exception Details: " + traceback.format_exc())
            return
    try:
        rval = exportFile.close()
        if rval:
            return rval 
    except Exception as exc:
        print("An error occurred while trying to write to close the output file.")
        printDebug("Exception Details: " + traceback.format_exc())

        return
    finally:
        print("Successfully wrote to outputfile " + exportFilename + "!")



def main(argv : list[str]):
    global Debug
    inputfile = ""
    outputfile = ""
    printers = []
    helpString = "Usage: main.py (--hex) (--binary) (--decimal) (--verbose) -i <inputfile> -o <outputfile>"

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
            printers.append(HexPrinter())
        elif opt in ("-b", "--binary"):
            printers.append(BinaryPrinter())
        elif opt in ('-d', "--decimal"):
            printers.append(DecimalPrinter())
        elif opt in ('-a', "--ascii"):
            printers.append(AsciiPrinter())
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

    generateFile(inputfile, printers, outputfile)
    return




if __name__ == "__main__":
   main(sys.argv[1:])
