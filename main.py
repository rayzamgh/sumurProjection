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

class DataFrameSteam:
    def __init__(self, currentTableInput):

        self.columnnames = ["mdlist", "segment","angle","diameter","roughness","pressure","massrate","gravity", "dryness","area","H_enthalpy","Dryness","Rhom_", "rhol","rhog","velocity","Vsl","Vsg","miu","miuL", "miug","deltaw","NoslipHoldup","LiqVelNumb", "GasVelNumb","diaNum","liqVisNum", "L1","L2","Lb","Ls","Lm","F1","F2","F3","F4","F5","F6", "F6aksen","F7","PolaAliran","Sbubble","Sslug", "S_pattern","slip_vel_for_bubble_slug", "HL","Re","Debil","fff","f1","R","f_input_bub_frifact", "f2","f3","fmBF","Nre","Nw","eD","fm","dpdz","A","B", "dens_correction","transisi","BLColumn", "EkComplement","Dpdz_total","Dptot","P2","ReBQ", "BRColumn","fff","mff","BUColumn","DeltaPGravity", "acceleration","DeltaPfriksi","DeltaPtotal","P2BZ", "rho_","velocityCB", "Ep", "Ek", "H2", "T2"]

        self.mdlist, self.segment,self.angle,self.diameter,self.roughness,self.pressure,self.massrate,self.gravity,self.dryness,self.area,self.H_enthalpy,self.Dryness,self.Rhom_,self.rhol,self.rhog,self.velocity,self.Vsl,self.Vsg,self.miu,self.miuL,self.miug,self.deltaw,self.NoslipHoldup,self.LiqVelNumb,self.GasVelNumb,self.diaNum,self.liqVisNum,self.L1,self.L2,self.Lb,self.Ls,self.Lm,self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F6aksen,self.F7,self.PolaAliran,self.Sbubble,self.Sslug,self.S_pattern,self.slip_vel_for_bubble_slug,self.HL,self.Re,self.Debil,self.fffAV,self.f1,self.R,self.f_input_bub_frifact,self.f2,self.f3,self.fmBF,self.Nre,self.Nw,self.eD,self.fm,self.dpdz,self.A,self.B,self.dens_correction,self.transisi,self.BLColumn,self.EkComplement,self.Dpdz_total,self.Dptot,self.P2,self.ReBQ,self.BRColumn,self.fff,self.mff,self.BUColumn,self.DeltaPGravity,self.acceleration,self.DeltaPfriksi,self.DeltaPtotal,self.P2BZ,self.rho_,self.velocityCB, self.Ep, self.Ek, self.H2, self.T2 = ([] for i in range(len(self.columnnames)))

        self.columns = [self.mdlist, self.segment,self.angle,self.diameter,self.roughness,self.pressure,self.massrate,self.gravity,self.dryness,self.area,self.H_enthalpy,self.Dryness,self.Rhom_,self.rhol,self.rhog,self.velocity,self.Vsl,self.Vsg,self.miu,self.miuL,self.miug,self.deltaw,self.NoslipHoldup,self.LiqVelNumb,self.GasVelNumb,self.diaNum,self.liqVisNum,self.L1,self.L2,self.Lb,self.Ls,self.Lm,self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F6aksen,self.F7,self.PolaAliran,self.Sbubble,self.Sslug,self.S_pattern,self.slip_vel_for_bubble_slug,self.HL,self.Re,self.Debil,self.fffAV,self.f1,self.R,self.f_input_bub_frifact,self.f2,self.f3,self.fmBF,self.Nre,self.Nw,self.eD,self.fm,self.dpdz,self.A,self.B,self.dens_correction,self.transisi,self.BLColumn,self.EkComplement,self.Dpdz_total,self.Dptot,self.P2BZ,self.ReBQ,self.BRColumn,self.fff,self.mff,self.BUColumn,self.DeltaPGravity,self.acceleration,self.DeltaPfriksi,self.DeltaPtotal,self.P2,self.rho_,self.velocityCB, self.Ep, self.Ek, self.H2, self.T2]
        
        # self.mdlist                     = []
        # self.segment                    = []
        # self.angle                      = []
        # self.diameter                   = []
        # self.roughness                  = []
        # self.pressure                   = []
        # self.massrate                   = []
        # self.gravity                    = []
        # self.dryness                    = []
        # self.area                       = []
        # self.H_enthalpy                 = []        
        # self.Dryness                    = []        
        # self.Rhom_                      = []    
        # self.rhol                       = []    
        # self.rhog                       = []    
        # self.velocity                   = []        
        # self.Vsl                        = []    
        # self.Vsg                        = []    
        # self.miu                        = []    
        # self.miuL                       = []    
        # self.miug                       = []    
        # self.deltaw                     = []    
        # self.NoslipHoldup               = []            
        # self.LiqVelNumb                 = []        
        # self.GasVelNumb                 = []        
        # self.diaNum                     = []    
        # self.liqVisNum                  = []        
        # self.L1                         = []
        # self.L2                         = []
        # self.Lb                         = []
        # self.Ls                         = []
        # self.Lm                         = []
        # self.F1                         = []
        # self.F2                         = []
        # self.F3                         = []
        # self.F4                         = []
        # self.F5                         = []
        # self.F6                         = []
        # self.F6aksen                    = []        
        # self.F7                         = []
        # self.PolaAliran                 = []        
        # self.Sbubble                    = []        
        # self.Sslug                      = []    
        # self.S_pattern                  = []        
        # self.slip_vel_for_bubble_slug   = []                        
        # self.HL                         = []
        # self.Re                         = []
        # self.Debil                      = []    
        # self.fff                        = []    
        # self.f1                         = []
        # self.R                          = []
        # self.f_input_bub_frifact        = []                    
        # self.f2                         = []
        # self.f3                         = []
        # self.fm                         = []
        # self.Nre                        = []    
        # self.Nw                         = []
        # self.eD                         = []
        # self.fm                         = []
        # self.dpdz                       = []
        # self.A                          = []
        # self.B                          = []
        # self.dens_correction            = []                
        # self.transisi                   = []        
        # self.BLColumn                   = []        
        # self.EkComplement               = []
        # self.Dpdz_total                 = []
        # self.Dptot                      = []    
        # self.P2                         = []
        # self.Re                         = []
        # self.BRColumn                   = []        
        # self.fff                        = []    
        # self.mff                        = []    
        # self.BUColumn                   = []        
        # self.DeltaPGravity              = []            
        # self.acceleration               = []            
        # self.DeltaPfriksi               = []            
        # self.DeltaPtotal                = []            
        # self.P2                         = []
        # self.rho_                       = []    
        # self.velocity                   = []        
        # self.Ep                         = []
        # self.Ek                         = []
        # self.H2                         = []
        # self.T2                         = []

        self.lenofdata = 0

        for x in range(0, int(np.floor(currentTableInput.subTable[-1].md)), 3):
            self.lenofdata += 1
        self.lenofdata += 1
        
        for x in self.columns:
            for _ in range(0,self.lenofdata):
                x.append(0)
        
        i = 0
        for x in range(0, int(np.floor(currentTableInput.subTable[-1].md)), 3):
            self.mdlist[i] = x
            i += 1
        self.mdlist[i] = (int(np.floor((currentTableInput.subTable[-1].md))))

        i = 0
        for x in self.mdlist:
            self.segment[i] = (x * -1)

            self.massrate[i] = currentTableInput.massrate
            
            self.gravity[i] = (9.81)
            i += 1

        i = 0
        for x in self.mdlist:
            for y in currentTableInput.subTable:
                if x <= y.md:
                    self.angle[i] = (y.angle)
                    self.diameter[i] = (y.diameter)
                    self.roughness[i] = (y.roughness)
                    i += 1
                    break

        i = 0
        for x in self.diameter:
            self.area[i] = (calc.area(x))
            i += 1
        
        if (currentTableInput.whp == 0) :
            self.pressure[0] = currentTableInput.pwf
        else:
            self.pressure[0] = currentTableInput.whp

        self.H_enthalpy[0] = currentTableInput.enthalpy

        self.Dryness[0] = st.x_ph(self.pressure[0], self.H_enthalpy[0])

    # def dataPreparation(self):


        
    def print(self):
        self.data = {
        'MDmeter'                   : self.mdlist,
        'Segment'                   : self.segment,
        'Angle'                     : self.angle,
        'Diameter'                  : self.diameter,
        'Roughness'                 : self.roughness,
        'Pressure'                  : self.pressure,
        'Massrate'                  : self.massrate,
        'H_enthalpy'                : self.H_enthalpy,
        'Dryness'                   : self.Dryness,
        'Rhom_'                     : self.Rhom_,
        "rhol"                      : self.rhol,	
        "rhog"                      : self.rhog,
        'Gravity'                   : self.gravity,
        'Area'                      : self.area,
        "velocity"                  : self.velocity,
        "Vsl"                       : self.Vsl,
        "Vsg"                       : self.Vsg,
        "miu"                       : self.miu,
        "miuL"                      : self.miuL,
        "miug"                      : self.miug,
        "deltaw"                    : self.deltaw,
        "NoslipHoldup"              : self.NoslipHoldup,
        "LiqVelNumb"                : self.LiqVelNumb,
        "GasVelNumb"                : self.GasVelNumb,
        "diaNum"                    : self.diaNum,
        "liqVisNum"                 : self.liqVisNum,
        "L1"                        : self.L1,        
        "L2"                        : self.L2,
        "Lb"                        : self.Lb,
        "Ls"                        : self.Ls,
        "Lm"                        : self.Lm,
        "F1"                        : self.F1,
        "F2"                        : self.F2,
        "F3"                        : self.F3,
        "F4"                        : self.F4,
        "F5"                        : self.F5,
        "F6"                        : self.F6,
        "F6aksen"                   : self.F6aksen,
        "F7"                        : self.F7,
        "PolaAliran"                : self.PolaAliran,
        "Sbubble"                   : self.Sbubble,
        "Sslug"                     : self.Sslug,
        "S_pattern"                 : self.S_pattern,
        "slip_vel_for_bubble_slug"  : self.slip_vel_for_bubble_slug,
        "HL"                        : self.HL,
        "ReBQ"                      : self.ReBQ,
        "Debil"                     : self.Debil,
        "fffAV"                     : self.fffAV,
        "f1"                        : self.f1,
        "R"                         : self.R,
        "f_input_bub_frifact"       : self.f_input_bub_frifact,  
        "f2"                        : self.f2,
        "f3"                        : self.f3,
        "fm"                        : self.fm,
        "Nre"                       : self.Nre,
        "Nw"                        : self.Nw,
        "e/D"                       : self.eD,
        "fmBF"                      : self.fmBF,
        "dp/dz"                     : self.dpdz,
        "A"                         : self.A,
        "B"                         : self.B,
        "dens_correction"           : self.dens_correction,
        "transisi"                  : self.transisi,
        "BLColumn"                  : self.BLColumn,
        "EkComplement"              : self.EkComplement,
        "Dp/dz_total"               : self.Dpdz_total,
        "Dptot"                     : self.Dptot,
        "P2"                        : self.P2,
        "Re"                        : self.Re,
        "BRColumn"                  : self.BRColumn,
        "fff"                       : self.fff,
        "mff"                       : self.mff,
        "BUColumn"                  : self.BUColumn,
        "DeltaPGravity"             : self.DeltaPGravity,
        "acceleration"              : self.acceleration,
        "DeltaPfriksi"              : self.DeltaPfriksi,
        "DeltaPtotal"               : self.DeltaPtotal,
        "P2BZ"                      : self.P2BZ,
        "rho_"                      : self.rho_,
        "velocityCB"                : self.velocityCB,
        "Ep"                        : self.Ep,
        "Ek"                        : self.Ek,
        "H2"                        : self.H2,
        "T2"                        : self.T2,
        }

        print("===============================")
        print("Harusnya:" +  str(self.lenofdata))
        for x in self.columnnames:
            if (eval("len(self." + x + ") != self.lenofdata")):
                print(x)
                print(eval("len(self." + x + ")"))
        df = pd.DataFrame(self.data)
        print(df)

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

    currentDataframe = DataFrameSteam(currentTableInput)

    currentDataframe.print()

    

main()