package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Problem_733_FloodFill {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		int row = fs.nextInt();
		int column = fs.nextInt();
		int[][] image = new int[row][column];
		for(int i = 0; i < row; i++) {
			for(int j = 0; j < column; j++) 
				image[i][j] = fs.nextInt();
		}
		int sr = fs.nextInt();
		int sc = fs.nextInt();
		int newColor = fs.nextInt();
		int[][] ans = floodFill(image, sr, sc, newColor);
		for(int i = 0; i < row; i++) {
			for(int j = 0; j < column; j++) 
				out.print(ans[i][j] + " ");
			out.println();
		}
        out.close();
	}

	public static int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int color = image[sr][sc];
        if(color != newColor) 
        	dfs(image, sr, sc, color, newColor);
        return image;
    }
	
	public static void dfs(int[][] image, int r, int c, int color, int newColor) {
		if(image[r][c] == color) {
			image[r][c] = newColor;
			if(r >= 1)
				dfs(image, r-1, c, color, newColor);
			if(c >= 1)
				dfs(image, r, c-1, color, newColor);
			if(r+1 < image.length)
				dfs(image, r+1, c, color, newColor);
			if(c+1 < image[0].length)
				dfs(image, r, c+1, color, newColor);
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
