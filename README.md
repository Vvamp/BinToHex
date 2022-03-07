<!-- Project Badges-->
![Contributors Badge](https://img.shields.io/github/contributors/Vvamp/DDDToHex.svg?)
![Forks Badge](https://img.shields.io/github/forks/Vvamp/DDDToHex.svg?)
![Stars Badge](https://img.shields.io/github/stars/Vvamp/DDDToHex.svg?)
![Issues Badge](https://img.shields.io/github/issues/Vvamp/DDDToHex.svg?)
![License Badge](https://img.shields.io/github/license/Vvamp/DDDToHex.svg?)

# DDD To Hex
A simple script that converts DDD(tachograph files) into binary, or hex. 
This tool should work for any binary file, but is only tested with DDD files.

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
    - `git clone https://github.com/Vvamp/DDDToHex`
2. Cd into the project directory
    - `cd DDDToHex`

## Usage
### Command Line Arguments
Run : `python main.py -h` shows all the available command line arguments and their usage.  
The command `python main.py -i hello.DDD -o output.txt --hex` converts the hello.DDD file to hex into `output.txt`. 
The command `python main.py -i hello.DDD -o output.txt --binary` converts the hello.DDD file to binary. 
The command `python main.py -i hello.DDD -o output.txt --binary --hex` converts the hello.DDD file to both binary and hex(seperated by a '|' character). 

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
Project: [DDD To Hex](https://github.com/Vvamp/DDDToHex)

## Acknowledgements
- [Shields.io](https://shields.io/)
