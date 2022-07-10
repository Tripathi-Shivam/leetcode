package contest;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Problem_6117_TheLatestTimeToCatchABus {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
    	int n = fs.nextInt();
    	int[] buses = fs.readArray(n);
    	int m = fs.nextInt();
    	int[] passengers = fs.readArray(m);
    	int capacity = fs.nextInt();
    	out.println(latestTimeCatchTheBus(buses, passengers, capacity));
		out.close();
	}

	public static int latestTimeCatchTheBus(int[] buses, int[] passengers, int capacity) {
        int n = buses.length, m = passengers.length;
		sort(buses);
        sort(passengers);
        HashMap<Integer, ArrayList<Integer>> map = new HashMap<>();
        int pIndex = 0;
        for(int i = 0; i < n; i++) {
        	ArrayList<Integer> a = new ArrayList<>();
        	int onBus = 0;
        	while(onBus < capacity && pIndex < m && buses[i] >= passengers[pIndex]) {
        		a.add(passengers[pIndex]);
        		pIndex++;
        		onBus++;
        	}
        	map.put(buses[i], a);
        }
        //out.println(map);
        HashSet<Integer> set = new HashSet<>();
        for(int i = 0; i < m; i++) {
        	set.add(passengers[i]);
        }
        for(int i = n-1; i >= 0; i--) {
        	ArrayList<Integer> latest = map.get(buses[i]);
        	int size = latest.size();
        	if(size == 0)
        		return buses[i];
        	if(size < capacity && buses[i] != latest.get(size-1))
        		return buses[i];
        	for(int j = size-1; j >= 0; j--) {
        		int max = latest.get(j);
        		if(max - 1 <= buses[i]) {
        			if(!set.contains(max-1))
        				return (max-1);
        		}
        	}
        }
        return -1;
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
