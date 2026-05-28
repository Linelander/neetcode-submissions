class Solution {
public:
    int getSum(int a, int b) {
        std::stack<int> stack;
        
        int r = 0;
        bool carry = 0;

        for (int i = 0; i < 32; i++) {
            // Get current LSBs of a and b
            int ax = (a & 1);
            int bx = (b & 1);

            stack.push(ax ^ bx ^ carry);
            printf("%d\n", ax ^ bx ^ carry);
            carry = (ax & bx) | (ax & carry) | (bx & carry);

            a = (a >> 1);
            b = (b >> 1);
        }

        printf("%d\n", carry);
        stack.push(carry);

        // Unroll stack into r
        while (!stack.empty()) {
            int p = stack.top();
            stack.pop();
            r = (r | p);
            // printf("%d\n", r);
            if (!stack.empty()) {
                r = r << 1;
            }
        }

        return r;
    }
};