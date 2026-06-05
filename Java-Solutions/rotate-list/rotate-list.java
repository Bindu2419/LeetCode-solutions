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
    public ListNode rotateRight(ListNode head, int k) {

        if (head == null || head.next == null || k == 0)
            return head;

        // Find length
        ListNode current = head;
        int length = 1;

        while (current.next != null) {
            current = current.next;
            length++;
        }

        // Reduce k
        k = k % length;
        if (k == 0)
            return head;

        // Make circular
        current.next = head;

        // Find new tail
        int steps = length - k;
        ListNode newTail = head;

        for (int i = 1; i < steps; i++) {
            newTail = newTail.next;
        }

        // Break circle
        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }
}

