public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length){
            return false;
        }
        Dictionary<char, int> dic = new Dictionary<char, int>();
        foreach(char w in s){
            dic[w] = dic.GetValueOrDefault(w, 0) + 1;
        }
        foreach(char w in t){
            if (dic.ContainsKey(w) && dic[w] > 0){
                dic[w] -= 1;
            }
            else{
                return false;
            }

        }
        return true;
    }
}
