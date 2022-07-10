package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_392_IsSubsequence {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
    	out.println(solve(fs.next(), fs.next()));
        out.close();
	}

	public static boolean solve(String s, String t) {
		int n = s.length(), m = t.length(), j = 0;
		for(int i = 0; i < n; i++) {
			boolean found = false;
			while(j < m) {
				if(s.charAt(i) == t.charAt(j)) {
					j++;
					found = true;
					break;
				}
				j++;
			}
			if(j >= m && !found)
				return false;
		}
		
		return true;
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
