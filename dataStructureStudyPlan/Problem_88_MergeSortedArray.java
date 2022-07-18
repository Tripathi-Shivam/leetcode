package dataStructureStudyPlan;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Problem_88_MergeSortedArray {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		int a = fs.nextInt(), m = fs.nextInt(), n = fs.nextInt();
		int[] nums1 = new int[a];
		for(int i = 0; i < m; i++)
			nums1[i] = fs.nextInt();
		int[] nums2 = new int[n];
		for(int i = 0; i < n; i++)
			nums2[i] = fs.nextInt();
		merge(nums1, m, nums2, n);
		out.println(Arrays.toString(nums1));
    	out.close();
	}

	public static void merge(int[] nums1, int m, int[] nums2, int n) {
		// get positions
        int pos = m + n - 1;

        m--;
        n--;
        
        while (m >= 0 || n >= 0) {
            if (n < 0   // second arr is done
                    || (m >= 0 && nums1[m] > nums2[n])) {   // first arr is not done yet
                nums1[pos--] = nums1[m--];
            } else {
                nums1[pos--] = nums2[n--];
            }
        }

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
