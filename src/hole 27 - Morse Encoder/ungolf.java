class M{
    public static void main(String[]a) {
        // Printing
		String s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10";
        for(String w:a[0].split(" ")){
			for(char c:w.toCharArray()){
				System.out.print(new StringBuffer(Integer.toBinaryString(s.indexOf(c)).substring(1)).reverse().toString().replace("0","▄ ").replace("1","▄▄▄ ")+"  ");
			}
			System.out.print(" ".repeat(7));
		}
    }
}
