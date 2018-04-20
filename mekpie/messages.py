# Local Imports
from .definitions import VERSION
from .util        import tab

usage = '''
Usage:
    mekpie [options] <command> [<args>...]

Options:
    -h, --help      Display this message
    -V, --version   Print version info and exit
    -v, --verbose   Use verbose output
    -q, --quiet     No output to stdout
    -r, --release   Run the command for release
    -d, --developer Run mekpie in developer mode

Commands:
    new <name>  Create a new mekpie project
    init <name> Create a project in an existing directory
    test <name> Build and execute tests or test
    build       Compile the current project
    run         Build and execute main
    debug       Build and execute under a debugger
'''

version = tab(f'    mekpie version {VERSION}')

no_action = '''
Invalid command: No command provided!

    mekpie expects a command following its invocation.
    The following commands are available:

        help        Display a help message
        version     Print version info and exit
        new <name>  Create a new mekpie project
        init <name> Create a project in an existing directory
        test <name> Build and execute tests or test
        build       Compile the current project
        run         Build and execute main
        debug       Build and execute under a debugger
'''

repeated_option = 'Repeated option: option {} appears twice!'

too_many_arguments = 'Unexpected argument: Too many arguments provided!'

unknown_argument = 'Unexpected argument: Unknown argument provided!'

name_cannot_already_exist = '''
Invalid argument: Cannot create a project in a directory that already exists!

    The directory "./{}" already exists. If you want to use this folder with
    mekpie, navigate within the folder, and run the `init` command.
'''

name_cannot_be_empty = '''
Missing argument: You must provide the positional argument `name`!

    When creating a project with `new` or `init` you must provide a positional
    argument `name` after the command.
'''