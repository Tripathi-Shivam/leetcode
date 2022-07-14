package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Problem_278_FirstBadVersion {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		int n = fs.nextInt();
		int v = fs.nextInt();
		setBadVersion(v);
		out.println(firstBadVersion(n));
        out.close();
	}

	static int badVersion = 0;
	/*
		n = 5
		1 2 3 4 5 
		badVersion = 4
		start = 4
		end = 4
		mid = 3
		
	*/
	public static int firstBadVersion(int n) {
        int start = 1, end = n;
        while(start < end) {
        	int mid = start + (end - start) / 2;
        	if(isBadVersion(mid)) 
        		end = mid;
    		else
        		start = mid + 1;
        }
        return start;
    }
	
	public static boolean isBadVersion(int version) {
		return (version == badVersion) ? true : false;
	}
	
	static void setBadVersion(int v) {
		badVersion = v;
	}
	
	static void sort(int[] a) {
		ArrayList<Integer> l=new ArrayList<>();
		for (int i:a) l.add(i);
		Collections.sort(l);
		for (int i=0; i<a.length; i++) a[i]=l.get(i);
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
