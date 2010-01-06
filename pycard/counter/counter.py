#!/usr/bin/python

"""
__version__ = "$Revision: 1.10 $"
__date__ = "$Date: 2004/04/24 22:13:31 $"
"""

from PythonCard import model

class Minimal(model.Background):
    pass

if __name__ == '__main__':
    app = model.Application(Minimal)
    app.MainLoop()
