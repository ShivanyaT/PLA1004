package 17-07-2026.2247B;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(System.out);
        StringTokenizer st = new StringTokenizer(br.readLine());

        int t = Integer.parseInt(st.nextToken());
        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if (k > m) {
                out.println("-1");
            } else {
                int[] a = new int[n];
                for (int i = 1; i <= n; i++) {
                    if (i % k == 0) {
                        a[i - 1] = m - k + 1;
                    } else {
                        a[i - 1] = 1;
                    }
                }
                
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < n; i++) {
                    sb.append(a[i]).append(" ");
                }
                out.println(sb.toString().trim());
            }
        }
        out.flush();
    }
}
