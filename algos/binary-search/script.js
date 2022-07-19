/* 
  Array: Binary Search (non recursive)
  Given a sorted array and a value, return whether the array contains that value.
  Do not sequentially iterate the array. Instead, ‘divide and conquer’,
  taking advantage of the fact that the array is sorted .
  Bonus (alumni interview): 
    first complete it without the bonus, because they ask for additions
    after the initial algo is complete
    return how many times the given number occurs
*/

const nums1 = [1, 3, 5, 6];
const searchNum1 = 4;
const expected1 = false;

const nums2 = [4, 5, 6, 8, 12];
const searchNum2 = 5;
const expected2 = true; //1 for bonus

const nums3 = [3, 4, 6, 8, 12];
const searchNum3 = 3;
const expected3 = true; //1 for bonus

// bonus, how many times does the search num appear?
const nums4 = [2, 2, 2, 2, 3, 4, 5, 6, 7, 8, 9];
const searchNum4 = 2;
const expected4 = 4;

/**
 * Efficiently determines if the given num exists in the given array.
 * - Time: O(?).
 * - Space: O(?).
 * @param {Array<number>} sortedNums
 * @param {number} searchNum
 * @returns {boolean} Whether the given num exists in the given array.
 */
//  * pseudocode:
//  * - sort input array
//  * - initialize two variables, start and end
//  * - start would be the first index
//  * - end would be last index in array
//  * - put everything in a while loop with condition start <= end
//  * - initialize mid value to be math.floor(avg of start and end)
//  * - check if mid is expected value ( return true if true)
//  * - if not check if value at mid is less or greater than expected value
//  * - if greater start = mid + 1
//  * - if less end = mid - 1
//  * - return false at end of method
//  */
function binarySearch(sortedNums, searchNum) {
    sortedNums = sortedNums.sort();
    let start = 0;
    let end = sortedNums.length-1;
    while (start <= end){
        if (sortedNums[end] == searchNum || sortedNums[start] == searchNum){
            countNums(sortedNums, searchNum);
            return true;
        }
        let mid = Math.floor((start + end) / 2);
        if (sortedNums[mid] == searchNum){
            countNums(sortedNums, searchNum);
            return true;
        } else if(searchNum > sortedNums[mid]){
            start = mid + 1;
        } else if(searchNum < sortedNums[mid]){
            end = mid - 1;
        }
        // console.log(start);
        // console.log(end);
    }
    return false;
}

function countNums(sortedNums, searchNum){
    let count = 0
    for (var i = 0; i < sortedNums.length; i++){
        if (sortedNums[i] == searchNum){
            count++;
        }
    }
    console.log(count);
    return count;
}


console.log(binarySearch(nums1, searchNum1)); // false
console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)

function binarySearchWithCounting(sortedNums, searchNum) {
    sortedNums = sortedNums.sort();
    let start = 0;
    let end = sortedNums.length-1;
    let count = 0;
    while (start <= end){
        if (sortedNums[end] == searchNum){
            while (sortedNums[end] == searchNum){
                end-=1
                count++
            }
            start = end + 1;
        } else if (sortedNums[start] == searchNum){
            while (sortedNums[start] == searchNum){
                start+=1
                count++
            }
            start = end + 1;
        }
        let mid = Math.floor((start + end) / 2);
        if (sortedNums[mid] == searchNum){
            while (sortedNums[mid] == searchNum){
                mid+=1
                count++
            }
            start = end;
        } else if(searchNum > sortedNums[mid]){
            start = mid + 1;
        } else if(searchNum < sortedNums[mid]){
            end = mid - 1;
        }
    }
    if(count != 0){
        return count;
    }
    return false;
}

// console.log(binarySearch(nums1, searchNum1)); // false
// console.log(binarySearch(nums2, searchNum2)); // true (1 for bonus)
// console.log(binarySearch(nums3, searchNum3)); // true (1 for bonus)
// console.log(binarySearch(nums4, searchNum4));
console.log(binarySearchWithCounting(nums1, searchNum1)); // false
console.log(binarySearchWithCounting(nums2, searchNum2)); // true (1 for bonus)
console.log(binarySearchWithCounting(nums3, searchNum3)); // true (1 for bonus)
console.log(binarySearchWithCounting(nums4, searchNum4));