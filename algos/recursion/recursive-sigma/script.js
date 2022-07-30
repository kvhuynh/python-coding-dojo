/* 
  Recursively sum an arr of ints
*/

const nums1 = [1, 2, 3];
const expected1 = 6;

const nums2 = [1];
const expected2 = 1;

const nums3 = [];
const expected3 = 0;

/**
 * Add params if needed for recursion
 * Recursively sums the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} nums
 * @returns {number} The sum of the given nums.
 */
function sumArr(nums, i=0) {
    // edge case (pri 1)

    // base case (pri 0)
    if (i === nums.length){
        return 0
    }

    // recursive call (pri 0)
    return nums[i] + sumArr(nums, i+=1)

    // let sum = 0
    // for (let i=0; i<nums.length; i++){
    //     sum += nums[i]
    // }
    // return sum
}

/*****************************************************************************/

/* 
Recursive Sigma
Input: integer
Output: sum of integers from 1 to Input integer
*/

const two_num1 = 5;
const two_expected1 = 15;
// Explanation: (1+2+3+4+5)

const two_num2 = 2.9;
const two_expected2 = 3;
// Explanation: (1+2)

const two_num3 = -1;
const two_expected3 = 0;

/**
 * Recursively sum the given int and every previous positive int.
 * - Time: O(?).
 * - Space: O(?).
 * @param {number} num
 * @returns {number}
 */
function recursiveSigma(num) {
    if (num < 0) {
        return 0
    }

    return Math.floor(num) + recursiveSigma(num-1)
}

console.log(recursiveSigma(two_num1));
console.log(recursiveSigma(two_num2));
console.log(recursiveSigma(two_num3));