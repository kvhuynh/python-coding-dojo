/* 
  Given in an alumni interview in 2021.
  String Encode
  You are given a string that may contain sequences of consecutive characters.
  Create a function to shorten a string by including the character,
  then the number of times it appears. 
  
  
  If final result is not shorter (such as "bb" => "b2" ),
  return the original string.
  */

  const str1 = "aaaabbcdddaa";
  const expected1 = "a4b2c1d3a2";
  
  const str2 = "";
  const expected2 = "";
  
  const str3 = "a";
  const expected3 = "a";
  
  const str4 = "bbcc";
  const expected4 = "bbcc";
  
  /**
   * Encodes the given string such that duplicate characters appear once followed
   * by a number representing how many times the char occurs. Only encode strings
   * when the result yields a shorter length.
   * - Time: O(?).
   * - Space: O(?).
   * @param {string} str The string to encode.
   * @returns {string} The given string encoded.
   */
   function encode(str){
    var currLetter = str[0];
    var currTally = 1;
    var tally = ""
    if (str.length == 1){
        return str
    }
    for (var i =0; i< str.length; i++){
        if (str[i+1] != undefined){
            if (str[i+1]==currLetter){
                currTally+=1

            }
            else {
                tally += currLetter;
                tally += String(currTally);
                currLetter = str[i+1];
                currTally = 1;

            }
        } else {
            tally += currLetter
            tally += String(currTally)
        }

    }
    if (tally.length <= str.length) {

        return str
    }
    else {
        return tally

    }
    }

//   ***************************************************


/* 
  String Decode  
*/

const two_str1 = "a3b2c1d3";
const two_expected1 = "aaabbcddd";

const two_str2 = "a3b2c12d10";
const two_expected2 = "aaabbccccccccccccdddddddddd";

/**
 * Decodes the given string by duplicating each character by the following int
 * amount if there is an int after the character.
 * - Time: O(?).
 * - Space: O(?).
 * @param {string} str An encoded string with characters that may have an int
 *    after indicating how many times the character occurs.
 * @returns {string} The given str decoded / expanded.
 */
 function decodeStr(str) {
    var numList = ["1", "2", "3", "4", "5","6","7","8","9","0"]
    var currLetter = str[0]
    var currTally = ""
    var tally = ""
    
    for (var i=0; i <str.length; i++){

        if (str[i+1] == undefined) {
            currTally = parseInt(currTally)
            tally += currLetter.repeat(currTally)
            continue
        }
        
        if (numList.includes(str[i+1])) {
            currTally += str[i+1]
        }
        else {
            currTally = parseInt(currTally)
            console.log(currLetter)
            tally += currLetter.repeat(currTally)
            currLetter = str[i+1]
            currTally = ""
        }
    }

    return tally

}

// instructor solution

function strEncode(str = "") {
    let encoded = "";
  
    for (let i = 0; i < str.length; i++) {
      let currChar = str[i];
      let dupeCount = 1;
  
      while (str[i + 1] === currChar) {
        dupeCount++;
        i++;
      }
      encoded += currChar + dupeCount;
    }
    return encoded.length < str.length ? encoded : str;
  }

function decodeStr(str) {
    let decoded = ""

    let i = 0
    while (i < str.length){
        let char = str[i++]
        let numStr = ""

        let isNumber = isNaN(parseInt(str[i])) === false

        while ( i < str.length && isNumber){
            numStr += str[i++]
            isNumber = isNaN(parseInt(str[i])) === false
        }
        decoded += myRepeat(char, numStr)
        // decoded += char.repeat(numStr)
    }
    return decoded
}