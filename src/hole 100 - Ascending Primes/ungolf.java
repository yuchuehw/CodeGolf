// a translation of solution.py
import java.util.*;
class M {
  public static void main(String[] z) {
    int i = 1;
    String s = "123456789";
    ArrayList < Integer > a = new ArrayList < > ();
    while (i < 512) {
      String b = Integer.toBinaryString(i);
      String d = "";
      for (int n = b.length() - 1; n > -1; n--) {
        if (b.charAt(n) == '1') {
          d += (s.charAt(b.length() - 1 - n));
        }
      }
      a.add(Integer.valueOf(d));
      i++;
    }
    Collections.sort(a);
    a.remove(0);
    for (int n: a) {
      int f = 1;
      for (int j = 2; j < n; j++) {
        if (n % j == 0) {
          f = 0;
        }
      }
      if (f == 1) {
        System.out.println(n);
      }
    }
  }
}
