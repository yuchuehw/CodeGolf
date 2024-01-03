l={}for a=2,98 do f=true;for b,c in ipairs(l)do if a%c==0 then f=false end end;if f then l[#l+1]=a;print(a)end end
