package topInterviewQuestionsEasy;

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
        int[] prices = new int[n];
		
		for(int i = 0; i < n; i++)
			prices[i] = fs.nextInt();
		
		out.println(solve(prices));
        out.close();
	}

	public static int solve(int[] prices) {
		int max = 0, n = prices.length, i = 0, j = 1;
		while(i < n && j < n) {
			if(prices[i] < prices[j]) {
				max = Math.max(max, prices[j] - prices[i]);
				j++;
			}
			else {
				i = j;
				j++;
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
	
	public static String toString(char[] a) {
        StringBuilder sb = new StringBuilder();
 
        // Creating a string using append() method
        for (int i = 0; i < a.length; i++) {
            sb.append(a[i]);
        }
 
        return sb.toString();
    }
}
