#!/usr/bin/env python

# Tags related to output writing
LCHARG_LIST = ["True", "False"]
LELF_LIST = ["True", "False"]
LVTOT_LIST = ["True", "False"]
LWAVE_LIST = ["True","False"]
NWRITE_LIST = ["0","1","2","3"]
LORBIT_LIST = ["0","1","2","10","11"]
# Tags related to Ion Movement
IBRION_LIST = ["0","1","2","3","5"]

INCAR_Tags = {# Tags related to output writing
              "LCHARG" : LCHARG_LIST,
              "LELF" : LELF_LIST,
              "LVTOT" : LVTOT_LIST,
              "LWAVE" : LWAVE_LIST,
              "NWRITE" : NWRITE_LIST,
              "LORBIT" : LORBIT_LIST,
              # Tags related to Ion Movement
              "IBRION" : IBRION_LIST # how the ions are updated and moved
}

Tag_Tips = { "NWRITE" : ["For long MD-runs,least verbose",
                         "For long MD-runs",
                         "(Default)For short runs",
                         "Most verbose,might give information if something goes wrong"
                        ],
             "LORBIT" : ["(Default)RWIGS read from INCAR,Write DOSCAR and PROCAR",
                         "RWIGS read from INCAR,Write DOSCAR and extended PROCAR(COOP)",
                         "RWIGS read from INCAR,Write DOSCAR and PROOUT",
                         "Only for PAW,not for ultrasoft or norm conserving pseudopotentials,\n No RWIGS needed from INCAR, Write DOSCAR and PROCAR file",
                         "Only for PAW,not for ultrasoft or norm conserving pseudopotentials,\n No RWIGS needed from INCAR, Write spd and site projected DOSCAR and extended PROCAR(COOP)"
                        ],
             "IBRION" : ["MD(Const V)with Verlet,\n POTIM supplies the timestep(fs)\n SMASS controls the velocities",
                         "RMM-DIIS relaxation,\n fast&efficient(close to local minima),\n fails(for bad initial position),\n set NELMIN(set between 4 and 8)and reasonable POTIM",
                         "CG relaxation(useful for bad initial position)\n POTIM(length of the trial step)",
                         "damped relaxation(if SMASS(damping factor provied))\n reasonal POTIM",
                         "Freq calculation at Gamma \n NFREE(# displacements used,2 recomended)\n NSW(must be set positive)\n POTIM(step size)"
                        ]
    
}