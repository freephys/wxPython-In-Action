//----------------------------------------------------------------------------
// Name:         rad.cs
// Author:       XXXX
// Created:      XX/XX/XX
// Copyright:    
//----------------------------------------------------------------------------

using System;
using System.Drawing;
using wx;

// WDR: classes

public class MyDialog: Dialog
{
    public MyDialog(Window parent, int id, string title, Point pos, Size size, uint style)
        : base( parent, id, title, pos, size, style)
    {
        // WDR: dialog function MyDialogFunc for MyDialog
        radWdrClass.MyDialogFunc( this, true );
    
        // WDR: handler declarations for MyDialog
    }
    
    // WDR: methods for MyDialog
    
    public TextCtrl GetMyText() { return (TextCtrl) FindWindow( radWdrClass.ID_MY_TEXT ); }
    
    public SpinCtrl GetMyNumber() { return (SpinCtrl) FindWindow( radWdrClass.ID_MY_NUMBER ); }
    
    public override bool TransferDataToWindow()
    {
        MyFrame frame = (MyFrame) Parent;
        GetMyNumber().Value = frame.g_number;
        GetMyText().Value = frame.g_text;
        return true;
    }
    
    public override bool TransferDataFromWindow()
    {
        MyFrame frame = (MyFrame) Parent;
        frame.g_number = GetMyNumber().Value;
        frame.g_text = GetMyText().Value;
        return true;
    }
    
    // WDR: handler implementations for MyDialog

}

public class MyFrame: Frame
{
    int ID_TEST = 100;
    
    public int      g_number = 0;
    public string   g_text;

    public MyFrame(string title, Point pos, Size size )
        : base(title, pos, size)
    {
        CreateMyMenuBar();
        
        CreateStatusBar( 1 );
        SetStatusText( "Welcome to RAD!", 0);
        
        // insert main window here
        
        // WDR: handler declarations for MyFrame
        EVT_MENU( (int)MenuIDs.wxID_ABOUT, new EventListener(OnAbout) );
        EVT_MENU( ID_TEST, new EventListener(OnTest) );
        EVT_MENU( (int)MenuIDs.wxID_EXIT, new EventListener(OnQuit) );
        EVT_CLOSE( new EventListener(OnCloseWindow) );
    }
    
    // WDR: methods for MyFrame
    
    public void CreateMyMenuBar()
    {
        Menu file_menu = new Menu();
        file_menu.Append( (int)MenuIDs.wxID_ABOUT, "About...", "Program info" );
        file_menu.Append( ID_TEST, "Test dialog...", "Test RAD" );
        file_menu.Append( (int)MenuIDs.wxID_EXIT, "Quit...", "Quit program" );
        
        MenuBar menu_bar = new MenuBar();
        menu_bar.Append( file_menu, "File" );
        
        MenuBar = menu_bar;
    }
    
    // WDR: handler implementations for MyFrame
    
    public void OnTest(object sender, Event e)
    {
        MyDialog dialog = new MyDialog( this, -1, "Test dialog", 
            wxDefaultPosition, wxDefaultSize, (uint)wxDEFAULT_DIALOG_STYLE );
        dialog.ShowModal();
    }
    
    public void OnQuit(object sender, Event e)
    {
        Close();
    }
    
    public void OnAbout(object sender, Event e)
    {
        MessageDialog dialog = new MessageDialog( this, "Welcome to RAD sample\n(C)opyright Joe Hacker",
        "About RAD sample", Dialog.wxOK|Dialog.wxICON_INFORMATION );
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
        MyFrame frame = new MyFrame("RAD sample", new Point(50,50), new Size(450,340));
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
