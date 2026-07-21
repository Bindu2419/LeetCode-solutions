class Solution {
    public long minimumPerimeter(long neededApples) {

        long n = 0;

        while (2L * n * (n + 1) * (2 * n + 1) < neededApples) {
            n++;
        }

        return 8 * n;
    }
}