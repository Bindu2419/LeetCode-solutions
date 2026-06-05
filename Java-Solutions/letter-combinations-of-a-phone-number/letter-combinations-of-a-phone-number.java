import java.util.*;

class Solution {
    
    public List<String> letterCombinations(String digits) {
        
        List<String> result = new ArrayList<>();
        
        if (digits == null || digits.length() == 0)
            return result;
        
        String[] map = {
            "",     // 0
            "",     // 1
            "abc",  // 2
            "def",  // 3
            "ghi",  // 4
            "jkl",  // 5
            "mno",  // 6
            "pqrs", // 7
            "tuv",  // 8
            "wxyz"  // 9
        };
        
        result.add("");   // Start with empty string
        
        for (char digit : digits.toCharArray()) {
            
            String letters = map[digit - '0'];
            
            List<String> temp = new ArrayList<>();
            
            for (String combination : result) {
                for (char letter : letters.toCharArray()) {
                    temp.add(combination + letter);
                }
            }
            
            result = temp;  // Update result
        }
        
        return result;
    }
}
