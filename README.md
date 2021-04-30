## Practica2_EUE
UPM-SAT2 like sat NASTRAN-PATRAN analysis


# Estructura de directorios

    Bandeja_X/0: el db para Patran y el bdf original, para sacar elementos, grids, propiedades ...
    Bandeja_X/1: para hacer las iteraciones
  
Bandeja_X/1
 
    Bandeja_X.bdf: archivo sin cabecera que incluye los siguientes elementos
  
    1_RE : Rigidizador exterior
    2_RI : Rigidizador interior
    3_B1 : Bandeja
    4_G1 : Grid
    Al_7075 : Material
 
  Los nombres hay que cambiarlos en el bdf de la bandeja porque están puestos con includes, a medida que itermos habrá que darle nombres representativos para no liarnos pero mantener los números creo que es buena idea para no liarnos.

  
