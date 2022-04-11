<!-- Project Badges-->
![Contributors Badge](https://img.shields.io/github/contributors/Vvamp/BinToHex.svg?)
![Forks Badge](https://img.shields.io/github/forks/Vvamp/BinToHex.svg?)
![Stars Badge](https://img.shields.io/github/stars/Vvamp/BinToHex.svg?)
![Issues Badge](https://img.shields.io/github/issues/Vvamp/BinToHex.svg?)
![License Badge](https://img.shields.io/github/license/Vvamp/BinToHex.svg?)
![Build Badge](https://img.shields.io/github/workflow/status/Vvamp/BinToHex/Python%20application)

# Bin To Hex
A simple script that converts binary files into readable decimal, binary, or hex files. 
This tool should work for any binary file. 

## Table of Contents
- [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Installation]("#Installation)
- [Usage](#Usage)
    - [Command Line Arguments](#Command-Line-Arguments)
- [Tests](#Tests)
    - [Test Image](#Test-Image)
- [Contributing](#Contributing)
- [License](#License)
- [Contact](#Contact)
- [Acknowledgements](#Acknowledgements)

## Getting Started
### Prerequisites
1. [Python](https://www.python.org/)

### Installation
1. Clone this project somewhere you like
    - `git clone https://github.com/Vvamp/BinToHex`
2. Cd into the project directory
    - `cd BinToHex`

## Usage
### Command Line Arguments
Run : `python main.py -h` shows all the available command line arguments and their usage.  
The command `python main.py -i hello.DDD -o output.txt --hex` converts the hello.DDD file to hex into `output.txt`. 
The command `python main.py -i hello.DDD -o output.txt --binary` converts the hello.DDD file to binary text. 
The command `python main.py -i hello.bin -o output.txt --binary --hex` converts the hello.bin file to both binary and hex(seperated by a '|' character). 

**See `python main.py -h` for a list of commands**

## Contributing
1. Fork the project
2. Create a feature branch: `git checkout -b feature/<FeatureName>`
3. Make your changes
4. Commit your changes: `git commit -m "<Describe your changes>"`
5. Push to the branch: `git push origin feature/<FeatureName>`
6. Open a pull request

## License
Distributed under the Boost Software License Version 1.0.  
See `LICENSE` for more details.

## Contact
Vincent van Setten - [@Vvamp](https://github.com/Vvamp) - [info@vincentvansetten.com](mailto:info@vincentvansetten.com)  
Project: [Bin To Hex](https://github.com/Vvamp/BinToHex)

## Acknowledgements
- [Shields.io](https://shields.io/)
