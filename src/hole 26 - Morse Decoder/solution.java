/*
as of 01/04/2024 ranked 8th in bytes and 9th in chrs
*/
class M{public static void main(String[]a){String s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10";for(String w :a[0].split("          ")){for(String c:w.split("   ")){System.out.print(s.charAt(Integer.parseInt('1'+new StringBuffer(c.replace("▄▄▄","1").replace("▄","0").replace(" ","")).reverse().toString(),2)));}System.out.print(" ");}}}
