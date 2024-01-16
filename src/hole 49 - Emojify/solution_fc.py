"""
fewest character
ranked 111th as of 01/15/2024
"""
import sys
d={i:j for i,j in zip("Da)a|a(a\\a*aOa#a'Da'(a:'-)a:'-(aPa;-PaX-PaX-)aO)a;-)a$aaB-)aJa})a}(a@".split("a"),"😀🙂😐🙁😕😗😮🤐😅😓😂😢😛😜😝😆😇😉😳😶😎😏😈👿😡")}
for a in sys.argv[1:]:print(d[a.replace(":-","")])
