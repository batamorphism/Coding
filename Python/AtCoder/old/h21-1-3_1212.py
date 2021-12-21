S = 1_000_000
GP = 20_000
P = 14_500
i_p = 1.5/100
qd_p = 1.55/1000
E = 4_000
i_a = 2.0/100
qd_a = 1.05/1000
qw_a = 5/100
W = 100_000
Vp = [110_000, 125_000]
Va = [115_000, 130_500]
i_a_h = (1+i_a)**(1/2)-1
i_p_h = (1+i_p)**(1/2)-1

profit1 = 0
profit1 += GP-E+Va[0]  # 年始
profit1 += (-S*qd_a)  # 年央
profit1 += (-W*qw_a) +(-Va[1]*(1-qd_a-qw_a))  # 年始
profit1 += (GP-E+Va[0])*i_a  # 利息年始
profit1 += (-S*qd_a)*i_a_h  # 利息年央

print(1, profit1)

hisa = GP-E-P
sisa = -S*qd_a+Va[1]*qd_a+S*qd_p-Vp[1]*qd_p
risa = (GP-E+Va[0])*i_a+(-S*qd_a)*i_a_h-(Vp[0]+P)*i_p+(S*qd_p)*i_p_h
kouzyo = -W*qw_a + Vp[1]*qw_a
vkuri = Va[0]-Vp[0]-Va[1]+Vp[1]
kai_vkuri = (Va[1]-Vp[1])*qw_a

print(2, hisa)
print(3, sisa)
print(4, risa)
print(5, kouzyo)
print(6, vkuri)
print(7, kai_vkuri)
print(hisa+sisa+risa+vkuri+kouzyo+kai_vkuri)
