from iapws import IAPWS97
import numpy

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


def main():

    # Table Variable
    tableAll = Table([])

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

main()