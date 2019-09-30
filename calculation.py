import numpy as np
import pandas as pd

PI_CONST = 3.14159265358979323

# 0.25*PI()*D7^2
def area(d):
    return 0.25*PI_CONST*d**2

def velocity(m,rho,a):
    return m/(rho*a)

def vsl(x,m,rhoL,a):
    return (1-x)*m / (rhoL*a)

def vsg(x,m,rhoG,a):
    return x*m / (rhoG*a)

def noslipHoldup(vsl,vsg):
    return vsl / (vsl+vsg)

def liquidVelocityNumb(vsl,rhoL,g,delta):
    return vsl * ((rhoL / g*delta)**0,25)

def gasVelocityNumb(vsg,rhoL,g,delta):
    return vsg * ((rhoL / g*delta)**0.25)

def diameterNum(d,rhoL,g,delta):
    return d * (((rhoL*g)/delta)**0.5)
    
def liquidViscosityNum(miul,g,rhoL,delta):
    return miul * ((g/(rhoL*delta**3))**0.25)

def lb(l1,l2,nlv):
    return l1 + l2*nlv

def ls(nlv):
    return 50 + 36*nlv

def lm(nlv):
    return 75 + ((84*nlv)*0.75)

def f6accent(nd,f6):
    return 0.029*nd + f6

def sBubble(f1,f2,nlv,f3,ngv):
    return f1 + f2*nlv + f3 ((ngv/(1+nlv))**2)

def sSlug(f5,ngv,f6accent,f7,nlv):
    return (1+f5) * (ngv**0.982 + f6accent) / ((1 + f7*nlv)**2)

def slipVelForBubbleOrSlug(s,rhoL,deltaL,g):
    return s / ((rhoL / (deltaL*g))**0.25)

def re(rhoL,vsl,d,miul):
    return (rhoL * vsl * d) / miul

def r(vsg,vsl):
    return vsg/vsl

def AU3(roughness,diameter,re):
    # return ((roughness/diameter)**1.1098)2.8257 + ((7.419/re)**0.8981)
    return ((roughness/diameter)**1.1098)*2.8257 + ((7.419/re)**0.8981)

def fanningFF(roughness,diameter,re,au3):
    return 1/((4*np.log10(roughness/diameter/3.7065 - 5.0452/re*np.log10(au3)))**2)

def moddyFrictionFactor(fff):
    return 4*fff