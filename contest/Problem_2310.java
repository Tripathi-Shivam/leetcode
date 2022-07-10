package contest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_2310 {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
//		int testCases = s.nextInt();
//
//        for (int i = 0; i < testCases; i++) {
//        	solve();
//        	out.println(solve());
//        }
//    	solve();
    	out.println(solve(fs.nextInt(), fs.nextInt()));
        
        out.close();
	}

	public static int solve(int num, int k) {
		if(num % 2 == 1 && k % 2 == 0)
			return -1;
		if(num % 10 == k)
			return 1;
		if(num == 0)
			return 0;
		int temp = num, a = k, count = 0;
		while(temp > 0) {
			count++;
			temp = Math.abs(temp - a);
			
		}
		return 0;
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
