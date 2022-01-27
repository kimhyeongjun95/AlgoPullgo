const isPrimeNum = (num) => {
    if (num === 1) {
        return false;
    }
    for (let i = 2; i <= Math.round(Math.sqrt(num)); i++) {
        if (num % i === 0) {
            return false;
        }
    }
    return true;
}

const solution = (n, k) => {
    let ans = 0;

    const num = n.toString(k); // 10진수를 k진수로 변환 (문자열 리턴)
    // const num = parseInt(n, k); // k진수인 n을 10진수로 변환 (정수형 리턴)

    const PrimeList = num.split("0");

    PrimeList.map(function (num) {
        if (num && isPrimeNum(Number(num))) ans++;
    })
    return ans;
}

const n = 100
console.log(isPrimeNum(2))