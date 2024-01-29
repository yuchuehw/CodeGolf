package main;import ("fmt");func main(){for i:=1;i<200;i++{j:=i;for j > 4{sum := 0;for _, c:=range fmt.Sprint(j){digit:=int(c-'0');sum+=digit*digit};j=sum};if j<2{fmt.Println(i)}}}
