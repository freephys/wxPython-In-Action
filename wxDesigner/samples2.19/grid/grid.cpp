/////////////////////////////////////////////////////////////////////////////
// Name:        grid.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "grid.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "grid.h"

// WDR: class implementations

//----------------------------------------------------------------------------
// MyDialog
//----------------------------------------------------------------------------

// WDR: event table for MyDialog

BEGIN_EVENT_TABLE(MyDialog,wxDialog)
END_EVENT_TABLE()

MyDialog::MyDialog( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxDialog( parent, id, title, position, size, style )
{
    // WDR: dialog function MyDialogFunc for MyDialog
    MyDialogFunc( this, TRUE ); 
}

// WDR: handler implementations for MyDialog


//----------------------------------------------------------------------------
// MyGrid
//----------------------------------------------------------------------------

IMPLEMENT_CLASS(MyGrid,wxGrid)

// WDR: event table for MyGrid

BEGIN_EVENT_TABLE(MyGrid,wxGrid)
    EVT_GRID_CELL_RIGHT_CLICK( MyGrid::OnRightClick )
END_EVENT_TABLE()

MyGrid::MyGrid( wxWindow *parent, wxWindowID id,
    const wxPoint &position, const wxSize& size, long style ) :
    wxGrid( parent, id, position, size, style )
{
}

// WDR: handler implementations for MyGrid

void MyGrid::OnRightClick( wxGridEvent &event )
{
    wxMessageDialog dialog( this, wxT("A cell has been right clicked!"), wxT("MyGrid"), wxICON_INFORMATION );
    dialog.CentreOnParent();
    dialog.ShowModal();
}


//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(ID_GRID, MyFrame::OnGrid)
    EVT_MENU(ID_QUIT, MyFrame::OnQuit)
    EVT_CLOSE(MyFrame::OnCloseWindow)
END_EVENT_TABLE()

MyFrame::MyFrame( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxFrame( parent, id, title, position, size, style )
{
    CreateMyMenuBar();
    
    CreateStatusBar(1);
    SetStatusText( wxT("Welcome!") );
    
     // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
#ifdef __WXMAC__
    wxApp::s_macAboutMenuItemId = ID_ABOUT;
#endif

    SetMenuBar( MyMenuBarFunc() );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnGrid( wxCommandEvent &event )
{
    MyDialog dialog( this, -1, wxT("MyGrid dialog") );
    dialog.CentreOnParent();
    dialog.ShowModal();
}

void MyFrame::OnQuit( wxCommandEvent &event )
{
     Close( TRUE );
}

void MyFrame::OnCloseWindow( wxCloseEvent &event )
{
    // if ! saved changes -> return
    
    Destroy();
}

//------------------------------------------------------------------------------
// MyApp
//------------------------------------------------------------------------------

IMPLEMENT_APP(MyApp)

MyApp::MyApp()
{
}

bool MyApp::OnInit()
{
    MyFrame *frame = new MyFrame( NULL, -1, wxT("SuperApp"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

