#
# File:        Makefile
# Author:      Robert Roebling
# Created:     2000
# Copyright:   (c) 2000 Robert Roebling
#
# This makefile requires a Unix version of wxWindows
# to be installed on your system. This is most often
# done typing "make install" when using the complete
# sources of wxWindows or by installing the two
# RPM packages wxGTK.XXX.rpm and wxGTK-devel.XXX.rpm
# under Linux.
#

CC = g++

PROGRAM = notebook

RESOURCE = $(PROGRAM)_wdr

OBJECTS = $(RESOURCE).o $(PROGRAM).o

# implementation

.SUFFIXES:	.o .cpp

.cpp.o :
	$(CC) -c `wx-config --cxxflags` -o $@ $<

all:    $(PROGRAM)

$(PROGRAM):	$(OBJECTS)
	$(CC) -o $(PROGRAM) $(OBJECTS) `wx-config --libs`

clean: 
	rm -f *.o $(RESOURCE)_wdr.py $(RESOURCE)_wdr.cpp $(RESOURCE)_wdr.h $(RESOURCE)_wdr.pyc $(PROGRAM)
	rm -f $(RESOURCE)_wdr/*
	@if test -d $(RESOURCE)_wdr; then rmdir -f $(RESOURCE)_wdr; fi
