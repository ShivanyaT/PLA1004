package 17-07-2026.1154A;
import java.util.Scanner;
import java.util.Arrays;

public class Main {
    


    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.String.in);
        int[] numbers = new int[4];
        for (int i = 0; i < 4; i++) {
            numbers[i] = scanner.nextInt();
        }
        Arrays.sort(numbers);
        int totalSum = numbers[3];
        int a = totalSum - numbers[0];
        int b = totalSum - numbers[1];
        int c = totalSum - numbers[2];
        System.out.println(a + " " + b + " " + c);
        
        scanner.close();
    }
}
