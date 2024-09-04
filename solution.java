class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] newArr = new int[nums.length];
        for(int i = 0; i < nums.length; i++)
        {
            int product = 1;
            for(int j = 0; j < nums.length; j++)
            {
                if(i!=j)
                {
                    product*=j;
                }
            }
            newArr[i] = product;

        }

        return newArr;
    }
}