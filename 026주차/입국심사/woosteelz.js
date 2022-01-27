function solution(n, times) {
    let answer = 0;

    let left = 1
    let right = n * Math.max(...times) // 배열에서 max값을 구할때는 전개연산자 사용(Spread Operator)

    while (left <= right) {
        let mid = parseInt((left + right) / 2)
        let cnt = 0


        for (let i = 0; i < times.length; i++) {
            cnt += parseInt(mid / times[i])
            if (cnt >= n) break
        }

        if (cnt >= n) {
            answer = mid
            right = mid - 1
        }
        else left = mid + 1
    }

    return answer;
}