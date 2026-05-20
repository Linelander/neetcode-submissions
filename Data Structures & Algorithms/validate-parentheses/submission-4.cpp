class Solution {
public:
    bool isValid(string s) {
        std::list<char> stack;
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == '(' || s[i] == '{' || s[i] == '[') {
                stack.push_back(s[i]);
            }
            else {
                if (s[i] == ')' && stack.back() != '(') {return false;}
                if (s[i] == ']' && stack.back() != '[') {return false;}
                if (s[i] == '}' && stack.back() != '{') {return false;}
                stack.pop_back();
            }
        }
        return (!stack.size());
    }
};
