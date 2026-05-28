class Solution {
public:
    int getSum(int a, int b) {        
        int r = 0;
        int carry = 0;

        for (int i = 0; i < 32; i++) {
            // int ax = (a & 1);
            // int bx = (b & 1);

            int x = ((a & 1) ^ (b & 1) ^ carry) << i;
            r = (r | x);
            carry = ((a & 1) & (b & 1)) | ((a & 1) & carry) | ((b & 1) & carry);

            a = (a >> 1);
            b = (b >> 1);
        }

        return r;
    }
};