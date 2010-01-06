/////////////////////////////////////////////////////////////////////////////
// Name:        derived.h
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifndef __derived_H__
#define __derived_H__

#ifdef __GNUG__
    #pragma interface "derived.h"
#endif

// Include wxWindows' headers

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

// Include private header

#include "derived_wdr.h"

//----------------------------------------------------------------------------
//   constants
//----------------------------------------------------------------------------

#define ID_ABOUT    100
#define ID_QUIT     101
#define ID_MYTEST   102

// WDR: class declarations

//----------------------------------------------------------------------------
// MyTextCtrl
//----------------------------------------------------------------------------

class MyTextCtrl: public wxTextCtrl
{
public:
    // constructors and destructors
    MyTextCtrl( wxWindow *parent, wxWindowID id = -1,
        const wxString &value = wxT(""),
        const wxPoint& pos = wxDefaultPosition,
        const wxSize& size = wxDefaultSize,
        long style = 0 );
    
    // WDR: method declarations for MyTextCtrl
    
private:
    // WDR: member variable declarations for MyTextCtrl
    
private:
    // WDR: handler declarations for MyTextCtrl
    void OnChar( wxKeyEvent &event );

private:
    DECLARE_EVENT_TABLE()
};

//----------------------------------------------------------------------------
// MyDialog
//----------------------------------------------------------------------------

class MyDialog: public wxDialog
{
public:
    // constructors and destructors
    MyDialog( wxWindow *parent, wxWindowID id, const wxString &title,
        const wxPoint& pos = wxDefaultPosition,
        const wxSize& size = wxDefaultSize,
        long style = wxDEFAULT_DIALOG_STYLE );
    
    // WDR: method declarations for MyDialog
    MyTextCtrl* GetTextctrl2()  { return (MyTextCtrl*) FindWindow( ID_TEXTCTRL2 ); }
    MyTextCtrl* GetTextctrl1()  { return (MyTextCtrl*) FindWindow( ID_TEXTCTRL1 ); }
    
    
private:
    // WDR: member variable declarations for MyDialog
    
private:
    // WDR: handler declarations for MyDialog
    void OnTest( wxCommandEvent &event );

private:
    DECLARE_EVENT_TABLE()
};

//----------------------------------------------------------------------------
// MyFrame
//----------------------------------------------------------------------------

class MyFrame: public wxFrame
{
public:
    // constructors and destructors
    MyFrame( wxWindow *parent, wxWindowID id, const wxString &title,
        const wxPoint& pos = wxDefaultPosition,
        const wxSize& size = wxDefaultSize,
        long style = wxDEFAULT_FRAME_STYLE );
    
private:
    // WDR: method declarations for MyFrame
    void CreateMyMenuBar();
    
private:
    // WDR: member variable declarations for MyFrame
    
private:
    // WDR: handler declarations for MyFrame
    void OnAbout( wxCommandEvent &event );
    void OnQuit( wxCommandEvent &event );
    void OnTest( wxCommandEvent &event );
    void OnCloseWindow( wxCloseEvent &event );
    
private:
    DECLARE_EVENT_TABLE()
};

//----------------------------------------------------------------------------
// MyApp
//----------------------------------------------------------------------------

class MyApp: public wxApp
{
public:
    MyApp();
    
    virtual bool OnInit();
    virtual int OnExit();
};

#endif
