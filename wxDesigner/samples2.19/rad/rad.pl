#!/usr/bin/perl
#----------------------------------------------------------------------------
# Name:         rad.pl
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

use strict;
use Wx;

do 'rad_wdr.pl';

# constants & variables

use vars qw($ID_TEST $g_text $g_number);
$ID_TEST = 100;
$g_text = "";
$g_number = 0;

# WDR: classes

package MyDialog;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::Dialog);

use Wx qw(wxID_OK wxID_CANCEL);

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );
    
    &main::MyDialogFunc( $this, 1 );
    
    $this->CentreOnParent();
    
    # WDR: handler declarations for MyDialog
    
    $this;
}

# WDR: methods for MyDialog

sub GetMyNumber {
    $_[0]->FindWindow( $main::ID_MY_NUMBER );
}

sub GetMyText {
    $_[0]->FindWindow( $main::ID_MY_TEXT );
}

# WDR: handler implementations for MyDialog


package MyFrame;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::Frame);

use Wx::Event qw(EVT_MENU EVT_CLOSE EVT_SIZE EVT_UPDATE_UI);
use Wx qw(wxID_OK wxOK wxICON_INFORMATION wxID_ABOUT wxID_EXIT);

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );

    $this->CreateMyMenuBar();
    
    $this->CreateStatusBar(1);
    $this->SetStatusText("Welcome to RAD!", 0);
    
    # insert main window here
    
    # WDR: handler declarations for MyFrame
    EVT_MENU($this, wxID_ABOUT, \&OnAbout);
    EVT_MENU($this, $main::ID_TEST, \&OnTest);
    EVT_MENU($this, wxID_EXIT, \&OnQuit);
    EVT_CLOSE($this, \&OnCloseWindow);
    
    $this;
}

# WDR: methods for MyFrame

sub CreateMyMenuBar {
    my( $this ) = shift;
    
    my( $file_menu ) = Wx::Menu->new();
    $file_menu->Append( $main::ID_TEST, "&Test dialog...\tCtrl-T", "Test dialog");
    $file_menu->Append( wxID_EXIT, "&Quit...\tCtrl-Q", "Quit program");
    
    my( $help_menu ) = Wx::Menu->new();
    $help_menu->Append( wxID_ABOUT, "&About...\tCtrl-A", "Program info");
    
    my( $menu_bar ) = Wx::MenuBar->new();
    $menu_bar->Append( $file_menu, "&File");
    $menu_bar->Append( $help_menu, "&Help");
    
    $this->SetMenuBar( $menu_bar );
}

# WDR: handler implementations for MyFrame

sub OnAbout {
    my( $this, $event ) = @_;
    
    Wx::MessageBox( "Welcome to RAD\n(C)opyright 2000 Robert Roebling",
        "About RAD", wxOK|wxICON_INFORMATION, $this );
}

sub OnTest {
    my( $this, $event ) = @_;
    
    my( $dialog ) = MyDialog->new( $this, -1, "Testing getters" );
    
    $dialog->GetMyNumber()->SetValue( $main::g_number );
    $dialog->GetMyText()->SetValue( $main::g_text );

    if( $dialog->ShowModal() == wxID_OK ) {
        $main::g_number = $dialog->GetMyNumber()->GetValue();
        $main::g_text = $dialog->GetMyText()->GetValue();
    }
}

sub OnQuit {
    my( $this, $event ) = @_;
    
    $this->Close( 1 );
}

sub OnCloseWindow {
    my( $this, $event ) = @_;
    
    $this->Destroy();
}

package MyApp;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::App);

sub OnInit {
    my( $this ) = @_;
    
    my( $frame ) = MyFrame->new( undef, -1, "RAD", [20,20], [500,340] );
    $frame->Show(1);
    
    1;
}

package main;

my( $app ) = MyApp->new();
$app->MainLoop();

