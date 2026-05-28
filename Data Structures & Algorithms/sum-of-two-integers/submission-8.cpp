class Solution {
public:
    int getSum(int a, int b) {
        std::stack<int> stack;
        
        int r = 0;
        int carry = 0;

        for (int i = 0; i < 32; i++) {
            // Get current LSBs of a and b
            int ax = (a & 1);
            int bx = (b & 1);

            int x = (ax ^ bx ^ carry) << i;
            r = (r | x);
            carry = (ax & bx) | (ax & carry) | (bx & carry);

            a = (a >> 1);
            b = (b >> 1);
        }

        return r;
    }
};