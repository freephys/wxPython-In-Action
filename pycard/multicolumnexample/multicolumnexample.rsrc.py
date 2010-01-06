{'application':{'type':'Application',
          'name':'MulticolumnExample',
    'backgrounds': [
    {'type':'Background',
          'name':'bgMulticolumnExample',
          'title':'Multicolumn Example PythonCard Application',
          'size':(620, 500),

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
    'name':'demoButton', 
    'position':(510, 5), 
    'size':(85, 25), 
    'label':u'Load Demo', 
    },

{'type':'Button', 
    'name':'clearButton', 
    'position':(510, 30), 
    'size':(85, 25), 
    'label':u'Clear', 
    },

{'type':'Button', 
    'name':'loadButton', 
    'position':(510, 55), 
    'size':(85, 25), 
    'label':u'Load CSV', 
    },

{'type':'Button', 
    'name':'appendButton', 
    'position':(510, 80), 
    'size':(85, 25), 
    'label':u'Append CSV', 
    },

{'type':'Button', 
    'name':'swapButton', 
    'position':(510, 105), 
    'size':(85, 25), 
    'label':u'Swap Lists', 
    },

{'type':'Button', 
    'name':'prevButton', 
    'position':(510, 130), 
    'size':(85, 25), 
    'label':u'Prev', 
    },

{'type':'Button', 
    'name':'nextButton', 
    'position':(510, 155), 
    'size':(85, 25), 
    'label':u'Next', 
    },

{'type':'Button', 
    'name':'exitButton', 
    'position':(510, 180), 
    'size':(85, 25), 
    'label':u'Exit', 
    },

{'type':'MultiColumnList', 
    'name':'theList', 
    'position':(3, 3), 
    'size':(500, 390), 
    'backgroundColor':(255, 255, 255, 255), 
    'columnHeadings':['Example List'], 
    'font':{'faceName': u'Tahoma', 'family': 'sansSerif', 'size': 8}, 
    'items':[u'Example 1', u'Example 2', u'Example 3'], 
    'maxColumns':20, 
    'rules':1, 
    },

{'type':'TextArea', 
    'name':'displayArea', 
    'position':(3, 398), 
    'size':(500, 40), 
    'font':{'family': 'monospace', 'size': 12}, 
    },

{'type':'TextArea', 
    'name':'countArea', 
    'position':(507, 398), 
    'size':(85, 40), 
    'font':{'family': 'monospace', 'size': 12}, 
    },

] # end components
} # end background
] # end backgrounds
} }
