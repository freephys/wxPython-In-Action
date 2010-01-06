/////////////////////////////////////////////////////////////////////////////
// Name:        notebook.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma implementation "notebook.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "notebook.h"
#include "notebook_wdr.h"

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
    EVT_MENU(ID_TEST, MyFrame::OnTest)
    EVT_MENU(wxID_EXIT, MyFrame::OnQuit)
    EVT_CLOSE(MyFrame::OnCloseWindow)
END_EVENT_TABLE()

MyFrame::MyFrame( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxFrame( parent, id, title, position, size, style )
{
    CreateMyMenuBar();
    
    CreateStatusBar(1);
    SetStatusText( wxT("Welcome to Notebook!") );
    
    SetIcon(wxICON(mondrian));
    
     // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
    wxMenu *file_menu = new wxMenu;
    file_menu->Append( wxID_ABOUT, wxT("About..."), wxT("Program info") );
    file_menu->Append( ID_TEST, wxT("Test dialog..."), wxT("Test dialog") );
    file_menu->Append( wxID_EXIT, wxT("Quit..."), wxT("Quit program") );
    
    wxMenuBar *menu_bar = new wxMenuBar();
    menu_bar->Append( file_menu, wxT("File") );
    
    SetMenuBar( menu_bar );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnAbout( wxCommandEvent &event )
{
    wxMessageDialog dialog( this, wxT("Welcome to Notebook\n(C)opyright 2000 Robert Roebling"),
        wxT("About Notebook"), wxOK|wxICON_INFORMATION );
    dialog.ShowModal();
}

void MyFrame::OnTest( wxCommandEvent &event )
{
    wxDialog dialog( this, -1, wxT("Notebook pages"), wxDefaultPosition );
    NotebookFunc( &dialog, TRUE );
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
    MyFrame *frame = new MyFrame( NULL, -1, wxT("Notebook"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

