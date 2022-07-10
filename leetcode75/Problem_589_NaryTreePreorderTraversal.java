package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Problem_589_NaryTreePreorderTraversal {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		
        out.close();
	}

	static List<Integer> result = new ArrayList<>();
	public static List<Integer> recursive(Node root) {
		if(root == null)
			return result;
		preOrderHelper(root);
		return result;
	}
	
	public static void preOrderHelper(Node node) {
		if(node.children == null) 
			return;
		result.add(node.val);
		for(Node child : node.children) 
			preOrderHelper(child);
	}
	
	public static List<Integer> iterative(Node root) {
		if(root == null)
			return result;
		
		Stack<Node> stack = new Stack<>();
		stack.push(root);
		while(!stack.isEmpty()) {
			Node node = stack.pop();
			result.add(node.val);
			// Pushing the children in reverse order
			for(int i = node.children.size() - 1; i >= 0; i--) 
				stack.push(node.children.get(i));
		}
		return result;
	}
	
	// Definition for a Node.
	static class Node {
	    public int val;
	    public List<Node> children;

	    public Node() {}

	    public Node(int _val) {
	        val = _val;
	    }

	    public Node(int _val, List<Node> _children) {
	        val = _val;
	        children = _children;
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
