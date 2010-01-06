#!/usr/bin/perl
#----------------------------------------------------------------------------
# Name:         notebook.pl
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

use strict;
use Wx;

do 'notebook_wdr.pl';

# constants

use vars qw($ID_TEST); $ID_TEST = 100;

# WDR: classes

package MyFrame;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::Frame);

use Wx::Event qw(EVT_MENU EVT_CLOSE EVT_SIZE EVT_UPDATE_UI);
use Wx qw(wxOK wxID_ABOUT wxID_EXIT wxICON_INFORMATION wxTB_HORIZONTAL wxNO_BORDER);

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );

    $this->CreateMyMenuBar();
    
    $this->CreateStatusBar( 1 );
    $this->SetStatusText( "Welcome!", 0);
    
    # insert main window here
    
    # WDR: handler declarations for MyFrame
    EVT_MENU( $this, wxID_ABOUT, \&OnAbout );
    EVT_MENU( $this, $main::ID_TEST, \&OnTest );
    EVT_MENU( $this, wxID_EXIT, \&OnQuit );
    EVT_CLOSE( $this, \&OnCloseWindow );
    
    $this;
}

# WDR: methods for MyFrame

sub CreateMyMenuBar {
    my( $this ) = shift;
    
    my( $file_menu ) = Wx::Menu->new();
    $file_menu->Append( wxID_ABOUT, "About...", "Program info" );
    $file_menu->Append( $main::ID_TEST, "Test...", "Test notebook" );
    $file_menu->Append( wxID_EXIT, "Quit...", "Quit program" );
    
    my( $menu_bar ) = Wx::MenuBar->new();
    $menu_bar->Append( $file_menu, "File" );
    
    $this->SetMenuBar( $menu_bar );
}

# WDR: handler implementations for MyFrame

sub OnAbout {
    my( $this, $event ) = @_;
    
    Wx::MessageBox( "Welcome to SuperApp 1.0\n(C)opyright Joe Hacker",
        "About SuperApp", wxOK|wxICON_INFORMATION, $this );
}

sub OnTest {
    my( $this, $event ) = @_;
    
    my( $dialog ) = Wx::Dialog->new( $this, -1, "About Minimal" );
    &main::NotebookFunc( $dialog, 1 );
    $dialog->CentreOnParent();
    $dialog->ShowModal();
}

sub OnQuit {
    my( $this, $event ) = @_;
    
    $this->Close(1);
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
    Wx::InitAllImageHandlers();
    
    my( $frame ) = MyFrame->new( undef, -1, "SuperApp", [20,20], [500,340] );
    $frame->Show(1);
    
    1;
}

package main;

my( $app ) = MyApp->new();
$app->MainLoop();

