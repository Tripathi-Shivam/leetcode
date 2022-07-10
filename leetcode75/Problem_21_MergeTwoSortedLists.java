package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_21_MergeTwoSortedLists {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
    	int n = fs.nextInt();
    	int m = fs.nextInt();
    	ListNode list1 = new ListNode();
    	for(int i = 0; i < n; i++) {
    		
    	}
    	ListNode list2 = new ListNode();
    	for(int i = 0; i < m; i++) {
    		
    	}
		ListNode ans = solve(list1, list2);
		while(ans != null) {
			out.print(ans.val + " ");
			ans = ans.next;
		}
        out.close();
	}

	public static ListNode solve(ListNode list1, ListNode list2) {
		ListNode dummy = new ListNode(0);
		ListNode curr = dummy;
		while(list1 != null && list2 != null) {
			if(list1.val <= list2.val) {
				curr.next = list1;
				list1 = list1.next;
			}
			else {
				curr.next = list2;
				list2 = list2.next;
			}
			curr = curr.next;
		}
		
		curr.next = (list1 == null) ? list2 : list1;
		
		return dummy.next;
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

//Definition for singly-linked list.
class ListNode {
	int val;
	ListNode next;
	
	ListNode() {}
	
	ListNode(int val)  {
		this.val = val;
	}
	
	ListNode(int val, ListNode next) { 
		this.val = val; 
		this.next = next; 
	}
}
