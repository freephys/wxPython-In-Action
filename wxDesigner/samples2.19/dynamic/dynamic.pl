#!/usr/bin/perl
#----------------------------------------------------------------------------
# Name:         dynamic.pl
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

use strict;
use Wx;

do 'dynamic_wdr.pl';

# constants

# WDR: classes

package MyDialog;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::Dialog);

use Wx qw(wxID_OK wxID_CANCEL wxALL);

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );
    
    # WDR: dialog function MyDialogFunc for MyDialog
    $this->SetSizer( &main::MyDialogFunc( $this, 1 ) );

    $this->{sub_page} = &main::MyPageOneFunc( $this, 0, 0 );
    $this->{my_sizer}->Add( $this->{sub_page} );
    $this->GetSizer()->Fit( $this );
    
    $this->CentreOnParent();
    
    # WDR: handler declarations for MyDialog
    Wx::Event::EVT_CHOICE( $this, $main::ID_CHOICE, \&OnPage );
    
    $this;
}

# WDR: methods for MyDialog

# WDR: handler implementations for MyDialog

sub OnPage {
    my( $this, $event ) = @_;
    $this->{sub_page}->DeleteWindows();
    $this->{my_sizer}->RemoveSizer( $this->{sub_page} );
    if( $event->GetInt() == 1 ) {
        $this->{sub_page} = &main::MyPageTwoFunc( $this, 0, 0 );
    } else {
        $this->{sub_page} = &main::MyPageOneFunc( $this, 0, 0 );
    }
    $this->{my_sizer}->Add( $this->{sub_page} );
    $this->GetSizer()->Fit( $this );
}

package MyFrame;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::Frame);

use Wx::Event qw(EVT_MENU EVT_CLOSE EVT_SIZE EVT_UPDATE_UI);
use Wx qw(wxOK wxICON_INFORMATION wxTB_HORIZONTAL wxNO_BORDER wxID_EXIT wxID_ABOUT);
use Wx qw(wxDefaultPosition wxDefaultSize wxDEFAULT_DIALOG_STYLE wxRESIZE_BORDER );

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );

    $this->CreateMyMenuBar();
    
    $this->CreateStatusBar( 1 );
    $this->SetStatusText( "Welcome!", 0);
    
    # insert main window here
    
    # WDR: handler declarations for MyFrame
    EVT_MENU( $this, $main::ID_TEST, \&OnTest );
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

# WDR: handler implementations for MyFrame

sub OnTest {
    my( $this, $event ) = @_;
    
    my( $dialog ) = MyDialog->new( $this, -1, 'Test dialog', 
        wxDefaultPosition, wxDefaultSize, wxDEFAULT_DIALOG_STYLE|wxRESIZE_BORDER );
    $dialog->ShowModal();
}

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
    
    my( $frame ) = MyFrame->new( undef, -1, "SuperApp", [20,20], [500,340] );
    $frame->Show(1);
    
    1;
}

package main;

my( $app ) = MyApp->new();
$app->MainLoop();

