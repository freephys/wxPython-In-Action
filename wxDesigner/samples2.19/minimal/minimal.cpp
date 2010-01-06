/////////////////////////////////////////////////////////////////////////////
// Name:        minimal.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma implementation "minimal.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "minimal.h"

#include "minimal_wdr.h"

// Include icon header

#if defined(__WXGTK__) || defined(__WXMOTIF__)
    #include "mondrian.xpm"
#endif

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
    
    CreateStatusBar(1);
    SetStatusText( wxT("Welcome to minimal!") );

#ifndef __WXMAC__    
    SetIcon(wxICON(mondrian));
#endif

     // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
    wxMenu *file_menu = new wxMenu;
    file_menu->Append( wxID_EXIT, wxT("&Quit...\tCtrl-Q"), wxT("Quit program") );
    
    wxMenu *help_menu = new wxMenu;
    help_menu->Append( wxID_ABOUT, wxT("&About...\tCtrl-A"), wxT("Program info") );
    
    wxMenuBar *menu_bar = new wxMenuBar();
    menu_bar->Append( file_menu, wxT("&File") );
    menu_bar->Append( help_menu, wxT("&Help") );
    
    SetMenuBar( menu_bar );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnAbout( wxCommandEvent &event )
{
    wxDialog dialog( this, -1, wxT("About Minimal"), wxDefaultPosition );
    MyDialogFunc( &dialog, TRUE );
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
    MyFrame *frame = new MyFrame( NULL, -1, wxT("Minimal"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

