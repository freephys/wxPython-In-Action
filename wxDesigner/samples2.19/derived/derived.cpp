/////////////////////////////////////////////////////////////////////////////
// Name:        derived.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "derived.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "derived.h"

// Include icon header

#if defined(__WXGTK__) || defined(__WXMOTIF__)
    #include "mondrian.xpm"
#endif

// WDR: class implementations

//----------------------------------------------------------------------------
// MyTextCtrl
//----------------------------------------------------------------------------

// WDR: event table for MyTextCtrl

BEGIN_EVENT_TABLE(MyTextCtrl,wxTextCtrl)
    EVT_CHAR( MyTextCtrl::OnChar )
END_EVENT_TABLE()

MyTextCtrl::MyTextCtrl( wxWindow *parent, wxWindowID id,
    const wxString &value,
    const wxPoint &position, const wxSize& size, long style ) :
    wxTextCtrl( parent, id, value, position, size, style )
{
}

// WDR: handler implementations for MyTextCtrl

void MyTextCtrl::OnChar(wxKeyEvent &event)
{
    // do something special here
    wxBell();

    event.Skip();
}

//----------------------------------------------------------------------------
// MyDialog
//----------------------------------------------------------------------------

// WDR: event table for MyDialog

BEGIN_EVENT_TABLE(MyDialog,wxDialog)
    EVT_BUTTON( ID_TEST, MyDialog::OnTest )
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

void MyDialog::OnTest( wxCommandEvent &event )
{
    MyTextCtrl *text1 = GetTextctrl1();
    MyTextCtrl *text2 = GetTextctrl2();
    wxString text = text1->GetValue();
    text2->SetValue( text );
}

//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(ID_ABOUT, MyFrame::OnAbout)
    EVT_MENU(ID_MYTEST, MyFrame::OnTest)
    EVT_MENU(ID_QUIT, MyFrame::OnQuit)
    EVT_CLOSE(MyFrame::OnCloseWindow)
END_EVENT_TABLE()

MyFrame::MyFrame( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxFrame( parent, id, title, position, size, style )
{
    CreateMyMenuBar();
    
    CreateStatusBar(1);
    SetStatusText( wxT("Welcome to Derived!") );
    
    SetIcon(wxICON(mondrian));
    
    // insert main window here
}

void MyFrame::CreateMyMenuBar()
{
#ifdef __WXMAC__
    wxApp::s_macAboutMenuItemId = ID_ABOUT;
#endif

    wxMenu *file_menu = new wxMenu;
    file_menu->Append( ID_ABOUT, wxT("About..."), wxT("Program info") );
    file_menu->Append( ID_MYTEST, wxT("Test dialog..."), wxT("Test dialog") );
    file_menu->Append( ID_QUIT, wxT("Quit..."), wxT("Quit program") );
    
    wxMenuBar *menu_bar = new wxMenuBar();
    menu_bar->Append( file_menu, wxT("File") );
    
    SetMenuBar( menu_bar );
}

// WDR: handler implementations for MyFrame

void MyFrame::OnAbout( wxCommandEvent &event )
{
    wxMessageDialog dialog( this, wxT("Welcome to Derived\n(C)opyright 2000 Robert Roebling"),
        wxT("About Derived"), wxOK|wxICON_INFORMATION );
    dialog.ShowModal();
}

void MyFrame::OnTest( wxCommandEvent &event )
{
    MyDialog dialog( this, -1, wxT("Derived control") );
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
    MyFrame *frame = new MyFrame( NULL, -1, wxT("Derived"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

