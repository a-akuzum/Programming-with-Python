#All libraries used in this project:
import math
from pylab import *
import numpy
from matplotlib.pylab import *

#DC Motor's parameters:
Vdc=220
Po=150*745.6
N=1500
Ra=0.05
La=0.002
Kb=1.6
J=0.16 
B=0.01
fs=60
ws=2*math.pi*60

#Supply Input:
Vs=230

#Control Parameter:
Vcm=10
Hw=0.0634
Tw=0.002
Hc=0.01124
Kpi=100
Kii=1.5
Kps=10
Kis=1

#Rated Values
Trated=Po/(2*math.pi*(N/60))
Idc=Trated/Kb

wmref=(2*math.pi*(N/60))*Hw	#Speed reference in volts
Tc=Kii/Kpi	#Current controller
Kc=Tc*Kpi	#Current controller
Ts=Kis/Kps	#Speed controller
Ks=Ts*Kps	#Speed controller

#Initial Values
ia=0
Tl=0
alpha1=0
wm=0
x4=0
x5=0
x6=0

#Times
dt=0.0001	#Time increment for each step
t_final=0.2	#Final time 
t=0		#Initial time
t1=0

#Empty Array is created here to save every datas in 
#inside the While Loop
wmrefx=[]	#Speed reference
wmx=[]
Iarefx=[]	#Armature current reference
ex=[]
Iax=[]
alphax=[]	#Triggering Angle
Vax=[]
time=[]

def savingDatas():    #Function is created to call back in loop
	wmrefx.append(wmref)	#Which means in each iteration
	wmx.append(wm*Hw)	#datas will be saved into
	Iarefx.append(Iaref)	#empty array that is created 
	ex.append(Kb*wm)	#right before While loop
	Iax.append(ia)
	alphax.append(alpha1)
	Vax.append(Va)
	time.append(t)

def IarefLimitter(x,y):		#Function is created to check 
	if x > y:		#Iaref, basically its limitter
		x = y
	elif x < 0:
		x = 0

#While loop should run here 
loop=0

while t <= t_final:
	x4=x4+((Hw*wm)-x4)*dt/Tw	#State x4 
	wmerr=wmref-x4
	x5=x5+wmerr*dt	 #State x5	
	Iaref=((-Kps*x4)+(Kis*x5)+(Kps*wmref))*(Hc/Kb)
	
	IarefLimitter(Iaref,Vcm)	#Function is called back	

	x6=x6+((Iaref-(ia*Hc))*dt)	#State x6, PI Current controller
	vc=((-Kpi*ia*Hc)+(Kii*x6)+(Kpi*Iaref))	#Control voltage

	if vc>Vcm:
		vc=Vcm

	elif vc<0:
		vc=0

	wst=ws*t1
	t1=t1+dt

	if wst>math.pi/3:	#In every 60 degree, angular position
		t1=0
		alpha1=math.acos(vc/Vcm)	#Triggering angle


	Va=math.sqrt(2)*Vs*math.sin(wst+pi/3+alpha1)	#Armature input voltage	
	ia=(((-(Ra/La)*ia)-(Kb*wm)/La+(Va/La)))*dt+ia	#Armature current

	if ia<0:	#Only positive values of Armature current
		ia=0

	wm=wm+((Kb/J)*ia-(B/J)*wm-Tl/J)*dt	#Rotor speed
	t=t+dt	#Increment time in each iterations
	
	
	savingDatas()
	

	loop+=1	#Incrementing loop and start While loop again till	
		#condition of loop is fullfilled
	
#PLOTTING SECTION
figure(1)	#Speed and reference speed 
a=[x/wmref for x in wmx]
a1=[x/wmref for x in wmrefx]
plot(time,a,color="red", linewidth=2.5, linestyle="-",label="Speed")
#plot(time,a1,color="pink", linewidth=1.5, linestyle="-",label="Wmrefx/Wmref")
legend(loc='upper right')
xlabel('Time')
ylabel('Wmx/Wm_ref')

figure(2)	#Armature current
c=[x/Idc for x in Iax] #p.u
plot(time,c,color="green", linewidth=2.5, linestyle="-",label="Armature current [pu]")
legend(loc='upper right')
xlabel('Time')
ylabel('Iax / Idc')

figure(3)	#Armature current reference
b=[x/(Hc * Idc) for x in Iarefx] #p.u
plot(time,b,color="blue", linewidth=2.5, linestyle="-",label="Armature current reference [pu]")
legend(loc='upper right')
xlabel('Time')
ylabel('Ia_refx / (Hc*Idc)')



figure(4)	#Induced EMF
d=[x/Vdc for x in ex] #p.u
plot(time,d,color="yellow", linewidth=2.5, linestyle="-",label="Induced EMF [pu]")
legend(loc='upper right')
xlabel('Time')
ylabel('ex / Vdc')

figure(5)	#Armature input voltage
e=[x/Vdc for x in Vax] #p.u
plot(time,e, color="purple", linewidth=1.5, linestyle="-",label="Armature input voltage [pu]")
legend(loc='upper right')
xlabel('Time')
ylabel('Vax / Vdc')

figure(6)	#Trigger delay
plot(time,alphax, color="red", linewidth=2.5, linestyle="-",label="Trigger delay, alphax [rad]")
legend(loc='upper right')
xlabel('Time')
ylabel('alphax')

figure(7) #All figures in one besides Armature input voltage and trigger delay
plot(time,a,color="red", linewidth=2.5, linestyle="-",label="Speed")
plot(time,b,color="blue", linewidth=2.5, linestyle="-",label="Armature Current")
plot(time,c,color="green", linewidth=2.5, linestyle="-",label="Armature Current Reference")
plot(time,d,color="yellow", linewidth=2.5, linestyle="-",label="Induced Emf")
plot(time,e, color="purple", linewidth=0.3, linestyle="-",label="Armature Input Voltage")
legend(loc='lower right')
xlabel('Time')
ylabel('All Values')

show()






