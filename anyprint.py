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
    
    # C like
    'puts': print,
    'printf': printf,

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
}


def make_module(name, members):
    m = types.ModuleType(name)
    m.__name__ = name
    for k, v in members.items():
        if callable(v):
            m.__dict__[k] = v
        elif type(v) is dict:
            m.__dict__[k] = make_module(k, v)
    return m


for k, v in prints.items():
    if type(v) is dict:
        globals()['__builtins__'][k] = make_module(k, v)
    else:
        globals()['__builtins__'][k] = v
