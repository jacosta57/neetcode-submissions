class Solution {
    public int search(int[] nums, int target) {
        int left = 0;
        int right = nums.length;

        while(left < right){
            int middle = left + (right - left) / 2;
            int current = nums[middle];
            if(current == target){
                return middle;
            } else if(current < target){
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        return -1;
    }
}
