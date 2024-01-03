# get helped from this post https://discourse.julialang.org/t/constants-like-e-and-eulergamma-in-julia-v1-0-no-longer-available/15917
# note you must use ℯ and not e.
setprecision(Int(ceil(log2(10)*2000))) do
    println(string(BigFloat(ℯ))[1:1002])
end
