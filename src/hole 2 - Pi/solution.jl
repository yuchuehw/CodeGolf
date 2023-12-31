#= 
   implemning a solution proposed in this SO post https://stackoverflow.com/questions/54660426/in-julia-1-0-print-the-first-2-000-digits-of-pi-after-the-decimal-point
   original by user: Julia Learner
   modified by: yuchuehw
=#

setprecision(Int(ceil(log2(10)*1000))) do
    println(string(BigFloat(pi))[1:1002])
end
