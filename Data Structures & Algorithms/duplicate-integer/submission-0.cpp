class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            if (map[nums[i]] > 0) {
                return true;
            }
            map[nums[i]]++;
        }
        return false;
    }
};