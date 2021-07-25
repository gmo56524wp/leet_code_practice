class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2) return n;
        else{
            int x = 1;
            int y = 2;
            int result;
            for (int i = 3; i <= n; i++){
                if (i == n){
                    result = y + x;
                }else{
                    result = y+x;
                    x = y;
                    y = result;
                }
            }
            return result;
        }
    }
};