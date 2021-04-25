import pyNastran
import os

from pyNastran.bdf.bdf import BDF, read_bdf

def mass(bdf_filename,name):

    model = BDF()
    model.read_bdf(bdf_filename)

    bdf_xref = read_bdf(bdf_filename, xref=True)

    ## Masa de la estructura
    from pyNastran.bdf.mesh_utils.mass_properties import mass_properties
    from pyNastran.bdf.mesh_utils.breakdowns import get_area_breakdown, get_mass_breakdown, get_volume_breakdown
    mass, cg, I = mass_properties(bdf_xref)
    print(name," mass =", mass)
    #mass_properties(bdf_xref)

bdf_filename = './Bandeja_B/Bandeja_B.bdf'
mass(bdf_filename,'B')

bdf_filename = './Bandeja_A/Bandeja_A.bdf'
mass(bdf_filename,'A')
