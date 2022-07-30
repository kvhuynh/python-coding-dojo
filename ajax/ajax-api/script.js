
async function getGitHub() {
    var response = await fetch("https://api.github.com/users/kvhuynh");
    var coderData = await response.json();
    return coderData;
}

console.log(getGitHub())