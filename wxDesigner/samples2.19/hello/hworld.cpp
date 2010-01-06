/////////////////////////////////////////////////////////////////////////////
// Name:        hworld.cpp
// Author:      XX
// Created:     XX/XX/XX
// Copyright:   
/////////////////////////////////////////////////////////////////////////////

#ifdef __GNUG__
    #pragma implementation "hworld.h"
#endif

// For compilers that support precompilation
#include "wx/wxprec.h"

#ifdef __BORLANDC__
    #pragma hdrstop
#endif

// Include private headers
#include "hworld.h"
#include "hworld_wdr.h"

// WDR: class implementations

//------------------------------------------------------------------------------
// MyApp
//------------------------------------------------------------------------------

IMPLEMENT_APP(MyApp)

MyApp::MyApp()
{
}

bool MyApp::OnInit()
{
    wxDialog dialog( NULL, -1, wxT("Hello World"), wxDefaultPosition );
    MyDialogFunc( &dialog, true );
    dialog.CentreOnScreen();
    dialog.ShowModal();
    
    return TRUE;
}

int MyApp::OnExit()
{
    return 0;
}

