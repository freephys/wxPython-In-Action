//----------------------------------------------------------------------------
// Name:         toolbar.cs
// Author:       XXXX
// Created:      XX/XX/XX
// Copyright:    
//----------------------------------------------------------------------------

using System;
using System.Drawing;
using wx;

// WDR: classes

public class MyFrame: Frame
{
    public MyFrame(string title, Point pos, Size size )
        : base(title, pos, size)
    {
        CreateMyMenuBar();
        
        CreateMyToolBar();
        
        CreateStatusBar( 1 );
        SetStatusText( "Welcome!", 0);
        
        // insert main window here
        
        // WDR: handler declarations for MyFrame
        EVT_MENU( (int)MenuIDs.wxID_ABOUT, new EventListener(OnAbout) );
        EVT_MENU( (int)MenuIDs.wxID_EXIT, new EventListener(OnQuit) );
        EVT_CLOSE( new EventListener(OnCloseWindow) );
    }
    
    // WDR: methods for MyFrame
    
    public void CreateMyMenuBar()
    {
        MenuBar = toolbarWdrClass.MyMenuBarFunc();
    }
    
    public void CreateMyToolBar()
    {
        ToolBar tb = CreateToolBar(Window.wxNO_BORDER);
        toolbarWdrClass.MyToolBarFunc( tb );
    }
    
    // WDR: handler implementations for MyFrame
    
    public void OnQuit(object sender, Event e)
    {
        Close();
    }
    
    public void OnAbout(object sender, Event e)
    {
        MessageDialog dialog = new MessageDialog( this, "Welcome to SuperApp 1.0\n(C)opyright Joe Hacker",
        "About SuperApp", Dialog.wxOK|Dialog.wxICON_INFORMATION );
        dialog.ShowModal();
    }
    
    public void OnCloseWindow(object sender, Event e)
    {
        Destroy();
    }
    
}

public class MyApp: App
{
    //---------------------------------------------------------------------
    
    public override bool OnInit()
    {
        MyFrame frame = new MyFrame("wxWindows App", new Point(50,50), new Size(450,340));
        frame.Show(true);
        
        return true;
    }
    
    //---------------------------------------------------------------------
    
    [STAThread]
    static void Main()
    {
        MyApp app = new MyApp();
        app.Run();
    }

}
