#!/usr/bin/python

"""
__version__ = "$Revision: 1.9 $"
__date__ = "$Date: 2004/11/07 18:13:12 $"
"""

from PythonCard import dialog, model
from types import TupleType, ListType, StringTypes, NoneType
import pprint

# Music list borrowed from wxListCtrl demo (Removed long song titles)
demolists = [(('List'),('Item 1', 'Item 2', 'Item 3','Item 4','Item 5','Hit demo button again')),
             (('Artist','Title','Genre'),
              (("Bad English", "The Price Of Love", "Rock"),
               ("George Michael", "Praying For Time", "Rock"),
               ("Gloria Estefan", "Here We Are", "Rock"),
               ("Linda Ronstadt", "Don't Know Much", "Rock"),
               ("Paul Young", "Oh Girl", "Rock"),
               ("Paula Abdul", "Opposites Attract", "Rock"),
               ("Richard Marx", "Should've Known Better", "Rock"),
               ("Rod Stewart", "Forever Young", "Rock"),
               ("Roxette", "Dangerous", "Rock"),
               ("Sheena Easton", "The Lover In Me", "Rock"),
               ("Sinead O'Connor", "Nothing Compares 2 U", "Rock"),
               ("Stevie B.", "Because I Love You", "Rock"),
               ("Taylor Dayne", "Love Will Lead You Back", "Rock"),
               ("The Bangles", "Eternal Flame", "Rock"),
               ("Wilson Phillips", "Release Me", "Rock"),
               ("Billy Joel", "Blonde Over Blue", "Rock"),
               ("Billy Joel", "Famous Last Words", "Rock"),
               ("Billy Joel", "The River Of Dreams", "Rock"),
               ("Billy Joel", "Two Thousand Years", "Rock"),
               ("Janet Jackson", "Alright", "Rock"),
               ("Janet Jackson", "Black Cat", "Rock"),
               ("Janet Jackson", "Come Back To Me", "Rock"),
               ("Janet Jackson", "Escapade", "Rock"),
               ("Janet Jackson", "Miss You Much", "Rock"),
               ("Janet Jackson", "Rhythm Nation", "Rock"),
               ("Janet Jackson", "State Of The World", "Rock"),
               ("Janet Jackson", "The Knowledge", "Rock"),
               ("Spyro Gyra", "End of Romanticism", "Jazz"),
               ("Spyro Gyra", "Heliopolis", "Jazz"),
               ("Spyro Gyra", "Jubilee", "Jazz"),
               ("Spyro Gyra", "Little Linda", "Jazz"),
               ("Spyro Gyra", "Morning Dance", "Jazz"),
               ("Spyro Gyra", "Song for Lorraine", "Jazz"),
               ("Yes", "Owner Of A Lonely Heart", "Rock"),
               ("Yes", "Rhythm Of Love", "Rock"),
               ("Cusco", "Dream Catcher", "New Age"),
               ("Cusco", "Geronimos Laughter", "New Age"),
               ("Cusco", "Ghost Dance", "New Age"),
               ("Blue Man Group", "Drumbone", "New Age"),
               ("Blue Man Group", "Endless Column", "New Age"),
               ("Blue Man Group", "Klein Mandelbrot", "New Age"),
               ("Kenny G", "Silhouette", "Jazz"),
               ("Sade", "Smooth Operator", "Jazz"),
               ("David Arkenstone", "Stepping Stars", "New Age"),
               ("David Arkenstone", "Carnation Lily Lily Rose", "New Age"),
               ("David Lanz", "Behind The Waterfall", "New Age"),
               ("David Lanz", "Cristofori's Dream", "New Age"),
               ("David Lanz", "Heartsounds", "New Age"),
               ("David Lanz", "Leaves on the Seine", "New Age"),
               ("William Volkman","Hit demo button again","Unclassified")))]

"""
The Multicolumn list component is based on the wxListCtrl.
The implementation here allows either single column mode or multi-column mode.
Some methods have been added to allow simple replacement of the List component
(which is based on the wxListBox) this is done because we had the requirement
to display 3000 to 10000 items and the wxListBox will can only handle about
100 items per second (on a 663 MHz PIII system) whereas the wxListCtrl will
load about 1000 items per second.

The multicolumn list includes the mixins wxColumnSorterMixin (click on a
column heading and it sorts by that column) and wxListCtrlAutoWidthMixin
(resizes the last column to fill remaining space).  A side effect of this
is that the SetItemData method is *NOT* available to your application
(the ItemData is set to the index of the item in the list).

Pythoncard specific methods:

Clear(): Removes all items from the list.

GetCount(): Returns the number of items in the list.

GetColumnHeadings(): Returns a list of the column headings.

GetColumnHeadingInfo(): Returns a list of lists of column information consisting of
                      column heading text
                      specific size (or wx_LIST_AUTOSIZE if not specified on creation)
                      column alignment.

GetListCtrl():  Used if you want to ignore the Pythoncard interface and
              directly work with the wxListCtrl widget.

GetSelectedItems(): Returns a list of items in the list (either strings for
                  single column lists or a list of the text in each column).

getStringSelection(): same as GetSelectedItems

Append(aList):  Inserts items at end of list

InsertItems(aList, pos):  Inserts items at a particular position in a list, existing items are moved down.
                          Negative offsets are interpreted to be from the end of the list.

SetColumnHeadings(aList):  A list of strings which are the column headings or a list of
                    lists containing the same information as returned by GetColumnHeadingInfo.

GetItemDataMap():  This returns the dictionary, indexed by row number, of the data in the list,
                   (mostly reserved for wxColumnSorterMixin use however here to facilitate
                   replacement of the SetItemData method).
SetItemDataMap(aDict):  The wxColumnSorterMixin uses this to control column sorting. It contains
                        a dictionary object, keyed on item number, which contain the data
                        within the list item.

SetSelection(pos):  Selects the item in the list indexed by item number.

SetStringSelection(aString):  Selects the first item that it finds that matches the string.
                              For multicolumn lists only the first column is examined
                              (this is what the wxListCtrl does by default). Note that
                              this uses exact matching.

Additionally you can set the contents of the list by assigning a list to the 'items'
attribute or retrieve the contents of the list by referencing the 'items' attribute.

Notes:
1. Setting the Column Headings will clear the list so always set the headings before
you add your list data.

2. When assigning to 'items', the number of columns is determined by the first element
in the list or tuple that you pass in.  If there is a difference from the number of column
headings that have been set, the number of columns will be either be reduced (in the case
that the first item is shorter in length) or additional columns will be added with
their column number as the heading (in the case that it is larger).  Subsequent
items in the insertion list with either be truncated or padded with spaces to match the
length of the first item.

3. The SetItemData method is reserved for use by the column sorting mixin.
"""

class MulticolumnExample(model.Background):

    def on_initialize(self, event):
        """
        This method is the PythonCard equivalent to a constructor or __init__ method.
        We initialize our list of items to an empty list.
        """
        self.demolists = demolists
        self.demoidx = -1
        self.listcache = []
        self.listcacheidx = 0

    def on_appendButton_mouseClick(self, event):
        self._save_current_list()
        wildcard = "CSV files (*.csv)|*.csv|Text files (*.txt;*.log)|*.txt;*.log|All Files (*.*)|*.*"
        result = dialog.fileDialog(self, 'Open', '', '', wildcard )
        if not result.accepted:
            pprint.pprint(result)
            return
        for fn in result.paths:
            lines = open(fn, 'r').read().strip().split('\n')
            items = [x.split(',') for x in lines]
            self.components.theList.Append(items)

    def on_clearButton_mouseClick(self, event):
        self.components.theList.Clear()

    def on_demoButton_mouseClick(self, event):
        self._save_current_list()
        self.demoidx = self.demoidx + 1
        if self.demoidx >= len(self.demolists):
            self.demoidx = 0
        self.components.theList.columnHeadings = self.demolists[self.demoidx][0]
        self.components.theList.items = self.demolists[self.demoidx][1]
        self.components.countArea.text = str(self.components.theList.GetCount())
        if self.demoidx == 0:
            self.components.theList.SetSelection(self.components.theList.GetCount()-1)
        elif self.demoidx == 1:
            idx = self.components.theList.SetStringSelection('William Volkman')
            if idx >= 0:
                self.components.theList.EnsureVisible(idx)

    def on_exitButton_mouseClick(self, event):
        self.close()

    def on_loadButton_mouseClick(self, event):
        """Load the list with the contents of a CSV file.
        The first row is assumed to be column headings.
        Suggestion: replace this simple CSV hack with one of the packages
        designed for this purpose."""
        self._save_current_list()
        wildcard = "CSV files (*.csv)|*.csv|Text files (*.txt;*.log)|*.txt;*.log|All Files (*.*)|*.*"
        result = dialog.fileDialog(self, 'Open', '', '', wildcard )
        if not result.accepted:
            pprint.pprint(result)
            return
        items = []
        for fn in result.paths:
            lines = open(fn, 'r').read().strip().split('\n')
            items.extend([x.split(',') for x in lines])
        if len(items) < 2:
            return
        self.components.theList.columnHeadings = items[0]
        self.components.theList.items = items[1:]

    def on_nextButton_mouseClick(self, event):
        self._forward_in_cache()

    def on_prevButton_mouseClick(self, event):
        self._backward_in_cache()

    def on_swapButton_mouseClick(self, event):
        if len(self.listcache) < 1:
            return
        headings = self.components.theList.columnHeadings
        items = self.components.theList.items
        self.components.theList.columnHeadings = self.listcache[self.listcacheidx][0]
        self.components.theList.items = self.listcache[self.listcacheidx][1]
        self.listcache[self.listcacheidx] = (headings, items)

    def on_theList_itemActivated(self, event):
        """When an entry is double clicked"""
        base = self.components
        rows = base.theList.getStringSelection()
        if len(rows) == 0:
            return
        if not isinstance(rows[0], StringTypes):
            rows = [','.join(x) for x in rows]
        text = '\n'.join(rows)
        dlg = dialog.scrolledMessageDialog(self, text, 'List data')

    def on_theList_select(self, event):
        """When list entries are selected, display them
        (note only display first one in selection)"""
        base = self.components
        rows = base.theList.getStringSelection()
        if len(rows) == 0:
            return
        row = rows[0]
        if not isinstance(row, StringTypes):
            row = ' '.join(row)
        base.displayArea.text = row

    def _save_current_list(self):
        """Save column headings (including settings) and items into cache"""
        headings = self.components.theList.GetColumnHeadingInfo()
        items = self.components.theList.items
        llen = len(self.listcache)
        if llen > 5:
            self.listcache = self.listcache[1:] + [(headings, items)]
        else:
            self.listcache.append((headings, items))
        self.listcacheidx = len(self.listcache) - 1

    def _forward_in_cache(self):
        """Display the next list in the cache, wrap around if necessary, uses Append method"""
        llen = len(self.listcache)
        if llen == 0:
            return
        self.listcacheidx += 1
        if self.listcacheidx >= llen:
            self.listcacheidx = 0
        self.components.theList.columnHeadings = self.listcache[self.listcacheidx][0]
        self.components.theList.Append(self.listcache[self.listcacheidx][1])

    def _backward_in_cache(self):
        """Display the previous list in the cache, wrap around if necessary, uses Insert method"""
        llen = len(self.listcache)
        if llen == 0:
            return
        self.listcacheidx -= 1
        if self.listcacheidx < 0:
            self.listcacheidx = llen - 1
        self.components.theList.columnHeadings = self.listcache[self.listcacheidx][0]
        self.components.theList.InsertItems(self.listcache[self.listcacheidx][1], 0)

if __name__ == '__main__':
    app = model.Application(MulticolumnExample)
    app.MainLoop()
