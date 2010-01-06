/////////////////////////////////////////////////////////////////////////////
// Name:        toolbar.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma implementation "toolbar.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "toolbar.h"

// WDR: class implementations

//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(wxID_ABOUT, MyFrame::OnAbout)
    EVT_MENU(wxID_EXIT, MyFrame::OnQuit)
    EVT_CLOSE(MyFrame::OnCloseWindow)
END_EVENT_TABLE()

MyFrame::MyFrame( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxFrame( parent, id, title, position, size, style )
{
    CreateMyMenuBar();
    
    CreateMyToolBar();
    
    CreateStatusBar(1);
    SetStatusText( wxT("Welcome!") );
    
     // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
    SetMenuBar( MyMenuBarFunc() );
}

void MyFrame::CreateMyToolBar()
{
    wxToolBar *tb = CreateToolBar( wxTB_HORIZONTAL|wxNO_BORDER );
    
    MyToolBarFunc( tb );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnAbout( wxCommandEvent &event )
{
    wxMessageDialog dialog( this, wxT("Welcome to SuperApp 1.0\n(C)opyright Joe Hacker"),
        wxT("About SuperApp"), wxOK|wxICON_INFORMATION );
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

