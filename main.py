"""
Usage:
    register create_tutor <username> <password>
    register create_student <student_name>
    register create_class <class_name>
    register log_start <class_id>
    register log_end <class_id>
    register check_in <student_id> <class_name>
    register check_out <student_id> <class_id>
    register list_classes
    register list_students
    register classes_log <student_id>
    register students_log <class_id>
    register delete_class <class_id>
    register delete_student <student_id>
    register (-i | --interactive)
    register (-h | --help | --version)

Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.

Examples:
    register create_student <"Good Student">
    register create_class <Example>
    register check_in <1> <1>
"""
from colorama import Fore, Back, Style
from pyfiglet import Figlet, figlet_format
from termcolor import cprint
import os
import sys
from docopt import docopt, DocoptExit
import cmd
from CAMA.controller import create_tutor, create_student, create_darasa, list_of_students, anza_darasa
from CAMA.controller import list_of_classes, check_in_student, maliza_darasa


def docopt_cmd(func):
    """Pass the arguments from docopt to the commands"""

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


def intro():
    cprint(figlet_format('   \n W E L C O M E \n ', font='slant'),
           'blue', attrs=['blink','bold'])
    cprint(__doc__)


class Register(cmd.Cmd):
    """Class register cli."""

    prompt = '<<CAMA>> '

    file = None

    @docopt_cmd
    def do_create_tutor(self, args):
        """Usage: create_tutor <username> <password>"""

        create_tutor(args["<username>"], args["<password>"])

    @docopt_cmd
    def do_create_class(self, args):
        """Usage: create_class <class_name>"""

        create_darasa(args["<class_name>"])

    @docopt_cmd
    def do_create_student(self, args):
        """Usage: create_student <student_name>"""

        create_student(args["<student_name>"])

    @docopt_cmd
    def do_list_students(self, args):
        """Usage: list_students """
        list_of_students()

    @docopt_cmd
    def do_list_classes(self, args):
        """Usage: list_classes """
        list_of_classes()

    @docopt_cmd
    def do_log_start(self, args):
        """Usage: log_start <class_name> """
        anza_darasa(args["<class_name>"])

    @docopt_cmd
    def do_log_end(self, args):
        """Usage: log_end <class_name> """
        maliza_darasa(args["<class_name>"])

    @docopt_cmd
    def do_check_in(self, args):
        """Usage: check_in <student_id> <class_name>"""
        check_in_student(args['<student_id>'], args["<class_name>"])

    @docopt_cmd
    def do_check_out(self, args):
        """Usage: check_in <student_id> <class_id>"""

    def do_clear(self, args):
        os.system('clear')

    def do_quit(self, args):
        cprint(figlet_format(' \nG O O D  BY E\n ', font='slant'),
               'blue', 'on_white', attrs=['blink', 'bold'])
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    # create_tables()
    os.system('clear')
    intro()
    Register().cmdloop()

print(opt)
