package leetcode75;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.util.StringTokenizer;

public class Problem_142_LinkedListCycleII {

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
    	list.next = head.next.next; // to form a loop
    	ListNode ans = solve(head.next);
		while(ans != null) {
			out.print(ans.val + " ");
			ans = ans.next;
		}
        out.close();
	}

	public static ListNode solve(ListNode head) {
		ListNode slow = head, fast = head;
        while(fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
            if(slow == fast) {
                ListNode slow2 = head;
                while(slow2 != slow) {
                    slow2 = slow2.next;
                    slow = slow.next;
                }
                return slow;
            }
        }
        return null;
	}
	
	//Definition for singly-linked list.
	static class ListNode {
		int val;
		ListNode next;
		
		ListNode() {}
		
		ListNode(int val)  {
			this.val = val;
			this.next = null;
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
