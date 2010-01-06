#
# File:       makefile.wat
# Author:     Robert Roebling
# Created:    2000
# Copyright:  (c) 2000 Robert Roebling
#
# Makefile for wxDesigner sample for Watcom C++

WXDIR = $(%WXWIN)

PROGRAM = hworld

RESOURCE = $(PROGRAM)_wdr

OBJECTS = $(PROGRAM).obj $(RESOURCE).obj

!include $(WXDIR)\src\makeprog.wat


