package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_1480_RunningSumOf1dArray {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
//		int testCases = fs.nextInt();
//
//        for (int i = 0; i < testCases; i++) {
//        	solve();
//        	out.println(solve());
//        }
		int n = fs.nextInt();
		int[] nums = fs.readArray(n);
		int[] a = solve(nums); 
    	for(int i : a)
    		out.print(i + " ");
        
        out.close();
	}

	public static int[] solve(int[] nums) {
		int n = nums.length;
		int[] ans = new int[n];
		int sum = 0;
		for(int i = 0; i < n; i++) {
			sum += nums[i];
			ans[i] = sum;
		}
		return ans;
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
