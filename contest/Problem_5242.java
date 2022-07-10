package contest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_5242 {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
//		int testCases = fs.nextInt();
//
//        for (int i = 0; i < testCases; i++) {
//        	solve();
//       	out.println(solve());
//        }
//        solve();
    	out.println(solve(fs.next()));
        out.close();
	}

	public static String solve(String s) {
		char[] a = s.toCharArray();
		int n = a.length;
		int[] upperCase = new int[26];
		int[] lowerCase = new int[26];
		
		for(int i = 0; i < n; i++) {
			if(a[i] >= 97) {
				lowerCase[a[i] - 97]++;
			}
			else {
				upperCase[a[i] - 65]++;
			}
		}
		String max = "";
		for(int i = 0; i < 26; i++) {
			if(upperCase[i] >= 1 && lowerCase[i] >= 1) {
				max = (char)(i + 65) + "";
			}
		}
		
		return max;
	}
	
	static class FastScanner {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer("");
		
		String next() {
			while(!st.hasMoreTokens()) {
				try {
					st = new StringTokenizer(br.readLine());
				} catch(IOException e) {
					e.printStackTrace();
				}
			}
			return st.nextToken();
		}
		
		int nextInt() {
            return Integer.parseInt(next());
        }
 
        int[] readArray(int n) {
            int[] a = new int[n];
            for (int i = 0; i<n; i++) a[i]=nextInt();
            return a;
        }
 
        long nextLong() {
            return Long.parseLong(next());
        }
	}
}
