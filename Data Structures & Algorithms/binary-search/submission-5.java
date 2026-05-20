class Solution {
    public int binary(int l, int r, int[] nums, int target) {
        if (l>r)
        {
            return -1;
        }

        int mid = l + (r-l)/2;

        if (nums[mid] == target) return mid;

        return (nums[mid] < target) ? 
            binary(mid + 1, r, nums, target) : 
            binary(l, mid - 1, nums, target);

    }

    public int search(int[] nums, int target) {
        return binary(0, nums.length - 1, nums, target);
    }
}
