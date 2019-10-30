# from iapws import IAPWS97
from __future__ import absolute_import
import SteamTable as st
import calculation as calc
import numpy as np
import collections
import os
import pandas as pd


class Table(object):
    def __init__(self, multipleSegments):
        self.segments = multipleSegments

    def addSegment(self, singleSegment):
        self.segments.append(singleSegment)

# class OneSegment:
#     def __init__()

class OneInput(object):
    def __init__(self, md, angle, diameter, roughness):
        self.md = md
        self.angle = angle
        self.diameter = diameter
        self.roughness = roughness

    def printl(self):
        print "MD(meter):"
        print self.md

        print "Angle:"
        print self.angle
        
        print "Diameter(m):"
        print self.diameter
        
        print "Roughn(m):"
        print self.roughness

class inputTable(object):
    def __init__(self, whp, massrate, enthalpy, pwf):
        self.whp = whp
        self.massrate = massrate
        self.enthalpy = enthalpy
        self.pwf = pwf
        self.subTable = []
    
    def printl(self):
        print "WHP (bar)"
        print self.whp
        print "Massrate (Kg/s)"
        print self.massrate
        print "Enthalpy (KJ/kg)"
        print self.enthalpy
        print "Pwf (bar)"
        print self.pwf, ""
        for v in self.subTable:
            v.printl()

class DataFrameSteam(object):
    def __init__(self, currentTableInput):

        self.columnnames = ["mdlist","Tanradian", "segment","angle","diameter","roughness","pressure","massrate","gravity","area","H_enthalpy","Dryness","Rhom_", "rhol","rhog","velocity","Vsl","Vsg","miu","miuL", "miug","deltaw","NoslipHoldup","LiqVelNumb", "GasVelNumb","diaNum","liqVisNum", "L1","L2","Lb","Ls","Lm","F1","F2","F3","F4","F5","F6", "F6aksen","F7","PolaAliran","Sbubble","Sslug", "S_pattern","slip_vel_for_bubble_slug", "HL","Re","AUColumn","fff","f1","R","f_input_bub_frifact", "f2","f3","fmBF","Nre","Nw","eD","fm","dpdz","A","B", "dens_correction","transisi","BLColumn", "EkComplement","Dpdz_total","Dptot","P2","ReHomogen","BRColumnHomogen","fffHomogen","mffHomogen","BUColumnHomogen","DeltaPGravityHomogen","accelerationHomogen","DeltaPfriksiHomogen","DeltaPtotalHomogen","P2Homogen","rho_Homogen","velocityHomogen", "EpHomogen", "EkHomogen", "H2Homogen", "T2Homogen"]

        self.mdlist, self.segment,self.angle,self.Tanradian,self.diameter,self.roughness,self.pressure,self.massrate,self.gravity,self.area,self.H_enthalpy,self.Dryness,self.Rhom_,self.rhol,self.rhog,self.velocity,self.Vsl,self.Vsg,self.miu,self.miuL,self.miug,self.deltaw,self.NoslipHoldup,self.LiqVelNumb,self.GasVelNumb,self.diaNum,self.liqVisNum,self.L1,self.L2,self.Lb,self.Ls,self.Lm,self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F6aksen,self.F7,self.PolaAliran,self.Sbubble,self.Sslug,self.S_pattern,self.slip_vel_for_bubble_slug,self.HL,self.Re,self.AUColumn,self.fff,self.f1,self.R,self.f_input_bub_frifact,self.f2,self.f3,self.fmBF,self.Nre,self.Nw,self.eD,self.fm,self.dpdz,self.A,self.B,self.dens_correction,self.transisi,self.BLColumn,self.EkComplement,self.Dpdz_total,self.Dptot,self.P2,self.ReHomogen,self.BRColumnHomogen,self.fffHomogen,self.mffHomogen,self.BUColumnHomogen,self.DeltaPGravityHomogen,self.accelerationHomogen,self.DeltaPfriksiHomogen,self.DeltaPtotalHomogen,self.P2Homogen,self.rho_Homogen,self.velocityHomogen, self.EpHomogen, self.EkHomogen, self.H2Homogen, self.T2Homogen = ([] for i in xrange(len(self.columnnames)))

        self.columns = [self.mdlist, self.segment,self.Tanradian,self.angle,self.diameter,self.roughness,self.pressure,self.massrate,self.gravity,self.area,self.H_enthalpy,self.Dryness,self.Rhom_,self.rhol,self.rhog,self.velocity,self.Vsl,self.Vsg,self.miu,self.miuL,self.miug,self.deltaw,self.NoslipHoldup,self.LiqVelNumb,self.GasVelNumb,self.diaNum,self.liqVisNum,self.L1,self.L2,self.Lb,self.Ls,self.Lm,self.F1,self.F2,self.F3,self.F4,self.F5,self.F6,self.F6aksen,self.F7,self.PolaAliran,self.Sbubble,self.Sslug,self.S_pattern,self.slip_vel_for_bubble_slug,self.HL,self.Re,self.AUColumn,self.fff,self.f1,self.R,self.f_input_bub_frifact,self.f2,self.f3,self.fmBF,self.Nre,self.Nw,self.eD,self.fm,self.dpdz,self.A,self.B,self.dens_correction,self.transisi,self.BLColumn,self.EkComplement,self.Dpdz_total,self.Dptot,self.P2,self.ReHomogen,self.BRColumnHomogen,self.fffHomogen,self.mffHomogen,self.BUColumnHomogen,self.DeltaPGravityHomogen,self.accelerationHomogen,self.DeltaPfriksiHomogen,self.DeltaPtotalHomogen,self.P2Homogen,self.rho_Homogen,self.velocityHomogen, self.EpHomogen, self.EkHomogen, self.H2Homogen, self.T2Homogen]

        self.lenofdata = 0

        for x in xrange(0, int(np.floor(currentTableInput.subTable[-1].md)), 3):
            self.lenofdata += 1
        self.lenofdata += 1
        
        for x in self.columns:
            for _ in xrange(0,self.lenofdata):
                x.append(0)
        
        i = 0
        for x in xrange(0, int(np.floor(currentTableInput.subTable[-1].md)), 3):
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
            self.area[i] = (calc.funcN(x))
            i += 1
        
        if (currentTableInput.whp == 0) :
            self.pressure[0] = currentTableInput.pwf
        else:
            self.pressure[0] = currentTableInput.whp

        self.H_enthalpy[0]      = currentTableInput.enthalpy
        self.Dryness[0]         = st.x_ph(self.pressure[0], self.H_enthalpy[0])
        self.Rhom_[0]           = st.rho_ph(self.pressure[0], self.H_enthalpy[0])
        self.rhol[0]            = st.rhoL_p(self.pressure[0])
        self.rhog[0]            = st.rhoV_p(self.pressure[0])
        self.velocity[0]        = calc.funcO(self.massrate[0], self.Rhom_[0], self.area[0])
        self.Vsl[0]             = calc.funcP(self.Dryness[0], self.massrate[0], self.rhol[0], self.area[0])
        self.Vsg[0]             = calc.funcQ(self.Dryness[0], self.massrate[0], self.rhog[0], self.area[0])
        self.miu[0]             = st.mixvisco(self.pressure[0], self.H_enthalpy[0])
        self.miuL[0]            = st.my_pT(self.pressure[0], st.Tsat_p(self.pressure[0] - 0.001))
        self.miug[0]            = st.my_pT(self.pressure[0], st.Tsat_p(self.pressure[0] + 0.001))
        self.deltaw[0]          = st.st_p(self.pressure[0])
        self.NoslipHoldup[0]    = calc.funcV(self.Vsl[0], self.Vsg[0])
        self.LiqVelNumb[0]      = calc.funcW(self.Vsl[0], self.rhol[0], self.gravity[0], self.deltaw[0])
        self.GasVelNumb[0]      = calc.funcX(self.Vsg[0], self.rhol[0], self.gravity[0], self.deltaw[0])
        self.diaNum[0]          = calc.funcY(self.diameter[0], self.rhol[0], self.gravity[0], self.deltaw[0])
        self.liqVisNum[0]       = calc.funcZ(self.miuL[0], self.gravity[0], self.rhol[0], self.deltaw[0])
        self.L1[0]              = calc.funcAA(self.diaNum[0])               
        self.L2[0]              = calc.funcAB(self.diaNum[0])
        self.Lb[0]              = calc.funcAC(self.L1[0], self.L2[0], self.LiqVelNumb[0])
        self.Ls[0]              = calc.funcAD(self.LiqVelNumb[0])
        self.Lm[0]              = calc.funcAE(self.LiqVelNumb[0])
        self.F1[0]              = calc.funcAF(self.liqVisNum[0])
        self.F2[0]              = calc.funcAG(self.liqVisNum[0])
        self.F3[0]              = calc.funcAH(self.liqVisNum[0])
        self.F4[0]              = calc.funcAI(self.liqVisNum[0])
        self.F5[0]              = calc.funcAJ(self.liqVisNum[0])

        # homogen
        self.ReHomogen[0]                      = calc.funcBQ(self.Rhom_[0], self.velocity[0], self.diameter[0], self.miu[0])
        self.BRColumnHomogen[0]                = calc.funcBR(self.roughness[0], self.diameter[0], self.ReHomogen[0])
        self.fffHomogen[0]                     = calc.funcBS(self.roughness[0], self.diameter[0], self.ReHomogen[0], self.BRColumnHomogen[0])
        self.mffHomogen[0]                     = calc.funcBT(self.fffHomogen[0])
        self.Tanradian[0]                      = calc.funcBU(self.angle[0])
        self.DeltaPGravityHomogen[0]           = calc.funcBV(self.Rhom_[0], self.gravity[0], self.segment[1], self.segment[0], self.angle[0])
        self.accelerationHomogen[0]            = calc.funcBW(self.Rhom_[0], self.velocity[0], self.pressure[0])
        self.DeltaPfriksiHomogen[0]            = calc.funcBX(self.mffHomogen[0], self.segment[1], self.segment[0], self.Rhom_[0], self.velocity[0], self.diameter[0])
        self.DeltaPtotalHomogen[0]             = calc.funcBY(self.DeltaPGravityHomogen[0], self.DeltaPfriksiHomogen[0], self.accelerationHomogen[0])
        self.P2Homogen[0]                      = calc.funcBZ(self.DeltaPtotalHomogen[0], self.pressure[0])
        self.rho_Homogen[0]                    = st.rho_ph(self.P2Homogen[0], self.H_enthalpy[0])
        self.velocityHomogen[0]                = calc.funcCB(self.massrate[0], self.rho_Homogen[0] ,self.area[0])
        self.EpHomogen[0]                      = calc.funcCC(self.gravity[0], self.segment[1], self.segment[0])
        self.EkHomogen[0]                      = calc.funcCD(self.velocity[0], self.velocityHomogen[0])
        self.H2Homogen[0]                      = calc.funcCE(self.H_enthalpy[0], self.EkHomogen[0], self.EpHomogen[0])
        self.T2Homogen[0]                      = st.T_ph(self.pressure[0], self.H_enthalpy[0])


        # second part after fffHomogen has been determined
        self.F6[0]                        = calc.funcAK(self.liqVisNum[0], self.fffHomogen[5])
        self.F6aksen[0]                   = calc.funcAL(self.diaNum[0], self.F6[0])
        self.F7[0]                        = calc.funcAM(self.liqVisNum[0])
        self.PolaAliran[0]                = calc.funcAN(self.GasVelNumb[0], self.Lb[0], self.Ls[0], self.Lm[0])
        self.Sbubble[0]                   = calc.funcAO(self.F1[0], self.F2[0], self.LiqVelNumb[0], self.F3[0], self.GasVelNumb[0])
        self.Sslug[0]                     = calc.funcAP(self.F5[0], self.GasVelNumb[0], self.F6aksen[0], self.F7[0], self.LiqVelNumb[0])     
        self.S_pattern[0]                 = calc.funcAQ(self.PolaAliran[0], self.Sbubble[0], self.Sslug[0])         
        self.slip_vel_for_bubble_slug[0]  = calc.funcAR(self.S_pattern[0], self.rhol[0], self.deltaw[0], self.gravity[0])                         
        self.HL[0]                        = calc.funcAS(self.PolaAliran[0], self.Vsl[0], self.velocity[0], self.slip_vel_for_bubble_slug[0])

        # non-homogen
        self.Re[0]                             = calc.funcAT(self.rhol[0], self.Vsl[0], self.diameter[0], self.miuL[0]) 
        self.AUColumn[0]                       = calc.funcAU(self.roughness[0], self.diameter[0], self.Re[0])         
        self.fff[0]                            = calc.funcAV(self.roughness[0], self.diameter[0], self.Re[0], self.AUColumn[0])
        self.f1[0]                             = calc.funcAW(self.fff[0])
        self.R[0]                              = calc.funcAX(self.Vsg[0], self.Vsl[0])
        self.f_input_bub_frifact[0]            = calc.funcAY(self.f1[0], self.R[0], self.diaNum[0], self.Vsl[0])
        self.f2[0]                             = calc.funcAZ(self.f_input_bub_frifact[0])
        self.f3[0]                             = calc.funcBA(self.f1[0], self.R[0])
        self.fm[0]                             = calc.funcBB(self.f1[0], self.f2[0], self.f3[0])
        self.Nre[0]                            = calc.funcBC(self.rhog[0], self.Vsg[0], self.diameter[0], self.miug[0])
        self.Nw[0]                             = calc.funcBD(self.Vsg[0], self.miuL[0], self.rhog[0], self.rhol[0], self.deltaw[0])
        self.eD[0]                             = calc.funcBE(self.Nw[0], self.deltaw[0], self.rhog[0], self.Vsg[0], self.diameter[0])
        self.fmBF[0]                           = calc.funcBF(self.eD[0], self.f1[0])    
        self.dpdz[0]                           = calc.funcBG(self.PolaAliran[0], self.fmBF[0], self.rhog[0], self.Vsg[0], self.diameter[0], self.fm[0], self.rhol[0], self.Vsl[0], self.velocity[0])     
        self.A[0]                              = calc.funcBH(self.Lm[0], self.GasVelNumb[0], self.Ls[0])
        self.B[0]                              = calc.funcBI(self.GasVelNumb[0], self.Ls[0], self.Lm[0])
        self.dens_correction[0]                = calc.funcBJ(self.rhog[0], self.GasVelNumb[0], self.Lm[0])             
        self.transisi[0]                       = calc.funcBK(self.PolaAliran[0], self.A[0], self.dpdz[0], self.B[0], self.fm[0], self.rhog[0], self.gravity[0], self.Vsg[0], self.diameter[0], self.dpdz[0])
        self.BLColumn[0]                       = calc.funcBL(self.gravity[0], self.HL[0], self.rhol[0], self.rhog[0])         
        self.EkComplement[0]                   = calc.funcBM(self.rhog[0], self.velocity[0], self.Vsg[0], self.pressure[0])
        self.Dpdz_total[0]                     = calc.funcBN(self.transisi[0], self.BLColumn[0], self.EkComplement[0])
        self.Dptot[0]                          = calc.funcBO(self.Dpdz_total[0], self.segment[1], self.segment[0], self.angle[0])
        self.P2[0]                             = calc.funcBP(self.Dptot[0], self.pressure[0])

    def secondIteration(self):
        for i in range(1, len(self.mdlist)):
            self.pressure[i]        = calc.funcF(self.Dryness[i - 1], self.P2[i - 1], self.P2Homogen[i - 1])
            self.H_enthalpy[i]      = self.H2Homogen[i - 1]
            self.Dryness[i]         = st.x_ph(self.pressure[i], self.H_enthalpy[i])
            self.Rhom_[i]           = st.rho_ph(self.pressure[i], self.H_enthalpy[i])
            self.rhol[i]            = st.rhoL_p(self.pressure[i])
            self.rhog[i]            = st.rhoV_p(self.pressure[i])
            self.velocity[i]        = calc.funcO(self.massrate[i], self.Rhom_[i], self.area[i])
            self.Vsl[i]             = calc.funcP(self.Dryness[i], self.massrate[i], self.rhol[i], self.area[i])
            self.Vsg[i]             = calc.funcQ(self.Dryness[i], self.massrate[i], self.rhog[i], self.area[i])
            self.miu[i]             = st.mixvisco(self.pressure[i], self.H_enthalpy[i])
            self.miuL[i]            = st.my_pT(self.pressure[i], st.Tsat_p(self.pressure[i] - 0.001))
            self.miug[i]            = st.my_pT(self.pressure[i], st.Tsat_p(self.pressure[i] + 0.001))
            self.deltaw[i]          = st.st_p(self.pressure[i])
            self.NoslipHoldup[i]    = calc.funcV(self.Vsl[i], self.Vsg[i])
            self.LiqVelNumb[i]      = calc.funcW(self.Vsl[i], self.rhol[i], self.gravity[i], self.deltaw[i])
            self.GasVelNumb[i]      = calc.funcX(self.Vsg[i], self.rhol[i], self.gravity[i], self.deltaw[i])
            self.diaNum[i]          = calc.funcY(self.diameter[i], self.rhol[i], self.gravity[i], self.deltaw[i])
            self.liqVisNum[i]       = calc.funcZ(self.miuL[i], self.gravity[i], self.rhol[i], self.deltaw[i])
            self.L1[i]              = calc.funcAA(self.diaNum[i])               
            self.L2[i]              = calc.funcAB(self.diaNum[i])
            self.Lb[i]              = calc.funcAC(self.L1[i], self.L2[i], self.LiqVelNumb[i])
            self.Ls[i]              = calc.funcAD(self.LiqVelNumb[i])
            self.Lm[i]              = calc.funcAE(self.LiqVelNumb[i])
            self.F1[i]              = calc.funcAF(self.liqVisNum[i])
            self.F2[i]              = calc.funcAG(self.liqVisNum[i])
            self.F3[i]              = calc.funcAH(self.liqVisNum[i])
            self.F4[i]              = calc.funcAI(self.liqVisNum[i])
            self.F5[i]              = calc.funcAJ(self.liqVisNum[i])
        
    def printl(self):
        self.data = collections.OrderedDict([
        ("MDmeter"                   , self.mdlist),
        ("Segment"                   , self.segment),
        ("Angle"                     , self.angle),
        ("Diameter"                  , self.diameter),
        ("Roughness"                 , self.roughness),
        ("Pressure"                  , self.pressure),
        ("Massrate"                  , self.massrate),
        ("H_enthalpy"                , self.H_enthalpy),
        ("Dryness"                   , self.Dryness),
        ("Rhom_"                     , self.Rhom_),
        ("rhol"                      , self.rhol,),
        ("rhog"                      , self.rhog),
        ("Gravity"                   , self.gravity),
        ("Area"                      , self.area),
        ("velocity"                  , self.velocity),
        ("Vsl"                       , self.Vsl),
        ("Vsg"                       , self.Vsg),
        ("mi"                        , self.miu),
        ("miuL"                      , self.miuL),
        ("miug"                      , self.miug),
        ("deltaw"                    , self.deltaw),
        ("NoslipHoldup"              , self.NoslipHoldup),
        ("LiqVelNumb"                , self.LiqVelNumb),
        ("GasVelNumb"                , self.GasVelNumb),
        ("diaNum"                    , self.diaNum),
        ("liqVisNum"                 , self.liqVisNum),
        ("L1"                        , self.L1,       ),
        ("L2"                        , self.L2),
        ("Lb"                        , self.Lb),
        ("Ls"                        , self.Ls),
        ("Lm"                        , self.Lm),
        ("F1"                        , self.F1),
        ("F2"                        , self.F2),
        ("F3"                        , self.F3),
        ("F4"                        , self.F4),
        ("F5"                        , self.F5),
        ("F6"                        , self.F6),
        ("F6aksen"                   , self.F6aksen),
        ("F7"                        , self.F7),
        ("PolaAliran"                , self.PolaAliran),
        ("Sbubble"                   , self.Sbubble),
        ("Sslug"                     , self.Sslug),
        ("S_pattern"                 , self.S_pattern),
        ("slip_vel_for_bubble_slug"  , self.slip_vel_for_bubble_slug),
        ("HL"                        , self.HL),
        ("Re"                        , self.Re),
        ("AUColumn"                  , self.AUColumn),
        ("fff"                       , self.fff),
        ("f1"                        , self.f1),
        ("R"                         , self.R),
        ("f_input_bub_frifact"       , self.f_input_bub_frifact),
        ("f2"                        , self.f2),
        ("f3"                        , self.f3),
        ("fm"                        , self.fm),
        ("Nre"                       , self.Nre),
        ("Nw"                        , self.Nw),
        ("e/D"                       , self.eD),
        ("fmBF"                      , self.fmBF),
        ("dp/dz"                     , self.dpdz),
        ("A"                         , self.A),
        ("B"                         , self.B),
        ("dens_correction"           , self.dens_correction),
        ("transisi"                  , self.transisi),
        ("BLColumn"                  , self.BLColumn),
        ("EkComplement"              , self.EkComplement),
        ("Dp/dz_total"               , self.Dpdz_total),
        ("Dptot"                     , self.Dptot),
        ("P2"                        , self.P2),
        ("Re_Homogen"                , self.ReHomogen),
        ("BRColumn_Homogen"          , self.BRColumnHomogen),
        ("fff_Homogen"               , self.fffHomogen),
        ("mff_Homogen"               , self.mffHomogen),
        ("BUColumn_Homogen"          , self.BUColumnHomogen),
        ("DeltaPGravity_Homogen"     , self.DeltaPGravityHomogen),
        ("acceleration_Homogen"      , self.accelerationHomogen),
        ("DeltaPfriksi_Homogen"      , self.DeltaPfriksiHomogen),
        ("DeltaPtotal_Homogen"       , self.DeltaPtotalHomogen),
        ("P2_Homogen"                , self.P2Homogen),
        ("rho__Homogen"              , self.rho_Homogen),
        ("velocity_Homogen"          , self.velocityHomogen),
        ("Ep_Homogen"                , self.EpHomogen),
        ("Ek_Homogen"                , self.EkHomogen),
        ("H2_Homogen"                , self.H2Homogen),
        ("Tanradian"                 , self.Tanradian),
        ("T2_Homogen"                , self.T2Homogen),
        ])
        # print self.data.keys()
        print "==============================="
        print "Harusnya:" +  unicode(self.lenofdata)
        for x in self.columnnames:
            if (eval("len(self." + x + ") != self.lenofdata")):
                print x
                print eval("len(self." + x + ")")
        df = pd.DataFrame(collections.OrderedDict(self.data))
        if (os.path.isfile("pepeg.csv")):
            os.remove("pepeg.csv")
        df.to_csv(r'pepeg.csv')

        print df

SEGMENT_CONST = 3 

def main():

    # Table Variable

    print "WHP (bar)"
    whp = float(raw_input())
    print "Massrate (Kg/s)"
    massrate = float(raw_input())
    print "Enthalpy (KJ/kg)"
    enthalpy = float(raw_input())
    print "Pwf (bar)"
    pwf = float(raw_input())

    currentTableInput = inputTable(whp, massrate, enthalpy, pwf)   

    loopInput = False
    n = 0

    while not loopInput:
        
        n = n + 1
        print "Loop input baris", n
        print "MD(meter):"
        md = float(raw_input())
        print "Angle:"
        angle = float(raw_input())
        print "Diameter(m):"
        diameter = float(raw_input())
        print "Roughn(m):"
        roughness = float(raw_input())

        elemListSubinput = OneInput(md, angle, diameter, roughness)

        currentTableInput.subTable.append(elemListSubinput)
        
        print "Stop input? y/n"
        loopStop = raw_input()
        if loopStop == "y" :
            loopInput = True
    
    currentTableInput.printl()

    currentDataframe = DataFrameSteam(currentTableInput)

    currentDataframe.secondIteration()
    currentDataframe.printl()

    

main()