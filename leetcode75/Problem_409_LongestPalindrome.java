package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_409_LongestPalindrome {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
    	out.println(solve(fs.next()));
        out.close();
	}

	public static int solve(String s) {
		char[] a = s.toCharArray();
		int[] lower = new int[26];
		int[] upper = new int[26];
		int letters = 0, n = a.length; 
		for(int i = 0; i < n; i++) {
			if(a[i] >= 97)
				lower[a[i] - 97]++;
		}
		for(int i = 0; i < n; i++) {
			if(a[i] <= 90)
				upper[a[i] - 65]++;
		}
		for(int i = 0; i < 26; i++) {
			if(lower[i] >= 2) {
				letters += (lower[i] % 2 == 0) ? lower[i] : lower[i] - 1;
				lower[i] = (lower[i] % 2 == 0) ? 0 : 1;
			}
		}
		for(int i = 0; i < 26; i++) {
			if(upper[i] >= 2) {
				letters += (upper[i] % 2 == 0) ? upper[i] : upper[i] - 1;
				upper[i] = (upper[i] % 2 == 0) ? 0 : 1;
			}
		}
		for(int i = 0; i < 26; i++) {
			if(lower[i] > 0 || upper[i] > 0) {
				letters++;
				break;
			}
		}
		return letters;
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
