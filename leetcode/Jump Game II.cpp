class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        int jumps = 0;
        int currEnd = 0;
        int currFarthest = 0;
        for (int i = 0; i < n - 1; i++) {
            currFarthest = max(currFarthest, i + nums[i]);
            
            if (i == currEnd) {
                jumps++;
                currEnd = currFarthest;
            }
        }
        return jumps;
    }
};