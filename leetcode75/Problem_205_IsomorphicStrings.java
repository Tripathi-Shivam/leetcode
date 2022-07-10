package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Problem_205_IsomorphicStrings {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
    	out.println(solve(fs.next(), fs.next()));
        out.close();
	}

	public static boolean solve(String s, String t) {
		HashMap<Character, Character> map = new HashMap<>();
		HashSet<Character> set = new HashSet<>();
		int n = s.length();
		for(int i = 0; i < n; i++) {
			char a = s.charAt(i);
			char b = t.charAt(i);
			if(map.containsKey(a) || set.contains(b))
				continue;
			set.add(b);
			map.put(a, b);
		}
		StringBuilder ans = new StringBuilder();
		for(int i = 0; i < n; i++) {
			ans.append(map.get(s.charAt(i)));
		}
		
		return (ans.toString().equals(t)) ? true : false;
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
