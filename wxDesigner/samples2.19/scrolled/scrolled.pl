#!/usr/bin/perl
#----------------------------------------------------------------------------
# Name:         scrolled.pl
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

use strict;
use Wx;

do 'scrolled_wdr.pl';

# constants

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
    
    # WDR: handler declarations for MyDialog
    
    $this;
}

# WDR: methods for MyDialog

# WDR: handler implementations for MyDialog


package MyFrame;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::Frame);

use Wx::Event qw(EVT_MENU EVT_CLOSE EVT_SIZE EVT_UPDATE_UI);

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );

    $this->CreateMyMenuBar();
    
    $this->CreateStatusBar( 1 );
    $this->SetStatusText( "Welcome!", 0);
    
    # insert main window here
    
    # WDR: handler declarations for MyFrame
    EVT_MENU( $this, $main::ID_SCROLLED, \&OnScrolled );
    EVT_MENU( $this, $main::ID_QUIT, \&OnQuit );
    EVT_CLOSE( $this, \&OnCloseWindow );
    
    $this;
}

# WDR: methods for MyFrame

sub CreateMyMenuBar {
    my( $this ) = shift;
    
    $this->SetMenuBar( &main::MyMenuBarFunc() );
}

# WDR: handler implementations for MyFrame

sub OnScrolled {
    my( $this, $event ) = @_;
    
    my( $dialog ) = MyDialog->new( $this, -1, "Testing getters" );
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
    
    my( $frame ) = MyFrame->new( undef, -1, "SuperApp", [20,20], [500,340] );
    $frame->Show(1);
    
    1;
}

package main;

my( $app ) = MyApp->new();
$app->MainLoop();

