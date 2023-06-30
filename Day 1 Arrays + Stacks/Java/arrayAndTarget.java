// Q: Given a set of numbers, find a pair of numbers that add up to a certain target. 
// Ex: given [1,2,3,9] and a target of 10, identify that 1 and 9 add up to 10.

//Brute Force Approach (O(n^2))

import java.util.Arrays;

public class arrayAndTarget{
    public static void main(String[] args){
        int[] nums = {1, 2, 3, 9};
        int target = 10;
        System.out.println(Arrays.toString(findPairBrute(nums, target))); // Prints: [1,9]
    }

    static int[] findPairBrute(int[] nums, int target) {
        for (int i=0; i< nums.length; i++){
            for (int j = i+1; j<nums.length; j++){
                if (nums[i] + nums[j] == target){
                    return new int[]{nums[i], nums[j]};
                }
            }
        }
        return null;
    }
}