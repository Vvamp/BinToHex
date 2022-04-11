'''
    File name: printers.py
    Description: Declare different methods to print bytes
    Author: Vincent van Setten
    Date created: 23/02/2022
    Date last modified: 11/04/2022
    Python Version: 3.10.2
    License: LICENSE.md
'''

from typing import List


class DataPrinter:
    """Abstracts a data printer object
    """
    def __init__(self, binary_data : bytes = None):
        """Instantiate a data printer

        Args:
            binary_data (bytes): binary data read as bytes
        """
        self.data = binary_data

    def process(self):
        """Process the binary data into an array of lines in a specified method

        Returns:
            List<str>: Output array of processed data
        """
        output=[]
        for _data in self.data:
            output.append(_data)
        return output

    def set_data(self, data : bytes):
        """Set the internal data

        Args:
            data (bytes): List of input bytes
        """
        self.data = data

class HexPrinter(DataPrinter):
    def process(self):
        """Process the binary data into an array of lines in HEX Format

        Returns:
            List<str>: Output array of processed data in hex format
        """
        output=[]
        for _data in self.data:
            output.append("{0:#0{1}x}".format(_data,4))
        return output

class BinaryPrinter(DataPrinter):
    def process(self):
        """Process the binary data into an array of lines in Binary format

        Returns:
            List<str>: Output array of processed data in binary format
        """
        output=[]
        for _data in self.data:
            output.append("{0:08b}".format(_data))
        return output


class DecimalPrinter(DataPrinter):
    def process(self):
        """Process the binary data into an array of lines in Decimal format

        Returns:
            List<str>: Output array of processed data in Decimal format
        """
        output=[]
        for _data in self.data:
            output.append("{}".format(_data))
        return output


class AsciiPrinter(DataPrinter):
    def process(self):
        """Process the binary data into an array of lines in ascii text format

        Returns:
            List<str>: Output array of processed data in ascii text format
        """
        output=[]
        for _data in self.data:
            try:
                print(_data.decode("ascii"))
                output.append("{}".format(_data.decode("ascii")))
            except:
                output.append(BinaryPrinter([_data]).process()[0])
        return output
