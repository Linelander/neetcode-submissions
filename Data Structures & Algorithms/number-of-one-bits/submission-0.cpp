class Solution {
public:
    int hammingWeight(uint32_t n) {
        int ct = 0;
        for (int i = 0; i < sizeof(n) * 8; i++) {
            if ((1 & n) == 1) {
                ct++;
            }
            n = n >> 1;
        }
        return ct;
    }
};
