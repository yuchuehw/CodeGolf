import java.util.ArrayList;
import java.util.Collections;
class Triangle {
    public static ArrayList<String> t(int x) {
        ArrayList<String> result = new ArrayList<>();
        ArrayList<String> p = (x > 0) ? t(x - 1) : new ArrayList<>(Collections.singletonList("▲"));

        if (x > 0) {
            for (int i = 0; i < p.size(); i++) {
                result.add(p.get(i) + " ".repeat(i + 1) + p.get(i));
            }

            for (String c : p) {
                result.add(" ".repeat(p.size()) + c);
            }
        } else {
            result.add("▲");
        }

        return result;
    }

    public static void main(String[] args) {
        ArrayList<String> triangle = t(4);
        Collections.reverse(triangle);
        System.out.println(String.join("\n", triangle));
    }
}
