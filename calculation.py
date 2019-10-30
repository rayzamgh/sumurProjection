import numpy as np
import pandas as pd
import math

PI_CONST = 3.14159265358979323
RADIANS = 0.0174533

CRK5 = 2.17698613994
CRK6 = 0.0340019622762
CRK7 = -0.00186762652262
CRK8 = 0.0000164593735483

CRU5 = 1.1949704158
CRU6 = 21.2171276373
CRU7 = -1318.1143978
CRU8 = 26922.1917491
CRU12 = -0.359606790974
CRU13 = 95.0889763613
CRU14 = 29.6377912629
CRU15 = 47.6519638263

CRY5 = -0.281735075074 
CRY6 = 33.4691605435
CRY7 = 24.1085244714
CRY8 = 14.140002265
CRY12 = 0.198962683949
CRY13 = 165.610849564
CRY14 = 40.5602334868
CRY15 = -0.605063289872

CRAC5 = -130.359865362
CRAC6 = 0.0118723787963
CRAC7 = 65.4413706125
CRAC8 = 0.672287359402
CRAC12 = 0.0271606181764
CRAC13 = 0.104002271509
CRAC14 = -0.049428382393
CRAC15 = 0.00919779154689

CRAH5 = 0.156607348381
CRAH6 = 0.000403183935144
CRAH7 = -0.061333623307
CRAH12 = 0.000567516268889
CRAH13 = 2901.14346223
CRAH14 = -1.69325583209

CRAK5 = 4.5703803465
CRAK6 = -620.727124902
CRAK7 = 1481.17551769
CRAK8 = 32276.8266466
CRAK12 = -1.18005847056
CRAK13 = 63.7552762686
CRAK14 = -524.284673377
CRAK15 = 2215.30455836

CRAU5 = 1.54774823716
CRAU6 = 1.37639926261
CRAU7 = 0.502754698143
CRAU8 = -0.734838089563

CRAO5 = 1.73605330498
CRAO6 = 183.918365132
CRAO7 = 2.21480948062
CRAO8 = -3.33101005192

CRAO12 = 0.180686525103
CRAO13 = 0.0272344110216
CRAO14 = 0.0199653895751
CRAO15 = 0.714379712487

CRP5 = 0.17668956841
CRP6 = 0.020194360332
CRP7 = -0.00000278914571449
CRP8 = -0.00000144116520574

#  0,25*PI()*D3^2
# area
# d 		= D3
def funcN(d):
    return 0.25*PI_CONST*d**2

def funcF(i, bp, bz):
	if (i < 0.9999) and (i > 0.0001) :
		return bp
	else:
		return bz

# M/(rho*A)
# G3/(J3*N3)
# velocity
# m 		= G3
# rho	= J3
# a		= N3
def funcO(m,rho,a):
    return m/(rho*a)

# (1-x)*M/(rhol*A)
# (1-I3)*G3/(K3*N3)
# vsl
# x		= I3
# m		= G3
# rhoL	= K3
# a		= N3
def funcP(x,m,rhoL,a):
    return (1-x)*m / (rhoL*a)
	
# x*M/(rhog*A)
# I3*G3/(L3*N3)
# vsg
# x		= I3
# m		= G3
# rhoG	= L3
# a		= N3
def funcQ(x,m,rhoG,a):
    return x*m / (rhoG*a)

# vsl/(vsl+vsg)
# P3/(P3+Q3)
# noslipHoldup
# vsl	= P3
# vsg	= Q3
def funcV(vsl,vsg):
	return vsl / (vsl+vsg)

# vsl * ((rhoL / g/delta)**0.25)
# P3*(K3/M3/U3)^0,25
# liquidVelocityNumb
# vsl	= P3
# rhoL	= K3
# g		= M3
# delta	= U3
def funcW(vsl,rhoL,g,delta):
    return vsl * ((rhoL / g / delta)**0.25)

# vsg * ((rhoL / g/delta)**0.25)
# Q3*(K3/U3/M3)^0,25
# gasVelocityNumb
# vsg	= Q3
# rhoL	= K3
# g		= U3
# delta	= M3
def funcX(vsg,rhoL,g,delta):
    return vsg * ((rhoL / g/delta)**0.25)

# d * (((rhoL*g)/delta)**0.5)
# D3*(K3*M3/U3)^0,5
# diameterNum
# d		= D3
# rhoL	= K3
# g		= M3
# delta	= U3
def funcY(d,rhoL,g,delta):
    return d * (((rhoL*g)/delta)**0.5)

# miul * ((g/(rhoL*delta**3))**0.25)
# S3*(M3/K3/U3^3)^0,25
# liquidviscositynum
# miul	= S3
# g		= M3
# rhoL	= K3
# delta	= U3

def funcZ(miul,g,rhoL,delta):
    return miul * ((g/(rhoL*delta**3))**0.25)

# l1 + l2*nlv
# AA3+AB3*W3
# lb
# l1		= AA3
# l2		= AB3
# nlv	= W3
def funcAC(l1,l2,nlv):
    return l1 + l2*nlv

# 50 + 36*nlv
# 50+36*W3
# ls
# nlv	= W3
def funcAD(nlv):
    return 50 + 36*nlv

# 75 + (84*nlv**0.75)
# 75+84*W3^0,75
# lm
# nlv	= W3
def funcAE(nlv):
    return 75 + (84*(nlv**0.75))

# 0.029*nd + f6
# 0,029*Y3+AK3
# f6'  (F6 accent)
# nd		= Y3
# f6		= AK3
def funcAL(nd,f6):
    return 0.029*nd + f6

# f1 + f2*nlv + f3 ((ngv/(1+nlv))**2)
# AF3+AG3*W3+AH3*(X3/(1+W3))^2
# Sbubble
# f1		= AF3
# f2		= AG3
# nlv	= W3
# f3		= AH3
# ngv	= X3
def funcAO(f1,f2,nlv,f3,ngv):
    return f1 + f2*nlv + f3 * ((ngv/(1+nlv))**2)

# (1+f5) * (ngv**0.982 + f6accent) / ((1 + f7*nlv)**2)
# (1+AJ3)*(X3^0,982+AL3)/(1+AM3*W3)^2
# sSlug
# f5			= AJ3
# ngv		= X3
# f6accent	= AL3
# f7			= AM3
# nlv		= W3
def funcAP(f5,ngv,f6accent,f7,nlv):
    return (1+f5) * (ngv**0.982 + f6accent) / ((1 + f7*nlv)**2)

# s / ((rhoL / (deltaL*g))**0.25)
# AQ3/(K3/(M3*U3))^0,25
# slipVelForBubbleOrSlug
# s		= AQ3
# rhoL	= K3
# deltaL	= M3
# g		= U3
def funcAR(s,rhoL,deltaL,g):
    return s / ((rhoL / (deltaL*g))**0.25)

# (rhoL * vsl * d) / miul
# K3*P3*D3/S3
# re
# rhoL	= K3
# vsl	= P3
# d		= D3
# miuL	= S3
def funcAT(rhoL,vsl,d,miuL):
    return (rhoL * vsl * d) / miuL

# vsg/vsl
# Q3/P3
# r
# vsg	= Q3
# vsl	= P3
def funcAX(vsg,vsl):
    return vsg/vsl

# ((roughness/diameter)**1.1098)/2.8257 + ((7.419/re)**0.8981)
# ((E3/D3)^1,1098)/2,8257+(7,149/AT3)^0,8981
# lambda /\
# roughness	= E3
# diameter	= D3
# re			= AT3
def funcAU(roughness,diameter,re):
    #  return ((roughness/diameter)**1.1098)/2.8257 + ((7.419/re)**0.8981)
    return ((roughness/diameter)**1.1098)/2.8257 + ((7.419/re)**0.8981)

# 1/((4*np.log10(roughness/diameter/3.7065 - 5.0452/re*np.log10(au)))**2)
# 1/(4*LOG10(E3/D3/3,7065-5,0452/AT3*LOG10(AU3)))^2
# fanningFF
# roughness	= E3
# diameter	= D3
# re			= AT3
# au			= AU3
def funcAV(roughness,diameter,re,au):
    return 1/((4*np.log10(roughness/diameter/3.7065 - 5.0452/re*np.log10(au)))**2)

# 4*fff
# 4*AV3
# moddyFrictionFactor
# fff	= AV3
def funcAW(fff):
    return 4*fff

#  x = H3
#  y = CD3
#  z = CC3
#  H3+(CD3+CC3)
def funcCE(x, y, z):
	return x + y + z


#  0.5*(O3^2-CB3^2)/10^3
#  x = O3
#  y = CB3
def funcCD(x, y):
	return 0.5 * (x**2 - y**2) / (10**3)

#  -M3*(B4-B3)/10^3
#  x = M3
#  y = B4
#  z = B3
def funcCC(x, y, z):
	return -x*(y-z)/10**3

#  G3/(CA3*N3)
  #  x = G3
#  y = CA3
#  z = N3
def funcCB(x, y, z):
	return x/(y*z)

#  -BY3+F3
#  x = BY3
#  y= F3
def funcBZ(x, y):
	return -x+y

#  (BV3+BX3)/BW3
#  x = BV3
#  y = BX3
#  z = BW3
def funcBY(x, y, z):
	return (x+y)/z

#  (0.5*BT3*(B4-B3)*J3*O3^2)/D3/10^5
#  x = BT3
#  y = B4
#  z = B3
#  a = J3
#  b = O3
#  c = D3 
def funcBX(x, y, z, a, b, c):
	return (0.5*x*(y-z)*a*b**2)/c/(10**5)

#  1-J3*(O3^2)/10^5/F3
#  x = J3
#  y = O3
#  z = F3
def funcBW(x, y, z):
	return 1-(x*(y**2)/10**5/z)

#  J3*M3*(B4-B3)*COS(RADIANS(C3))/(10^5)
#  x = J3
#  y = M3
#  z = B4
#  a = B3
#  b = C3
def funcBV(x, y, z, a, b):
	return(x*y*(z-a)*np.cos(np.radians(b))/10**5)

#  TAN(RADIANS(C3))
#  x = C3
def funcBU(x):
	return np.tan(np.radians(x))

#  4*BS3
#  x = BS3
def funcBT(x):
	return 4*x

#  1/(4*LOG10(E3/D3/3.7065-5.0452/BQ3*LOG10(BR3)))^2
#  x = E3
#  y = D3
#  z = BQ3
#  a = BR3
def funcBS(x, y, z, a):
	return 1/math.pow((4*np.log10(x/y/3.7065 - 5.0452/z*np.log10(a))),2)

#  ((E3/D3)^1.1098)/2.8257+(7.149/BQ3)^0.8981
#  x = E3
#  y = D3
#  z = BQ3
def funcBR(x, y, z):
	return ((x/y)**1.1098)/2.8257+(7.149/z)**0.8981

#  J3*O3*D3/R3
#  x = J3
#  y = O3
#  z = D3
#  a = R3
def funcBQ(x, y, z, a):
	return x*y*z/a

#  -BO3+F3
#  x = BO3
#  y = F3
def funcBP(x, y):
	return -x+y

#  BN3*(B4-B3)*COS(RADIANS(C3))
#  x = BN3 
#  y = B4
#  z = B3
#  a = C3
def funcBO(x, y, z, a):
	return x*(y-z)*np.cos(np.radians(a))

#  (BK3+BL3)/BM3
#  x = BK3
#  y = BL3
#  z = BM3
def funcBN(x, y, z):
	return (x+y)/z

#  1-L3*(O3*Q3)/10^5/F3
#  x = L3
#  y = O3
#  z = Q3
#  a = F3
def funcBM(x, y, z, a):
	return 1-x*(y*z)/10**5/a

#  M3*(AS3*K3+(1-AS3)*L3)/10^5
#  x = M3
#  y = AS3
#  z = K3
#  a = L3
def funcBL(x, y, z, a):
	return x*(y*z+(1-y)*a)/10**5

#  IF(AN3="transition",BH3*BG3+BI3*(BF3*L3*M3*Q3^2)/2/D3/10^5,BG3)
#  x = AN3
#  y = BH3
#  z = BG3
#  a = BI3
#  b = BF3
#  c = L3
#  d = M3
#  e = Q3
#  f = D3
#  g = BG3
def funcBK(x, y, z, a, b, c, d, e, f, g):
	if(x == "transition"):
		return y*z+a*(b*c*d*e**2)/2/f/10**5
	else:
		return g

#  L3*X3/AE3
#  x = L3
#  y = X3
#  z = AE3
def funcBJ(x, y, z):
	return x*y/z

#  (X3-AD3)/(AE3-AD3)
#  x = X3
#  y = AD3
#  z = AE3
def funcBI(x, y, z):
	return (x-y)/(z-y)

#  (AE3-X3)/(AE3-AD3)
#  x = AE3
#  y = X3
#  z = AD3
def funcBH(x, y, z):
	return (x-y)/(x-z)

#  IF(AN3="Mist",(BF3*L3*Q3^2)/2/D3,BB3*K3*P3*O3/2/D3)/10^5
#  x = AN3
#  y = BF3
#  z = L3
#  a = Q3
#  b = D3
#  c = BB3
#  d = K3
#  e = P3
#  f = O3
def funcBG(x, y, z, a, b, c, d, e, f):
	if(x == "Mist"):
		return (y*z*a**2)/2/b/10**5
	else:
		return c*d*e*f/2/b/10**5

#  IF(BE3>0.005,4*(1/(4*LOG(0.027*BE3))^2+0.067*BE3^1.73),AW3)
#  x = BE3
#  y = AW3
def funcBF(x, y):
	if(x > 0.005):
		return 4 * (1/(4*np.log10(0.027*x))**2+0.067*x**1.73)
	else:
		return y

#  IF(BD3<0.005,34*U3/L3/Q3/D3,174.8*U3*(BD3^0.302)/L3/(Q3^2)/D3)
#  x = BD3
#  y = U3
#  z = L3
#  a = Q3
#  b = D3
def funcBE(x, y, z, a, b):
	if(x < 0.005):
		return 34*y/z/a/b
	else:
		return 8*y*(x**0.302)/z/(a**2)/b

#  ((Q3*S3)^2)*L3/K3/U3
#  x = Q3
#  y = S3
#  z = L3
#  a = K3
#  b = U3
def funcBD(x, y, z, a, b):
	return ((x*y)**2)*z/a/b

#  L3*Q3*D3/T3
#  x = L3
#  y = Q3
#  z = D3
#  a = T3
def funcBC(x, y, z, a):
	return x*y*z/a

#  AW3*AZ3/BA3
#  x = AW3
#  y = AZ3
#  z = BA3
def funcBB(x, y, z):
	return x*y/z

#  1+AW3*(AX3/50)^0.5
#  x = AW3
#  y = AX3
def funcBA(x, y):
	return 1+x*(y/50)**0.5

#  IF(AY3<0.45,1,'Chart Regresion'!$AU$5-'Chart Regresion'!$AU$6*EXP(-'Chart Regresion'!$AU$7*AY3^'Chart Regresion'!$AU$8))
#  x = AY3
#  
def funcAZ(x):
	if(x < 0.45):
		return 1
	else:
		return CRAU5-CRAU6*np.exp(-CRAU7*x**CRAU8)

#  (AW3*AX3*Y3^(2/3))/P3
#  x = AW3
#  y = AX3
#  z = Y3
#  a = P3
def funcAY(x, y, z, a):
	return (x * y * z**(float(2)/3)/a)

#  IF(AN3="Mist",(P3/O3),(AR3-O3+SQRT((O3-AR3)^2+4*AR3*P3))/(2*AR3))
#  x = AN3
#  y = P3
#  z = O3
#  a = AR3
def funcAS(x, y, z, a):
	if(x == "Mist"):
		return (y/z)
	else:
		return (a-z+np.sqrt((z-a)**2+4*a*y))/(2*a)

#  IF(AN3="Bubble",AO3,AP3)
#  x = AN3
#  y = AO3
#  z = AP3
def funcAQ(x, y, z):
	if(x == "Bubble"):
		return y
	else:
		return z

#  IF(X3<=AC3,"Bubble",IF(X3<=AD3,"Slug",IF(X3<=AE3,"Transition","Mist")))
#  x = X3
#  y = AC3
#  z = AD3
#  a = AE3
def funcAN(x, y, z, a):
	if(x <= y):
		return "Bubble"
	else:
		if(x <= z):
			return "Slug"
		else:
			if(x <= a):
				return "Transition"
			else:
				return "Mist"

#  ('Chart Regresion'!$AO$12*'Chart Regresion'!$AO$13+'Chart Regresion'!$AO$14*(Z3^'Chart Regresion'!$AO$15))/('Chart Regresion'!$AO$13+(Z3^'Chart Regresion'!$AO$15))
#  x = Z3
def funcAM(x):
	return (CRAO12*CRAO13 + CRAO14*(x**CRAO15))/(CRAO13+(x**CRAO15))

#  IF(Z3<0.016,
#  	('Chart Regresion'!$AK$5+'Chart Regresion'!$AK$6*Z3)/(1+'Chart Regresion'!$AK$7*Z3+'Chart Regresion'!$AK$8*Z3^2),
#  	IF(Z3<0.07,
#  		'Chart Regresion'!$AK$12+'Chart Regresion'!$AK$13*Z3+'Chart Regresion'!$AK$14*(Z3^2)+'Chart Regresion'!$AK$15*(Z3^3),
#  		('Chart Regresion'!$AO$5*'Chart Regresion'!$AO$6+'Chart Regresion'!$AO$7*(Z3^'Chart Regresion'!$AO$8))/($BS$6+(Z3^'Chart Regresion'!$AO$8))))
#  x = Z3
#  y = $BS$6 		
def funcAK(x, y):
	if(x < 0.016):
		return (CRAK5 + CRAK6*x)/(1+CRAK7*x+CRAK8*(x**2))
	else:
		if(x < 0.07):
			return (CRAK12 + CRAK13*x + CRAK14*(x**2) + CRAK15*(x**3))
		else:
			return (CRAO5*CRAO6 + CRAO7*(x**CRAO8))/(y+(x**CRAO8))


#  IF(Z3<0.05,
#  	'Chart Regresion'!$AH$5*('Chart Regresion'!$AH$6^Z3)*(Z3^'Chart Regresion'!$AH$7),
#  	IF(Z3<0.5,
#  		'Chart Regresion'!$AH$12*('Chart Regresion'!$AH$13^Z3)*(Z3^'Chart Regresion'!$AH$14),
#  		'Chart Regresion'!$AC$12+'Chart Regresion'!$AC$13*Z3+'Chart Regresion'!$AC$14*(Z3^2)+'Chart Regresion'!$AC$15*(Z3^3)))
#  x = Z3
def funcAJ(x):
	if(x < 0.05):
		return CRAH5*(CRAH6**x)*(x**CRAH7)
	else:
		if(x < 0.5):
			return CRAH12*(CRAH13**x)*(x**CRAH14)
		else:
			return CRAC12+CRAC13*x+CRAC14*(x**2)+CRAC15*(x**3)

#  IF(Z3<0.195,
#  	('Chart Regresion'!$AC$5*'Chart Regresion'!$AC$6+'Chart Regresion'!$AC$7*Z3^'Chart Regresion'!$AC$8)/('Chart Regresion'!$AC$6+Z3^'Chart Regresion'!$AC$8),
#  	56)
#  x = Z3
def funcAI(x):
	if(x < 0.195):
		return (CRAC5*CRAC6+CRAC7*x**CRAC8)/(CRAC6+x**CRAC8)
	else:
		return 56

#  IF(Z3<0.04,
#  	0.86,
#  	('Chart Regresion'!$Y$12+'Chart Regresion'!$Y$13*Z3)/(1+'Chart Regresion'!$Y$14*Z3+'Chart Regresion'!$Y$15*Z3^2))
#  x = Z3
def funcAH(x):
	if(x < 0.04):
		return 0.86
	else:
		return (CRY12+CRY13*x)/(1+CRY14*x+CRY15*x**2)

#  IF(Z3<0.016,
#  	0.25,
#  	('Chart Regresion'!$Y$5+'Chart Regresion'!$Y$6*Z3)/(1+'Chart Regresion'!$Y$7*Z3+'Chart Regresion'!$Y$8*Z3^2))
#  x = Z3
#  
def funcAG(x):
	if(x < 0.016):
		return 0.25
	else:
		return (CRY5+CRY6*x)/(1+CRY7*x+CRY8*x**2)

#  IF(Z3<=0.03,
#  	'Chart Regresion'!$U$5+'Chart Regresion'!$U$6*Z3+'Chart Regresion'!$U$7*(Z3^2)+'Chart Regresion'!$U$8*(Z3^3),
#  	('Chart Regresion'!$U$12+'Chart Regresion'!$U$13*Z3)/(1+'Chart Regresion'!$U$14*Z3+'Chart Regresion'!$U$15*(Z3^2)))
#  x = Z3
def funcAF(x):
	if(x <= 0.03):
		return CRU5 + CRU6*x + CRU7*(x**2) + CRU8*(x**3)
	else:
		return (CRU12 + CRU13*x) / (1 + CRU14*x + CRU15*(x**2))

#  IF(Y3<30,
#  	2,
#  	IF(Y3<70,
#  		'Chart Regresion'!$K$5+'Chart Regresion'!$K$6*Y3+'Chart Regresion'!$K$7*(Y3^2)+'Chart Regresion'!$K$8*(Y3^3),
#  		1))
#  x = Y3
def funcAA(x):
	if(x < 30):
		return 2
	else:
		if(x < 70):
			return CRK5 + CRK6 * x + CRK7 * (x**2)  + CRK8 * (x**3)
		else :
			return 1

# =IF(Y3<70;
#  'Chart Regresion'!$P$5+'Chart Regresion'!$P$6*Y3+'Chart Regresion'!$P$7*(Y3^2)+'Chart Regresion'!$P$8*(Y3^3);1,1)
#  x = Y3
def funcAB(x):
	if (x < 70):
		return CRP5 + CRP6 * x + CRP7 * (x ** 2) + CRP8 * (x ** 3)
	else:
		return 1.1