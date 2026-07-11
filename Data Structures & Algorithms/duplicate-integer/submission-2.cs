public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> s = new HashSet<int>();
        for (int x = 0; x < nums.Length; x++){
            if (s.Contains(nums[x])){
                return true;
            }else{
                s.Add(nums[x]);
            }
        }
        return false;

    }
}