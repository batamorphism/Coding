S=map(int,input())
input()
mask=sum(2**i for i in map(int,input().split()))
MOD=998244353

digits=0  # set(S[:i]) をbitで表したもの
Spre=0  # int(S[:i])%MOD
dps=[0]*1024  # 総和
dpc=[0]*1024  # 個数
for i,c in enumerate(S):
	new_dpc=[0]*1024
	new_dps=[0]*1024
	for m in range(1,1024):
		for d in range(10):
			new_dpc[m|1<<d]+=dpc[m]
			new_dps[m|1<<d]+=dps[m]*10+dpc[m]*d
	# この桁から
	if i:
		for d in range(1,10):
			new_dpc[1<<d]+=1
			new_dps[1<<d]+=d
	# 上がSpre
	for d in range(not i,c):
		new_dpc[digits|1<<d]+=1
		new_dps[digits|1<<d]+=Spre*10+d

	for m in range(1,1024):
		dpc[m]=new_dpc[m]%MOD
		dps[m]=new_dps[m]%MOD
	digits|=1<<c
	Spre=(Spre*10+c)%MOD

ans=sum(dps[m] for m in range(1024) if (m&mask)==mask)
if (digits&mask)==mask: ans+=Spre

print(ans%MOD)
