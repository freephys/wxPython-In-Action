{'application':{'type':'Application',
          'name':'Minimal',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMin',
          'title':'Minimal PythonCard Application',
          'size':(398, 249),

        'menubar': {'type':'MenuBar',
         'menus': [
             {'type':'Menu',
             'name':'menuFile',
             'label':'&File',
             'items': [
                  {'type':'MenuItem',
                   'name':'menuFileExit',
                   'label':'E&xit\tAlt+X',
                   'command':'exit',
                  },
              ]
             },
         ]
     },
         'components': [

{'type':'Button', 
    'name':'ResetButton', 
    'position':(18, 100), 
    'label':u'Reset', 
    },

{'type':'Button', 
    'name':'DecrementButton', 
    'position':(18, 52), 
    'label':u'Decrement', 
    },

{'type':'Button', 
    'name':'IncrementButton', 
    'position':(18, 12), 
    'label':u'Increment', 
    'toolTip':u'Increment the number', 
    },

{'type':'TextField', 
    'name':'field1', 
    'position':(182, 17), 
    'size':(118, 43), 
    'editable':False, 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 24}, 
    'text':u'42', 
    },

] # end components
} # end background
] # end backgrounds
} }
