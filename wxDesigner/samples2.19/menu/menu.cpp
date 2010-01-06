/////////////////////////////////////////////////////////////////////////////
// Name:        menu.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "menu.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "menu.h"

// WDR: class implementations

//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(wxID_ABOUT, MyFrame::OnAbout)
    EVT_MENU(wxID_EXIT, MyFrame::OnQuit)
    EVT_CLOSE(MyFrame::OnCloseWindow)
    EVT_MENU( ID_TEST1, MyFrame::OnTest1 )
    EVT_MENU_HIGHLIGHT( ID_TEST2, MyFrame::OnHighlightTest2 )
    EVT_UPDATE_UI( ID_TEST3, MyFrame::OnUpdateTest3 )
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
    SetMenuBar( MyMenuBarFunc() );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnUpdateTest3( wxUpdateUIEvent &event )
{
    event.Enable( FALSE );
}

void MyFrame::OnHighlightTest2( wxMenuEvent &event )
{
    SetStatusText( wxT("Hightlighted test1!!!") );
}

void MyFrame::OnTest1( wxCommandEvent &event )
{
    wxMessageDialog dialog( this, wxT("Test1 selected or unselected"),
        wxT("About SuperApp"), wxOK|wxICON_INFORMATION );
    dialog.ShowModal();
}

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

