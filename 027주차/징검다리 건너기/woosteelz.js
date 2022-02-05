const solution = (stones, k) => {
    let ans = 0
    // let [start, end] = [Math.min(...stones), Math.max(...stones)]
    let start = 1
    let end = 200000000

    while (start <= end) {
        const mid = Math.round((start + end) / 2)
        let temp = 0
        let flag = true

        for (let i = 0; i < stones.length; i++) {
            if (stones[i] < mid) {
                temp++
                if (temp === k) {
                    flag = false
                    break
                }
            } else temp = 0
        }
        if (flag) {
            ans = Math.max(ans, mid)
            start = mid + 1
        } else end = mid - 1
    }
    return ans
}