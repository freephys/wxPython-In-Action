//------------------------------------------------------------------------------
// Header generated by wxDesigner from file: toolbar.wdr
// Do not modify this file, all changes will be lost!
//------------------------------------------------------------------------------

#ifndef __WDR_toolbar_H__
#define __WDR_toolbar_H__

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma interface "toolbar_wdr.h"
#endif

// Include wxWidgets' headers

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include <wx/image.h>
#include <wx/statline.h>
#include <wx/spinbutt.h>
#include <wx/spinctrl.h>
#include <wx/splitter.h>
#include <wx/listctrl.h>
#include <wx/treectrl.h>
#include <wx/notebook.h>
#include <wx/grid.h>
#include <wx/toolbar.h>

// Declare window functions

// Declare menubar functions

const int ID_MENU = 10000;
wxMenuBar *MyMenuBarFunc();

// Declare toolbar functions

const int ID_OPEN = 10001;
const int ID_CUT = 10002;
const int ID_COPY = 10003;
const int ID_PASTE = 10004;
const int ID_FONT = 10005;
void MyToolBarFunc( wxToolBar *parent );

// Declare bitmap functions

wxBitmap MyBitmapsFunc( size_t index );

#endif

// End of generated file