class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> hash=new HashMap<>();
        for (int i=0;i<nums.length;i++){
            int d=target-nums[i];
            if (hash.containsKey(d))return new int[]{hash.get(d),i};
            hash.put(nums[i],i);
        }
        return new int[]{};
    }
}