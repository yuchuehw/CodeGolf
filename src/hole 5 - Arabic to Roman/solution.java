"""
a translation of the python code
"""
class M{public static void main(String[]args){String[]romanSymbols={"","I","II","III","IV","V","VI","VII","VIII","IX"};String[]romanTens={"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};String[]romanHundreds={"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};for(String arg:args){int num=Integer.parseInt(arg);StringBuilder result=new StringBuilder();int thousands=num/1000;int hundreds=(num%1000)/100;int tens=(num%100)/10;int ones=num%10;result.append("M".repeat(thousands));result.append(romanHundreds[hundreds]);result.append(romanTens[tens]);result.append(romanSymbols[ones]);System.out.println(result.toString());}}}
