
#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<string> g(n);

        for (int i = 0; i < n; i++) {
            cin >> g[i];
        }

        vector<int> perm(n);
        iota(perm.begin(), perm.end(), 0);

        sort(perm.begin(), perm.end(), [&](int u, int v) {
            
            if(u<v)
            {
                return g[u][v]=='1';
                
            }
            
            return g[v][u]=='0';
        });

        for (int i = 0; i < n; i++) {
            cout << perm[i] + 1 << (i + 1 == n ? "\n" : " ");
        }
    }

    return 0;
}
