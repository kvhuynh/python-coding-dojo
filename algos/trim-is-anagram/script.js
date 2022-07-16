/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "   hello world     ";
const expected1 = "hello world";

const str2 = "   hello     world     ";
const expected2 = "hello     world";

/**
 * Trims any leading or trailing white space from the given str.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str
 * @returns {string} The given string with any leading or trailing white space
 *    stripped.
 */
function trim(str) {
    let startIndex = 0;
    let endIndex = 0;
    let returnString = "";
    for(let i = 0; i < str.length; i++) {
        if (str[i] !== " ") {
            console.log(i)
            startIndex = i
            break
        }

    }
    for(let j = str.length; j > 0; j--) {
        if (str[j] !== " ") {
            continue;
        }
        else {
            endIndex = j
        }
    }
    for(let k = endIndex; k <= startIndex; k++) {
        returnString += str[k];
    }
    return returnString;
}

// console.log(trim(str1))
// console.log(trim(str2))


/*****************************************************************************/

/* 
  An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
  typically using all the original letters exactly once.
  Is there a quick way to determine if they aren't an anagram before spending more time?
  Given two strings
  return whether or not they are anagrams
*/

const two_strA1 = "yes";
const two_strB1 = "eys";
const two_expected1 = true;

const two_strA2 = "yes";
const two_strB2 = "eYs";
const two_expected2 = true;

const two_strA3 = "no";
const two_strB3 = "noo";
const two_expected3 = false;

const two_strA4 = "silent";
const two_strB4 = "listen";
const two_expected4 = true;

/**
 * Determines whether s1 and s2 are anagrams of each other.
 * Anagrams have all the same letters but in different orders.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} s1
 * @param {string} s2
 * @returns {boolean} Whether s1 and s2 are anagrams.
 */
function isAnagram(s1, s2) {
    let counter = 0;
    if (s1.length !== s2.length) {
        return false
    }

    for (let i = 0; i < s1.length; i++) {
        for (let j = 0; j < s2.length; j++) {
            if (s1[i] === s2[i]) {
                counter++;
            }
        }
    }
    if (counter === s1.length) {
        return true
    } else {
        return false
    }


}
// instructor solution
function isAnagram(s1, s2) { 
    if (s1.length !== s2.length){
        return false
    }

    let freqObj1 = {}
    let freqObj2 = {}

    s1 = s1.toLowerCase()
    s2 = s2.toLowerCase()

    for (let i=0; i<s1.length; i++){
        if (freqObj1.hasOwnProperty(s1[i])){
            freqObj1[s1[i]]++
        } else {
            freqObj1[s1[i]] = 1
        }

        if (freqObj2.hasOwnProperty(s2[i])){
            freqObj2[s2[i]]++
        } else {
            freqObj2[s2[i]] = 1
        }
    }

    for (const char in freqObj1) {
        // compare to see if the character is in the obj
        if (!freqObj2.hasOwnProperty(char)){
            return false
        }

        // compare the number of times they shown up
        if (freqObj1[char] !== freqObj2[char]){
            return false
        }
    }
    return true
}
console.log(isAnagram(two_strA1, two_strB1))
console.log(isAnagram(two_strA2, two_strB2))
console.log(isAnagram(two_strA3, two_strB3))
console.log(isAnagram(two_strA4, two_strB4))
