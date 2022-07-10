package contest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_6104_CountAsterisks {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
    	out.println(solve(fs.next()));
        out.close();
	}

	public static int solve(String s) {
		int count = 0, n = s.length();
		boolean isPipe = false;
		
		for(int i = 0; i < n; i++) {
			if(s.charAt(i) == '|') {
				isPipe = true;
				while(isPipe && i < n) {
					i++;
					if(s.charAt(i) == '|') 
						isPipe = false;
				}
			}
			else if(s.charAt(i) == '*')
				count++;
		}
		return count;
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
