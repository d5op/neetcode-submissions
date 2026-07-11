public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
            return false;
        }
        Dictionary <char, int> dic = new Dictionary<char, int>();
        foreach(char c in s){
            dic[c] = dic.GetValueOrDefault(c, 0) + 1;
        }
        foreach(char c in t){
            if (dic.ContainsKey(c) && dic[c] > 0){
                dic[c] -= 1;
            }else{
                return false;
            }
        }
        return true;
    }
}
