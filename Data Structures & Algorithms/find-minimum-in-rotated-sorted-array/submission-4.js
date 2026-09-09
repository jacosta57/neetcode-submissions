class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    findMin(nums) {
        let left = 0;
        let right = nums.length - 1;

        while (left < right) {
            const middle = left + Math.floor((right - left) / 2);
            if (nums[middle] < nums[right]){
                right = middle;
            } else {
                left = middle + 1;
            }
        }
        return nums[left];
    }
}
