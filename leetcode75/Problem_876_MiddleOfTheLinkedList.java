package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_876_MiddleOfTheLinkedList {

	public static FastScanner fs = new FastScanner();
    public static PrintWriter out = new PrintWriter(System.out);
	
	public static void main(String[] args) {
		int n = fs.nextInt();
		ListNode head = new ListNode(0);
    	ListNode list = head;
    	for(int i = 0; i < n; i++) {
    		list.next = new ListNode(fs.nextInt());
    		list = list.next;
    	}
    	ListNode ans = solve(head.next);
		while(ans != null) {
			out.print(ans.val + " ");
			ans = ans.next;
		}
        out.close();
	}

	public static ListNode solve(ListNode head) {
		ListNode newHead = head;
		int size = 0;
		while(newHead != null) {
			size++;
			newHead = newHead.next;
		}
		int mid = (size / 2) + 1;
		for(int i = 1; i < mid; i++) 
			head = head.next;
		
		return head;
	}
	
	//Definition for singly-linked list.
	static class ListNode {
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
