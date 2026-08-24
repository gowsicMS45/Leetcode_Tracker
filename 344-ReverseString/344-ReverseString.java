// Last updated: 8/24/2026, 12:20:15 PM
class Solution {
    public void reverseString(char[] s) {
        int l=0;
        int r=s.length-1;
        while(l<r){
            char t=s[l];
            s[l]=s[r];
            s[r]=t;
            r--;
            l++;
        }
    }
}
