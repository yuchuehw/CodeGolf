class M{
    public static void main(String[]a) {
        String s="..ETINAMSDRGUKWOHBLZFCP.VX.Q.YJ.56.7...8.......94.......3...2.10";
        for(String w :a[0].split(" ".repeat(10))){
			for(String c:w.split(" ".repeat(3))){
				System.out.print(s.charAt(Integer.parseInt('1'+new StringBuffer(c.replace("▄".repeat(3),"1").replace("▄","0").replace(" ","")).reverse().toString(),2)));
			}
			System.out.print(" ");
		}
	
    }
}
