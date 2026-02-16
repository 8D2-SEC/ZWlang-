import sys

CHEAT=False
ZWSP="\u200b"

if "-cheat" in sys.argv:
	CHEAT=True
	sys.argv.remove("-cheat")

TOKEN = "u" if CHEAT else ZWSP

if len(sys.argv)!=2:
	print("Usage: python zwlang.py [-cheat] program.zw")
	sys.exit(1)

f=open(sys.argv[1],"r",encoding="utf-8")
lines=f.readlines()
f.close()

mem=[0]*300
ptr=0

i=0
for line in lines:
	i+=1
	for c in line:
		if c!=TOKEN and not c.isspace():
			print("Line",i,": invalid character detected")
			sys.exit(1)

	count=line.count(TOKEN)
	if count==1:
		ptr+=1
	elif count==2:
		ptr-=1
	elif count==3:
		mem[ptr]=(mem[ptr]+1)%256
	elif count==4:
		mem[ptr]=(mem[ptr]-1)%256
	elif count==5:
		print(chr(mem[ptr]),end="")
	elif count==6:
		x=input()
		if x:
			mem[ptr]=ord(x[0])
		else:
			mem[ptr]=0
	elif count==0:
		pass
	else:
		print("Line",i,": invalid instruction (",count,")")
		sys.exit(1)
