class Solution {
public:
    int getSum(int a, int b) {
        while(b != 0)
        {
            int temp = a & b ;
            a = a ^ b;
            b =  (unsigned)  temp << 1;
        }
        return a;
    }
};