package 14-07-2026.144A;


}
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int n = sc.nextInt();
        int maxVal = 0;
        int minVal = 101; 
        int maxIndex = 0;
        int minIndex = 0;
        for (int i = 0; i < n; i++) {
            int current = sc.nextInt();
            if (current > maxVal) {
                maxVal = current;
                maxIndex = i;
            }
            if (current <= minVal) {
                minVal = current;
                minIndex = i;
            }
        }
        int totalSwaps = maxIndex + (n - 1 - minIndex);
        if (maxIndex > minIndex) {
            totalSwaps--;
        }
        System.out.println(totalSwaps);
        sc.close();
    }
}
