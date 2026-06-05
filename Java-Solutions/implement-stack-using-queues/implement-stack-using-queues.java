import java.util.*;

class MyStack {
    
    Queue<Integer> q1;
    Queue<Integer> q2;

    public MyStack() {
        q1 = new LinkedList<>();
        q2 = new LinkedList<>();
    }
    
    public void push(int x) {
        // Step 1: Push to q2
        q2.add(x);
        
        // Step 2: Move all elements from q1 to q2
        while (!q1.isEmpty()) {
            q2.add(q1.remove());
        }
        
        // Step 3: Swap q1 and q2
        Queue<Integer> temp = q1;
        q1 = q2;
        q2 = temp;
    }
    
    public int pop() {
        return q1.remove();   // front element
    }
    
    public int top() {
        return q1.peek();     // front element
    }
    
    public boolean empty() {
        return q1.isEmpty();
    }
}
