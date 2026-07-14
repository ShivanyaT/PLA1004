package 14-07-2026.32B;
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        if (!scanner.hasNext()) {
            return;
        }
        
        String input = scanner.next();
        StringBuilder output = new StringBuilder();
        
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '.') {
                output.append("0");
            } else if (input.charAt(i) == '-') {
                if (input.charAt(i + 1) == '.') {
                    output.append("1");
                } else {
                    output.append("2");
                }
                i++;
            }
        }
        
        System.out.println(output.toString());
        scanner.close();
    }
}
