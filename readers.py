'''
    File name: readers.py
    Description: Declare different methods to read bytes
    Author: Vincent van Setten
    Date created: 18/04/2023
    Date last modified: 18/04/2023
    Python Version: 3.10.2
    License: LICENSE.md
'''

from typing import List


class DataReader:
    """Abstracts a data reader object
    """
    def __init__(self, text_data : str = None):
        """Instantiate a data reader

        Args:
            text_data (bytes): binary data read as bytes
        """
        self.data = text_data

    def process(self):
        """Process the binary data into an array of lines in a specified method

        Returns:
            List<str>: Output array of processed data
        """
        output=[]
        for _data in self.data:
            output.append(_data)
        return output

    def set_data(self, data : str):
        """Set the internal data

        Args:
            data (bytes): List of input bytes
        """
        self.data = data

class HexReader(DataReader):
    def __init__(self, byte_length : int, text_data : str = None):
        super().__init__(text_data)
        self.byte_length = byte_length

    def process(self):
        """Process the binary data into an array of lines in HEX Format

        Returns:
            List<str>: Output array of processed data in hex format
        """
        output=[]
        self.data = self.data.replace("0x", "")

        for data_index in range(0, len(self.data), self.byte_length*2):
            cur_string = str(self.data[data_index])
            for i in range(data_index+1, data_index+self.byte_length*2):
                cur_string += str(self.data[i])
            cur_byte = bytearray.fromhex(cur_string)
            output.append(cur_byte)
        return output