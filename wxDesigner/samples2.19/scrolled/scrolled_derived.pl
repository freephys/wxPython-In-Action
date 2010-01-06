#!/usr/bin/perl
#----------------------------------------------------------------------------
# Name:         scrolled_derived.pl
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

use Wx;
use strict;

# WDR: classes

package MyScrolledWindow;

use strict;
use vars qw(@ISA);

@ISA=qw(Wx::ScrolledWindow);

use Wx qw(wxICON_INFORMATION wxOK);

sub new {
    my( $class ) = shift;
    my( $this ) = $class->SUPER::new( @_ );
    
    # WDR: handler declarations for MyScrolledWindow
    Wx::Event::EVT_LEFT_DOWN( $this, \&OnLeftDown );
    Wx::Event::EVT_PAINT( $this, \&OnPaint );
    
    $this;
}

# WDR: methods for MyScrolledWindow

# WDR: handler implementations for MyScrolledWindow

sub OnLeftDown {
    my( $this, $event ) = @_;
    
    my( $dialog ) = Wx::MessageDialog->new( $this, "Left click.", "Test", wxOK|wxICON_INFORMATION );
    $dialog->ShowModal();
    $dialog->Destroy();
}

sub OnPaint {
    my( $this, $event ) = @_;
    my( $dc ) = Wx::PaintDC->new( $this );
    $this->PrepareDC( $dc );
    $dc->DrawLine( 0,0,300,300 );
}

