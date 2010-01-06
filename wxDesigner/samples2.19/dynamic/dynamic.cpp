/////////////////////////////////////////////////////////////////////////////
// Name:        dynamic.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "dynamic.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "dynamic.h"

// WDR: class implementations

//----------------------------------------------------------------------------
// MyDialog
//----------------------------------------------------------------------------

// WDR: event table for MyDialog

BEGIN_EVENT_TABLE(MyDialog,wxDialog)
    EVT_CHOICE( ID_CHOICE, MyDialog::OnPage )
END_EVENT_TABLE()

MyDialog::MyDialog( wxWindow *parent, wxWindowID id, const wxString &title,
    const wxPoint &position, const wxSize& size, long style ) :
    wxDialog( parent, id, title, position, size, style|wxRESIZE_BORDER )
{
    // WDR: dialog function MyDialogFunc for MyDialog
    MyDialogFunc( this, TRUE ); 
    
    m_subPage = MyPageOneFunc( this, FALSE, FALSE );
    my_sizer->Add( m_subPage );
    
    GetSizer()->Fit( this );
    
    CentreOnParent();
}

// WDR: handler implementations for MyDialog

void MyDialog::OnPage( wxCommandEvent &event )
{
    m_subPage->DeleteWindows();
    my_sizer->Remove( m_subPage );
    
    if (event.GetInt() == 1)
        m_subPage = MyPageTwoFunc( this, FALSE, FALSE );
    else
        m_subPage = MyPageOneFunc( this, FALSE, FALSE );
    my_sizer->Add( m_subPage );
    
    GetSizer()->Fit( this );
}

//------------------------------------------------------------------------------
// MyFrame
//------------------------------------------------------------------------------

// WDR: event table for MyFrame

BEGIN_EVENT_TABLE(MyFrame,wxFrame)
    EVT_MENU(wxID_ABOUT, MyFrame::OnAbout)
    EVT_MENU(wxID_EXIT, MyFrame::OnQuit)
    EVT_CLOSE(MyFrame::OnCloseWindow)
    EVT_MENU(ID_TEST, MyFrame::OnTest )
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

void MyFrame::OnTest( wxCommandEvent &event )
{
    MyDialog dialog( this, -1, wxT("Test dialog") );
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
    MyFrame *frame = new MyFrame( NULL, -1, wxT("Dynamic"), wxPoint(20,20), wxSize(500,340) );
    frame->Show( TRUE );
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

