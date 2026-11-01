class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int, int> visited;

        for (const auto& num : nums) {
            if (visited.contains(num)) {
                return true;
            }

            visited[num] = 1;
        }

        return false;
    }
};