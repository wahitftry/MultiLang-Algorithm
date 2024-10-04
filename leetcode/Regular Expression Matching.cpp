class Solution {
public:
    bool isMatch(string s, string p) {
        int m = s.length();
        int n = p.length();
        bool dp[m+1][n+1];
        memset(dp, false, sizeof(dp));
        dp[0][0] = true;
        
        for(int j=2; j<=n; j++){
            if(p[j-1] == '*' && dp[0][j-2]){
                dp[0][j] = true;
            }
        }
        
        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                if(s[i-1] == p[j-1] || p[j-1] == '.'){
                    dp[i][j] = dp[i-1][j-1];
                }
                else if(p[j-1] == '*'){
                    dp[i][j] = dp[i][j-2];
                    if(s[i-1] == p[j-2] || p[j-2] == '.'){
                        dp[i][j] = dp[i][j] || dp[i-1][j];
                    }
                }
            }
        }
        
        return dp[m][n];
    }
};