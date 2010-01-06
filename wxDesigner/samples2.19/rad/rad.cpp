/////////////////////////////////////////////////////////////////////////////
// Name:        rad.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma implementation "rad.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "rad.h"

// Include icon header

#if defined(__WXGTK__) || defined(__WXMOTIF__)
    #include "mondrian.xpm"
#endif

//----------------------------------------------------------------------------
// global data
//----------------------------------------------------------------------------

wxString   g_text;
int        g_number = 0;

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
    MyDialogFunc( this, TRUE );
    
    CentreOnParent();
}

bool MyDialog::TransferDataToWindow()
{
    // The IDs of the two controls are ID_MY_NUMBER and ID_MY_TEXT.
    // wxDesigner has added two getters (names see below) and we
    // use these to set the values upon startup and to retrieve the
    // values when closing the dialog (next method).

    GetMyNumber()->SetValue( g_number );
    GetMyText()->SetValue( g_text );

    return TRUE;
}

bool MyDialog::TransferDataFromWindow()
{
    g_number = GetMyNumber()->GetValue();
    g_text = GetMyText()->GetValue();

    return TRUE;
}

// WDR: handler implementations for MyDialog


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
    SetStatusText( wxT("Welcome to RAD!") );
    
#ifndef __WXMAC__
    SetIcon(wxICON(mondrian));
#endif
    
     // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
    wxMenu *file_menu = new wxMenu;
    file_menu->Append( ID_TEST, wxT("&Test dialog...\tCtrl-T"), wxT("Test dialog") );
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
    wxMessageDialog dialog( this, wxT("Welcome to RAD\n(C)opyright 2000 Robert Roebling"),
        wxT("About RAD"), wxOK|wxICON_INFORMATION );
    dialog.ShowModal();
}

void MyFrame::OnTest( wxCommandEvent &event )
{
    MyDialog dialog( this, -1, wxT("Test Getters") );
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
    MyFrame *frame = new MyFrame( NULL, -1, wxT("Testing RAD"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

