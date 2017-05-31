# Contact Manager
*Contact Manager + SMS* is a command line application that send messages using twilio api and is written using the Python Language

### Features
* Add contact directly from the terminal to the contact manager list
* Search for a contact using name from the terminal
* Send a text to a twilio verified phone number.

### Dependencies | Requirements

* [Python 2.7] (https://www.python.org/downloads/) : Python Interpreter

* [docopt==0.6.2] ( http://docopt.org) : docopt makes command-line interfaces

* [SQLAlchemy==1.1.6] ( http://www.sqlalchemy.org): The Python SQL Toolkit and Object Relational Mapper

* [twilio==5.7.0] ( https://github.com/twilio/twilio-python/) : Twilio API client and TwiML generator

* [Colorama==0.3.7 ]  (https://pypi.python.org/pypi/colorama) : Colour and font enhancing for python applications. ```pip install colorama```

* [pyfiglet==0.7.5] (https://pypi.python.org/pypi/pyfiglet): Takes ASCII text and renders it in ASCII art fonts.
```pip install https://pypi.python.org/packages/source/p/pyfiglet/pyfiglet-0.7.5.tar.gz```

* [termcolor==1.1.0] (https://pypi.python.org/pypi/termcolor): ANSII Color formatting for output in terminal. 
```pip install termcolor```

### To install all the requirements, download the [requirements.txt](https://github.com/Awinja/bc-16-contact_manager) file then type the following command on your terminal.
pip install -r /path/to/requirements.txt  

### Commands

|Command| Description|
|-----|---------------------------------------------------------|
|help | Displays all available commands and their descriptions |
| help (command) | Describes the command |
| Add -n<firstname><lastname> -p<phonenumber> | Adds name and phone number to the contact list |
| Search (name) | Searches the contact name |
| Text (name) -m <message> | Sends text message number in the contact manager |

### Contact Information
Find the author at [@Awinja] (https://github.com/Awinja/bc-16-contact_manager) on github.
