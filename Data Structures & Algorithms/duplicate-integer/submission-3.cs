public class Solution {
    public bool hasDuplicate(int[] nums) {
        HashSet<int> s = new HashSet<int>(nums);
        if (s.Count != nums.Length){
            return true;
        }else{
            return false;
        }

    }
}