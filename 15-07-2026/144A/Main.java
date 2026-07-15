
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);       
        int flag = 0;
        int minn = 0, maxx = 0;
        int imin = 0, imax = 0;
        int n, a;       
        n = scanner.nextInt();      
        for (int i = 0; i < n; i++) {
            a = scanner.nextInt();           
            if (i == 0) {
                minn = a;
                maxx = a;
            } else {
                if (a > maxx) {
                    maxx = a;
                    imax = i;
                }
                
                if (a <= minn) {
                    minn = a;
                    imin = i;
                }
            }
        }       
        if (imin < imax) {
            flag = 1;
        }       
        System.out.println(n - 1 - imin + imax - flag);       
        scanner.close();
    }
}