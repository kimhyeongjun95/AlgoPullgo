function isPalindrome(s) {
    let start = 0;
    let end = s.length - 1;

    while (start < end) {
        if (s[start] !== s[end]) {
            return false;
        }
        start++;
        end--;
    }
    return true;
}

function solution(s) {
    let len = s.length;

    for (let i = len; i >= 0; i--) {
        for (let j = 0; j <= len - i; j++) {
            if (isPalindrome(s.slice(j, j + i))) {
                return i
            }
        }
    }
    return 1
}

console.log(solution("abacde"))