import pickle

vVar=pickle.load( open( "SOURCE/_var.pick", "rb" ) )
vRoom=pickle.load( open( "SOURCE/_room.pick", "rb" ) )

aR=list(filter(lambda x: x.later==True, vRoom))
bR=list(filter(lambda x: x.later==False, vRoom))
vRoom=bR+aR

QSP=""

def print(p):
	global QSP
	QSP+=(p+"\n")

print("#main")
print("""
$lastloc2=$curloc
$lastloc1=$curloc
""")
print("SET CND = 0")
for V in vVar.keys():
	if vVar[V]==True:
		print("SET {} = 1".format(V))
	else:
		print("SET {} = 0".format(V))
print("GOTO '{}'".format(vRoom[0].roomname))
print("-")



def IFTRUE(cvar):
	print("""IF {}=1:
	SET CND = CND AND 1
ELSE
	SET CND = CND AND 0
END""".format(cvar))

def IFFALSE(cvar):
	print("""IF {}=0:
	SET CND = CND AND 1
ELSE
	SET CND = CND AND 0
END""".format(cvar))

for i in range(0,len(vRoom)):
	R=vRoom[i]
	
	print("#"+R.roomname)
	
	print("""
$lastloc2=$lastloc1
$lastloc1=$curloc
""")
	
	for T in R.vText:
		print("SET CND=1")
		for C in T.trueVec:
			if C=="always":
				pass
			else:
				IFTRUE(C)
		for C in T.falseVec:
			IFFALSE(C)
		
		ptotal=""
		lines=T.text.split("\n")
		for l in lines:
			ptotal+="*pl '{}'\n".format(l.replace("'",""))
		
		print("""IF CND=1:
	{}
END""".format(ptotal))
	
	
	for A in R.vAct:
		print("SET CND=1")
		for C in A.trueVec:
			if C=="always":
				pass
			else:
				IFTRUE(C)
		for C in A.falseVec:
			IFFALSE(C)
		
		commands=""
		
		for CC in A.vComm:
			if CC.name=="goto":
				commands+="\t\tGOTO '{}'\n".format(CC.arg)
			if CC.name=="set":
				commands+="\t\tSET {}=1\n".format(CC.arg)
			if CC.name=="unset":
				commands+="\t\tSET {}=0\n".format(CC.arg)
			if CC.name=="return":
				commands+="\t\tGOTO $lastloc2\n"
			if CC.name=="next":
				commands+="\t\tGOTO '{}'\n".format(vRoom[i+1].roomname)
		
		print("""IF CND=1:
\tACT '{}':
{}
\tEND
END""".format(A.text,commands))
	print("-\n")
	
import sys
QSP=QSP.replace("\n","\r\n")
QSP=QSP.encode('cp1251')
f=open("qsp.txt","wb")
f.write(QSP)
f.close()
