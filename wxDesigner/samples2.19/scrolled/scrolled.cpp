/////////////////////////////////////////////////////////////////////////////
// Name:        scrolled.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "scrolled.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "scrolled.h"

// WDR: class implementations

//----------------------------------------------------------------------------
// MyScrolledWindow
//----------------------------------------------------------------------------

// WDR: event table for MyScrolledWindow

BEGIN_EVENT_TABLE(MyScrolledWindow,wxScrolledWindow)
    EVT_PAINT( MyScrolledWindow::OnPaint )
    EVT_LEFT_DOWN( MyScrolledWindow::OnLeftDown )
END_EVENT_TABLE()

MyScrolledWindow::MyScrolledWindow( wxWindow *parent, wxWindowID id,
    const wxPoint &position, const wxSize& size, long style ) :
    wxScrolledWindow( parent, id, position, size, style )
{
}

// WDR: handler implementations for MyScrolledWindow

void MyScrolledWindow::OnLeftDown( wxMouseEvent &event )
{
    wxMessageDialog dialog( this, wxT("Left Click."), wxT("Test"), wxOK|wxICON_INFORMATION );
    dialog.ShowModal();
}

void MyScrolledWindow::OnPaint( wxPaintEvent &event )
{
    wxPaintDC dc(this);
    PrepareDC( dc );
    dc.DrawLine( 0,0,300,300 );
}


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
    
    CentreOnParent();
}

// WDR: handler implementations for MyDialog


//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(ID_SCROLLED, MyFrame::OnScrolled)
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

void MyFrame::OnScrolled( wxCommandEvent &event )
{
    MyDialog dialog( this, -1, wxT("Test MyScrolledWindow") );
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

