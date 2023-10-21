public class Solution {
    public bool IsPalindrome(int x) {
        string k = x.ToString();
        Console.WriteLine(k);
        int j = k.Length - 1;
        for (int i = 0; i < k.Length; i++) {
            if (k[i] != k[j]) {
                return false;
            }
            j--;
        }
        return true;
    }
}