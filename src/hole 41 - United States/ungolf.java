"""
minimized solution ranked 14th as of 01/12/2024
"""
interface M {
  public static void main(String[] a) {
    for (String S: a) {
      String A = S.toUpperCase();
      int i = 0;
      String j = A.contains(" ") ? "" + A.charAt(0) + A.charAt(A.lastIndexOf(' ') + 1) : "";
      for (String s: "las.z.G.ow.Ka.ui.ot.ur.pi.Mo.ev.sy.ee.xa.Vi".split("\\.")) {
        j += S.contains(s) ? "AK.AZ.GA.IA.KS.LA.MN.MO.MS.MT.NV.PA.TN.TX.VA".split("\\.")[i] : "";
        i++;
      }
      for (String s: "deity".split("")) {
        j += S.endsWith(s) ? "" + A.charAt(0) + A.charAt(A.length() - 1) : "";
      }
      j += "" + A.charAt(0) + A.charAt(1);
      System.out.println("" + j.charAt(0) + j.charAt(1));
    }
  }
}
