import java.util.*;

class BrainfuckInterpreter {
    public static void main(String[] args) {
        for (String s : args) {
            List<Integer> m = new ArrayList<>(Collections.nCopies(1, 0));
            int p = 0, q = 0;
            while (true) {
                char i = s.charAt(p);
                if (i == '.') {
                    System.out.print((char) m.get(q).intValue());
                } else if (i == '+' || i == '-') {
                    int t = m.get(q);
                    m.set(q, (i == '+') ? t + 1 : t - 1);
                } else if (i == '>') {
                    q++;
                    if (m.size() == q) {
                        m.add(0);
                    }
                } else if (i == '<') {
                    if (q == 0) {
                        m.add(0, 0);
                    }
                    q = (q > 0) ? q - 1 : 0;
                } else {
                    int f = m.get(q);

                    int counter1 = (i == '[') ? 1 : 0;
                    int counter2 = 1 - counter1;
                    int direction = (i == '[') ? 1 : -1;

                    int c = (i == '[') ? 1 : -1;

                    if ((i == '[') ? f == 0 : f != 0) {
                        while (counter1 != counter2) {
                            p += direction;
                            if (s.charAt(p) == '[') {
                                counter1++;
                            } else if (s.charAt(p) == ']') {
                                counter2++;
                            }
                        }
                    }
                }

                p++;

                if (p == s.length()) {
                    break;
                }
            }
        }
    }
}
