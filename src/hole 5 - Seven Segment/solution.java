class M{public static void main(String[]a){StringBuilder t=new StringBuilder();StringBuilder m=new StringBuilder();StringBuilder b=new StringBuilder();for(char c:a[0].toCharArray()){int n=Character.getNumericValue(c);t.append((n==1||n==4)?"   ":" _ ");m.append((n==1||n==2||n==3||n==7)?" ":"|");m.append((n==0||n==1||n==7)?" ":"_");m.append((n==5||n==6)?" ":"|");b.append((n==0||n==2||n==6||n==8)?"|":" ");b.append((n==1||n==4||n==7)?" ":"_");b.append((n==2)?" ":"|");}System.out.println(t.toString());System.out.println(m.toString());System.out.println(b.toString());}}
