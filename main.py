# from iapws import IAPWS97
import SteamTable as st
import calculation as calc
import numpy as np

import pandas as pd


class Table:
    def __init__(self, multipleSegments):
        self.segments = multipleSegments

    def addSegment(self, singleSegment):
        self.segments.append(singleSegment)

# class OneSegment:
#     def __init__()

class OneInput:
    def __init__(self, md, angle, diameter, roughness):
        self.md = md
        self.angle = angle
        self.diameter = diameter
        self.roughness = roughness

    def print(self):
        print("MD(meter):")
        print(self.md)

        print("Angle:")
        print(self.angle)
        
        print("Diameter(m):")
        print(self.diameter)
        
        print("Roughn(m):")
        print(self.roughness)

class inputTable:
    def __init__(self, whp, massrate, enthalpy, pwf):
        self.whp = whp
        self.massrate = massrate
        self.enthalpy = enthalpy
        self.pwf = pwf
        self.subTable = []
    
    def print(self):
        print("WHP (bar)")
        print(self.whp)
        print("Massrate (Kg/s)")
        print(self.massrate)
        print("Enthalpy (KJ/kg)")
        print(self.enthalpy)
        print("Pwf (bar)")
        print(self.pwf, "")
        for v in self.subTable:
            v.print()


SEGMENT_CONST = 3 

def main():

    # Table Variable

    print("WHP (bar)")
    whp = float(input())
    print("Massrate (Kg/s)")
    massrate = float(input())
    print("Enthalpy (KJ/kg)")
    enthalpy = float(input())
    print("Pwf (bar)")
    pwf = float(input())

    currentTableInput = inputTable(whp, massrate, enthalpy, pwf)   

    loopInput = False
    n = 0

    while not loopInput:
        
        n = n + 1
        print("Loop input baris", n)
        print("MD(meter):")
        md = float(input())
        print("Angle:")
        angle = float(input())
        print("Diameter(m):")
        diameter = float(input())
        print("Roughn(m):")
        roughness = float(input())

        elemListSubinput = OneInput(md, angle, diameter, roughness)

        currentTableInput.subTable.append(elemListSubinput)
        
        print("Stop input? y/n")
        loopStop = input()
        if loopStop == "y" :
            loopInput = True
    
    currentTableInput.print()


    # INPUT TO PANDAS

    mdlist      = []
    segment     = []
    angle       = []
    diameter    = []
    roughness   = []
    massrate    = []
    gravity     = []
    dryness     = []
    area        = []

    for x in range(0, int(np.floor(currentTableInput.subTable[-1].md)), 3):
        mdlist.append(x)
    mdlist.append(int(np.floor((currentTableInput.subTable[-1].md))))

    for x in mdlist:
        segment.append(x *-1)
        massrate.append(currentTableInput.massrate)
        gravity.append(9.81)

    for x in mdlist:
        for y in currentTableInput.subTable:
            if x <= y.md:
                angle.append(y.angle)
                diameter.append(y.diameter)
                roughness.append(y.roughness)
                break

    for x in diameter:
        area.append(calc.area(x))

    data = {
        'MDmeter'                   : mdlist,
        'Segment'                   : segment,
        'Angle'                     : angle,
        'Diameter'                  : diameter,
        'Roughness'                 : roughness,
        # 'Pressure'                : "",
        'Massrate'                  : massrate,
        # 'H-entalphy'              : "",
        # 'Dryness'                 : dryness,
        # 'Rhom_'                   : "",
        # "rhol"                    : "",	
        # "rhog"                    : "",
        'Gravity'                   : gravity,
        'Area'                      : area,
        # "velocity"                  : "",
        # "Vsl"                       : "",
        # "Vsg"                       : "",
        # "miu"                       : "",
        # "miuL"                      : "",
        # "miug"                      : "",
        # "deltaw"                    : "",
        # "NoslipHoldup"              : "",
        # "LiqVelNumb"                : "",
        # "GasVelNumb"                : "",
        # "diaNum"                    : "",
        # "liqVisNum"                 : "",
        # "L1"                        : "",
        # "L2"                        : "",
        # "Lb"                        : "",
        # "Ls"                        : "",
        # "Lm"                        : "",
        # "F1"                        : "",
        # "F2"                        : "",
        # "F3"                        : "",
        # "F4"                        : "",
        # "F5"                        : "",
        # "F6"                        : "",
        # "F6aksen"                   : "",
        # "F7"                        : "",
        # "PolaAliran"                : "",
        # "Sbubble"                   : "",
        # "Sslug"                     : "",
        # "S_pattern"                 : "",
        # "slip_vel_for_bubble_slug"  : "",
        # "HL"                        : "",
        # "Re"                        : "",
        # "Debil"                     : "",
        # "fff"                       : "",
        # "f1"                        : "",
        # "R"                         : "",
        # "f_input_bub_frifact"       : "",  
        # "f2"                        : "",
        # "f3"                        : "",
        # "fm"                        : "",
        # "Nre"                       : "",
        # "Nw"                        : "",
        # "e/D"                       : "",
        # "fm"                        : "",
        # "dp/dz"                     : "",
        # "A"                         : "",
        # "B"                         : "",
        # "dens_correction"           : "",
        # "transisi"                  : "",
        # "BLColumn"                  : "",
        # "1-Ek"                      : "",
        # "Dp/dz_total"               : "",
        # "Dptot"                     : "",
        # "P2"                        : "",
        # "Re"                        : "",
        # "BRColumn"                  : "",
        # "fff"                       : "",
        # "mff"                       : "",
        # "BUColumn"                  : "",
        # "DeltaPGravity"             : "",
        # "acceleration"              : "",
        # "DeltaPfriksi"              : "",
        # "DeltaPtotal"               : "",
        # "P2"                        : "",
        # "rho_"                      : "",
        # "velocity"                  : "",
        # "Ep"                        : "",
        # "Ek"                        : "",
        # "H2"                        : "",
        # "T2"                        : "",
    }

    df = pd.DataFrame(data)
    
    print(df)
    

main()