class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
        {
            return false;
        }

        PriorityQueue<Character> heapS = new PriorityQueue<Character>();
        PriorityQueue<Character> heapT = new PriorityQueue<Character>();
        
        for (char c : s.toCharArray()) {
            heapS.offer(c);
        }
        
        for (char c : t.toCharArray()) {
            heapT.offer(c);
        }

        for (int i = 0; i < s.length(); i++)
        {
            if (heapS.poll() != heapT.poll())
            {
                return false;
            }
        }
        
        return true;
    }
}
