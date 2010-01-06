/////////////////////////////////////////////////////////////////////////////
// Name:        grid.h
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifndef __grid_H__
#define __grid_H__

#ifdef __GNUG__
    #pragma interface "grid.h"
#endif

// Include wxWindows' headers

#ifndef WX_PRECOMP
    #include <wx/wx.h>
#endif
#include <wx/grid.h>

#include "grid_wdr.h"

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
    
private:
    // WDR: member variable declarations for MyDialog
    
private:
    // WDR: handler declarations for MyDialog

private:
    DECLARE_EVENT_TABLE()
};

//----------------------------------------------------------------------------
// MyGrid
//----------------------------------------------------------------------------

class MyGrid: public wxGrid
{
public:
    // constructors and destructors
    MyGrid( wxWindow *parent, wxWindowID id = -1,
        const wxPoint& pos = wxDefaultPosition,
        const wxSize& size = wxDefaultSize,
        long style = 0 );
    
    // WDR: method declarations for MyGrid
    
private:
    // WDR: member variable declarations for MyGrid
    
private:
    // WDR: handler declarations for MyGrid
    void OnRightClick( wxGridEvent &event );

private:
    DECLARE_CLASS(MyGrid)
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
    void OnGrid( wxCommandEvent &event );
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
