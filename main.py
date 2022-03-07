def readFile(fileName):
    ddd_file = open(f"{fileName}.DDD", "rb")
    ddd_data = ddd_file.read()
    ddd_file.close()
    return ddd_data

def generateDiffFile(fileName):
    ddd_file = open(f"{fileName}.DDD", "rb")
    ddd_data = ddd_file.read()
    ddd_file.close()
    diff_file =open(f"{fileName}.txt", "a+")
    for byte in ddd_data:
        diff_file.write("{0:#0{1}x}\n".format(byte,4))
    diff_file.close()


target_file = "vehicle"


generateDiffFile(target_file)
ddd_data = readFile(target_file)
identifier0 = ddd_data[0]
identifier1 = ddd_data[1]
clockstopLength = ddd_data[2]
clockstop = ddd_data[3]
cardserialLength = ddd_data[4]
cardserialZero = ddd_data[5]
cardserial = int.from_bytes(ddd_data[6:10], "big")
cardMonth = hex(ddd_data[10])[2:]
cardYear = hex(ddd_data[11])[2:]
cardType = ddd_data[12]
cardManuCode = hex(ddd_data[13])
cardAppr1 = chr(ddd_data[14])
cardAppr2 = chr(ddd_data[15])
cardAppr3 = chr(ddd_data[16])   
cardAppr4 = chr(ddd_data[17])
cardAppr5 = chr(ddd_data[18])
cardAppr6 = chr(ddd_data[19])
cardAppr7 = chr(ddd_data[20])
cardAppr8 = chr(ddd_data[21])


print(f"Identifier: {identifier0}{identifier1} \nClockstop: ({clockstopLength}) {clockstop}\nCard Serial: ({cardserialLength}) [{cardserialZero}] {cardserial}\n Month Year: {cardMonth}/{cardYear}\nType: {cardType}\nManufacturer Code: {cardManuCode}\nApproval: {cardAppr1}{cardAppr2}{cardAppr3}{cardAppr4}{cardAppr5}{cardAppr6}{cardAppr7}{cardAppr8}")

def main(args):
    return




if __name__ == "__main__":
   main(sys.argv[1:])