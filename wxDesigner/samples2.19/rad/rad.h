/////////////////////////////////////////////////////////////////////////////
// Name:        rad.h
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifndef __rad_H__
#define __rad_H__

#if defined(__GNUG__) && !defined(NO_GCC_PRAGMA)
    #pragma interface "rad.h"
#endif

// Include wxWindows' headers

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "rad_wdr.h"

//----------------------------------------------------------------------------
//   constants
//----------------------------------------------------------------------------

#define ID_TEST     100

// WDR: class declarations

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
    wxSpinCtrl* GetMyNumber()  { return (wxSpinCtrl*) FindWindow( ID_MY_NUMBER ); }
    wxTextCtrl* GetMyText()  { return (wxTextCtrl*) FindWindow( ID_MY_TEXT ); }
    
    virtual bool TransferDataToWindow();
    virtual bool TransferDataFromWindow();
    
private:
    // WDR: member variable declarations for MyDialog
    
private:
    // WDR: handler declarations for MyDialog

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
    void OnTest( wxCommandEvent &event );
    void OnQuit( wxCommandEvent &event );
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
