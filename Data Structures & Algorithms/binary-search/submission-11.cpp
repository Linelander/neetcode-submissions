class Solution {
public:
    int search(vector<int>& nums, int target) {
        int l = 0;
        int r = nums.size() - 1;
        int m = nums.size() / 2;
        while (nums[m] != target && l < r) {
            if (target < nums[m]) {
                r = m - 1;
                m = (l + r) / 2;
            } else if (target > nums[m]) {
                l = m + 1;
                m = (l + r) / 2;
            }
        }
        if (nums[m] == target) {
            return m;
        }
        return -1;
    }
};
