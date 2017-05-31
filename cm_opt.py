#!venv/bin/python
"""

Usage:
cm_opt.py add -n <firstname> [<lastname>] -p <number>    adds number to contact manager list
cm_opt.py search [name] [number]        Searches for name or number
cm_opt.py text <name> -m <message>...        Texts the name or number input
cm_opt.py (-i | --interactive)
cm_opt.py (-h | --help)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from colorama import init
init(strip=not sys.stdout.isatty())
from docopt import docopt, DocoptExit
from contact_manager import c_manager
from termcolor import cprint
from pyfiglet import figlet_format


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """
    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class contact_manager(cmd.Cmd):
    text = "Contact Manager"
    cprint(figlet_format(text, font="basic"), "white")
    intro = " Welcome to Contact Manager"
    prompt = 'Contact_Manager>> '
    file = None

    @docopt_cmd
    def do_add(self, arg):
        """Usage: add -n <firstname> [<lastname>] -p <phonenumber>"""
        full_name = arg['<firstname>'] + ' ' + arg['<lastname>']
        phone_number = arg['<phonenumber>']
        print(c_manager.add(full_name, phone_number))

    @docopt_cmd
    def do_search(self, args):
        """Usage: Searches <name>"""
        full_name = args['<name>']
        print(c_manager.search(full_name))

    @docopt_cmd
    def do_text(self, args):
        """Usage: text <name> -m <message>..."""
        name = args['<name>']
        message = " ".join(args['<message>'])
        print(c_manager.text(name, message))

    def do_quit(self, arg):
        """quit"""
        print('System closed.')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    try:
        print(__doc__)
        contact_manager().cmdloop()
    except KeyboardInterrupt:
        print("Exiting App")
