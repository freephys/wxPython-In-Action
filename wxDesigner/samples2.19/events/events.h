/////////////////////////////////////////////////////////////////////////////
// Name:        events.h
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifndef __events_H__
#define __events_H__

#ifdef __GNUG__
    #pragma interface "events.h"
#endif

// Include wxWindows' headers

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif

#include "events_wdr.h"

//----------------------------------------------------------------------------
//   constants
//----------------------------------------------------------------------------

#define ID_ABOUT    100
#define ID_QUIT     101
#define ID_TEST     102

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
    wxGauge* GetGauge()  { return (wxGauge*) FindWindow( ID_GAUGE ); }
    wxSlider* GetSlider()  { return (wxSlider*) FindWindow( ID_SLIDER ); }
    
private:
    // WDR: member variable declarations for MyDialog
    
private:
    // WDR: handler declarations for MyDialog
    void OnSlider( wxCommandEvent &event );

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
