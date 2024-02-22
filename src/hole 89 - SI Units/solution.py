import sys
P={k:v for k,v in zip('Q R Y Z E P T G M k h ~ d c m μ n p f a z y r q'.split(' '),[*range(30,2,-3),2,1,-1,-2,*range(-3,-31,-3)])}
U={k:v for k,v in zip("cd s g A m K mol rad sr Hz N Pa J W C V F Ω S Wb T H °C lm lx Bq Gy Sv kat".split(),"cd_s_kg_A_m_K_mol___s^-1_kg m s^-2_kg m^-1 s^-2_kg m^2 s^-2_kg m^2 s^-3_A s_kg m^2 s^-3 A^-1_kg^-1 m^-2 s^4 A^2_kg m^2 s^-3 A^-2_kg^-1 m^-2 s^3 A^2_kg m^2 s^-2 A^-1_kg s^-2 A^-1_kg m^2 s^-2 A^-2_K_cd_cd m^-2_s^-1_m^2 s^-2_m^2 s^-2_mol s^-1".split("_"))}
for a in sys.argv[1:]:a=a.replace("da","~");p,u=a[0],a[1:];C=0if(B:=a in U)else P[p];C-=3if 'g'in a else 0;C=1if C==0else 10if C==1else"10^"+str(C);print(C,end=" ");a=[u,a][B];print(U[a])
