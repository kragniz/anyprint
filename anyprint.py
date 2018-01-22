from __future__ import print_function
import functools
import types


printf = lambda *args: print(args[0] % args[1:], end='')
printn = lambda *args: print(*args, end='')


class Cout:
    def __lshift__(self, v):
        printn(v)
        return self


class SquareFunc:
    def __init__(self, f):
        self.f = f

    def __getitem__(self, k):
        self.f(k)


prints = {
    # go
    'fmt': {
        'Println': print,
        'Printf': printf,
        'Print': printn,
    },

    # java
    'System': {
        'out': {
            'println': print,
            'printf': printf,
        },
        # Visual Basic .NET
        'Console': {
            'Write': printn,
            'WriteLine': print,
        },
    },
    
    # kotlin
    'println': print,

    # C like
    'printf': printf,
    'puts': lambda *args: print(*args, sep='\n'),     # shared with Ruby

    # actionscript
    'trace': print,

    # ada
    'Ada': {
        'Text_IO': {
            'Put_Line': print,
        },
    },

    # AmigaE
    'WriteF': print,

    # ASP
    'Response': {
        'Write': print,
    },

    # B
    'putchar': print,

    # D
    'writeln': print,
    'std': {
        'stdio': {
            'writeln': print,
        },
    },

    # PureBasic
    'PrintN': print,

    # Clipper
    'Qout': print,

    # C++
    'cout': Cout(),
    'endl': '\n',

    # C#
    'Console': {
        'WriteLine': print,
        'println': print,
    },

    # Delphi
    'Writeln': print,

    # javascript
    'console': {
        'log': print,
    },

    # lua
    'io': {
        'write': printn,
    },

    # Mathematica
    'Print': SquareFunc(print),

    # matlab
    'disp': print,
    'fprintf': printn,

    # nim
    'echo': print,

    # Pascal
    'writeln': print,

    # pike
    'write': lambda x: print(x, end=''),
    'writeln': print,

    # Elixir
    'IO': {
        'puts': print,
        'write': lambda x: print(x, end=''),
    },

    # Unity3D in C#
    'Debug': {
        'Log': print,
    },
  
    # Objective-C
    'NSLog': lambda *args: print(args[0].replace('%@', '%s') % args[1:]),

    # Ruby
    'p': lambda *args: (print(*(repr(a) for a in args), sep='\n') and False) or list(args),

    # Haskell
    'putStrLn': print,
    'putStr': printn,
}


def make_module(name, members):
    m = types.ModuleType(name)
    m.__name__ = name
    for k, v in members.items():
        if type(v) is dict:
            m.__dict__[k] = make_module(k, v)
        else:
            m.__dict__[k] = v
    return m


for k, v in prints.items():
    if type(v) is dict:
        globals()['__builtins__'][k] = make_module(k, v)
    else:
        globals()['__builtins__'][k] = v
