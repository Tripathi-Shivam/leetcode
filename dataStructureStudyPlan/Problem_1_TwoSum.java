package dataStructureStudyPlan;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.StringTokenizer;

public class Problem_1_TwoSum {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		int n = fs.nextInt(), target = fs.nextInt();
		int[] a = fs.readArray(n);
		out.println(Arrays.toString(twoSum(a, target)));
    	out.close();
	}

    public static int[] twoSum(int[] nums, int target) {
        int n = nums.length;
    	int[] ans = new int[2];
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int i = 0; i < n; i++) 
        	map.put(nums[i], i);
        out.println(map);
        for(int i = 0; i < n; i++) {
        	int difference = target - nums[i];
        	out.println(difference);
        	if(map.containsKey(difference) && i != map.get(difference)) {
        		ans[0] = i;
        		ans[1] = map.get(difference);
        		return ans;	
        	}
        }
        
        return ans;
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
