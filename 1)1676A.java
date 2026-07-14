//Problem name :Lucky?

import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();       
        while (t-- > 0) {
            String s = sc.next();
            
            //first three digits sum
            int sum1 = s.charAt(0) + s.charAt(1) + s.charAt(2);
            //last three digits sum
            int sum2 = s.charAt(3) + s.charAt(4) + s.charAt(5);           
            if (sum1 == sum2) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        sc.close();
    }
}
