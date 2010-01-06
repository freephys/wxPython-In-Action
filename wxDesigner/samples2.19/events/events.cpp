/////////////////////////////////////////////////////////////////////////////
// Name:        events.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "events.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "events.h"

// WDR: class implementations

//----------------------------------------------------------------------------
// MyDialog
//----------------------------------------------------------------------------

// WDR: event table for MyDialog

BEGIN_EVENT_TABLE(MyDialog,wxDialog)
    EVT_SLIDER( ID_SLIDER, MyDialog::OnSlider )
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

void MyDialog::OnSlider( wxCommandEvent &event )
{
   GetGauge()->SetValue( GetSlider()->GetValue() );
   
   // GetGauge()->SetValue( event.GetInt() );
}


//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(ID_ABOUT, MyFrame::OnAbout)
    EVT_MENU(ID_QUIT, MyFrame::OnQuit)
    EVT_MENU(ID_TEST, MyFrame::OnTest)
    EVT_CLOSE(MyFrame::OnCloseWindow)
END_EVENT_TABLE()

MyFrame::MyFrame( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxFrame( parent, id, title, position, size, style )
{
    CreateMyMenuBar();
    
    CreateStatusBar(1);
    SetStatusText( wxT("Welcome to Events!") );
    
     // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
#ifdef __WXMAC__
    wxApp::s_macAboutMenuItemId = ID_ABOUT;
#endif

    wxMenu *file_menu = new wxMenu;
    file_menu->Append( ID_ABOUT, wxT("About..."), wxT("Program info") );
    file_menu->Append( ID_TEST, wxT("Test dialog..."), wxT("Test dialog") );
    file_menu->Append( ID_QUIT, wxT("Quit..."), wxT("Quit program") );
    
    wxMenuBar *menu_bar = new wxMenuBar();
    menu_bar->Append( file_menu, wxT("File") );
    
    SetMenuBar( menu_bar );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnAbout( wxCommandEvent &event )
{
    wxMessageDialog dialog( this, wxT("Welcome to Events\n(C)opyright 2000 Robert Roebling"),
        wxT("About Events"), wxOK|wxICON_INFORMATION );
    dialog.ShowModal();
}

void MyFrame::OnTest( wxCommandEvent &event )
{
    MyDialog dialog( this, -1, wxT("Events") );
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
    MyFrame *frame = new MyFrame( NULL, -1, wxT("Events"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

