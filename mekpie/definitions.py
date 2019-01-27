from .record import Record, required

DEFAULT_MEKPY = '''
# This is a standard configuration file for mekpie

# the name of your project
name = '{}' 
# the .c file containing `main`
main = '{}'
# the c compiler configuration to use (gcc_clang, avr_gcc, or emscripten)
cc = {}
# any libraries to load
libs = []
# additional compiler flags
flags = []

if options.release:
    flags += {}
else:
    flags += {}
'''

MAIN = '''
#include <stdio.h>
#include <stdlib.h>

int main() {
    puts("Hello, World!");
    return EXIT_SUCCESS;
}
'''.strip()

VERSION = '0.0.1'

Option = Record({
    'names'   : required, 
    'nargs'   : None,
    'handler' : None,
})

Options = Record({
    'quiet'       : False,     # -q --quiet
    'release'     : False,     # -r --release
    'developer'   : False,     # -d --developer
    'mode'        : False,     # -m --mode
    'changedir'   : False,     # -c --changedir
    'command'     : None,      # new, init, clean, build, run, test, debug
    'commandargs' : [],        # <optionargs...>
    'programargs' : [],        # -- <programargs...>
})

Config = Record({
    'name'       : None, # Project name
    'main'       : None, # Entry point
    'libs'       : [],   # Libraries to link
    'cc'         : None, # Compiler Configuration
    'flags'      : [],   # User compiler flags
    'options'    : None, # The provided command line options
    'includes'   : [],   # Include directories
    'once'       : None, # Provided by plugin
    'targetpath' : None, # Function that providees target path
    'run'        : None, # Provides a run function with correct flags
})

CompilerConfig = Record({
    'name'         : required, # Name of the config
    'compile'      : required, # Compilation function
    'link'         : required, # Linking function
    'run'          : required, # Runnning function
    'debug'        : required, # Debug function
    'once'         : (lambda *args : None),
    'ccsource'     : None,     # Mekpy source for project creation
    'csource'      : MAIN,     # csource, by default hello world
    'debugflags'   : [],       # Default debug flags    
    'releaseflags' : [],       # Default release flags
})