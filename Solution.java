class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        boolean result = false;
        int num = 0;

        for (int i = 1; i < flowerbed.length; i++)
        {
            if (flowerbed[i] == 0)
            {

                for (int j = i + 2; j <  flowerbed.length; j++)
                {
                    if (flowerbed[j] == 0 && flowerbed[j + 2] == 0)
                    {
                        num++;
                    }
                }
            }
        }

        if (num)
    }
}
