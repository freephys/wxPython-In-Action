# Important: This file should be placed in the Plug-ins directory if you want 
#            it to execute

import wx
import PaletteStore

import ArtProviderExample

# register art ids for use at design-time
PaletteStore.artProviderArtIds.extend(ArtProviderExample.ART_IDS)
# install the art provider in the IDE global environment
wx.ArtProvider.PushProvider(ArtProviderExample.ArtProviderExample())