//-----------------------------------------------------------------------------
// C# source generated by wxDesigner from file: minimal.wdr
// Do not modify this file, all changes will be lost!
//-----------------------------------------------------------------------------

using System;
using System.Drawing;
using wx;

public class minimalWdrClass
{
   // Window functions

    public const int ID_TEXT = 10000;
    public const int ID_LINE = 10001;

    public static Sizer MyDialogFunc( Window parent )
    { return MyDialogFunc( parent, true, true ); }

    public static Sizer MyDialogFunc( Window parent, bool call_fit )
    { return MyDialogFunc( parent, call_fit, true ); }

    public static Sizer MyDialogFunc( Window parent, bool call_fit, bool set_sizer )
    {
        BoxSizer item0 = new BoxSizer( Orientation.wxVERTICAL );
    
        StaticBox item2 = new StaticBox( parent, -1, "Copyright" );
        item2.Font = new wx.Font( 16, wx.FontFamily.wxROMAN, wx.FontStyle.wxNORMAL, wx.FontWeight.wxNORMAL );
        StaticBoxSizer item1 = new StaticBoxSizer( item2, Orientation.wxVERTICAL );
    
        StaticText item3 = new StaticText( parent, ID_TEXT, "Copyright 2002 T. Coon. 1000,- �.", Window.wxDefaultPosition, Window.wxDefaultSize, 0 );
        item3.ForegroundColour = Colour.wxBLUE;
        item3.Font = new wx.Font( 16, wx.FontFamily.wxROMAN, wx.FontStyle.wxNORMAL, wx.FontWeight.wxNORMAL );
        item1.Add( item3, 0, Alignment.wxALIGN_CENTER|Direction.wxALL, 5 );

        item0.Add( item1, 0, Stretch.wxGROW|Alignment.wxALIGN_CENTER_VERTICAL|Direction.wxALL, 5 );

        StaticLine item4 = new StaticLine( parent, ID_LINE, Window.wxDefaultPosition, new Size(20,-1), StaticLine.wxLI_HORIZONTAL );
        item0.Add( item4, 0, Stretch.wxGROW|Alignment.wxALIGN_CENTER_VERTICAL|Direction.wxALL, 5 );

        Button item5 = new Button( parent, Window.wxID_OK, "OK", Window.wxDefaultPosition, Window.wxDefaultSize, 0 );
        item0.Add( item5, 0, Alignment.wxALIGN_CENTER|Direction.wxALL, 5 );

        if (set_sizer)
        {
            parent.SetSizer( item0 );
            if (call_fit)
                item0.SetSizeHints( parent );
        }
        
        return item0;
    }

    // Menubar functions

    // Toolbar functions

    // Bitmap functions

}

// End of generated file
