import java.util.*;class M{public static void main(String[]a){ArrayList<Integer> l=new ArrayList<>();for(int i=2;i<99;i++){int f=1;for(int j:l){if(i%j==0){f=0;}}if(f==1){l.add(i);System.out.println(i);}}}}