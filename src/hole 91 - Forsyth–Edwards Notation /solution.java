// for unminimized version see ungolf.java Solution ranked 13th in bytes and char as of 01/03/2023
import java.util.*;class C{public static void main(String[]g){HashMap<Character,String>d=new HashMap<>();d.put('/',"\n");for(int i=0;i<12;i++){char p="KQRBNPkqrbnp".charAt(i);d.put(p,""+(char)(9812+i));d.put((char)(i+'0')," ".repeat(i));}for(String a:g){for(char c:a.split(" ")[0].toCharArray()){System.out.print(d.get(c));}System.out.println("\n");}}}
