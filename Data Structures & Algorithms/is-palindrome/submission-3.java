class Solution {   
    public boolean isPalindrome(String s) {
        int i = 0;
        int j = s.length()-1;

        while (i < j)
        {
            while (i<j && !Character.isLetterOrDigit(s.charAt(i)))
            {
                i++;
            }
            while (j>i && !Character.isLetterOrDigit(s.charAt(j)))
            {
                j--;
            }

            if (Character.isLetter(s.charAt(i)) && Character.isLetter(s.charAt(j)))
            {
                if (Character.toUpperCase(s.charAt(i)) != Character.toUpperCase(s.charAt(j)))
                {
                    return false;
                }
            }
            else if (s.charAt(i) != s.charAt(j))
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
}
