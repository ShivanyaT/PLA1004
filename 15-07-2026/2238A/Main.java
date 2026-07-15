package 15-07-2026.2238A;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;
import java.util.Arrays;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        StringBuilder out = new StringBuilder();
        while (t-- > 0) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            int[] a = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                a[i] = Integer.parseInt(st.nextToken());
            }
            int[] b = new int[n];
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                b[i] = Integer.parseInt(st.nextToken());
            }
            boolean needReorder = false;
            long ans = 0;
            for (int i = 0; i < n; i++) {
                if (a[i] < b[i]) {
                    needReorder = true;
                }
                ans += (a[i] - b[i]);
            }
            if (needReorder) {
                Arrays.sort(a);
                Arrays.sort(b);              
                boolean impossible = false;
                for (int i = 0; i < n; i++) {
                    if (a[i] < b[i]) {
                        impossible = true;
                        break;
                    }
                }
                if (impossible) {
                    out.append("-1\n");
                } else {
                    out.append(ans + c).append("\n");
                }
            } else {
                out.append(ans).append("\n");
            }
        }
        System.out.print(out);
    }
}