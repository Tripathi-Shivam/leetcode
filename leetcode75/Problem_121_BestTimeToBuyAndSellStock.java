package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_121_BestTimeToBuyAndSellStock {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		int n = fs.nextInt();
		int[] a = fs.readArray(n);
    	out.println(solve(a));        
        out.close();
	}
	
	public static int solve(int[] prices) {
		int sum = 0, i = 0, j = 1, n = prices.length;
		while(i < n && j < n) {
			if(prices[i] >= prices[j]) {
				i = j;
				j++;
			}
			else {
				int profit = prices[j] - prices[i];
				sum = Math.max(sum, profit);
				j++;
			}
		}
		return sum;
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
