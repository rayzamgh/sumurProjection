"""***********************************************************************************************************
* Water and steam properties according to IAPWS IF-97                                                     *
* By Magnus Holmgren, www.x-eng.com                                                                       *
* The steam tables are free and provided as is.                                                           *
* We take no responsibilities for any errors in the code or damage thereby.                               *
* You are free to use, modify and distribute the code as long as authorship is properly acknowledged.     *
* Please notify me at magnus@x-eng.com if the code is used in commercial applications                     *
***********************************************************************************************************'

 The code is also avalibale for matlab at www.x-eng.com
*Contents.
*1 Calling functions
*1.1
*1.2 Temperature (T)
*1.3 Pressure (p)
*1.4 Enthalpy (h)
*1.5 Specific Volume (v)
*1.6 Density (rho)
*1.7 Specific entropy (s)
*1.8 Specific internal energy (u)
*1.9 Specific isobaric heat capacity (Cp)
*1.10 Specific isochoric heat capacity (Cv)
*1.11 Speed of sound
*1.12 Viscosity
*1.13 Prandtl
*1.14 Kappa
*1.15 Surface tension
*1.16 Heat conductivity
*1.17 Vapour fraction
*1.18 Vapour Volume Fraction

*2 IAPWS IF 97 Calling functions
*2.1 Functions for region 1
*2.2 Functions for region 2
*2.3 Functions for region 3
*2.4 Functions for region 4
*2.5 Functions for region 5

*3 Region Selection
*3.1 Regions as a function of pT
*3.2 Regions as a function of ph
*3.3 Regions as a function of ps
*3.4 Regions as a function of hs
*3.5 Regions as a function of p and rho

4 Region Borders
4.1 Boundary between region 1 and 3.
4.2 Region 3. pSat_h and pSat_s
4.3 Region boundary 1to3 and 3to2 as a functions of s

5 Transport properties
5.1 Viscosity (IAPWS formulation 1985)
5.2 Thermal Conductivity (IAPWS formulation 1985)
5.3 Surface Tension

6 Units
***********************************************************************************************************
*1 Calling functions                                                                                      *
***********************************************************************************************************
***********************************************************************************************************
*1.1
***********************************************************************************************************
*1.2 Temperature
***********************************************************************************************************
*1.3 Pressure (p)
***********************************************************************************************************
*1.4 Enthalpy (h)
***********************************************************************************************************
*1.5 Specific Volume (v)
***********************************************************************************************************
*1.6 Density (rho)
 Density is calculated as 1/v
***********************************************************************************************************
*1.7 Specific entropy (s)
***********************************************************************************************************
*1.8 Specific internal energy (u)
***********************************************************************************************************
*1.9 Specific isobaric heat capacity (Cp)
***********************************************************************************************************
*1.10 Specific isochoric heat capacity (Cv)
***********************************************************************************************************
*1.11 Speed of sound
***********************************************************************************************************
*1.12 Viscosity
***********************************************************************************************************
*1.13 Prandtl
***********************************************************************************************************
*1.14 Kappa
***********************************************************************************************************
*1.15 Surface tension
***********************************************************************************************************
*1.16 Thermal conductivity
***********************************************************************************************************
*1.17 Vapour fraction
***********************************************************************************************************
*1.18 Vapour Volume Fraction
***********************************************************************************************************
*2 IAPWS IF 97 Calling functions                                                                          *
***********************************************************************************************************

***********************************************************************************************************
*2.1 Functions for region 1
***********************************************************************************************************
*2.2 Functions for region 2
***********************************************************************************************************
*2.3 Functions for region 3
***********************************************************************************************************
*2.4 Functions for region 4
***********************************************************************************************************
*2.5 Functions for region 5
***********************************************************************************************************
*3 Region Selection
***********************************************************************************************************
*3.1 Regions as a function of pT
***********************************************************************************************************
*3.2 Regions as a function of ph
***********************************************************************************************************
*3.3 Regions as a function of ps
***********************************************************************************************************
*3.4 Regions as a function of hs
***********************************************************************************************************
*3.5 Regions as a function of p and rho
***********************************************************************************************************
*4 Region Borders
***********************************************************************************************************
***********************************************************************************************************
*4.1 Boundary between region 2 and 3.
***********************************************************************************************************
*4.2 Region 3. pSat_h and pSat_s
***********************************************************************************************************
4.3 Region boundary 1to3 and 3to2 as a functions of s
***********************************************************************************************************
*5 Transport properties
***********************************************************************************************************
*5.1 Viscosity (IAPWS formulation 1985, Revised 2003)
***********************************************************************************************************
***********************************************************************************************************
*5.2 Thermal Conductivity (IAPWS formulation 1985)
***********************************************************************************************************
5.3 Surface Tension
***********************************************************************************************************
*6 Units                                                                                      *
***********************************************************************************************************
"""

def CVErr(x):
    return None

def Tsat_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p >= 0.000611657 and p <= 22.06395 + 0.001:
        _ret = fromSIunit_T(T4_p(p))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Tsat_s(s):
    _ret = None
    s = toSIunit_s(s)
    if s > - 0.0001545495919 and s < 9.155759395:
        _ret = fromSIunit_T(T4_p(p4_s(s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def T_ph(p, h):
    _ret = None
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select0 = region_ph(p, h)
    if (_select0 == 1):
        _ret = fromSIunit_T(T1_ph(p, h))
    elif (_select0 == 2):
        _ret = fromSIunit_T(T2_ph(p, h))
    elif (_select0 == 3):
        _ret = fromSIunit_T(T3_ph(p, h))
    elif (_select0 == 4):
        _ret = fromSIunit_T(T4_p(p))
    elif (_select0 == 5):
        _ret = fromSIunit_T(T5_ph(p, h))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def T_ps(p, s):
    _ret = None
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select1 = region_ps(p, s)
    if (_select1 == 1):
        _ret = fromSIunit_T(T1_ps(p, s))
    elif (_select1 == 2):
        _ret = fromSIunit_T(T2_ps(p, s))
    elif (_select1 == 3):
        _ret = fromSIunit_T(T3_ps(p, s))
    elif (_select1 == 4):
        _ret = fromSIunit_T(T4_p(p))
    elif (_select1 == 5):
        _ret = fromSIunit_T(T5_ps(p, s))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def T_hs(h, s):
    _ret = None
    h = toSIunit_h(h)
    s = toSIunit_s(s)
    _select2 = Region_hs(h, s)
    if (_select2 == 1):
        _ret = fromSIunit_T(T1_ph(p1_hs(h, s), h))
    elif (_select2 == 2):
        _ret = fromSIunit_T(T2_ph(p2_hs(h, s), h))
    elif (_select2 == 3):
        _ret = fromSIunit_T(T3_ph(p3_hs(h, s), h))
    elif (_select2 == 4):
        _ret = fromSIunit_T(T4_hs(h, s))
    elif (_select2 == 5):
        _ret = CVErr("""xlErrValue""")
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def psat_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T <= 647.096 and T > 273.15:
        _ret = fromSIunit_p(p4_T(T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def psat_s(s):
    _ret = None
    s = toSIunit_s(s)
    if s > - 0.0001545495919 and s < 9.155759395:
        _ret = fromSIunit_p(p4_s(s))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def p_hs(h, s):
    _ret = None
    h = toSIunit_h(h)
    s = toSIunit_s(s)
    _select3 = Region_hs(h, s)
    if (_select3 == 1):
        _ret = fromSIunit_p(p1_hs(h, s))
    elif (_select3 == 2):
        _ret = fromSIunit_p(p2_hs(h, s))
    elif (_select3 == 3):
        _ret = fromSIunit_p(p3_hs(h, s))
    elif (_select3 == 4):
        _ret = fromSIunit_p(p4_T(T4_hs(h, s)))
    elif (_select3 == 5):
        _ret = CVErr("""xlErrValue""")
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def p_hrho(h, rho):
    _ret = None
    # High_Bound = Double()

    # Low_Bound = Double()

    # p = Double()

    # rhos = Double()
    #*Not valid for water or sumpercritical since water rho does not change very much with p.
    #*Uses iteration to find p.
    High_Bound = fromSIunit_p(100)
    Low_Bound = fromSIunit_p(0.000611657)
    p = fromSIunit_p(10)
    rhos = 1 / v_ph(p, h)
    while Abs(rho - rhos) > 0.0000001:
        rhos = 1 / v_ph(p, h)
        if rhos >= rho:
            High_Bound = p
        else:
            Low_Bound = p
        p = ( Low_Bound + High_Bound )  / 2
    _ret = p
    return _ret

def hV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        _ret = fromSIunit_h(h4V_p(p))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def hL_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        _ret = fromSIunit_h(h4L_p(p))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def hV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        _ret = fromSIunit_h(h4V_p(p4_T(T)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def hL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        _ret = fromSIunit_h(h4L_p(p4_T(T)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def h_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select4 = region_pT(p, T)
    if (_select4 == 1):
        _ret = fromSIunit_h(h1_pT(p, T))
    elif (_select4 == 2):
        _ret = fromSIunit_h(h2_pT(p, T))
    elif (_select4 == 3):
        _ret = fromSIunit_h(h3_pT(p, T))
    elif (_select4 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select4 == 5):
        _ret = fromSIunit_h(h5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def h_ps(p, s):
    _ret = None
    # xs = Double()
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select5 = region_ps(p, s)
    if (_select5 == 1):
        _ret = fromSIunit_h(h1_pT(p, T1_ps(p, s)))
    elif (_select5 == 2):
        _ret = fromSIunit_h(h2_pT(p, T2_ps(p, s)))
    elif (_select5 == 3):
        _ret = fromSIunit_h(h3_rhoT(1 / v3_ps(p, s), T3_ps(p, s)))
    elif (_select5 == 4):
        xs = x4_ps(p, s)
        _ret = fromSIunit_h(xs * h4V_p(p) +  ( 1 - xs )  * h4L_p(p))
    elif (_select5 == 5):
        _ret = fromSIunit_h(h5_pT(p, T5_ps(p, s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def h_px(p, x):
    _ret = None
    # hL = Double()

    # hV = Double()
    p = toSIunit_p(p)
    x = toSIunit_x(x)
    if x > 1 or x < 0 or p >= 22.064:
        _ret = CVErr("""xlErrValue""")
        return _ret
    hL = h4L_p(p)
    hV = h4V_p(p)
    _ret = fromSIunit_h(hL + x *  ( hV - hL ))
    return _ret

def h_Tx(T, x):
    _ret = None
    # hL = Double()

    # hV = Double()

    # p = Double()
    T = toSIunit_T(T)
    x = toSIunit_x(x)
    if x > 1 or x < 0 or T >= 647.096:
        _ret = CVErr("""xlErrValue""")
        return _ret
    p = p4_T(T)
    hL = h4L_p(p)
    hV = h4V_p(p)
    _ret = fromSIunit_h(hL + x *  ( hV - hL ))
    return _ret

def h_prho(p, rho):
    _ret = None
    # hL = Variant()

    # hV = Variant()

    # vL = Variant()

    # vV = Variant()

    # x = Double()
    p = toSIunit_p(p)
    rho = 1 / toSIunit_v(1 / rho)
    _select6 = Region_prho(p, rho)
    if (_select6 == 1):
        _ret = fromSIunit_h(h1_pT(p, T1_prho(p, rho)))
    elif (_select6 == 2):
        _ret = fromSIunit_h(h2_pT(p, T2_prho(p, rho)))
    elif (_select6 == 3):
        _ret = fromSIunit_h(h3_rhoT(rho, T3_prho(p, rho)))
    elif (_select6 == 4):
        if p < 16.529:
            vV = v2_pT(p, T4_p(p))
            vL = v1_pT(p, T4_p(p))
        else:
            vV = v3_ph(p, h4V_p(p))
            vL = v3_ph(p, h4L_p(p))
        hV = h4V_p(p)
        hL = h4L_p(p)
        x = ( 1 / rho - vL )  /  ( vV - vL )
        _ret = fromSIunit_h(( 1 - x )  * hL + x * hV)
    elif (_select6 == 5):
        _ret = fromSIunit_h(h5_pT(p, T5_prho(p, rho)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def vV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_v(v2_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_v(v3_ph(p, h4V_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def vL_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_v(v1_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_v(v3_ph(p, h4L_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def vV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_v(v2_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_v(v3_ph(p4_T(T), h4V_p(p4_T(T))))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def vL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_v(v1_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_v(v3_ph(p4_T(T), h4L_p(p4_T(T))))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def v_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select7 = region_pT(p, T)
    if (_select7 == 1):
        _ret = fromSIunit_v(v1_pT(p, T))
    elif (_select7 == 2):
        _ret = fromSIunit_v(v2_pT(p, T))
    elif (_select7 == 3):
        _ret = fromSIunit_v(v3_ph(p, h3_pT(p, T)))
    elif (_select7 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select7 == 5):
        _ret = fromSIunit_v(v5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def v_ph(p, h):
    _ret = None
    # xs = Double()

    # v4V = Double()

    # v4L = Double()
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select8 = region_ph(p, h)
    if (_select8 == 1):
        _ret = fromSIunit_v(v1_pT(p, T1_ph(p, h)))
    elif (_select8 == 2):
        _ret = fromSIunit_v(v2_pT(p, T2_ph(p, h)))
    elif (_select8 == 3):
        _ret = fromSIunit_v(v3_ph(p, h))
    elif (_select8 == 4):
        xs = x4_ph(p, h)
        if p < 16.529:
            v4V = v2_pT(p, T4_p(p))
            v4L = v1_pT(p, T4_p(p))
        else:
            v4V = v3_ph(p, h4V_p(p))
            v4L = v3_ph(p, h4L_p(p))
        _ret = fromSIunit_v(( xs * v4V +  ( 1 - xs )  * v4L ))
    elif (_select8 == 5):
        _ret = fromSIunit_v(v5_pT(p, T5_ph(p, h)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def v_ps(p, s):
    _ret = None
    # xs = Double()

    # v4V = Double()

    # v4L = Double()
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select9 = region_ps(p, s)
    if (_select9 == 1):
        _ret = fromSIunit_v(v1_pT(p, T1_ps(p, s)))
    elif (_select9 == 2):
        _ret = fromSIunit_v(v2_pT(p, T2_ps(p, s)))
    elif (_select9 == 3):
        _ret = fromSIunit_v(v3_ps(p, s))
    elif (_select9 == 4):
        xs = x4_ps(p, s)
        if p < 16.529:
            v4V = v2_pT(p, T4_p(p))
            v4L = v1_pT(p, T4_p(p))
        else:
            v4V = v3_ph(p, h4V_p(p))
            v4L = v3_ph(p, h4L_p(p))
        _ret = fromSIunit_v(( xs * v4V +  ( 1 - xs )  * v4L ))
    elif (_select9 == 5):
        _ret = fromSIunit_v(v5_pT(p, T5_ps(p, s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def rhoV_p(p):
    _ret = None
    _ret = 1 / vV_p(p)
    return _ret

def rhoL_p(p):
    _ret = None
    _ret = 1 / vL_p(p)
    return _ret

def rhoL_T(T):
    _ret = None
    _ret = 1 / vL_T(T)
    return _ret

def rhoV_T(T):
    _ret = None
    _ret = 1 / vV_T(T)
    return _ret

def rho_pT(p, T):
    _ret = None
    _ret = 1 / v_pT(p, T)
    return _ret

def rho_ph(p, h):
    _ret = None
    _ret = 1 / v_ph(p, h)
    return _ret

def rho_ps(p, s):
    _ret = None
    _ret = 1 / v_ps(p, s)
    return _ret

def sV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_s(s2_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_s(s3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def sL_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_s(s1_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_s(s3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def sV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_s(s2_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_s(s3_rhoT(1 /  ( v3_ph(p4_T(T), h4V_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def sL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_s(s1_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_s(s3_rhoT(1 /  ( v3_ph(p4_T(T), h4L_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def s_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select10 = region_pT(p, T)
    if (_select10 == 1):
        _ret = fromSIunit_s(s1_pT(p, T))
    elif (_select10 == 2):
        _ret = fromSIunit_s(s2_pT(p, T))
    elif (_select10 == 3):
        _ret = fromSIunit_s(s3_rhoT(1 / v3_ph(p, h3_pT(p, T)), T))
    elif (_select10 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select10 == 5):
        _ret = fromSIunit_s(s5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def s_ph(p, h):
    _ret = None
    # Ts = Double()

    # xs = Double()

    # s4V = Double()

    # s4L = Double()

    # v4V = Double()

    # v4L = Double()
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select11 = region_ph(p, h)
    if (_select11 == 1):
        _ret = fromSIunit_s(s1_pT(p, T1_ph(p, h)))
    elif (_select11 == 2):
        _ret = fromSIunit_s(s2_pT(p, T2_ph(p, h)))
    elif (_select11 == 3):
        _ret = fromSIunit_s(s3_rhoT(1 / v3_ph(p, h), T3_ph(p, h)))
    elif (_select11 == 4):
        Ts = T4_p(p)
        xs = x4_ph(p, h)
        if p < 16.529:
            s4V = s2_pT(p, Ts)
            s4L = s1_pT(p, Ts)
        else:
            v4V = v3_ph(p, h4V_p(p))
            s4V = s3_rhoT(1 / v4V, Ts)
            v4L = v3_ph(p, h4L_p(p))
            s4L = s3_rhoT(1 / v4L, Ts)
        _ret = fromSIunit_s(( xs * s4V +  ( 1 - xs )  * s4L ))
    elif (_select11 == 5):
        _ret = fromSIunit_s(s5_pT(p, T5_ph(p, h)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def uV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_u(u2_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_u(u3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def uL_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_u(u1_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_u(u3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def uV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_u(u2_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_u(u3_rhoT(1 /  ( v3_ph(p4_T(T), h4V_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def uL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_u(u1_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_u(u3_rhoT(1 /  ( v3_ph(p4_T(T), h4L_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def u_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select12 = region_pT(p, T)
    if (_select12 == 1):
        _ret = fromSIunit_u(u1_pT(p, T))
    elif (_select12 == 2):
        _ret = fromSIunit_u(u2_pT(p, T))
    elif (_select12 == 3):
        _ret = fromSIunit_u(u3_rhoT(1 / v3_ph(p, h3_pT(p, T)), T))
    elif (_select12 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select12 == 5):
        _ret = fromSIunit_u(u5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def u_ph(p, h):
    _ret = None
    # Ts = Double()

    # xs = Double()

    # u4v = Double()

    # u4L = Double()

    # v4V = Double()

    # v4L = Double()
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select13 = region_ph(p, h)
    if (_select13 == 1):
        _ret = fromSIunit_u(u1_pT(p, T1_ph(p, h)))
    elif (_select13 == 2):
        _ret = fromSIunit_u(u2_pT(p, T2_ph(p, h)))
    elif (_select13 == 3):
        _ret = fromSIunit_u(u3_rhoT(1 / v3_ph(p, h), T3_ph(p, h)))
    elif (_select13 == 4):
        Ts = T4_p(p)
        xs = x4_ph(p, h)
        if p < 16.529:
            u4v = u2_pT(p, Ts)
            u4L = u1_pT(p, Ts)
        else:
            v4V = v3_ph(p, h4V_p(p))
            u4v = u3_rhoT(1 / v4V, Ts)
            v4L = v3_ph(p, h4L_p(p))
            u4L = u3_rhoT(1 / v4L, Ts)
        _ret = fromSIunit_u(( xs * u4v +  ( 1 - xs )  * u4L ))
    elif (_select13 == 5):
        Ts = T5_ph(p, h)
        _ret = fromSIunit_u(u5_pT(p, Ts))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def u_ps(p, s):
    _ret = None
    # x = Double()

    # u4v = Variant()

    # uLp = Variant()

    # uVp = Variant()

    # u4L = Double()
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select14 = region_ps(p, s)
    if (_select14 == 1):
        _ret = fromSIunit_u(u1_pT(p, T1_ps(p, s)))
    elif (_select14 == 2):
        _ret = fromSIunit_u(u2_pT(p, T2_ps(p, s)))
    elif (_select14 == 3):
        _ret = fromSIunit_u(u3_rhoT(1 / v3_ps(p, s), T3_ps(p, s)))
    elif (_select14 == 4):
        if p < 16.529:
            uLp = u1_pT(p, T4_p(p))
            uVp = u2_pT(p, T4_p(p))
        else:
            uLp = u3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p))
            uVp = u3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p))
        x = x4_ps(p, s)
        _ret = fromSIunit_u(( x * uVp +  ( 1 - x )  * uLp ))
    elif (_select14 == 5):
        _ret = fromSIunit_u(u5_pT(p, T5_ps(p, s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CpV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_Cp(Cp2_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_Cp(Cp3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CpL_p(p):
    _ret = None
    # T = Variant()

    # h = Variant()

    # v = Double()
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_Cp(Cp1_pT(p, T4_p(p)))
        else:
            T = T4_p(p)
            h = h4L_p(p)
            v = v3_ph(p, h4L_p(p))
            _ret = fromSIunit_Cp(Cp3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CpV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_Cp(Cp2_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_Cp(Cp3_rhoT(1 /  ( v3_ph(p4_T(T), h4V_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CpL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_Cp(Cp1_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_Cp(Cp3_rhoT(1 /  ( v3_ph(p4_T(T), h4L_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Cp_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select15 = region_pT(p, T)
    if (_select15 == 1):
        _ret = fromSIunit_Cp(Cp1_pT(p, T))
    elif (_select15 == 2):
        _ret = fromSIunit_Cp(Cp2_pT(p, T))
    elif (_select15 == 3):
        _ret = fromSIunit_Cp(Cp3_rhoT(1 / v3_ph(p, h3_pT(p, T)), T))
    elif (_select15 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select15 == 5):
        _ret = fromSIunit_Cp(Cp5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Cp_ph(p, h):
    _ret = None
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select16 = region_ph(p, h)
    if (_select16 == 1):
        _ret = fromSIunit_Cp(Cp1_pT(p, T1_ph(p, h)))
    elif (_select16 == 2):
        _ret = fromSIunit_Cp(Cp2_pT(p, T2_ph(p, h)))
    elif (_select16 == 3):
        _ret = fromSIunit_Cp(Cp3_rhoT(1 / v3_ph(p, h), T3_ph(p, h)))
    elif (_select16 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select16 == 5):
        _ret = fromSIunit_Cp(Cp5_pT(p, T5_ph(p, h)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Cp_ps(p, s):
    _ret = None
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select17 = region_ps(p, s)
    if (_select17 == 1):
        _ret = fromSIunit_Cp(Cp1_pT(p, T1_ps(p, s)))
    elif (_select17 == 2):
        _ret = fromSIunit_Cp(Cp2_pT(p, T2_ps(p, s)))
    elif (_select17 == 3):
        _ret = fromSIunit_Cp(Cp3_rhoT(1 / v3_ps(p, s), T3_ps(p, s)))
    elif (_select17 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select17 == 5):
        _ret = fromSIunit_Cp(Cp5_pT(p, T5_ps(p, s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CvV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_Cv(Cv2_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_Cv(Cv3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CvL_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_Cv(Cv1_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_Cv(Cv3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CvV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_Cv(Cv2_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_Cv(Cv3_rhoT(1 /  ( v3_ph(p4_T(T), h4V_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def CvL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_Cv(Cv1_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_Cv(Cv3_rhoT(1 /  ( v3_ph(p4_T(T), h4L_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Cv_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select18 = region_pT(p, T)
    if (_select18 == 1):
        _ret = fromSIunit_Cv(Cv1_pT(p, T))
    elif (_select18 == 2):
        _ret = fromSIunit_Cv(Cv2_pT(p, T))
    elif (_select18 == 3):
        _ret = fromSIunit_Cv(Cv3_rhoT(1 / v3_ph(p, h3_pT(p, T)), T))
    elif (_select18 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select18 == 5):
        _ret = fromSIunit_Cv(Cv5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Cv_ph(p, h):
    _ret = None
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select19 = region_ph(p, h)
    if (_select19 == 1):
        _ret = fromSIunit_Cv(Cv1_pT(p, T1_ph(p, h)))
    elif (_select19 == 2):
        _ret = fromSIunit_Cv(Cv2_pT(p, T2_ph(p, h)))
    elif (_select19 == 3):
        _ret = fromSIunit_Cv(Cv3_rhoT(1 / v3_ph(p, h), T3_ph(p, h)))
    elif (_select19 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select19 == 5):
        _ret = fromSIunit_Cv(Cv5_pT(p, T5_ph(p, h)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def Cv_ps(p, s):
    _ret = None
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select20 = region_ps(p, s)
    if (_select20 == 1):
        _ret = fromSIunit_Cv(Cv1_pT(p, T1_ps(p, s)))
    elif (_select20 == 2):
        _ret = fromSIunit_Cv(Cv2_pT(p, T2_ps(p, s)))
    elif (_select20 == 3):
        _ret = fromSIunit_Cv(Cv3_rhoT(1 / v3_ps(p, s), T3_ps(p, s)))
    elif (_select20 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select20 == 5):
        _ret = fromSIunit_Cv(Cv5_pT(p, T5_ps(p, s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def wV_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_w(w2_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_w(w3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def wL_p(p):
    _ret = None
    p = toSIunit_p(p)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            _ret = fromSIunit_w(w1_pT(p, T4_p(p)))
        else:
            _ret = fromSIunit_w(w3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def wV_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_w(w2_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_w(w3_rhoT(1 /  ( v3_ph(p4_T(T), h4V_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def wL_T(T):
    _ret = None
    T = toSIunit_T(T)
    if T > 273.15 and T < 647.096:
        if T <= 623.15:
            _ret = fromSIunit_w(w1_pT(p4_T(T), T))
        else:
            _ret = fromSIunit_w(w3_rhoT(1 /  ( v3_ph(p4_T(T), h4L_p(p4_T(T))) ), T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def w_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select21 = region_pT(p, T)
    if (_select21 == 1):
        _ret = fromSIunit_w(w1_pT(p, T))
    elif (_select21 == 2):
        _ret = fromSIunit_w(w2_pT(p, T))
    elif (_select21 == 3):
        _ret = fromSIunit_w(w3_rhoT(1 / v3_ph(p, h3_pT(p, T)), T))
    elif (_select21 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select21 == 5):
        _ret = fromSIunit_w(w5_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def w_ph(p, h):
    _ret = None
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select22 = region_ph(p, h)
    if (_select22 == 1):
        _ret = fromSIunit_w(w1_pT(p, T1_ph(p, h)))
    elif (_select22 == 2):
        _ret = fromSIunit_w(w2_pT(p, T2_ph(p, h)))
    elif (_select22 == 3):
        _ret = fromSIunit_w(w3_rhoT(1 / v3_ph(p, h), T3_ph(p, h)))
    elif (_select22 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select22 == 5):
        _ret = fromSIunit_w(w5_pT(p, T5_ph(p, h)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def w_ps(p, s):
    _ret = None
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    _select23 = region_ps(p, s)
    if (_select23 == 1):
        _ret = fromSIunit_w(w1_pT(p, T1_ps(p, s)))
    elif (_select23 == 2):
        _ret = fromSIunit_w(w2_pT(p, T2_ps(p, s)))
    elif (_select23 == 3):
        _ret = fromSIunit_w(w3_rhoT(1 / v3_ps(p, s), T3_ps(p, s)))
    elif (_select23 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select23 == 5):
        _ret = fromSIunit_w(w5_pT(p, T5_ps(p, s)))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def my_pT(p, T):
    _ret = None
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    _select24 = region_pT(p, T)
    if (_select24 == 4):
        _ret = CVErr("""xlErrValue""")
    elif (_select24 == 1) or (_select24 == 2) or (_select24 == 3) or (_select24 == 5):
        _ret = fromSIunit_my(my_AllRegions_pT(p, T))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def my_ph(p, h):
    _ret = None
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    _select25 = region_ph(p, h)
    if (_select25 == 1) or (_select25 == 2) or (_select25 == 3) or (_select25 == 5):
        _ret = fromSIunit_my(my_AllRegions_ph(p, h))
    elif (_select25 == 4):
        _ret = CVErr("""xlErrValue""")
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def my_ps(p, s):
    _ret = None
    _ret = my_ph(p, h_ps(p, s))
    return _ret

def Pr_pT(p, T):
    _ret = None
    # Cp = Double()

    # my = Double()

    # tc = Double()
    Cp = toSIunit_Cp(Cp_pT(p, T))
    my = toSIunit_my(my_pT(p, T))
    tc = toSIunit_tc(tc_pT(p, T))
    _ret = Cp * 1000 * my / tc
    return _ret

def Pr_ph(p, h):
    _ret = None
    # Cp = Double()

    # my = Double()

    # tc = Double()
    Cp = toSIunit_Cp(Cp_ph(p, h))
    my = toSIunit_my(my_ph(p, h))
    tc = toSIunit_tc(tc_ph(p, h))
    _ret = Cp * 1000 * my / tc
    return _ret

def Kappa_pT(p, T):
    _ret = None
    # Cp = Double()

    # Cv = Double()
    Cp = Cp_pT(p, T)
    Cv = Cv_pT(p, T)
    _ret = Cp / Cv
    return _ret

def Kappa_ph(p, h):
    _ret = None
    # Cp = Double()

    # Cv = Double()
    Cv = Cv_ph(p, h)
    Cp = Cp_ph(p, h)
    _ret = Cp / Cv
    return _ret

def st_t(T):
    _ret = None
    T = toSIunit_T(T)
    _ret = fromSIunit_st(Surface_Tension_T(T))
    return _ret

def st_p(p):
    _ret = None
    # T = Double()
    T = Tsat_p(p)
    T = toSIunit_T(T)
    _ret = fromSIunit_st(Surface_Tension_T(T))
    return _ret

def tcL_p(p):
    _ret = None
    # T = Double()

    # v = Double()
    T = Tsat_p(p)
    v = vL_p(p)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def tcV_p(p):
    _ret = None
    # T = Double()

    # v = Double()
    T = Tsat_p(p)
    v = vV_p(p)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def tcL_T(T):
    _ret = None
    # p = Variant()

    # v = Double()
    p = psat_T(T)
    v = vL_T(T)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def tcV_T(T):
    _ret = None
    # p = Variant()

    # v = Double()
    p = psat_T(T)
    v = vV_T(T)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def tc_pT(p, T):
    _ret = None
    # v = Double()
    v = v_pT(p, T)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def tc_ph(p, h):
    _ret = None
    # v = Double()

    # T = Double()
    v = v_ph(p, h)
    T = T_ph(p, h)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def tc_hs(h, s):
    _ret = None
    # p = Double()

    # v = Double()

    # T = Double()
    p = p_hs(h, s)
    v = v_ph(p, h)
    T = T_ph(p, h)
    p = toSIunit_p(p)
    T = toSIunit_T(T)
    v = toSIunit_v(v)
    _ret = fromSIunit_tc(tc_ptrho(p, T, 1 / v))
    return _ret

def x_ph(p, h):
    _ret = None
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    if p > 0.000611657 and p < 22.06395:
        _ret = fromSIunit_x(x4_ph(p, h))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def x_ps(p, s):
    _ret = None
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    if p > 0.000611657 and p < 22.06395:
        _ret = fromSIunit_x(x4_ps(p, s))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def vx_ph(p, h):
    _ret = None
    # vL = Double()

    # vV = Double()

    # xs = Double()
    p = toSIunit_p(p)
    h = toSIunit_h(h)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            vL = v1_pT(p, T4_p(p))
            vV = v2_pT(p, T4_p(p))
        else:
            vL = v3_ph(p, h4L_p(p))
            vV = v3_ph(p, h4V_p(p))
        xs = x4_ph(p, h)
        _ret = fromSIunit_vx(( xs * vV /  ( xs * vV +  ( 1 - xs )  * vL ) ))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def vx_ps(p, s):
    _ret = None
    # vL = Double()

    # vV = Double()

    # xs = Double()
    p = toSIunit_p(p)
    s = toSIunit_s(s)
    if p > 0.000611657 and p < 22.06395:
        if p < 16.529:
            vL = v1_pT(p, T4_p(p))
            vV = v2_pT(p, T4_p(p))
        else:
            vL = v3_ph(p, h4L_p(p))
            vV = v3_ph(p, h4V_p(p))
        xs = x4_ps(p, s)
        _ret = fromSIunit_vx(( xs * vV /  ( xs * vV +  ( 1 - xs )  * vL ) ))
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def v1_pT(p, T):
    _ret = None
    # i = Integer()

    # ps = Variant()

    # tau = Variant()

    # g_p = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32]
    J1 = [- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41]
    n1 = [0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26]
    ps = p / 16.53
    tau = 1386 / T
    g_p = 0
    for i in range(0, 1 + 33):
        g_p = g_p - n1(i) * I1(i) *  ( 7.1 - ps )  **  ( I1(i) - 1 )  *  ( tau - 1.222 )  ** J1(i)
    _ret = R * T / p * ps * g_p / 1000
    return _ret

def h1_pT(p, T):
    _ret = None
    # i = Integer()

    # ps = Variant()

    # tau = Variant()

    # g_t = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32]
    J1 = [- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41]
    n1 = [0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26]
    p = p / 16.53
    tau = 1386 / T
    g_t = 0
    for i in range(0, 1 + 33):
        g_t = g_t +  ( n1[i] *  ( 7.1 - p )  ** I1[i] * J1[i] *  ( tau - 1.222 )  **  ( J1[i] - 1 ) )
    _ret = R * T * tau * g_t
    return _ret

def u1_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g_t = Variant()

    # g_p = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32)
    J1 = Array(- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41)
    n1 = Array(0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26)
    p = p / 16.53
    tau = 1386 / T
    g_t = 0
    g_p = 0
    for i in range(0, 1 + 33):
        g_p = g_p - n1(i) * I1(i) *  ( 7.1 - p )  **  ( I1(i) - 1 )  *  ( tau - 1.222 )  ** J1(i)
        g_t = g_t +  ( n1(i) *  ( 7.1 - p )  ** I1(i) * J1(i) *  ( tau - 1.222 )  **  ( J1(i) - 1 ) )
    _ret = R * T *  ( tau * g_t - p * g_p )
    return _ret

def s1_pT(p, T):
    _ret = None
    # i = Integer()

    # g = Variant()

    # g_t = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32)
    J1 = Array(- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41)
    n1 = Array(0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26)
    p = p / 16.53
    T = 1386 / T
    g = 0
    g_t = 0
    for i in range(0, 1 + 33):
        g_t = g_t +  ( n1(i) *  ( 7.1 - p )  ** I1(i) * J1(i) *  ( T - 1.222 )  **  ( J1(i) - 1 ) )
        g = g + n1(i) *  ( 7.1 - p )  ** I1(i) *  ( T - 1.222 )  ** J1(i)
    _ret = R * T * g_t - R * g
    return _ret

def Cp1_pT(p, T):
    _ret = None
    # i = Integer()

    # G_tt = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32)
    J1 = Array(- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41)
    n1 = Array(0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26)
    p = p / 16.53
    T = 1386 / T
    G_tt = 0
    for i in range(0, 1 + 33):
        G_tt = G_tt +  ( n1(i) *  ( 7.1 - p )  ** I1(i) * J1(i) *  ( J1(i) - 1 )  *  ( T - 1.222 )  **  ( J1(i) - 2 ) )
    _ret = - R * T ** 2 * G_tt
    return _ret

def Cv1_pT(p, T):
    _ret = None
    # i = Integer()

    # g_p = Variant()

    # g_pp = Variant()

    # g_pt = Variant()

    # G_tt = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32)
    J1 = Array(- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41)
    n1 = Array(0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26)
    p = p / 16.53
    T = 1386 / T
    g_p = 0
    g_pp = 0
    g_pt = 0
    G_tt = 0
    for i in range(0, 1 + 33):
        g_p = g_p - n1(i) * I1(i) *  ( 7.1 - p )  **  ( I1(i) - 1 )  *  ( T - 1.222 )  ** J1(i)
        g_pp = g_pp + n1(i) * I1(i) *  ( I1(i) - 1 )  *  ( 7.1 - p )  **  ( I1(i) - 2 )  *  ( T - 1.222 )  ** J1(i)
        g_pt = g_pt - n1(i) * I1(i) *  ( 7.1 - p )  **  ( I1(i) - 1 )  * J1(i) *  ( T - 1.222 )  **  ( J1(i) - 1 )
        G_tt = G_tt + n1(i) *  ( 7.1 - p )  ** I1(i) * J1(i) *  ( J1(i) - 1 )  *  ( T - 1.222 )  **  ( J1(i) - 2 )
    _ret = R *  ( - ( T ** 2 * G_tt )  +  ( g_p - T * g_pt )  ** 2 / g_pp )
    return _ret

def w1_pT(p, T):
    _ret = None
    # i = Integer()

    # g_p = Variant()

    # g_pp = Variant()

    # g_pt = Variant()

    # G_tt = Variant()

    # tau = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation
    #Eqution 7, Table 3, Page 6
    I1 = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 8, 8, 21, 23, 29, 30, 31, 32)
    J1 = Array(- 2, - 1, 0, 1, 2, 3, 4, 5, - 9, - 7, - 1, 0, 1, 3, - 3, 0, 1, 3, 17, - 4, 0, 6, - 5, - 2, 10, - 8, - 11, - 6, - 29, - 31, - 38, - 39, - 40, - 41)
    n1 = Array(0.14632971213167, - 0.84548187169114, - 3.756360367204, 3.3855169168385, - 0.95791963387872, 0.15772038513228, - 0.016616417199501, 8.1214629983568E-04, 2.8319080123804E-04, - 6.0706301565874E-04, - 0.018990068218419, - 0.032529748770505, - 0.021841717175414, - 5.283835796993E-05, - 4.7184321073267E-04, - 3.0001780793026E-04, 4.7661393906987E-05, - 4.4141845330846E-06, - 7.2694996297594E-16, - 3.1679644845054E-05, - 2.8270797985312E-06, - 8.5205128120103E-10, - 2.2425281908E-06, - 6.5171222895601E-07, - 1.4341729937924E-13, - 4.0516996860117E-07, - 1.2734301741641E-09, - 1.7424871230634E-10, - 6.8762131295531E-19, 1.4478307828521E-20, 2.6335781662795E-23, - 1.1947622640071E-23, 1.8228094581404E-24, - 9.3537087292458E-26)
    p = p / 16.53
    tau = 1386 / T
    g_p = 0
    g_pp = 0
    g_pt = 0
    G_tt = 0
    for i in range(0, 1 + 33):
        g_p = g_p - n1(i) * I1(i) *  ( 7.1 - p )  **  ( I1(i) - 1 )  *  ( tau - 1.222 )  ** J1(i)
        g_pp = g_pp + n1(i) * I1(i) *  ( I1(i) - 1 )  *  ( 7.1 - p )  **  ( I1(i) - 2 )  *  ( tau - 1.222 )  ** J1(i)
        g_pt = g_pt - n1(i) * I1(i) *  ( 7.1 - p )  **  ( I1(i) - 1 )  * J1(i) *  ( tau - 1.222 )  **  ( J1(i) - 1 )
        G_tt = G_tt + n1(i) *  ( 7.1 - p )  ** I1(i) * J1(i) *  ( J1(i) - 1 )  *  ( tau - 1.222 )  **  ( J1(i) - 2 )
    _ret = ( 1000 * R * T * g_p ** 2 /  ( ( g_p - tau * g_pt )  ** 2 /  ( tau ** 2 * G_tt )  - g_pp ) )  ** 0.5
    return _ret

def T1_ph(p, h):
    _ret = None
    # i = Integer()

    # T = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation, 5.2.1 The Backward Equation T ( p,h )
    #Eqution 11, Table 6, Page 10
    I1 = Array(0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6)
    J1 = Array(0, 1, 2, 6, 22, 32, 0, 1, 2, 3, 4, 10, 32, 10, 32, 10, 32, 32, 32, 32)
    n1 = Array(- 238.72489924521, 404.21188637945, 113.49746881718, - 5.8457616048039, - 1.528548241314E-04, - 1.0866707695377E-06, - 13.391744872602, 43.211039183559, - 54.010067170506, 30.535892203916, - 6.5964749423638, 9.3965400878363E-03, 1.157364750534E-07, - 2.5858641282073E-05, - 4.0644363084799E-09, 6.6456186191635E-08, 8.0670734103027E-11, - 9.3477771213947E-13, 5.8265442020601E-15, - 1.5020185953503E-17)
    h = h / 2500
    T = 0
    for i in range(0, 1 + 19):
        T = T + n1(i) * p ** I1(i) *  ( h + 1 )  ** J1(i)
    _ret = T
    return _ret

def T1_ps(p, s):
    _ret = None
    # i = Integer()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #5 Equations for Region 1, Section. 5.1 Basic Equation, 5.2.2 The Backward Equation T ( p, s )
    #Eqution 13, Table 8, Page 11
    I1 = Array(0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 4)
    J1 = Array(0, 1, 2, 3, 11, 31, 0, 1, 2, 3, 12, 31, 0, 1, 2, 9, 31, 10, 32, 32)
    n1 = Array(174.78268058307, 34.806930892873, 6.5292584978455, 0.33039981775489, - 1.9281382923196E-07, - 2.4909197244573E-23, - 0.26107636489332, 0.22592965981586, - 0.064256463395226, 7.8876289270526E-03, 3.5672110607366E-10, 1.7332496994895E-24, 5.6608900654837E-04, - 3.2635483139717E-04, 4.4778286690632E-05, - 5.1322156908507E-10, - 4.2522657042207E-26, 2.6400441360689E-13, 7.8124600459723E-29, - 3.0732199903668E-31)
    _ret = 0
    for i in range(0, 1 + 19):
        _ret = T1_ps() + n1(i) * p ** I1(i) *  ( s + 2 )  ** J1(i)
    return _ret

def p1_hs(h, s):
    _ret = None
    # i = Integer()

    # p = Double()

    # I1 = Variant()

    # J1 = Variant()

    # n1 = Variant()
    #Supplementary Release on Backward Equations for Pressure as a Function of Enthalpy and Entropy p(h,s) to the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #5 Backward Equation p(h,s) for Region 1
    #Eqution 1, Table 2, Page 5
    I1 = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 5)
    J1 = Array(0, 1, 2, 4, 5, 6, 8, 14, 0, 1, 4, 6, 0, 1, 10, 4, 1, 4, 0)
    n1 = Array(- 0.691997014660582, - 18.361254878756, - 9.28332409297335, 65.9639569909906, - 16.2060388912024, 450.620017338667, 854.68067822417, 6075.23214001162, 32.6487682621856, - 26.9408844582931, - 319.9478483343, - 928.35430704332, 30.3634537455249, - 65.0540422444146, - 4309.9131651613, - 747.512324096068, 730.000345529245, 1142.84032569021, - 436.407041874559)
    h = h / 3400
    s = s / 7.6
    p = 0
    for i in range(0, 1 + 18):
        p = p + n1(i) *  ( h + 0.05 )  ** I1(i) *  ( s + 0.05 )  ** J1(i)
    _ret = p * 100
    return _ret

def T1_prho(p, rho):
    _ret = None
    # i = Integer()

    # Ts = Variant()

    # Low_Bound = Variant()

    # High_Bound = Variant()

    # rhos = Double()
    #Solve by iteration. Observe that fo low temperatures this equation has 2 solutions.
    #Solve with half interval method
    Low_Bound = 273.15
    High_Bound = T4_p(p)
    while Abs(rho - rhos) > 0.00001:
        Ts = ( Low_Bound + High_Bound )  / 2
        rhos = 1 / v1_pT(p, Ts)
        if rhos < rho:
            High_Bound = Ts
        else:
            Low_Bound = Ts
    _ret = Ts
    return _ret

def v2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0_pi = Variant()

    # gr_pi = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2, Section. 6.1 Basic Equation
    #Table 11 and 12, Page 14 and 15
    J0 = Array(0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3)
    n0 = Array(- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307)
    Ir = Array(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24)
    Jr = Array(0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58)
    nr = Array(- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07)
    tau = 540 / T
    g0_pi = 1 / p
    gr_pi = 0
    for i in range(0, 1 + 42):
        gr_pi = gr_pi + nr(i) * Ir(i) * p **  ( Ir(i) - 1 )  *  ( tau - 0.5 )  ** Jr(i)
    _ret = R * T / p * p *  ( g0_pi + gr_pi )  / 1000
    return _ret

def h2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0_tau = Variant()

    # gr_tau = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2, Section. 6.1 Basic Equation
    #Table 11 and 12, Page 14 and 15
    J0 = [0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3]
    n0 = [- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307]
    Ir = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24]
    Jr = [0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58]
    nr = [- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07]
    tau = 540 / T
    g0_tau = 0
    for i in range(0, 1 + 8):
        g0_tau = g0_tau + n0[i] * J0[i] * tau **  ( J0[i] - 1 )
    gr_tau = 0
    for i in range(0, 1 + 42):
        gr_tau = gr_tau + nr[i] * p ** Ir[i] * Jr[i] *  ( tau - 0.5 )  **  ( Jr[i] - 1 )
    _ret = R * T * tau *  ( g0_tau + gr_tau )
    return _ret

def u2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0_tau = Variant()

    # g0_pi = Variant()

    # gr_pi = Variant()

    # gr_tau = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2, Section. 6.1 Basic Equation
    #Table 11 and 12, Page 14 and 15
    J0 = Array(0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3)
    n0 = Array(- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307)
    Ir = Array(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24)
    Jr = Array(0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58)
    nr = Array(- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07)
    tau = 540 / T
    g0_pi = 1 / p
    g0_tau = 0
    for i in range(0, 1 + 8):
        g0_tau = g0_tau + n0(i) * J0(i) * tau **  ( J0(i) - 1 )
    gr_pi = 0
    gr_tau = 0
    for i in range(0, 1 + 42):
        gr_pi = gr_pi + nr(i) * Ir(i) * p **  ( Ir(i) - 1 )  *  ( tau - 0.5 )  ** Jr(i)
        gr_tau = gr_tau + nr(i) * p ** Ir(i) * Jr(i) *  ( tau - 0.5 )  **  ( Jr(i) - 1 )
    _ret = R * T *  ( tau *  ( g0_tau + gr_tau )  - p *  ( g0_pi + gr_pi ) )
    return _ret

def s2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0 = Variant()

    # g0_tau = Variant()

    # gr = Variant()

    # gr_tau = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2, Section. 6.1 Basic Equation
    #Table 11 and 12, Page 14 and 15
    J0 = Array(0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3)
    n0 = Array(- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307)
    Ir = Array(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24)
    Jr = Array(0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58)
    nr = Array(- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07)
    tau = 540 / T
    g0 = Log(p)
    g0_tau = 0
    for i in range(0, 1 + 8):
        g0 = g0 + n0(i) * tau ** J0(i)
        g0_tau = g0_tau + n0(i) * J0(i) * tau **  ( J0(i) - 1 )
    gr = 0
    gr_tau = 0
    for i in range(0, 1 + 42):
        gr = gr + nr(i) * p ** Ir(i) *  ( tau - 0.5 )  ** Jr(i)
        gr_tau = gr_tau + nr(i) * p ** Ir(i) * Jr(i) *  ( tau - 0.5 )  **  ( Jr(i) - 1 )
    _ret = R *  ( tau *  ( g0_tau + gr_tau )  -  ( g0 + gr ) )
    return _ret

def Cp2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0_tautau = Variant()

    # gr_tautau = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2, Section. 6.1 Basic Equation
    #Table 11 and 12, Page 14 and 15
    J0 = Array(0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3)
    n0 = Array(- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307)
    Ir = Array(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24)
    Jr = Array(0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58)
    nr = Array(- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07)
    tau = 540 / T
    g0_tautau = 0
    for i in range(0, 1 + 8):
        g0_tautau = g0_tautau + n0(i) * J0(i) *  ( J0(i) - 1 )  * tau **  ( J0(i) - 2 )
    gr_tautau = 0
    for i in range(0, 1 + 42):
        gr_tautau = gr_tautau + nr(i) * p ** Ir(i) * Jr(i) *  ( Jr(i) - 1 )  *  ( tau - 0.5 )  **  ( Jr(i) - 2 )
    _ret = - R * tau ** 2 *  ( g0_tautau + gr_tautau )
    return _ret

def Cv2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0_tautau = Variant()

    # gr_pi = Variant()

    # gr_pitau = Variant()

    # gr_pipi = Variant()

    # gr_tautau = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    J0 = Array(0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3)
    n0 = Array(- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307)
    Ir = Array(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24)
    Jr = Array(0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58)
    nr = Array(- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07)
    tau = 540 / T
    g0_tautau = 0
    for i in range(0, 1 + 8):
        g0_tautau = g0_tautau + n0(i) * J0(i) *  ( J0(i) - 1 )  * tau **  ( J0(i) - 2 )
    gr_pi = 0
    gr_pitau = 0
    gr_pipi = 0
    gr_tautau = 0
    for i in range(0, 1 + 42):
        gr_pi = gr_pi + nr(i) * Ir(i) * p **  ( Ir(i) - 1 )  *  ( tau - 0.5 )  ** Jr(i)
        gr_pipi = gr_pipi + nr(i) * Ir(i) *  ( Ir(i) - 1 )  * p **  ( Ir(i) - 2 )  *  ( tau - 0.5 )  ** Jr(i)
        gr_pitau = gr_pitau + nr(i) * Ir(i) * p **  ( Ir(i) - 1 )  * Jr(i) *  ( tau - 0.5 )  **  ( Jr(i) - 1 )
        gr_tautau = gr_tautau + nr(i) * p ** Ir(i) * Jr(i) *  ( Jr(i) - 1 )  *  ( tau - 0.5 )  **  ( Jr(i) - 2 )
    _ret = R *  ( - ( tau ** 2 *  ( g0_tautau + gr_tautau ) )  -  ( ( 1 + p * gr_pi - tau * p * gr_pitau )  ** 2 )  /  ( 1 - p ** 2 * gr_pipi ) )
    return _ret

def w2_pT(p, T):
    _ret = None
    # i = Integer()

    # tau = Variant()

    # g0_tautau = Variant()

    # gr_pi = Variant()

    # gr_pitau = Variant()

    # gr_pipi = Variant()

    # gr_tautau = Double()

    # Ir = Variant()

    # Jr = Variant()

    # nr = Variant()

    # J0 = Variant()

    # n0 = Variant()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2, Section. 6.1 Basic Equation
    #Table 11 and 12, Page 14 and 15
    J0 = Array(0, 1, - 5, - 4, - 3, - 2, - 1, 2, 3)
    n0 = Array(- 9.6927686500217, 10.086655968018, - 0.005608791128302, 0.071452738081455, - 0.40710498223928, 1.4240819171444, - 4.383951131945, - 0.28408632460772, 0.021268463753307)
    Ir = Array(1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 8, 8, 9, 10, 10, 10, 16, 16, 18, 20, 20, 20, 21, 22, 23, 24, 24, 24)
    Jr = Array(0, 1, 2, 3, 6, 1, 2, 4, 7, 36, 0, 1, 3, 6, 35, 1, 2, 3, 7, 3, 16, 35, 0, 11, 25, 8, 36, 13, 4, 10, 14, 29, 50, 57, 20, 35, 48, 21, 53, 39, 26, 40, 58)
    nr = Array(- 1.7731742473213E-03, - 0.017834862292358, - 0.045996013696365, - 0.057581259083432, - 0.05032527872793, - 3.3032641670203E-05, - 1.8948987516315E-04, - 3.9392777243355E-03, - 0.043797295650573, - 2.6674547914087E-05, 2.0481737692309E-08, 4.3870667284435E-07, - 3.227767723857E-05, - 1.5033924542148E-03, - 0.040668253562649, - 7.8847309559367E-10, 1.2790717852285E-08, 4.8225372718507E-07, 2.2922076337661E-06, - 1.6714766451061E-11, - 2.1171472321355E-03, - 23.895741934104, - 5.905956432427E-18, - 1.2621808899101E-06, - 0.038946842435739, 1.1256211360459E-11, - 8.2311340897998, 1.9809712802088E-08, 1.0406965210174E-19, - 1.0234747095929E-13, - 1.0018179379511E-09, - 8.0882908646985E-11, 0.10693031879409, - 0.33662250574171, 8.9185845355421E-25, 3.0629316876232E-13, - 4.2002467698208E-06, - 5.9056029685639E-26, 3.7826947613457E-06, - 1.2768608934681E-15, 7.3087610595061E-29, 5.5414715350778E-17, - 9.436970724121E-07)
    tau = 540 / T
    g0_tautau = 0
    for i in range(0, 1 + 8):
        g0_tautau = g0_tautau + n0(i) * J0(i) *  ( J0(i) - 1 )  * tau **  ( J0(i) - 2 )
    gr_pi = 0
    gr_pitau = 0
    gr_pipi = 0
    gr_tautau = 0
    for i in range(0, 1 + 42):
        gr_pi = gr_pi + nr(i) * Ir(i) * p **  ( Ir(i) - 1 )  *  ( tau - 0.5 )  ** Jr(i)
        gr_pipi = gr_pipi + nr(i) * Ir(i) *  ( Ir(i) - 1 )  * p **  ( Ir(i) - 2 )  *  ( tau - 0.5 )  ** Jr(i)
        gr_pitau = gr_pitau + nr(i) * Ir(i) * p **  ( Ir(i) - 1 )  * Jr(i) *  ( tau - 0.5 )  **  ( Jr(i) - 1 )
        gr_tautau = gr_tautau + nr(i) * p ** Ir(i) * Jr(i) *  ( Jr(i) - 1 )  *  ( tau - 0.5 )  **  ( Jr(i) - 2 )
    _ret = ( 1000 * R * T *  ( 1 + 2 * p * gr_pi + p ** 2 * gr_pi ** 2 )  /  ( ( 1 - p ** 2 * gr_pipi )  +  ( 1 + p * gr_pi - tau * p * gr_pitau )  ** 2 /  ( tau ** 2 *  ( g0_tautau + gr_tautau ) ) ) )  ** 0.5
    return _ret

def T2_ph(p, h):
    _ret = None
    # sub_reg = Integer()

    # i = Integer()

    # Ts = Variant()

    # hs = Double()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2,6.3.1 The Backward Equations T( p, h ) for Subregions 2a, 2b, and 2c
    if p < 4:
        sub_reg = 1
    else:
        if p <  ( 905.84278514723 - 0.67955786399241 * h + 1.2809002730136E-04 * h ** 2 ) :
            sub_reg = 2
        else:
            sub_reg = 3
    _select26 = sub_reg
    if (_select26 == 1):
        #Subregion A
        #Table 20, Eq 22, page 22
        Ji = Array(0, 1, 2, 3, 7, 20, 0, 1, 2, 3, 7, 9, 11, 18, 44, 0, 2, 7, 36, 38, 40, 42, 44, 24, 44, 12, 32, 44, 32, 36, 42, 34, 44, 28)
        Ii = Array(0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7)
        ni = Array(1089.8952318288, 849.51654495535, - 107.81748091826, 33.153654801263, - 7.4232016790248, 11.765048724356, 1.844574935579, - 4.1792700549624, 6.2478196935812, - 17.344563108114, - 200.58176862096, 271.96065473796, - 455.11318285818, 3091.9688604755, 252266.40357872, - 6.1707422868339E-03, - 0.31078046629583, 11.670873077107, 128127984.04046, - 985549096.23276, 2822454697.3002, - 3594897141.0703, 1722734991.3197, - 13551.334240775, 12848734.66465, 1.3865724283226, 235988.32556514, - 13105236.545054, 7399.9835474766, - 551966.9703006, 3715408.5996233, 19127.72923966, - 415351.64835634, - 62.459855192507)
        Ts = 0
        hs = h / 2000
        for i in range(0, 1 + 33):
            Ts = Ts + ni(i) * p **  ( Ii(i) )  *  ( hs - 2.1 )  ** Ji(i)
        _ret = Ts
    elif (_select26 == 2):
        #Subregion B
        #Table 21, Eq 23, page 23
        Ji = Array(0, 1, 2, 12, 18, 24, 28, 40, 0, 2, 6, 12, 18, 24, 28, 40, 2, 8, 18, 40, 1, 2, 12, 24, 2, 12, 18, 24, 28, 40, 18, 24, 40, 28, 2, 28, 1, 40)
        Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 7, 7, 9, 9)
        ni = Array(1489.5041079516, 743.07798314034, - 97.708318797837, 2.4742464705674, - 0.63281320016026, 1.1385952129658, - 0.47811863648625, 8.5208123431544E-03, 0.93747147377932, 3.3593118604916, 3.3809355601454, 0.16844539671904, 0.73875745236695, - 0.47128737436186, 0.15020273139707, - 0.002176411421975, - 0.021810755324761, - 0.10829784403677, - 0.046333324635812, 7.1280351959551E-05, 1.1032831789999E-04, 1.8955248387902E-04, 3.0891541160537E-03, 1.3555504554949E-03, 2.8640237477456E-07, - 1.0779857357512E-05, - 7.6462712454814E-05, 1.4052392818316E-05, - 3.1083814331434E-05, - 1.0302738212103E-06, 2.821728163504E-07, 1.2704902271945E-06, 7.3803353468292E-08, - 1.1030139238909E-08, - 8.1456365207833E-14, - 2.5180545682962E-11, - 1.7565233969407E-18, 8.6934156344163E-15)
        Ts = 0
        hs = h / 2000
        for i in range(0, 1 + 37):
            Ts = Ts + ni(i) *  ( p - 2 )  **  ( Ii(i) )  *  ( hs - 2.6 )  ** Ji(i)
        _ret = Ts
    else:
        #Subregion C
        #Table 22, Eq 24, page 24
        Ji = Array(0, 4, 0, 2, 0, 2, 0, 1, 0, 2, 0, 1, 4, 8, 4, 0, 1, 4, 10, 12, 16, 20, 22)
        Ii = Array(- 7, - 7, - 6, - 6, - 5, - 5, - 2, - 2, - 1, - 1, 0, 0, 1, 1, 2, 6, 6, 6, 6, 6, 6, 6, 6)
        ni = Array(- 3236839855524.2, 7326335090218.1, 358250899454.47, - 583401318515.9, - 10783068217.47, 20825544563.171, 610747.83564516, 859777.2253558, - 25745.72360417, 31081.088422714, 1208.2315865936, 482.19755109255, 3.7966001272486, - 10.842984880077, - 0.04536417267666, 1.4559115658698E-13, 1.126159740723E-12, - 1.7804982240686E-11, 1.2324579690832E-07, - 1.1606921130984E-06, 2.7846367088554E-05, - 5.9270038474176E-04, 1.2918582991878E-03)
        Ts = 0
        hs = h / 2000
        for i in range(0, 1 + 22):
            Ts = Ts + ni(i) *  ( p + 25 )  **  ( Ii(i) )  *  ( hs - 1.8 )  ** Ji(i)
        _ret = Ts
    return _ret

def T2_ps(p, s):
    _ret = None
    # sub_reg = Integer()

    # i = Integer()

    # teta = Variant()

    # sigma = Double()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #6 Equations for Region 2,6.3.2 The Backward Equations T( p, s ) for Subregions 2a, 2b, and 2c
    #Page 26
    if p < 4:
        sub_reg = 1
    else:
        if s < 5.85:
            sub_reg = 3
        else:
            sub_reg = 2
    _select27 = sub_reg
    if (_select27 == 1):
        #Subregion A
        #Table 25, Eq 25, page 26
        Ii = Array(- 1.5, - 1.5, - 1.5, - 1.5, - 1.5, - 1.5, - 1.25, - 1.25, - 1.25, - 1, - 1, - 1, - 1, - 1, - 1, - 0.75, - 0.75, - 0.5, - 0.5, - 0.5, - 0.5, - 0.25, - 0.25, - 0.25, - 0.25, 0.25, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.75, 0.75, 0.75, 0.75, 1, 1, 1.25, 1.25, 1.5, 1.5)
        Ji = Array(- 24, - 23, - 19, - 13, - 11, - 10, - 19, - 15, - 6, - 26, - 21, - 17, - 16, - 9, - 8, - 15, - 14, - 26, - 13, - 9, - 7, - 27, - 25, - 11, - 6, 1, 4, 8, 11, 0, 1, 5, 6, 10, 14, 16, 0, 4, 9, 17, 7, 18, 3, 15, 5, 18)
        ni = Array(- 392359.83861984, 515265.7382727, 40482.443161048, - 321.93790923902, 96.961424218694, - 22.867846371773, - 449429.14124357, - 5011.8336020166, 0.35684463560015, 44235.33584819, - 13673.388811708, 421632.60207864, 22516.925837475, 474.42144865646, - 149.31130797647, - 197811.26320452, - 23554.39947076, - 19070.616302076, 55375.669883164, 3829.3691437363, - 603.91860580567, 1936.3102620331, 4266.064369861, - 5978.0638872718, - 704.01463926862, 338.36784107553, 20.862786635187, 0.033834172656196, - 4.3124428414893E-05, 166.53791356412, - 139.86292055898, - 0.78849547999872, 0.072132411753872, - 5.9754839398283E-03, - 1.2141358953904E-05, 2.3227096733871E-07, - 10.538463566194, 2.0718925496502, - 0.072193155260427, 2.074988708112E-07, - 0.018340657911379, 2.9036272348696E-07, 0.21037527893619, 2.5681239729999E-04, - 0.012799002933781, - 8.2198102652018E-06)
        sigma = s / 2
        teta = 0
        for i in range(0, 1 + 45):
            teta = teta + ni(i) * p ** Ii(i) *  ( sigma - 2 )  ** Ji(i)
        _ret = teta
    elif (_select27 == 2):
        #Subregion B
        #Table 26, Eq 26, page 27
        Ii = Array(- 6, - 6, - 5, - 5, - 4, - 4, - 4, - 3, - 3, - 3, - 3, - 2, - 2, - 2, - 2, - 1, - 1, - 1, - 1, - 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5)
        Ji = Array(0, 11, 0, 11, 0, 1, 11, 0, 1, 11, 12, 0, 1, 6, 10, 0, 1, 5, 8, 9, 0, 1, 2, 4, 5, 6, 9, 0, 1, 2, 3, 7, 8, 0, 1, 5, 0, 1, 3, 0, 1, 0, 1, 2)
        ni = Array(316876.65083497, 20.864175881858, - 398593.99803599, - 21.816058518877, 223697.85194242, - 2784.1703445817, 9.920743607148, - 75197.512299157, 2970.8605951158, - 3.4406878548526, 0.38815564249115, 17511.29508575, - 1423.7112854449, 1.0943803364167, 0.89971619308495, - 3375.9740098958, 471.62885818355, - 1.9188241993679, 0.41078580492196, - 0.33465378172097, 1387.0034777505, - 406.63326195838, 41.72734715961, 2.1932549434532, - 1.0320050009077, 0.35882943516703, 5.2511453726066E-03, 12.838916450705, - 2.8642437219381, 0.56912683664855, - 0.099962954584931, - 3.2632037778459E-03, 2.3320922576723E-04, - 0.1533480985745, 0.029072288239902, 3.7534702741167E-04, 1.7296691702411E-03, - 3.8556050844504E-04, - 3.5017712292608E-05, - 1.4566393631492E-05, 5.6420857267269E-06, 4.1286150074605E-08, - 2.0684671118824E-08, 1.6409393674725E-09)
        sigma = s / 0.7853
        teta = 0
        for i in range(0, 1 + 43):
            teta = teta + ni(i) * p ** Ii(i) *  ( 10 - sigma )  ** Ji(i)
        _ret = teta
    else:
        #Subregion C
        #Table 27, Eq 27, page 28
        Ii = Array(- 2, - 2, - 1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 7, 7)
        Ji = Array(0, 1, 0, 0, 1, 2, 3, 0, 1, 3, 4, 0, 1, 2, 0, 1, 5, 0, 1, 4, 0, 1, 2, 0, 1, 0, 1, 3, 4, 5)
        ni = Array(909.68501005365, 2404.566708842, - 591.6232638713, 541.45404128074, - 270.98308411192, 979.76525097926, - 469.66772959435, 14.399274604723, - 19.104204230429, 5.3299167111971, - 21.252975375934, - 0.3114733441376, 0.60334840894623, - 0.042764839702509, 5.8185597255259E-03, - 0.014597008284753, 5.6631175631027E-03, - 7.6155864584577E-05, 2.2440342919332E-04, - 1.2561095013413E-05, 6.3323132660934E-07, - 2.0541989675375E-06, 3.6405370390082E-08, - 2.9759897789215E-09, 1.0136618529763E-08, 5.9925719692351E-12, - 2.0677870105164E-11, - 2.0874278181886E-11, 1.0162166825089E-10, - 1.6429828281347E-10)
        sigma = s / 2.9251
        teta = 0
        for i in range(0, 1 + 29):
            teta = teta + ni(i) * p ** Ii(i) *  ( 2 - sigma )  ** Ji(i)
        _ret = teta
    return _ret

def p2_hs(h, s):
    _ret = None
    # sub_reg = Integer()

    # i = Integer()

    # eta = Variant()

    # teta = Variant()

    # sigma = Variant()

    # p = Double()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()
    #Supplementary Release on Backward Equations for Pressure as a Function of Enthalpy and Entropy p(h,s) to the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #Chapter 6:Backward Equations p(h,s) for Region 2
    if h <  ( - 3498.98083432139 + 2575.60716905876 * s - 421.073558227969 * s ** 2 + 27.6349063799944 * s ** 3 ) :
        sub_reg = 1
    else:
        if s < 5.85:
            sub_reg = 3
        else:
            sub_reg = 2
    _select28 = sub_reg
    if (_select28 == 1):
        #Subregion A
        #Table 6, Eq 3, page 8
        Ii = Array(0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 6, 7)
        Ji = Array(1, 3, 6, 16, 20, 22, 0, 1, 2, 3, 5, 6, 10, 16, 20, 22, 3, 16, 20, 0, 2, 3, 6, 16, 16, 3, 16, 3, 1)
        ni = Array(- 1.82575361923032E-02, - 0.125229548799536, 0.592290437320145, 6.04769706185122, 238.624965444474, - 298.639090222922, 0.051225081304075, - 0.437266515606486, 0.413336902999504, - 5.16468254574773, - 5.57014838445711, 12.8555037824478, 11.414410895329, - 119.504225652714, - 2847.7798596156, 4317.57846408006, 1.1289404080265, 1974.09186206319, 1516.12444706087, 1.41324451421235E-02, 0.585501282219601, - 2.97258075863012, 5.94567314847319, - 6236.56565798905, 9659.86235133332, 6.81500934948134, - 6332.07286824489, - 5.5891922446576, 4.00645798472063E-02)
        eta = h / 4200
        sigma = s / 12
        p = 0
        for i in range(0, 1 + 28):
            p = p + ni(i) *  ( eta - 0.5 )  ** Ii(i) *  ( sigma - 1.2 )  ** Ji(i)
        _ret = p ** 4 * 4
    elif (_select28 == 2):
        #Subregion B
        #Table 7, Eq 4, page 9
        Ii = Array(0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 6, 6, 6, 7, 7, 8, 8, 8, 8, 12, 14)
        Ji = Array(0, 1, 2, 4, 8, 0, 1, 2, 3, 5, 12, 1, 6, 18, 0, 1, 7, 12, 1, 16, 1, 12, 1, 8, 18, 1, 16, 1, 3, 14, 18, 10, 16)
        ni = Array(8.01496989929495E-02, - 0.543862807146111, 0.337455597421283, 8.9055545115745, 313.840736431485, 0.797367065977789, - 1.2161697355624, 8.72803386937477, - 16.9769781757602, - 186.552827328416, 95115.9274344237, - 18.9168510120494, - 4334.0703719484, 543212633.012715, 0.144793408386013, 128.024559637516, - 67230.9534071268, 33697238.0095287, - 586.63419676272, - 22140322476.9889, 1716.06668708389, - 570817595.806302, - 3121.09693178482, - 2078413.8463301, 3056059461577.86, 3221.57004314333, 326810259797.295, - 1441.04158934487, 410.694867802691, 109077066873.024, - 24796465425889.3, 1888019068.65134, - 123651009018773)
        eta = h / 4100
        sigma = s / 7.9
        for i in range(0, 1 + 32):
            p = p + ni(i) *  ( eta - 0.6 )  ** Ii(i) *  ( sigma - 1.01 )  ** Ji(i)
        _ret = p ** 4 * 100
    else:
        #Subregion C
        #Table 8, Eq 5, page 10
        Ii = Array(0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 5, 5, 5, 5, 6, 6, 10, 12, 16)
        Ji = Array(0, 1, 2, 3, 4, 8, 0, 2, 5, 8, 14, 2, 3, 7, 10, 18, 0, 5, 8, 16, 18, 18, 1, 4, 6, 14, 8, 18, 7, 7, 10)
        ni = Array(0.112225607199012, - 3.39005953606712, - 32.0503911730094, - 197.5973051049, - 407.693861553446, 13294.3775222331, 1.70846839774007, 37.3694198142245, 3581.44365815434, 423014.446424664, - 751071025.760063, 52.3446127607898, - 228.351290812417, - 960652.417056937, - 80705929.2526074, 1626980172256.69, 0.772465073604171, 46392.9973837746, - 13731788.5134128, 1704703926305.12, - 25110462818730.8, 31774883083552, 53.8685623675312, - 55308.9094625169, - 1028615.22421405, 2042494187562.34, 273918446.626977, - 2.63963146312685E+15, - 1078908541.08088, - 29649262098.0124, - 1.11754907323424E+15)
        eta = h / 3500
        sigma = s / 5.9
        for i in range(0, 1 + 30):
            p = p + ni(i) *  ( eta - 0.7 )  ** Ii(i) *  ( sigma - 1.1 )  ** Ji(i)
        _ret = p ** 4 * 100
    return _ret

def T2_prho(p, rho):
    _ret = None
    # Low_Bound = Variant()

    # High_Bound = Variant()

    # rhos = Variant()

    # Ts = Double()
    #Solve by iteration. Observe that fo low temperatures this equation has 2 solutions.
    #Solve with half interval method
    if p < 16.5292:
        Low_Bound = T4_p(p)
    else:
        Low_Bound = B23T_p(p)
    High_Bound = 1073.15
    while Abs(rho - rhos) > 0.000001:
        Ts = ( Low_Bound + High_Bound )  / 2
        rhos = 1 / v2_pT(p, Ts)
        if rhos < rho:
            High_Bound = Ts
        else:
            Low_Bound = Ts
    _ret = Ts
    return _ret

def p3_rhoT(rho, T):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # delta = Variant()

    # tau = Variant()

    # fidelta = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #7 Basic Equation for Region 3, Section. 6.1 Basic Equation
    #Table 30 and 31, Page 30 and 31
    Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11)
    Ji = Array(0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26)
    ni = Array(1.0658070028513, - 15.732845290239, 20.944396974307, - 7.6867707878716, 2.6185947787954, - 2.808078114862, 1.2053369696517, - 8.4566812812502E-03, - 1.2654315477714, - 1.1524407806681, 0.88521043984318, - 0.64207765181607, 0.38493460186671, - 0.85214708824206, 4.8972281541877, - 3.0502617256965, 0.039420536879154, 0.12558408424308, - 0.2799932969871, 1.389979956946, - 2.018991502357, - 8.2147637173963E-03, - 0.47596035734923, 0.0439840744735, - 0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, - 0.32913623258954, - 0.50871062041158, - 0.022175400873096, 0.094260751665092, 0.16436278447961, - 0.013503372241348, - 0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, - 1.6557679795037E-04, - 4.4923899061815E-05)
    delta = rho / rhoc
    tau = tc / T
    fidelta = 0
    for i in range(1, 1 + 39):
        fidelta = fidelta + ni(i) * Ii(i) * delta **  ( Ii(i) - 1 )  * tau ** Ji(i)
    fidelta = fidelta + ni(0) / delta
    _ret = rho * R * T * delta * fidelta / 1000
    return _ret

def u3_rhoT(rho, T):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # delta = Variant()

    # tau = Variant()

    # fitau = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #7 Basic Equation for Region 3, Section. 6.1 Basic Equation
    #Table 30 and 31, Page 30 and 31
    Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11)
    Ji = Array(0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26)
    ni = Array(1.0658070028513, - 15.732845290239, 20.944396974307, - 7.6867707878716, 2.6185947787954, - 2.808078114862, 1.2053369696517, - 8.4566812812502E-03, - 1.2654315477714, - 1.1524407806681, 0.88521043984318, - 0.64207765181607, 0.38493460186671, - 0.85214708824206, 4.8972281541877, - 3.0502617256965, 0.039420536879154, 0.12558408424308, - 0.2799932969871, 1.389979956946, - 2.018991502357, - 8.2147637173963E-03, - 0.47596035734923, 0.0439840744735, - 0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, - 0.32913623258954, - 0.50871062041158, - 0.022175400873096, 0.094260751665092, 0.16436278447961, - 0.013503372241348, - 0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, - 1.6557679795037E-04, - 4.4923899061815E-05)
    delta = rho / rhoc
    tau = tc / T
    fitau = 0
    for i in range(1, 1 + 39):
        fitau = fitau + ni(i) * delta ** Ii(i) * Ji(i) * tau **  ( Ji(i) - 1 )
    _ret = R * T *  ( tau * fitau )
    return _ret

def h3_rhoT(rho, T):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # delta = Variant()

    # tau = Variant()

    # fidelta = Variant()

    # fitau = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #7 Basic Equation for Region 3, Section. 6.1 Basic Equation
    #Table 30 and 31, Page 30 and 31
    Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11)
    Ji = Array(0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26)
    ni = Array(1.0658070028513, - 15.732845290239, 20.944396974307, - 7.6867707878716, 2.6185947787954, - 2.808078114862, 1.2053369696517, - 8.4566812812502E-03, - 1.2654315477714, - 1.1524407806681, 0.88521043984318, - 0.64207765181607, 0.38493460186671, - 0.85214708824206, 4.8972281541877, - 3.0502617256965, 0.039420536879154, 0.12558408424308, - 0.2799932969871, 1.389979956946, - 2.018991502357, - 8.2147637173963E-03, - 0.47596035734923, 0.0439840744735, - 0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, - 0.32913623258954, - 0.50871062041158, - 0.022175400873096, 0.094260751665092, 0.16436278447961, - 0.013503372241348, - 0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, - 1.6557679795037E-04, - 4.4923899061815E-05)
    delta = rho / rhoc
    tau = tc / T
    fidelta = 0
    fitau = 0
    for i in range(1, 1 + 39):
        fidelta = fidelta + ni(i) * Ii(i) * delta **  ( Ii(i) - 1 )  * tau ** Ji(i)
        fitau = fitau + ni(i) * delta ** Ii(i) * Ji(i) * tau **  ( Ji(i) - 1 )
    fidelta = fidelta + ni(0) / delta
    _ret = R * T *  ( tau * fitau + delta * fidelta )
    return _ret

def s3_rhoT(rho, T):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # fi = Variant()

    # delta = Variant()

    # tau = Variant()

    # fitau = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #7 Basic Equation for Region 3, Section. 6.1 Basic Equation
    #Table 30 and 31, Page 30 and 31
    Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11)
    Ji = Array(0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26)
    ni = Array(1.0658070028513, - 15.732845290239, 20.944396974307, - 7.6867707878716, 2.6185947787954, - 2.808078114862, 1.2053369696517, - 8.4566812812502E-03, - 1.2654315477714, - 1.1524407806681, 0.88521043984318, - 0.64207765181607, 0.38493460186671, - 0.85214708824206, 4.8972281541877, - 3.0502617256965, 0.039420536879154, 0.12558408424308, - 0.2799932969871, 1.389979956946, - 2.018991502357, - 8.2147637173963E-03, - 0.47596035734923, 0.0439840744735, - 0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, - 0.32913623258954, - 0.50871062041158, - 0.022175400873096, 0.094260751665092, 0.16436278447961, - 0.013503372241348, - 0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, - 1.6557679795037E-04, - 4.4923899061815E-05)
    delta = rho / rhoc
    tau = tc / T
    fi = 0
    fitau = 0
    for i in range(1, 1 + 39):
        fi = fi + ni(i) * delta ** Ii(i) * tau ** Ji(i)
        fitau = fitau + ni(i) * delta ** Ii(i) * Ji(i) * tau **  ( Ji(i) - 1 )
    fi = fi + ni(0) * Log(delta)
    _ret = R *  ( tau * fitau - fi )
    return _ret

def Cp3_rhoT(rho, T):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # fideltatau = Variant()

    # fi = Variant()

    # delta = Variant()

    # tau = Variant()

    # fitautau = Variant()

    # fidelta = Variant()

    # fideltatautau = Variant()

    # fideltadelta = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #7 Basic Equation for Region 3, Section. 6.1 Basic Equation
    #Table 30 and 31, Page 30 and 31
    Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11)
    Ji = Array(0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26)
    ni = Array(1.0658070028513, - 15.732845290239, 20.944396974307, - 7.6867707878716, 2.6185947787954, - 2.808078114862, 1.2053369696517, - 8.4566812812502E-03, - 1.2654315477714, - 1.1524407806681, 0.88521043984318, - 0.64207765181607, 0.38493460186671, - 0.85214708824206, 4.8972281541877, - 3.0502617256965, 0.039420536879154, 0.12558408424308, - 0.2799932969871, 1.389979956946, - 2.018991502357, - 8.2147637173963E-03, - 0.47596035734923, 0.0439840744735, - 0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, - 0.32913623258954, - 0.50871062041158, - 0.022175400873096, 0.094260751665092, 0.16436278447961, - 0.013503372241348, - 0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, - 1.6557679795037E-04, - 4.4923899061815E-05)
    delta = rho / rhoc
    tau = tc / T
    fitautau = 0
    fidelta = 0
    fideltatau = 0
    fideltadelta = 0
    for i in range(1, 1 + 39):
        fitautau = fitautau + ni(i) * delta ** Ii(i) * Ji(i) *  ( Ji(i) - 1 )  * tau **  ( Ji(i) - 2 )
        fidelta = fidelta + ni(i) * Ii(i) * delta **  ( Ii(i) - 1 )  * tau ** Ji(i)
        fideltatau = fideltatau + ni(i) * Ii(i) * delta **  ( Ii(i) - 1 )  * Ji(i) * tau **  ( Ji(i) - 1 )
        fideltadelta = fideltadelta + ni(i) * Ii(i) *  ( Ii(i) - 1 )  * delta **  ( Ii(i) - 2 )  * tau ** Ji(i)
    fidelta = fidelta + ni(0) / delta
    fideltadelta = fideltadelta - ni(0) /  ( delta ** 2 )
    _ret = R *  ( - ( tau ** 2 * fitautau )  +  ( delta * fidelta - delta * tau * fideltatau )  ** 2 /  ( 2 * delta * fidelta + delta ** 2 * fideltadelta ) )
    return _ret

def w3_rhoT(rho, T):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # fi = Variant()

    # delta = Variant()

    # tau = Variant()

    # fitautau = Variant()

    # fidelta = Variant()

    # fideltatau = Variant()

    # fideltadelta = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #7 Basic Equation for Region 3, Section. 6.1 Basic Equation
    #Table 30 and 31, Page 30 and 31
    Ii = Array(0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 8, 9, 9, 10, 10, 11)
    Ji = Array(0, 0, 1, 2, 7, 10, 12, 23, 2, 6, 15, 17, 0, 2, 6, 7, 22, 26, 0, 2, 4, 16, 26, 0, 2, 4, 26, 1, 3, 26, 0, 2, 26, 2, 26, 2, 26, 0, 1, 26)
    ni = Array(1.0658070028513, - 15.732845290239, 20.944396974307, - 7.6867707878716, 2.6185947787954, - 2.808078114862, 1.2053369696517, - 8.4566812812502E-03, - 1.2654315477714, - 1.1524407806681, 0.88521043984318, - 0.64207765181607, 0.38493460186671, - 0.85214708824206, 4.8972281541877, - 3.0502617256965, 0.039420536879154, 0.12558408424308, - 0.2799932969871, 1.389979956946, - 2.018991502357, - 8.2147637173963E-03, - 0.47596035734923, 0.0439840744735, - 0.44476435428739, 0.90572070719733, 0.70522450087967, 0.10770512626332, - 0.32913623258954, - 0.50871062041158, - 0.022175400873096, 0.094260751665092, 0.16436278447961, - 0.013503372241348, - 0.014834345352472, 5.7922953628084E-04, 3.2308904703711E-03, 8.0964802996215E-05, - 1.6557679795037E-04, - 4.4923899061815E-05)
    delta = rho / rhoc
    tau = tc / T
    fitautau = 0
    fidelta = 0
    fideltatau = 0
    fideltadelta = 0
    for i in range(1, 1 + 39):
        fitautau = fitautau + ni(i) * delta ** Ii(i) * Ji(i) *  ( Ji(i) - 1 )  * tau **  ( Ji(i) - 2 )
        fidelta = fidelta + ni(i) * Ii(i) * delta **  ( Ii(i) - 1 )  * tau ** Ji(i)
        fideltatau = fideltatau + ni(i) * Ii(i) * delta **  ( Ii(i) - 1 )  * Ji(i) * tau **  ( Ji(i) - 1 )
        fideltadelta = fideltadelta + ni(i) * Ii(i) *  ( Ii(i) - 1 )  * delta **  ( Ii(i) - 2 )  * tau ** Ji(i)
    fidelta = fidelta + ni(0) / delta
    fideltadelta = fideltadelta - ni(0) /  ( delta ** 2 )
    _ret = ( 1000 * R * T *  ( 2 * delta * fidelta + delta ** 2 * fideltadelta -  ( delta * fidelta - delta * tau * fideltatau )  ** 2 /  ( tau ** 2 * fitautau ) ) )  ** 0.5
    return _ret

def T3_ph(p, h):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # h3ab = Variant()

    # ps = Variant()

    # hs = Variant()

    # Ts = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Revised Supplementary Release on Backward Equations for the Functions T(p,h), v(p,h) and T(p,s), v(p,s) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #2004
    #Section 3.3 Backward Equations T(p,h) and v(p,h) for Subregions 3a and 3b
    #Boundary equation, Eq 1 Page 5
    h3ab = ( 2014.64004206875 + 3.74696550136983 * p - 2.19921901054187E-02 * p ** 2 + 8.7513168600995E-05 * p ** 3 )
    if h < h3ab:
        #Subregion 3a
        #Eq 2, Table 3, Page 7
        Ii = Array(- 12, - 12, - 12, - 12, - 12, - 12, - 12, - 12, - 10, - 10, - 10, - 8, - 8, - 8, - 8, - 5, - 3, - 2, - 2, - 2, - 1, - 1, 0, 0, 1, 3, 3, 4, 4, 10, 12)
        Ji = Array(0, 1, 2, 6, 14, 16, 20, 22, 1, 5, 12, 0, 2, 4, 10, 2, 0, 1, 3, 4, 0, 2, 0, 1, 1, 0, 1, 0, 3, 4, 5)
        ni = Array(- 1.33645667811215E-07, 4.55912656802978E-06, - 1.46294640700979E-05, 6.3934131297008E-03, 372.783927268847, - 7186.54377460447, 573494.7521034, - 2675693.29111439, - 3.34066283302614E-05, - 2.45479214069597E-02, 47.8087847764996, 7.64664131818904E-06, 1.28350627676972E-03, 1.71219081377331E-02, - 8.51007304583213, - 1.36513461629781E-02, - 3.84460997596657E-06, 3.37423807911655E-03, - 0.551624873066791, 0.72920227710747, - 9.92522757376041E-03, - 0.119308831407288, 0.793929190615421, 0.454270731799386, 0.20999859125991, - 6.42109823904738E-03, - 0.023515586860454, 2.52233108341612E-03, - 7.64885133368119E-03, 1.36176427574291E-02, - 1.33027883575669E-02)
        ps = p / 100
        hs = h / 2300
        Ts = 0
        for i in range(0, 1 + 30):
            Ts = Ts + ni(i) *  ( ps + 0.24 )  ** Ii(i) *  ( hs - 0.615 )  ** Ji(i)
        _ret = Ts * 760
    else:
        #Subregion 3b
        #Eq 3, Table 4, Page 7,8
        Ii = Array(- 12, - 12, - 10, - 10, - 10, - 10, - 10, - 8, - 8, - 8, - 8, - 8, - 6, - 6, - 6, - 4, - 4, - 3, - 2, - 2, - 1, - 1, - 1, - 1, - 1, - 1, 0, 0, 1, 3, 5, 6, 8)
        Ji = Array(0, 1, 0, 1, 5, 10, 12, 0, 1, 2, 4, 10, 0, 1, 2, 0, 1, 5, 0, 4, 2, 4, 6, 10, 14, 16, 0, 2, 1, 1, 1, 1, 1)
        ni = Array(3.2325457364492E-05, - 1.27575556587181E-04, - 4.75851877356068E-04, 1.56183014181602E-03, 0.105724860113781, - 85.8514221132534, 724.140095480911, 2.96475810273257E-03, - 5.92721983365988E-03, - 1.26305422818666E-02, - 0.115716196364853, 84.9000969739595, - 1.08602260086615E-02, 1.54304475328851E-02, 7.50455441524466E-02, 2.52520973612982E-02, - 6.02507901232996E-02, - 3.07622221350501, - 5.74011959864879E-02, 5.03471360939849, - 0.925081888584834, 3.91733882917546, - 77.314600713019, 9493.08762098587, - 1410437.19679409, 8491662.30819026, 0.861095729446704, 0.32334644281172, 0.873281936020439, - 0.436653048526683, 0.286596714529479, - 0.131778331276228, 6.76682064330275E-03)
        hs = h / 2800
        ps = p / 100
        Ts = 0
        for i in range(0, 1 + 32):
            Ts = Ts + ni(i) *  ( ps + 0.298 )  ** Ii(i) *  ( hs - 0.72 )  ** Ji(i)
        _ret = Ts * 860
    return _ret

def v3_ph(p, h):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # h3ab = Variant()

    # ps = Variant()

    # hs = Variant()

    # vs = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Revised Supplementary Release on Backward Equations for the Functions T(p,h), v(p,h) and T(p,s), v(p,s) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #2004
    #Section 3.3 Backward Equations T(p,h) and v(p,h) for Subregions 3a and 3b
    #Boundary equation, Eq 1 Page 5
    h3ab = ( 2014.64004206875 + 3.74696550136983 * p - 2.19921901054187E-02 * p ** 2 + 8.7513168600995E-05 * p ** 3 )
    if h < h3ab:
        #Subregion 3a
        #Eq 4, Table 6, Page 9
        Ii = Array(- 12, - 12, - 12, - 12, - 10, - 10, - 10, - 8, - 8, - 6, - 6, - 6, - 4, - 4, - 3, - 2, - 2, - 1, - 1, - 1, - 1, 0, 0, 1, 1, 1, 2, 2, 3, 4, 5, 8)
        Ji = Array(6, 8, 12, 18, 4, 7, 10, 5, 12, 3, 4, 22, 2, 3, 7, 3, 16, 0, 1, 2, 3, 0, 1, 0, 1, 2, 0, 2, 0, 2, 2, 2)
        ni = Array(5.29944062966028E-03, - 0.170099690234461, 11.1323814312927, - 2178.98123145125, - 5.06061827980875E-04, 0.556495239685324, - 9.43672726094016, - 0.297856807561527, 93.9353943717186, 1.92944939465981E-02, 0.421740664704763, - 3689141.2628233, - 7.37566847600639E-03, - 0.354753242424366, - 1.99768169338727, 1.15456297059049, 5683.6687581596, 8.08169540124668E-03, 0.172416341519307, 1.04270175292927, - 0.297691372792847, 0.560394465163593, 0.275234661176914, - 0.148347894866012, - 6.51142513478515E-02, - 2.92468715386302, 6.64876096952665E-02, 3.52335014263844, - 1.46340792313332E-02, - 2.24503486668184, 1.10533464706142, - 4.08757344495612E-02)
        ps = p / 100
        hs = h / 2100
        vs = 0
        for i in range(0, 1 + 31):
            vs = vs + ni(i) *  ( ps + 0.128 )  ** Ii(i) *  ( hs - 0.727 )  ** Ji(i)
        _ret = vs * 0.0028
    else:
        #Subregion 3b
        #Eq 5, Table 7, Page 9
        Ii = Array(- 12, - 12, - 8, - 8, - 8, - 8, - 8, - 8, - 6, - 6, - 6, - 6, - 6, - 6, - 4, - 4, - 4, - 3, - 3, - 2, - 2, - 1, - 1, - 1, - 1, 0, 1, 1, 2, 2)
        Ji = Array(0, 1, 0, 1, 3, 6, 7, 8, 0, 1, 2, 5, 6, 10, 3, 6, 10, 0, 2, 1, 2, 0, 1, 4, 5, 0, 0, 1, 2, 6)
        ni = Array(- 2.25196934336318E-09, 1.40674363313486E-08, 2.3378408528056E-06, - 3.31833715229001E-05, 1.07956778514318E-03, - 0.271382067378863, 1.07202262490333, - 0.853821329075382, - 2.15214194340526E-05, 7.6965608822273E-04, - 4.31136580433864E-03, 0.453342167309331, - 0.507749535873652, - 100.475154528389, - 0.219201924648793, - 3.21087965668917, 607.567815637771, 5.57686450685932E-04, 0.18749904002955, 9.05368030448107E-03, 0.285417173048685, 3.29924030996098E-02, 0.239897419685483, 4.82754995951394, - 11.8035753702231, 0.169490044091791, - 1.79967222507787E-02, 3.71810116332674E-02, - 5.36288335065096E-02, 1.6069710109252)
        ps = p / 100
        hs = h / 2800
        vs = 0
        for i in range(0, 1 + 29):
            vs = vs + ni(i) *  ( ps + 0.0661 )  ** Ii(i) *  ( hs - 0.72 )  ** Ji(i)
        _ret = vs * 0.0088
    return _ret

def T3_ps(p, s):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # ps = Variant()

    # sigma = Variant()

    # teta = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Revised Supplementary Release on Backward Equations for the Functions T(p,h), v(p,h) and T(p,s), v(p,s) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #2004
    #3.4 Backward Equations T(p,s) and v(p,s) for Subregions 3a and 3b
    #Boundary equation, Eq 6 Page 11
    if s <= 4.41202148223476:
        #Subregion 3a
        #Eq 6, Table 10, Page 11
        Ii = Array(- 12, - 12, - 10, - 10, - 10, - 10, - 8, - 8, - 8, - 8, - 6, - 6, - 6, - 5, - 5, - 5, - 4, - 4, - 4, - 2, - 2, - 1, - 1, 0, 0, 0, 1, 2, 2, 3, 8, 8, 10)
        Ji = Array(28, 32, 4, 10, 12, 14, 5, 7, 8, 28, 2, 6, 32, 0, 14, 32, 6, 10, 36, 1, 4, 1, 6, 0, 1, 4, 0, 0, 3, 2, 0, 1, 2)
        ni = Array(1500420082.63875, - 159397258480.424, 5.02181140217975E-04, - 67.2057767855466, 1450.58545404456, - 8238.8953488889, - 0.154852214233853, 11.2305046746695, - 29.7000213482822, 43856513263.5495, 1.37837838635464E-03, - 2.97478527157462, 9717779473494.13, - 5.71527767052398E-05, 28830.794977842, - 74442828926270.3, 12.8017324848921, - 368.275545889071, 6.64768904779177E+15, 0.044935925195888, - 4.22897836099655, - 0.240614376434179, - 4.74341365254924, 0.72409399912611, 0.923874349695897, 3.99043655281015, 3.84066651868009E-02, - 3.59344365571848E-03, - 0.735196448821653, 0.188367048396131, 1.41064266818704E-04, - 2.57418501496337E-03, 1.23220024851555E-03)
        sigma = s / 4.4
        ps = p / 100
        teta = 0
        for i in range(0, 1 + 32):
            teta = teta + ni(i) *  ( ps + 0.24 )  ** Ii(i) *  ( sigma - 0.703 )  ** Ji(i)
        _ret = teta * 760
    else:
        #Subregion 3b
        #Eq 7, Table 11, Page 11
        Ii = Array(- 12, - 12, - 12, - 12, - 8, - 8, - 8, - 6, - 6, - 6, - 5, - 5, - 5, - 5, - 5, - 4, - 3, - 3, - 2, 0, 2, 3, 4, 5, 6, 8, 12, 14)
        Ji = Array(1, 3, 4, 7, 0, 1, 3, 0, 2, 4, 0, 1, 2, 4, 6, 12, 1, 6, 2, 0, 1, 1, 0, 24, 0, 3, 1, 2)
        ni = Array(0.52711170160166, - 40.1317830052742, 153.020073134484, - 2247.99398218827, - 0.193993484669048, - 1.40467557893768, 42.6799878114024, 0.752810643416743, 22.6657238616417, - 622.873556909932, - 0.660823667935396, 0.841267087271658, - 25.3717501764397, 485.708963532948, 880.531517490555, 2650155.92794626, - 0.359287150025783, - 656.991567673753, 2.41768149185367, 0.856873461222588, 0.655143675313458, - 0.213535213206406, 5.62974957606348E-03, - 316955725450471, - 6.99997000152457E-04, 1.19845803210767E-02, 1.93848122022095E-05, - 2.15095749182309E-05)
        sigma = s / 5.3
        ps = p / 100
        teta = 0
        for i in range(0, 1 + 27):
            teta = teta + ni(i) *  ( ps + 0.76 )  ** Ii(i) *  ( sigma - 0.818 )  ** Ji(i)
        _ret = teta * 860
    return _ret

def v3_ps(p, s):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # ps = Variant()

    # sigma = Variant()

    # omega = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Revised Supplementary Release on Backward Equations for the Functions T(p,h), v(p,h) and T(p,s), v(p,s) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #2004
    #3.4 Backward Equations T(p,s) and v(p,s) for Subregions 3a and 3b
    #Boundary equation, Eq 6 Page 11
    if s <= 4.41202148223476:
        #Subregion 3a
        #Eq 8, Table 13, Page 14
        Ii = Array(- 12, - 12, - 12, - 10, - 10, - 10, - 10, - 8, - 8, - 8, - 8, - 6, - 5, - 4, - 3, - 3, - 2, - 2, - 1, - 1, 0, 0, 0, 1, 2, 4, 5, 6)
        Ji = Array(10, 12, 14, 4, 8, 10, 20, 5, 6, 14, 16, 28, 1, 5, 2, 4, 3, 8, 1, 2, 0, 1, 3, 0, 0, 2, 2, 0)
        ni = Array(79.5544074093975, - 2382.6124298459, 17681.3100617787, - 1.10524727080379E-03, - 15.3213833655326, 297.544599376982, - 35031520.6871242, 0.277513761062119, - 0.523964271036888, - 148011.182995403, 1600148.99374266, 1708023226634.27, 2.46866996006494E-04, 1.6532608479798, - 0.118008384666987, 2.537986423559, 0.965127704669424, - 28.2172420532826, 0.203224612353823, 1.10648186063513, 0.52612794845128, 0.277000018736321, 1.08153340501132, - 7.44127885357893E-02, 1.64094443541384E-02, - 6.80468275301065E-02, 0.025798857610164, - 1.45749861944416E-04)
        ps = p / 100
        sigma = s / 4.4
        omega = 0
        for i in range(0, 1 + 27):
            omega = omega + ni(i) *  ( ps + 0.187 )  ** Ii(i) *  ( sigma - 0.755 )  ** Ji(i)
        _ret = omega * 0.0028
    else:
        #Subregion 3b
        #Eq 9, Table 14, Page 14
        Ii = Array(- 12, - 12, - 12, - 12, - 12, - 12, - 10, - 10, - 10, - 10, - 8, - 5, - 5, - 5, - 4, - 4, - 4, - 4, - 3, - 2, - 2, - 2, - 2, - 2, - 2, 0, 0, 0, 1, 1, 2)
        Ji = Array(0, 1, 2, 3, 5, 6, 0, 1, 2, 4, 0, 1, 2, 3, 0, 1, 2, 3, 1, 0, 1, 2, 3, 4, 12, 0, 1, 2, 0, 2, 2)
        ni = Array(5.91599780322238E-05, - 1.85465997137856E-03, 1.04190510480013E-02, 5.9864730203859E-03, - 0.771391189901699, 1.72549765557036, - 4.67076079846526E-04, 1.34533823384439E-02, - 8.08094336805495E-02, 0.508139374365767, 1.28584643361683E-03, - 1.63899353915435, 5.86938199318063, - 2.92466667918613, - 6.14076301499537E-03, 5.76199014049172, - 12.1613320606788, 1.67637540957944, - 7.44135838773463, 3.78168091437659E-02, 4.01432203027688, 16.0279837479185, 3.17848779347728, - 3.58362310304853, - 1159952.60446827, 0.199256573577909, - 0.122270624794624, - 19.1449143716586, - 1.50448002905284E-02, 14.6407900162154, - 3.2747778718823)
        ps = p / 100
        sigma = s / 5.3
        omega = 0
        for i in range(0, 1 + 30):
            omega = omega + ni(i) *  ( ps + 0.298 )  ** Ii(i) *  ( sigma - 0.816 )  ** Ji(i)
        _ret = omega * 0.0088
    return _ret

def p3_hs(h, s):
    _ret = None
    # i = Integer()

    # Ji = Variant()

    # Ii = Variant()

    # ni = Variant()

    # ps = Variant()

    # sigma = Variant()

    # eta = Double()

    R = 0.461526

    tc = 647.096

    pc = 22.064

    rhoc = 322
    #Supplementary Release on Backward Equations ( ) , p h s for Region 3,
    #Equations as a Function of h and s for the Region Boundaries, and an Equation
    #( ) sat , T hs for Region 4 of the IAPWS Industrial Formulation 1997 for the
    #Thermodynamic Properties of Water and Steam
    #2004
    #Section 3 Backward Functions p(h,s), T(h,s), and v(h,s) for Region 3
    if s < 4.41202148223476:
        #Subregion 3a
        #Eq 1, Table 3, Page 8
        Ii = Array(0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 6, 7, 8, 10, 10, 14, 18, 20, 22, 22, 24, 28, 28, 32, 32)
        Ji = Array(0, 1, 5, 0, 3, 4, 8, 14, 6, 16, 0, 2, 3, 0, 1, 4, 5, 28, 28, 24, 1, 32, 36, 22, 28, 36, 16, 28, 36, 16, 36, 10, 28)
        ni = Array(7.70889828326934, - 26.0835009128688, 267.416218930389, 17.2221089496844, - 293.54233214597, 614.135601882478, - 61056.2757725674, - 65127225.1118219, 73591.9313521937, - 11664650591.4191, 35.5267086434461, - 596.144543825955, - 475.842430145708, 69.6781965359503, 335.674250377312, 25052.6809130882, 146997.380630766, 5.38069315091534E+19, 1.43619827291346E+21, 3.64985866165994E+19, - 2547.41561156775, 2.40120197096563E+27, - 3.93847464679496E+29, 1.47073407024852E+24, - 4.26391250432059E+31, 1.94509340621077E+38, 6.66212132114896E+23, 7.06777016552858E+33, 1.75563621975576E+41, 1.08408607429124E+28, 7.30872705175151E+43, 1.5914584739887E+24, 3.77121605943324E+40)
        sigma = s / 4.4
        eta = h / 2300
        ps = 0
        for i in range(0, 1 + 32):
            ps = ps + ni(i) *  ( eta - 1.01 )  ** Ii(i) *  ( sigma - 0.75 )  ** Ji(i)
        _ret = ps * 99
    else:
        #Subregion 3b
        #Eq 2, Table 4, Page 8
        Ii = Array(- 12, - 12, - 12, - 12, - 12, - 10, - 10, - 10, - 10, - 8, - 8, - 6, - 6, - 6, - 6, - 5, - 4, - 4, - 4, - 3, - 3, - 3, - 3, - 2, - 2, - 1, 0, 2, 2, 5, 6, 8, 10, 14, 14)
        Ji = Array(2, 10, 12, 14, 20, 2, 10, 14, 18, 2, 8, 2, 6, 7, 8, 10, 4, 5, 8, 1, 3, 5, 6, 0, 1, 0, 3, 0, 1, 0, 1, 1, 1, 3, 7)
        ni = Array(1.25244360717979E-13, - 1.26599322553713E-02, 5.06878030140626, 31.7847171154202, - 391041.161399932, - 9.75733406392044E-11, - 18.6312419488279, 510.973543414101, 373847.005822362, 2.99804024666572E-08, 20.0544393820342, - 4.98030487662829E-06, - 10.230180636003, 55.2819126990325, - 206.211367510878, - 7940.12232324823, 7.82248472028153, - 58.6544326902468, 3550.73647696481, - 1.15303107290162E-04, - 1.75092403171802, 257.98168774816, - 727.048374179467, 1.21644822609198E-04, 3.93137871762692E-02, 7.04181005909296E-03, - 82.910820069811, - 0.26517881813125, 13.7531682453991, - 52.2394090753046, 2405.56298941048, - 22736.1631268929, 89074.6343932567, - 23923456.5822486, 5687958081.29714)
        sigma = s / 5.3
        eta = h / 2800
        ps = 0
        for i in range(0, 1 + 34):
            ps = ps + ni(i) *  ( eta - 0.681 )  ** Ii(i) *  ( sigma - 0.792 )  ** Ji(i)
        _ret = 16.6 / ps
    return _ret

def h3_pT(p, T):
    _ret = None
    # Ts = Variant()

    # Low_Bound = Variant()

    # High_Bound = Variant()

    # hs = Double()
    #Not avalible with IF 97
    #Solve function T3_ph-T=0 with half interval method.
    #ver2.6 Start corrected bug
    if p < 22.06395:
        Ts = T4_p(p)
        if T <= Ts:
            High_Bound = h4L_p(p)
            Low_Bound = h1_pT(p, 623.15)
        else:
            Low_Bound = h4V_p(p)
            High_Bound = h2_pT(p, B23T_p(p))
    else:
        Low_Bound = h1_pT(p, 623.15)
        High_Bound = h2_pT(p, B23T_p(p))
    #ver2.6 End corrected bug
    Ts = T + 1
    while Abs(T - Ts) > 0.000001:
        hs = ( Low_Bound + High_Bound )  / 2
        Ts = T3_ph(p, hs)
        if Ts > T:
            High_Bound = hs
        else:
            Low_Bound = hs
    _ret = hs
    return _ret

def T3_prho(p, rho):
    _ret = None
    # ps = Variant()

    # Low_Bound = Variant()

    # High_Bound = Variant()

    # Ts = Double()
    #Solve by iteration. Observe that fo low temperatures this equation has 2 solutions.
    #Solve with half interval method
    Low_Bound = 623.15
    High_Bound = 1073.15
    while Abs(p - ps) > 0.00000001:
        Ts = ( Low_Bound + High_Bound )  / 2
        ps = p3_rhoT(rho, Ts)
        if ps > p:
            High_Bound = Ts
        else:
            Low_Bound = Ts
    _ret = Ts
    return _ret

def p4_T(T):
    _ret = None
    # teta = Variant()

    # a = Variant()

    # b = Variant()

    # c = Double()
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Section 8.1 The Saturation-Pressure Equation
    #Eq 30, Page 33
    teta = T - 0.23855557567849 /  ( T - 650.17534844798 )
    a = teta ** 2 + 1167.0521452767 * teta - 724213.16703206
    b = - 17.073846940092 * teta ** 2 + 12020.82470247 * teta - 3232555.0322333
    c = 14.91510861353 * teta ** 2 - 4823.2657361591 * teta + 405113.40542057
    _ret = ( 2 * c /  ( - b +  ( b ** 2 - 4 * a * c )  ** 0.5 ) )  ** 4
    return _ret

def T4_p(p):
    _ret = None
    # beta = Variant()

    # e = Variant()

    # f = Variant()

    # g = Variant()

    # d = Double()
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Section 8.2 The Saturation-Temperature Equation
    #Eq 31, Page 34
    beta = p ** 0.25
    e = beta ** 2 - 17.073846940092 * beta + 14.91510861353
    f = 1167.0521452767 * beta ** 2 + 12020.82470247 * beta - 4823.2657361591
    g = - 724213.16703206 * beta ** 2 - 3232555.0322333 * beta + 405113.40542057
    d = 2 * g /  ( - f -  ( f ** 2 - 4 * e * g )  ** 0.5 )
    _ret = ( 650.17534844798 + d -  ( ( 650.17534844798 + d )  ** 2 - 4 *  ( - 0.23855557567849 + 650.17534844798 * d ) )  ** 0.5 )  / 2
    return _ret

def h4_s(s):
    _ret = None
    # Ii = Variant()

    # Ji = Variant()

    # ni = Variant()

    # eta = Variant()

    # sigma = Variant()

    # sigma1 = Variant()

    # sigma2 = Double()

    # i = Integer()
    #Supplementary Release on Backward Equations ( ) , p h s for Region 3,Equations as a Function of h and s for the Region Boundaries, and an Equation( ) sat , T hs for Region 4 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #4 Equations for Region Boundaries Given Enthalpy and Entropy
    # Se picture page 14
    if s > - 0.0001545495919 and s <= 3.77828134:
        #hL1_s
        #Eq 3,Table 9,Page 16
        Ii = Array(0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 7, 8, 12, 12, 14, 14, 16, 20, 20, 22, 24, 28, 32, 32)
        Ji = Array(14, 36, 3, 16, 0, 5, 4, 36, 4, 16, 24, 18, 24, 1, 4, 2, 4, 1, 22, 10, 12, 28, 8, 3, 0, 6, 8)
        ni = Array(0.332171191705237, 6.11217706323496E-04, - 8.82092478906822, - 0.45562819254325, - 2.63483840850452E-05, - 22.3949661148062, - 4.28398660164013, - 0.616679338856916, - 14.682303110404, 284.523138727299, - 113.398503195444, 1156.71380760859, 395.551267359325, - 1.54891257229285, 19.4486637751291, - 3.57915139457043, - 3.35369414148819, - 0.66442679633246, 32332.1885383934, 3317.66744667084, - 22350.1257931087, 5739538.75852936, 173.226193407919, - 3.63968822121321E-02, 8.34596332878346E-07, 5.03611916682674, 65.5444787064505)
        sigma = s / 3.8
        eta = 0
        for i in range(0, 1 + 26):
            eta = eta + ni(i) *  ( sigma - 1.09 )  ** Ii(i) *  ( sigma + 0.0000366 )  ** Ji(i)
        _ret = eta * 1700
    elif s > 3.77828134 and s <= 4.41202148223476:
        #hL3_s
        #Eq 4,Table 10,Page 16
        Ii = Array(0, 0, 0, 0, 2, 3, 4, 4, 5, 5, 6, 7, 7, 7, 10, 10, 10, 32, 32)
        Ji = Array(1, 4, 10, 16, 1, 36, 3, 16, 20, 36, 4, 2, 28, 32, 14, 32, 36, 0, 6)
        ni = Array(0.822673364673336, 0.181977213534479, - 0.011200026031362, - 7.46778287048033E-04, - 0.179046263257381, 4.24220110836657E-02, - 0.341355823438768, - 2.09881740853565, - 8.22477343323596, - 4.99684082076008, 0.191413958471069, 5.81062241093136E-02, - 1655.05498701029, 1588.70443421201, - 85.0623535172818, - 31771.4386511207, - 94589.0406632871, - 1.3927384708869E-06, 0.63105253224098)
        sigma = s / 3.8
        eta = 0
        for i in range(0, 1 + 18):
            eta = eta + ni(i) *  ( sigma - 1.09 )  ** Ii(i) *  ( sigma + 0.0000366 )  ** Ji(i)
        _ret = eta * 1700
    elif s > 4.41202148223476 and s <= 5.85:
        #Section 4.4 Equations ( ) 2ab " h s and ( ) 2c3b "h s for the Saturated Vapor Line
        #Page 19, Eq 5
        #hV2c3b_s(s)
        Ii = Array(0, 0, 0, 1, 1, 5, 6, 7, 8, 8, 12, 16, 22, 22, 24, 36)
        Ji = Array(0, 3, 4, 0, 12, 36, 12, 16, 2, 20, 32, 36, 2, 32, 7, 20)
        ni = Array(1.04351280732769, - 2.27807912708513, 1.80535256723202, 0.420440834792042, - 105721.24483466, 4.36911607493884E+24, - 328032702839.753, - 6.7868676080427E+15, 7439.57464645363, - 3.56896445355761E+19, 1.67590585186801E+31, - 3.55028625419105E+37, 396611982166.538, - 4.14716268484468E+40, 3.59080103867382E+18, - 1.16994334851995E+40)
        sigma = s / 5.9
        eta = 0
        for i in range(0, 1 + 15):
            eta = eta + ni(i) *  ( sigma - 1.02 )  ** Ii(i) *  ( sigma - 0.726 )  ** Ji(i)
        _ret = eta ** 4 * 2800
    elif s > 5.85 and s < 9.155759395:
        #Section 4.4 Equations ( ) 2ab " h s and ( ) 2c3b "h s for the Saturated Vapor Line
        #Page 20, Eq 6
        Ii = Array(1, 1, 2, 2, 4, 4, 7, 8, 8, 10, 12, 12, 18, 20, 24, 28, 28, 28, 28, 28, 32, 32, 32, 32, 32, 36, 36, 36, 36, 36)
        Ji = Array(8, 24, 4, 32, 1, 2, 7, 5, 12, 1, 0, 7, 10, 12, 32, 8, 12, 20, 22, 24, 2, 7, 12, 14, 24, 10, 12, 20, 22, 28)
        ni = Array(- 524.581170928788, - 9269472.18142218, - 237.385107491666, 21077015581.2776, - 23.9494562010986, 221.802480294197, - 5104725.33393438, 1249813.96109147, 2000084369.96201, - 815.158509791035, - 157.612685637523, - 11420042233.2791, 6.62364680776872E+15, - 2.27622818296144E+18, - 1.71048081348406E+31, 6.60788766938091E+15, 1.66320055886021E+22, - 2.18003784381501E+29, - 7.87276140295618E+29, 1.51062329700346E+31, 7957321.70300541, 1.31957647355347E+15, - 3.2509706829914E+23, - 4.18600611419248E+25, 2.97478906557467E+34, - 9.53588761745473E+19, 1.66957699620939E+24, - 1.75407764869978E+32, 3.47581490626396E+34, - 7.10971318427851E+38)
        sigma1 = s / 5.21
        sigma2 = s / 9.2
        eta = 0
        for i in range(0, 1 + 29):
            eta = eta + ni(i) *  ( 1 / sigma1 - 0.513 )  ** Ii(i) *  ( sigma2 - 0.524 )  ** Ji(i)
        _ret = Exp(eta) * 2800
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def p4_s(s):
    _ret = None
    # hsat = Double()
    #Uses h4_s and p_hs for the diffrent regions to determine p4_s
    hsat = h4_s(s)
    if s > - 0.0001545495919 and s <= 3.77828134:
        _ret = p1_hs(hsat, s)
    elif s > 3.77828134 and s <= 5.210887663:
        _ret = p3_hs(hsat, s)
    elif s > 5.210887663 and s < 9.155759395:
        _ret = p2_hs(hsat, s)
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def h4L_p(p):
    _ret = None
    # Low_Bound = Variant()

    # High_Bound = Variant()

    # hs = Variant()

    # ps = Variant()

    # Ts = Double()
    if p > 0.000611657 and p < 22.06395:
        Ts = T4_p(p)
        if p < 16.529:
            _ret = h1_pT(p, Ts)
        else:
            #Iterate to find the the backward solution of p3sat_h
            Low_Bound = 1670.858218
            High_Bound = 2087.23500164864
            while Abs(p - ps) > 0.00001:
                hs = ( Low_Bound + High_Bound )  / 2
                ps = p3sat_h(hs)
                if ps > p:
                    High_Bound = hs
                else:
                    Low_Bound = hs
            _ret = hs
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def h4V_p(p):
    _ret = None
    # Low_Bound = Variant()

    # High_Bound = Variant()

    # hs = Variant()

    # ps = Variant()

    # Ts = Double()
    if p > 0.000611657 and p < 22.06395:
        Ts = T4_p(p)
        if p < 16.529:
            _ret = h2_pT(p, Ts)
        else:
            #Iterate to find the the backward solution of p3sat_h
            Low_Bound = 2087.23500164864
            High_Bound = 2563.592004 + 5
            while Abs(p - ps) > 0.000001:
                hs = ( Low_Bound + High_Bound )  / 2
                ps = p3sat_h(hs)
                if ps < p:
                    High_Bound = hs
                else:
                    Low_Bound = hs
            _ret = hs
    else:
        _ret = CVErr("""xlErrValue""")
    return _ret

def x4_ph(p, h):
    _ret = None
    # h4v = Variant()

    # h4l = Double()
    #Calculate vapour fraction from hL and hV for given p
    h4v = h4V_p(p)
    h4l = h4L_p(p)
    if h > h4v:
        _ret = 1
    elif h < h4l:
        _ret = 0
    else:
        _ret = ( h - h4l )  /  ( h4v - h4l )
    return _ret

def x4_ps(p, s):
    _ret = None
    # ssV = Variant()

    # ssL = Double()
    if p < 16.529:
        ssV = s2_pT(p, T4_p(p))
        ssL = s1_pT(p, T4_p(p))
    else:
        ssV = s3_rhoT(1 /  ( v3_ph(p, h4V_p(p)) ), T4_p(p))
        ssL = s3_rhoT(1 /  ( v3_ph(p, h4L_p(p)) ), T4_p(p))
    if s < ssL:
        _ret = 0
    elif s > ssV:
        _ret = 1
    else:
        _ret = ( s - ssL )  /  ( ssV - ssL )
    return _ret

def T4_hs(h, s):
    _ret = None
    # Ii = Variant()

    # Ji = Variant()

    # ni = Variant()

    # hL = Variant()

    # Ts = Variant()

    # ss = Variant()

    # p = Variant()

    # sigma = Variant()

    # eta = Variant()

    # teta = Variant()

    # High_Bound = Variant()

    # Low_Bound = Variant()

    # PL = Variant()

    # s4V = Variant()

    # v4V = Variant()

    # s4L = Variant()

    # v4L = Variant()

    # xs = Double()

    # i = Integer()
    #Supplementary Release on Backward Equations ( ) , p h s for Region 3,
    #Chapter 5.3 page 30.
    #The if 97 function is only valid for part of region4. Use iteration outsida.
    Ii = Array(0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5, 5, 6, 6, 6, 8, 10, 10, 12, 14, 14, 16, 16, 18, 18, 18, 20, 28)
    Ji = Array(0, 3, 12, 0, 1, 2, 5, 0, 5, 8, 0, 2, 3, 4, 0, 1, 1, 2, 4, 16, 6, 8, 22, 1, 20, 36, 24, 1, 28, 12, 32, 14, 22, 36, 24, 36)
    ni = Array(0.179882673606601, - 0.267507455199603, 1.162767226126, 0.147545428713616, - 0.512871635973248, 0.421333567697984, 0.56374952218987, 0.429274443819153, - 3.3570455214214, 10.8890916499278, - 0.248483390456012, 0.30415322190639, - 0.494819763939905, 1.07551674933261, 7.33888415457688E-02, 1.40170545411085E-02, - 0.106110975998808, 1.68324361811875E-02, 1.25028363714877, 1013.16840309509, - 1.51791558000712, 52.4277865990866, 23049.5545563912, 2.49459806365456E-02, 2107964.67412137, 366836848.613065, - 144814105.365163, - 1.7927637300359E-03, 4899556021.00459, 471.262212070518, - 82929439019.8652, - 1715.45662263191, 3557776.82973575, 586062760258.436, - 12988763.5078195, 31724744937.1057)
    if  ( s > 5.210887825 and s < 9.15546555571324 ) :
        sigma = s / 9.2
        eta = h / 2800
        teta = 0
        for i in range(0, 1 + 35):
            teta = teta + ni(i) *  ( eta - 0.119 )  ** Ii(i) *  ( sigma - 1.07 )  ** Ji(i)
        _ret = teta * 550
    else:
        #Function psat_h
        if s > - 0.0001545495919 and s <= 3.77828134:
            Low_Bound = 0.000611
            High_Bound = 165.291642526045
            while Abs(hL - h) > 0.00001 and Abs(High_Bound - Low_Bound) > 0.0001:
                PL = ( Low_Bound + High_Bound )  / 2
                Ts = T4_p(PL)
                hL = h1_pT(PL, Ts)
                if hL > h:
                    High_Bound = PL
                else:
                    Low_Bound = PL
        elif s > 3.77828134 and s <= 4.41202148223476:
            PL = p3sat_h(h)
        elif s > 4.41202148223476 and s <= 5.210887663:
            PL = p3sat_h(h)
        Low_Bound = 0.000611
        High_Bound = PL
        while Abs(s - ss) > 0.000001 and Abs(High_Bound - Low_Bound) > 0.0000001:
            p = ( Low_Bound + High_Bound )  / 2
            #Calculate s4_ph
            Ts = T4_p(p)
            xs = x4_ph(p, h)
            if p < 16.529:
                s4V = s2_pT(p, Ts)
                s4L = s1_pT(p, Ts)
            else:
                v4V = v3_ph(p, h4V_p(p))
                s4V = s3_rhoT(1 / v4V, Ts)
                v4L = v3_ph(p, h4L_p(p))
                s4L = s3_rhoT(1 / v4L, Ts)
            ss = ( xs * s4V +  ( 1 - xs )  * s4L )
            if ss < s:
                High_Bound = p
            else:
                Low_Bound = p
        _ret = T4_p(p)
    return _ret

def h5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0_tau = Variant()

    # gammar_tau = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0_tau = 0
    for i in range(0, 1 + 5):
        gamma0_tau = gamma0_tau + ni0(i) * Ji0(i) * tau **  ( Ji0(i) - 1 )
    gammar_tau = 0
    for i in range(0, 1 + 4):
        gammar_tau = gammar_tau + nir(i) * p ** Iir(i) * Jir(i) * tau **  ( Jir(i) - 1 )
    _ret = R * T * tau *  ( gamma0_tau + gammar_tau )
    return _ret

def v5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0_pi = Variant()

    # gammar_pi = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0_pi = 1 / p
    gammar_pi = 0
    for i in range(0, 1 + 4):
        gammar_pi = gammar_pi + nir(i) * Iir(i) * p **  ( Iir(i) - 1 )  * tau ** Jir(i)
    _ret = R * T / p * p *  ( gamma0_pi + gammar_pi )  / 1000
    return _ret

def u5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0_pi = Variant()

    # gammar_pi = Variant()

    # gamma0_tau = Variant()

    # gammar_tau = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0_pi = 1 / p
    gamma0_tau = 0
    for i in range(0, 1 + 5):
        gamma0_tau = gamma0_tau + ni0(i) * Ji0(i) * tau **  ( Ji0(i) - 1 )
    gammar_pi = 0
    gammar_tau = 0
    for i in range(0, 1 + 4):
        gammar_pi = gammar_pi + nir(i) * Iir(i) * p **  ( Iir(i) - 1 )  * tau ** Jir(i)
        gammar_tau = gammar_tau + nir(i) * p ** Iir(i) * Jir(i) * tau **  ( Jir(i) - 1 )
    _ret = R * T *  ( tau *  ( gamma0_tau + gammar_tau )  - p *  ( gamma0_pi + gammar_pi ) )
    return _ret

def Cp5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0_tautau = Variant()

    # gammar_tautau = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0_tautau = 0
    for i in range(0, 1 + 5):
        gamma0_tautau = gamma0_tautau + ni0(i) * Ji0(i) *  ( Ji0(i) - 1 )  * tau **  ( Ji0(i) - 2 )
    gammar_tautau = 0
    for i in range(0, 1 + 4):
        gammar_tautau = gammar_tautau + nir(i) * p ** Iir(i) * Jir(i) *  ( Jir(i) - 1 )  * tau **  ( Jir(i) - 2 )
    _ret = - R * tau ** 2 *  ( gamma0_tautau + gammar_tautau )
    return _ret

def s5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0 = Variant()

    # gamma0_tau = Variant()

    # gammar = Variant()

    # gammar_tau = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0 = Log(p)
    gamma0_tau = 0
    for i in range(0, 1 + 5):
        gamma0_tau = gamma0_tau + ni0(i) * Ji0(i) * tau **  ( Ji0(i) - 1 )
        gamma0 = gamma0 + ni0(i) * tau ** Ji0(i)
    gammar = 0
    gammar_tau = 0
    for i in range(0, 1 + 4):
        gammar = gammar + nir(i) * p ** Iir(i) * tau ** Jir(i)
        gammar_tau = gammar_tau + nir(i) * p ** Iir(i) * Jir(i) * tau **  ( Jir(i) - 1 )
    _ret = R *  ( tau *  ( gamma0_tau + gammar_tau )  -  ( gamma0 + gammar ) )
    return _ret

def Cv5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0_tautau = Variant()

    # gammar_pi = Variant()

    # gammar_pitau = Variant()

    # gammar_pipi = Variant()

    # gammar_tautau = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0_tautau = 0
    for i in range(0, 1 + 5):
        gamma0_tautau = gamma0_tautau + ni0(i) *  ( Ji0(i) - 1 )  * Ji0(i) * tau **  ( Ji0(i) - 2 )
    gammar_pi = 0
    gammar_pitau = 0
    gammar_pipi = 0
    gammar_tautau = 0
    for i in range(0, 1 + 4):
        gammar_pi = gammar_pi + nir(i) * Iir(i) * p **  ( Iir(i) - 1 )  * tau ** Jir(i)
        gammar_pitau = gammar_pitau + nir(i) * Iir(i) * p **  ( Iir(i) - 1 )  * Jir(i) * tau **  ( Jir(i) - 1 )
        gammar_pipi = gammar_pipi + nir(i) * Iir(i) *  ( Iir(i) - 1 )  * p **  ( Iir(i) - 2 )  * tau ** Jir(i)
        gammar_tautau = gammar_tautau + nir(i) * p ** Iir(i) * Jir(i) *  ( Jir(i) - 1 )  * tau **  ( Jir(i) - 2 )
    _ret = R *  ( - ( tau ** 2 *  ( gamma0_tautau + gammar_tautau ) )  -  ( 1 + p * gammar_pi - tau * p * gammar_pitau )  ** 2 /  ( 1 - p ** 2 * gammar_pipi ) )
    return _ret

def w5_pT(p, T):
    _ret = None
    # Iir = Variant()

    # Jir = Variant()

    # nir = Variant()

    # ni0 = Variant()

    # Ji0 = Variant()

    # tau = Variant()

    # gamma0_tautau = Variant()

    # gammar_pi = Variant()

    # gammar_pitau = Variant()

    # gammar_pipi = Variant()

    # gammar_tautau = Double()

    # i = Integer()

    R = 0.461526
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam, September 1997
    #Basic Equation for Region 5
    #Eq 32,33, Page 36, Tables 37-41
    Ji0 = Array(0, 1, - 3, - 2, - 1, 2)
    ni0 = Array(- 13.179983674201, 6.8540841634434, - 0.024805148933466, 0.36901534980333, - 3.1161318213925, - 0.32961626538917)
    Iir = Array(1, 1, 1, 2, 3)
    Jir = Array(0, 1, 3, 9, 3)
    nir = Array(- 1.2563183589592E-04, 2.1774678714571E-03, - 0.004594282089991, - 3.9724828359569E-06, 1.2919228289784E-07)
    tau = 1000 / T
    gamma0_tautau = 0
    for i in range(0, 1 + 5):
        gamma0_tautau = gamma0_tautau + ni0(i) *  ( Ji0(i) - 1 )  * Ji0(i) * tau **  ( Ji0(i) - 2 )
    gammar_pi = 0
    gammar_pitau = 0
    gammar_pipi = 0
    gammar_tautau = 0
    for i in range(0, 1 + 4):
        gammar_pi = gammar_pi + nir(i) * Iir(i) * p **  ( Iir(i) - 1 )  * tau ** Jir(i)
        gammar_pitau = gammar_pitau + nir(i) * Iir(i) * p **  ( Iir(i) - 1 )  * Jir(i) * tau **  ( Jir(i) - 1 )
        gammar_pipi = gammar_pipi + nir(i) * Iir(i) *  ( Iir(i) - 1 )  * p **  ( Iir(i) - 2 )  * tau ** Jir(i)
        gammar_tautau = gammar_tautau + nir(i) * p ** Iir(i) * Jir(i) *  ( Jir(i) - 1 )  * tau **  ( Jir(i) - 2 )
    _ret = ( 1000 * R * T *  ( 1 + 2 * p * gammar_pi + p ** 2 * gammar_pi ** 2 )  /  ( ( 1 - p ** 2 * gammar_pipi )  +  ( 1 + p * gammar_pi - tau * p * gammar_pitau )  ** 2 /  ( tau ** 2 *  ( gamma0_tautau + gammar_tautau ) ) ) )  ** 0.5
    return _ret

def T5_ph(p, h):
    _ret = None
    # Low_Bound = Variant()

    # High_Bound = Variant()

    # Ts = Variant()

    # hs = Double()
    #Solve with half interval method
    Low_Bound = 1073.15
    High_Bound = 2273.15
    while Abs(h - hs) > 0.00001:
        Ts = ( Low_Bound + High_Bound )  / 2
        hs = h5_pT(p, Ts)
        if hs > h:
            High_Bound = Ts
        else:
            Low_Bound = Ts
    _ret = Ts
    return _ret

def T5_ps(p, s):
    _ret = None
    # Low_Bound = Variant()

    # High_Bound = Variant()

    # Ts = Variant()

    # ss = Double()
    #Solve with half interval method
    Low_Bound = 1073.15
    High_Bound = 2273.15
    while Abs(s - ss) > 0.00001:
        Ts = ( Low_Bound + High_Bound )  / 2
        ss = s5_pT(p, Ts)
        if ss > s:
            High_Bound = Ts
        else:
            Low_Bound = Ts
    _ret = Ts
    return _ret

def T5_prho(p, rho):
    _ret = None
    # Low_Bound = Variant()

    # High_Bound = Variant()

    # Ts = Variant()

    # rhos = Double()
    #Solve by iteration. Observe that fo low temperatures this equation has 2 solutions.
    #Solve with half interval method
    Low_Bound = 1073.15
    High_Bound = 2073.15
    while Abs(rho - rhos) > 0.000001:
        Ts = ( Low_Bound + High_Bound )  / 2
        rhos = 1 / v2_pT(p, Ts)
        if rhos < rho:
            High_Bound = Ts
        else:
            Low_Bound = Ts
    _ret = Ts
    return _ret

def region_pT(p, T):
    _ret = None
    # ps = Double()
    if T > 1073.15 and p < 10 and T < 2273.15 and p > 0.000611:
        _ret = 5
    elif T <= 1073.15 and T > 273.15 and p <= 100 and p > 0.000611:
        if T > 623.15:
            if p > B23p_T(T):
                _ret = 3
                if T < 647.096:
                    ps = p4_T(T)
                    if Abs(p - ps) < 0.00001:
                        _ret = 4
            else:
                _ret = 2
        else:
            ps = p4_T(T)
            if Abs(p - ps) < 0.00001:
                _ret = 4
            elif p > ps:
                _ret = 1
            else:
                _ret = 2
    else:
        _ret = 0
    return _ret

def region_ph(p, h):
    _ret = None
    # hL = Variant()

    # hV = Variant()

    # h_45 = Variant()

    # h_5u = Variant()

    # Ts = Double()
    #Check if outside pressure limits
    if p < 0.000611657 or p > 100:
        _ret = 0
        return _ret
    #Check if outside low h.
    if h < 0.963 * p + 2.2:
        if h < h1_pT(p, 273.15):
            _ret = 0
            return _ret
    if p < 16.5292:
        #Check Region 1
        Ts = T4_p(p)
        hL = 109.6635 * Log(p) + 40.3481 * p + 734.58
        if Abs(h - hL) < 100:
            hL = h1_pT(p, Ts)
        if h <= hL:
            _ret = 1
            return _ret
        #Check Region 4
        hV = 45.1768 * Log(p) - 20.158 * p + 2804.4
        if Abs(h - hV) < 50:
            hV = h2_pT(p, Ts)
        if h < hV:
            _ret = 4
            return _ret
        #Check upper limit of region 2 Quick Test
        if h < 4000:
            _ret = 2
            return _ret
        #Check region 2 (Real value)
        h_45 = h2_pT(p, 1073.15)
        if h <= h_45:
            _ret = 2
            return _ret
        #Check region 5
        if p > 10:
            _ret = 0
            return _ret
        h_5u = h5_pT(p, 2273.15)
        if h < h_5u:
            _ret = 5
            return _ret
        _ret = 0
        return _ret
    else:
        #Check if in region1
        if h < h1_pT(p, 623.15):
            _ret = 1
            return _ret
        #Check if in region 3 or 4 (Bellow Reg 2)
        if h < h2_pT(p, B23T_p(p)):
            #Region 3 or 4
            if p > p3sat_h(h):
                _ret = 3
                return _ret
            else:
                _ret = 4
                return _ret
        #Check if region 2
        if h < h2_pT(p, 1073.15):
            _ret = 2
            return _ret
    _ret = 0
    return _ret

def region_ps(p, s):
    _ret = None
    # ss = Double()
    if p < 0.000611657 or p > 100 or s < 0 or s > s5_pT(p, 2273.15):
        _ret = 0
        return _ret
    #Check region 5
    if s > s2_pT(p, 1073.15):
        if p <= 10:
            _ret = 5
            return _ret
        else:
            _ret = 0
            return _ret
    #Check region 2
    if p > 16.529:
        ss = s2_pT(p, B23T_p(p))
    else:
        ss = s2_pT(p, T4_p(p))
    if s > ss:
        _ret = 2
        return _ret
    #Check region 3
    ss = s1_pT(p, 623.15)
    if p > 16.529 and s > ss:
        if p > p3sat_s(s):
            _ret = 3
            return _ret
        else:
            _ret = 4
            return _ret
    #Check region 4 (Not inside region 3)
    if p < 16.529 and s > s1_pT(p, T4_p(p)):
        _ret = 4
        return _ret
    #Check region 1
    if p > 0.000611657 and s > s1_pT(p, 273.15):
        _ret = 1
        return _ret
    _ret = 1
    return _ret

def Region_hs(h, s):
    _ret = None
    # TMax = Variant()

    # hMax = Variant()

    # hB = Variant()

    # hL = Variant()

    # hV = Variant()

    # vmax = Variant()

    # Tmin = Variant()

    # hMin = Double()
    if s < - 0.0001545495919:
        _ret = 0
        return _ret
    #Check linear adaption to p=0.000611. If bellow region 4.
    hMin = ( ( ( - 0.0415878 - 2500.89262 )  /  ( - 0.00015455 - 9.155759 ) )  * s )
    if s < 9.155759395 and h < hMin:
        _ret = 0
        return _ret
    #******Kolla 1 eller 4. (+liten bit �ver B13)
    if s >= - 0.0001545495919 and s <= 3.77828134:
        if h < h4_s(s):
            _ret = 4
            return _ret
        elif s < 3.397782955:
            TMax = T1_ps(100, s)
            hMax = h1_pT(100, TMax)
            if h < hMax:
                _ret = 1
                return _ret
            else:
                _ret = 0
                return _ret
        else:
            hB = hB13_s(s)
            if h < hB:
                _ret = 1
                return _ret
            TMax = T3_ps(100, s)
            vmax = v3_ps(100, s)
            hMax = h3_rhoT(1 / vmax, TMax)
            if h < hMax:
                _ret = 3
                return _ret
            else:
                _ret = 0
                return _ret
    #******Kolla region 2 eller 4. (�vre delen av omr�de b23-> max)
    if s >= 5.260578707 and s <= 11.9212156897728:
        if s > 9.155759395:
            Tmin = T2_ps(0.000611, s)
            hMin = h2_pT(0.000611, Tmin)
            #Function adapted to h(1073.15,s)
            hMax = - 0.07554022 * s ** 4 + 3.341571 * s ** 3 - 55.42151 * s ** 2 + 408.515 * s + 3031.338
            if h > hMin and h < hMax:
                _ret = 2
                return _ret
            else:
                _ret = 0
                return _ret
        hV = h4_s(s)
        if h < hV:
            _ret = 4
            return _ret
        if s < 6.04048367171238:
            TMax = T2_ps(100, s)
            hMax = h2_pT(100, TMax)
        else:
            #Function adapted to h(1073.15,s)
            hMax = - 2.988734 * s ** 4 + 121.4015 * s ** 3 - 1805.15 * s ** 2 + 11720.16 * s - 23998.33
        if h < hMax:
            _ret = 2
            return _ret
        else:
            _ret = 0
            return _ret
    #Kolla region 3 eller 4. Under kritiska punkten.
    if s >= 3.77828134 and s <= 4.41202148223476:
        hL = h4_s(s)
        if h < hL:
            _ret = 4
            return _ret
        TMax = T3_ps(100, s)
        vmax = v3_ps(100, s)
        hMax = h3_rhoT(1 / vmax, TMax)
        if h < hMax:
            _ret = 3
            return _ret
        else:
            _ret = 0
            return _ret
    #Kolla region 3 eller 4 fr�n kritiska punkten till �vre delen av b23
    if s >= 4.41202148223476 and s <= 5.260578707:
        hV = h4_s(s)
        if h < hV:
            _ret = 4
            return _ret
        #Kolla om vi �r under b23 giltighetsomr�de.
        if s <= 5.048096828:
            TMax = T3_ps(100, s)
            vmax = v3_ps(100, s)
            hMax = h3_rhoT(1 / vmax, TMax)
            if h < hMax:
                _ret = 3
                return _ret
            else:
                _ret = 0
                return _ret
        else:
            if  ( h > 2812.942061 ) :
                if s > 5.09796573397125:
                    TMax = T2_ps(100, s)
                    hMax = h2_pT(100, TMax)
                    if h < hMax:
                        _ret = 2
                        return _ret
                    else:
                        _ret = 0
                        return _ret
                else:
                    _ret = 0
                    return _ret
            if  ( h < 2563.592004 ) :
                _ret = 3
                return _ret
            #Vi �r inom b23 omr�det i b�de s och h led.
            if p2_hs(h, s) > B23p_T(TB23_hs(h, s)):
                _ret = 3
                return _ret
            else:
                _ret = 2
                return _ret
    _ret = CVErr("""xlErrValue""")
    return _ret

def Region_prho(p, rho):
    _ret = None
    # v = Double()
    v = 1 / rho
    if p < 0.000611657 or p > 100:
        _ret = 0
        return _ret
    if p < 16.5292:
        if v < v1_pT(p, 273.15):
            _ret = 0
            return _ret
        if v <= v1_pT(p, T4_p(p)):
            _ret = 1
            return _ret
        if v < v2_pT(p, T4_p(p)):
            _ret = 4
            return _ret
        if v <= v2_pT(p, 1073.15):
            _ret = 2
            return _ret
        if p > 10:
            _ret = 0
            return _ret
        if v <= v5_pT(p, 2073.15):
            _ret = 5
            return _ret
    else:
        if v < v1_pT(p, 273.15):
            _ret = 0
            return _ret
        if v < v1_pT(p, 623.15):
            _ret = 1
            return _ret
        #Check if in region 3 or 4 (Bellow Reg 2)
        if v < v2_pT(p, B23T_p(p)):
            #Region 3 or 4
            if p > 22.064:
                _ret = 3
                return _ret
            if v < v3_ph(p, h4L_p(p)) or v > v3_ph(p, h4V_p(p)):
                _ret = 3
                return _ret
            else:
                _ret = 4
                return _ret
        #Check if region 2
        if v < v2_pT(p, 1073.15):
            _ret = 2
            return _ret
    _ret = 0
    return _ret

def B23p_T(T):
    _ret = None
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #1997
    #Section 4 Auxiliary Equation for the Boundary between Regions 2 and 3
    #Eq 5, Page 5
    _ret = 348.05185628969 - 1.1671859879975 * T + 1.0192970039326E-03 * T ** 2
    return _ret

def B23T_p(p):
    _ret = None
    #Release on the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #1997
    #Section 4 Auxiliary Equation for the Boundary between Regions 2 and 3
    #Eq 6, Page 6
    _ret = 572.54459862746 +  ( ( p - 13.91883977887 )  / 1.0192970039326E-03 )  ** 0.5
    return _ret

def p3sat_h(h):
    _ret = None
    # Ii = Variant()

    # Ji = Variant()

    # ni = Variant()

    # ps = Double()

    # i = Integer()
    #Revised Supplementary Release on Backward Equations for the Functions T(p,h), v(p,h) and T(p,s), v(p,s) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam
    #2004
    #Section 4 Boundary Equations psat(h) and psat(s) for the Saturation Lines of Region 3
    #Se pictures Page 17, Eq 10, Table 17, Page 18
    Ii = Array(0, 1, 1, 1, 1, 5, 7, 8, 14, 20, 22, 24, 28, 36)
    Ji = Array(0, 1, 3, 4, 36, 3, 0, 24, 16, 16, 3, 18, 8, 24)
    ni = Array(0.600073641753024, - 9.36203654849857, 24.6590798594147, - 107.014222858224, - 91582131580576.8, - 8623.32011700662, - 23.5837344740032, 2.52304969384128E+17, - 3.89718771997719E+18, - 3.33775713645296E+22, 35649946963.6328, - 1.48547544720641E+26, 3.30611514838798E+18, 8.13641294467829E+37)
    h = h / 2600
    ps = 0
    for i in range(0, 1 + 13):
        ps = ps + ni(i) *  ( h - 1.02 )  ** Ii(i) *  ( h - 0.608 )  ** Ji(i)
    _ret = ps * 22
    return _ret

def p3sat_s(s):
    _ret = None
    # Ii = Variant()

    # Ji = Variant()

    # ni = Variant()

    # sigma = Variant()

    # p = Double()

    # i = Integer()
    Ii = Array(0, 1, 1, 4, 12, 12, 16, 24, 28, 32)
    Ji = Array(0, 1, 32, 7, 4, 14, 36, 10, 0, 18)
    ni = Array(0.639767553612785, - 12.9727445396014, - 2.24595125848403E+15, 1774667.41801846, 7170793495.71538, - 3.78829107169011E+17, - 9.55586736431328E+34, 1.87269814676188E+23, 119254746466.473, 1.10649277244882E+36)
    sigma = s / 5.2
    p = 0
    for i in range(0, 1 + 9):
        p = p + ni(i) *  ( sigma - 1.03 )  ** Ii(i) *  ( sigma - 0.699 )  ** Ji(i)
    _ret = p * 22
    return _ret

def hB13_s(s):
    _ret = None
    # Ii = Variant()

    # Ji = Variant()

    # ni = Variant()

    # sigma = Variant()

    # eta = Double()

    # i = Integer()
    #Supplementary Release on Backward Equations ( ) , p h s for Region 3,
    #Chapter 4.5 page 23.
    Ii = Array(0, 1, 1, 3, 5, 6)
    Ji = Array(0, - 2, 2, - 12, - 4, - 3)
    ni = Array(0.913965547600543, - 4.30944856041991E-05, 60.3235694765419, 1.17518273082168E-18, 0.220000904781292, - 69.0815545851641)
    sigma = s / 3.8
    eta = 0
    for i in range(0, 1 + 5):
        eta = eta + ni(i) *  ( sigma - 0.884 )  ** Ii(i) *  ( sigma - 0.864 )  ** Ji(i)
    _ret = eta * 1700
    return _ret

def TB23_hs(h, s):
    _ret = None
    # Ii = Variant()

    # Ji = Variant()

    # ni = Variant()

    # sigma = Variant()

    # eta = Variant()

    # teta = Double()

    # i = Integer()
    #Supplementary Release on Backward Equations ( ) , p h s for Region 3,
    #Chapter 4.6 page 25.
    Ii = Array(- 12, - 10, - 8, - 4, - 3, - 2, - 2, - 2, - 2, 0, 1, 1, 1, 3, 3, 5, 6, 6, 8, 8, 8, 12, 12, 14, 14)
    Ji = Array(10, 8, 3, 4, 3, - 6, 2, 3, 4, 0, - 3, - 2, 10, - 2, - 1, - 5, - 6, - 3, - 8, - 2, - 1, - 12, - 1, - 12, 1)
    ni = Array(6.2909626082981E-04, - 8.23453502583165E-04, 5.15446951519474E-08, - 1.17565945784945, 3.48519684726192, - 5.07837382408313E-12, - 2.84637670005479, - 2.36092263939673, 6.01492324973779, 1.48039650824546, 3.60075182221907E-04, - 1.26700045009952E-02, - 1221843.32521413, 0.149276502463272, 0.698733471798484, - 2.52207040114321E-02, 1.47151930985213E-02, - 1.08618917681849, - 9.36875039816322E-04, 81.9877897570217, - 182.041861521835, 2.61907376402688E-06, - 29162.6417025961, 1.40660774926165E-05, 7832370.62349385)
    sigma = s / 5.3
    eta = h / 3000
    teta = 0
    for i in range(0, 1 + 24):
        teta = teta + ni(i) *  ( eta - 0.727 )  ** Ii(i) *  ( sigma - 0.864 )  ** Ji(i)
    _ret = teta * 900
    return _ret

def my_AllRegions_pT(p, T):
    _ret = None
    # h0 = Variant()

    # h1 = Variant()

    # h2 = Variant()

    # h3 = Variant()

    # h4 = Variant()

    # h5 = Variant()

    # h6 = Variant()

    # rho = Variant()

    # Ts = Variant()

    # ps = Variant()

    # my0 = Variant()

    # sum = Variant()

    # my1 = Variant()

    # rhos = Double()

    # i = Integer()
    h0 = Array(0.5132047, 0.3205656, 0, 0, - 0.7782567, 0.1885447)
    h1 = Array(0.2151778, 0.7317883, 1.241044, 1.476783, 0, 0)
    h2 = Array(- 0.2818107, - 1.070786, - 1.263184, 0, 0, 0)
    h3 = Array(0.1778064, 0.460504, 0.2340379, - 0.4924179, 0, 0)
    h4 = Array(- 0.0417661, 0, 0, 0.1600435, 0, 0)
    h5 = Array(0, - 0.01578386, 0, 0, 0, 0)
    h6 = Array(0, 0, 0, - 0.003629481, 0, 0)
    #Calcualte density.
    _select29 = region_pT(p, T)
    if (_select29 == 1):
        rho = 1 / v1_pT(p, T)
    elif (_select29 == 2):
        rho = 1 / v2_pT(p, T)
    elif (_select29 == 3):
        rho = 1 / v3_ph(p, h3_pT(p, T))
    elif (_select29 == 4):
        rho = CVErr("""xlErrValue""")
    elif (_select29 == 5):
        rho = 1 / v5_pT(p, T)
    else:
        _ret = CVErr("""xlErrValue""")
        return _ret
    rhos = rho / 317.763
    Ts = T / 647.226
    ps = p / 22.115
    #Check valid area
    if T > 900 + 273.15 or  ( T > 600 + 273.15 and p > 300 )  or  ( T > 150 + 273.15 and p > 350 )  or p > 500:
        _ret = CVErr("""xlErrValue""")
        return _ret
    my0 = Ts ** 0.5 /  ( 1 + 0.978197 / Ts + 0.579829 /  ( Ts ** 2 )  - 0.202354 /  ( Ts ** 3 ) )
    sum = 0
    for i in range(0, 1 + 5):
        sum = sum + h0(i) *  ( 1 / Ts - 1 )  ** i + h1(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 1 + h2(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 2 + h3(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 3 + h4(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 4 + h5(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 5 + h6(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 6
    my1 = Exp(rhos * sum)
    _ret = my0 * my1 * 0.000055071
    return _ret

def my_AllRegions_ph(p, h):
    _ret = None
    # h0 = Variant()

    # h1 = Variant()

    # h2 = Variant()

    # h3 = Variant()

    # h4 = Variant()

    # h5 = Variant()

    # h6 = Variant()

    # rho = Variant()

    # T = Variant()

    # Ts = Variant()

    # ps = Variant()

    # my0 = Variant()

    # sum = Variant()

    # my1 = Variant()

    # rhos = Variant()

    # v4V = Variant()

    # v4L = Variant()

    # xs = Double()

    # i = Integer()
    h0 = Array(0.5132047, 0.3205656, 0, 0, - 0.7782567, 0.1885447)
    h1 = Array(0.2151778, 0.7317883, 1.241044, 1.476783, 0, 0)
    h2 = Array(- 0.2818107, - 1.070786, - 1.263184, 0, 0, 0)
    h3 = Array(0.1778064, 0.460504, 0.2340379, - 0.4924179, 0, 0)
    h4 = Array(- 0.0417661, 0, 0, 0.1600435, 0, 0)
    h5 = Array(0, - 0.01578386, 0, 0, 0, 0)
    h6 = Array(0, 0, 0, - 0.003629481, 0, 0)
    #Calcualte density.
    _select30 = region_ph(p, h)
    if (_select30 == 1):
        Ts = T1_ph(p, h)
        T = Ts
        rho = 1 / v1_pT(p, Ts)
    elif (_select30 == 2):
        Ts = T2_ph(p, h)
        T = Ts
        rho = 1 / v2_pT(p, Ts)
    elif (_select30 == 3):
        rho = 1 / v3_ph(p, h)
        T = T3_ph(p, h)
    elif (_select30 == 4):
        xs = x4_ph(p, h)
        if p < 16.529:
            v4V = v2_pT(p, T4_p(p))
            v4L = v1_pT(p, T4_p(p))
        else:
            v4V = v3_ph(p, h4V_p(p))
            v4L = v3_ph(p, h4L_p(p))
        rho = 1 /  ( xs * v4V +  ( 1 - xs )  * v4L )
        T = T4_p(p)
    elif (_select30 == 5):
        Ts = T5_ph(p, h)
        T = Ts
        rho = 1 / v5_pT(p, Ts)
    else:
        _ret = CVErr("""xlErrValue""")
        return _ret
    rhos = rho / 317.763
    Ts = T / 647.226
    ps = p / 22.115
    #Check valid area
    if T > 900 + 273.15 or  ( T > 600 + 273.15 and p > 300 )  or  ( T > 150 + 273.15 and p > 350 )  or p > 500:
        _ret = CVErr("""xlErrValue""")
        return _ret
    my0 = Ts ** 0.5 /  ( 1 + 0.978197 / Ts + 0.579829 /  ( Ts ** 2 )  - 0.202354 /  ( Ts ** 3 ) )
    sum = 0
    for i in range(0, 1 + 5):
        sum = sum + h0(i) *  ( 1 / Ts - 1 )  ** i + h1(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 1 + h2(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 2 + h3(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 3 + h4(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 4 + h5(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 5 + h6(i) *  ( 1 / Ts - 1 )  ** i *  ( rhos - 1 )  ** 6
    my1 = Exp(rhos * sum)
    _ret = my0 * my1 * 0.000055071
    return _ret

def tc_ptrho(p, T, rho):
    _ret = None
    # tc0 = Variant()

    # tc1 = Variant()

    # dT = Variant()

    # Q = Variant()

    # s = Variant()

    # tc2 = Variant()

    # tc = Double()
    #Revised release on the IAPS Formulation 1985 for the Thermal Conductivity of ordinary water
    #IAPWS September 1998
    #Page 8
    #ver2.6 Start corrected bug
    if T < 273.15:
        _ret = CVErr("""xlErrValue""")
        return _ret
    elif T < 500 + 273.15:
        if p > 100:
            _ret = CVErr("""xlErrValue""")
            return _ret
    elif T <= 650 + 273.15:
        if p > 70:
            _ret = CVErr("""xlErrValue""")
            return _ret
    elif T <= 800 + 273.15:
        if p > 40:
            _ret = CVErr("""xlErrValue""")
            return _ret
    #ver2.6 End corrected bug
    T = T / 647.26
    rho = rho / 317.7
    tc0 = T ** 0.5 *  ( 0.0102811 + 0.0299621 * T + 0.0156146 * T ** 2 - 0.00422464 * T ** 3 )
    tc1 = - 0.39707 + 0.400302 * rho + 1.06 * Exp(- 0.171587 *  ( rho + 2.39219 )  ** 2)
    dT = Abs(T - 1) + 0.00308976
    Q = 2 + 0.0822994 / dT **  ( 3 / 5 )
    if T >= 1:
        s = 1 / dT
    else:
        s = 10.0932 / dT **  ( 3 / 5 )
    tc2 = ( 0.0701309 / T ** 10 + 0.011852 )  * rho **  ( 9 / 5 )  * Exp(0.642857 *  ( 1 - rho **  ( 14 / 5 ) )) + 0.00169937 * s * rho ** Q * Exp(( Q /  ( 1 + Q ) )  *  ( 1 - rho **  ( 1 + Q ) )) - 1.02 * Exp(- 4.11717 * T **  ( 3 / 2 )  - 6.17937 / rho ** 5)
    _ret = tc0 + tc1 + tc2
    return _ret

def Surface_Tension_T(T):
    _ret = None
    # tau = Double()

    tc = 647.096

    b = 0.2358

    bb = - 0.625

    my = 1.256
    #IAPWS Release on Surface Tension of Ordinary Water Substance,
    #September 1994
    if T < 0.01 or T > tc:
        _ret = 'Out of valid region'
        return _ret
    tau = 1 - T / tc
    _ret = b * tau ** my *  ( 1 + bb * tau )
    return _ret

def toSIunit_p(Ins):
    _ret = None
    #Translate bar to MPa
    _ret = Ins / 10
    return _ret

def fromSIunit_p(Ins):
    _ret = None
    #Translate bar to MPa
    _ret = Ins * 10
    return _ret

def toSIunit_T(Ins):
    _ret = None
    #Translate degC to Kelvon
    _ret = Ins + 273.15
    return _ret

def fromSIunit_T(Ins):
    _ret = None
    #Translate Kelvin to degC
    _ret = Ins - 273.15
    return _ret

def toSIunit_h(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_h(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_v(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_v(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_s(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_s(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_u(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_u(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_Cp(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_Cp(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_Cv(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_Cv(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_w(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_w(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_tc(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_tc(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_st(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_st(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_x(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_x(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_vx(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_vx(Ins):
    _ret = None
    _ret = Ins
    return _ret

def toSIunit_my(Ins):
    _ret = None
    _ret = Ins
    return _ret

def fromSIunit_my(Ins):
    _ret = None
    _ret = Ins
    return _ret

def mixvisco(pressure, enthalpy):
    _ret = None
    #this function is to calculate mixture viscosity
    if enthalpy >= hV_p(pressure):
        _ret = my_ph(pressure, enthalpy)
    elif enthalpy > hL_p(pressure):
        _ret = dryness(enthalpy, pressure) * my_ph(pressure, hV_p(pressure)) +  ( 1 - dryness(enthalpy, pressure) )  * my_ph(pressure, hL_p(pressure))
    else:
        _ret = my_ph(pressure, enthalpy)
    return _ret

def dryness(enthalpy, pressure):
    _ret = None
    if x_ph(pressure, enthalpy) > 0.999:
        _ret = 1
    elif x_ph(pressure, enthalpy) < 0.001:
        _ret = 0
    else:
        _ret = x_ph(pressure, enthalpy)
    return _ret

# VB2PY (UntranslatedCode) Attribute VB_Name = "SteamTable"
# VB2PY (UntranslatedCode) Option Explicit
