
The samples directory contains a number of sample projects
using resources created with wxDesigner 1.1. In order to
build the projects you have to start wxDesigner, load the 
resource file from the respective directory and write the
C++ or Python output to disk. The projects can then be
compiled with most compilers supported by wxWindows (most
importantly GNU C++, Microsoft Visual C++, Borland C++ and
Watcom C++) by using the makefiles in the directories. All
samples are provided in both C++ and Python and require
wxWindows 2.2.0 or higher and wxPython 2.2.0 or higher to
be installed respectively.

It is allowed to use these sample projects as templates
for user programs regardless of their licence or way of 
distribution.

hello:
This samples demonstrates the smallest possible program that
makes use of a resource created with wxDesigner. It displays
a dialog and exits directly afterwards.

minimal:
This is the wxDesigner version of "minimal", the demonstration
program of wxWindows.

controls:
This sample shows a dialog with a great variety of controls
supported by wxWindows and wxDesigner including the XML
output.

spacer:
Here you can look at a dialog created with wxDesigner which
contains many spacers, that it empty space required to create
a specific layout.

events:
This sample demonstrates how to intercept events from controls
in a dialog created with wxDesigner.

foreign:
The foreign sample shows how to place a control which is not
supported by wxDesigner directly into a dialog created with
wxDesigner. In this case, a list ctrl is inserted in the dialog
where wxDesigner shows a place-holder for it.

bitmaps:
As the name suggests, this sample show the use of bitmaps in
dialogs created with wxDesigner.

notebook:
Unsurprisingly, this sample uses a wxDesigner resource two create
two pages in a notebook, which in turn uses the notebook sizer.

rad:
This sample was largely created using the new RAD features of
wxDesigner 1.1 - it contains the various text marks used by
wxDesigner to insert source code automatically.

derived:
This sample demonstrates how to use custom controls (i.e.
controls derived from standard wxWindows controls) in 
wxDesigner - in this case a specialized variant of a 
wxTextCtrl.
 
menu:
Shows the various event types sent by menus.

scrolled:
This sample demonstrates the wxScrolledWindow class as a
derived class. It also uses system events (paint, mouse)
added by wxDesigner.

grid:
Beginning of a wxGrid sample. In progress.

dynamic:
Shows how to use sizers for creating interfaces/dialogs
which change their appearance dynamically.

toolbar:
Demonstrates the use of toolbar resources.

