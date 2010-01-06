#!/usr/bin/perl
#----------------------------------------------------------------------------
# Name:         toolbar.pl
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

use strict;
use Wx;

do 'toolbar_wdr.pl';
die $@ if $@;

# constants

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
    
    $this->CreateMyToolBar();
    
    $this->CreateStatusBar( 1 );
    $this->SetStatusText( "Welcome!", 0);
    
    # insert main window here
    
    # WDR: handler declarations for MyFrame
    EVT_MENU( $this, wxID_ABOUT, \&OnAbout );
    EVT_MENU( $this, wxID_EXIT, \&OnQuit );
    EVT_CLOSE( $this, \&OnCloseWindow );
    
    $this;
}

# WDR: methods for MyFrame

sub CreateMyMenuBar {
    my( $this ) = shift;
    
    $this->SetMenuBar( &main::MyMenuBarFunc() );
}

sub CreateMyToolBar {
    my( $this ) = shift;
    
    my( $tb ) = $this->CreateToolBar(wxTB_HORIZONTAL|wxNO_BORDER);
    
    &main::MyToolBarFunc( $tb );
}

# WDR: handler implementations for MyFrame

sub OnAbout {
    my( $this, $event ) = @_;
    
    Wx::MessageBox( "Welcome to SuperApp 1.0\n(C)opyright Joe Hacker",
        "About SuperApp", wxOK|wxICON_INFORMATION, $this );
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

