from collections import namedtuple

Options = namedtuple('Options', [
    'quiet',     # -q --quiet
    'verbose',   # -v --verbose
    'release',   # -r --release
    'developer', # -d --developer
    'action',    # new, init, build, run, test, debug
    'name',      # name argument
])

Config = namedtuple('Config', [
    'name',
    'main',
    'includes',
    'libs',
    'cc',
    'dbg',
])

DEFAULT_MEKPY='''
# This is a standard configuration file for mekpie

# the name of the project
name = '{}'
# the .c file containing `main`
main = '{}'
# any additional include directories
includes = []
# any libraries to load
libs = []
# the c copmiler to use
cc = 'gcc'
# the debugger to use
dbg = 'gdb'
'''

MAIN = '''
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char ** argv) {
    puts("Hello, World!");
    return EXIT_SUCCESS;
}
'''.strip()

VERSION = '0.0.1'