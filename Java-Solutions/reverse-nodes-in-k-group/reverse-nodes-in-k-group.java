/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        if(head==null || head.next==null) return head;
        ListNode curr=head;
        for(int i=0;i<k;i++){
            if(curr == null) return head;
            curr=curr.next;
        }
        int count=0;
        ListNode pre=null;
        curr=head;
        while(count<k){
            ListNode temp=curr.next;
            curr.next=pre;
            pre=curr;
            curr=temp;
            count++;
        }
        head.next = reverseKGroup(curr,k);
        return pre;
        
    }
}