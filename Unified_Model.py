

def calc_drain_current_nmos(Vgs, Vt0, Width, Length, Vds):
    drain_current = 0
    Vdsat=0.11
    Vt=Vt0-0.02*Vds                 #Vt0n is typically 0.2
    Vmin=min(Vdsat, Vds, Vgs-Vt)
    Kprime=420*(10**(-6))
    LambdaParam=0.02

    #print(Vgs-Vt)
    #print(Vmin)
    if (Vgs-Vt)<=0:
        drain_current=0
    elif (Vgs-Vt)>0:
        drain_current=Kprime*Width/Length*(((Vgs-Vt)*Vmin)-(Vmin**2)/2)*(1+LambdaParam*Vds)
    return drain_current

def calc_drain_current_pmos(Vgs, Vt0, Width, Length, Vds):
    drain_current = 0
    Vdsat=-0.11
    Vt=Vt0-0.04*Vds                 #Vt0p is typically 0.2
    Vmin=min(Vdsat, Vds, Vgs-Vt, key=abs)
    Kprime=-340*(10**(-6))
    LambdaParam=-0.15

    #print(Vgs-Vt)
    #print(Vmin)
    if (Vgs-Vt)>=0:
        drain_current=0
    elif (Vgs-Vt)<0:
        drain_current=Kprime*Width/Length*(((Vgs-Vt)*Vmin)-(Vmin**2)/2)*(1+LambdaParam*Vds)
    return drain_current


def calc_Req_n(Vdd):
    Id_nmos_fullVdd=calc_drain_current_nmos(Vdd,0.2,52,15,Vdd)
    Id_nmos_halfVdd=calc_drain_current_nmos(Vdd,0.2,52,15,Vdd*0.5)
##    print(Id_nmos_halfVdd)
    Req_n=0.5*(Vdd/Id_nmos_fullVdd+0.5*Vdd/Id_nmos_halfVdd)
    return Req_n

def calc_Req_p(Vdd):
    Id_pmos_fullVdd=calc_drain_current_pmos(-Vdd,-0.2,52,15,-Vdd)
    Id_pmos_halfVdd=calc_drain_current_pmos(-Vdd,-0.2,52,15,-Vdd*0.5)
    Req_p=0.5*(Vdd/Id_pmos_fullVdd+0.5*Vdd/Id_pmos_halfVdd)
    return abs(Req_p)    



##print(calc_drain_current_pmos(-0.8, -0.2, 52, 15, -0.4))
##print(calc_Req_n(0.8))
##print(calc_Req_p(0.8))