const solution = (maps) => {
    let ans = 0;
    const dirX = [0, -1, 1, 0]
    const dirY = [1, 0, 0, -1]
    const n = maps.length
    const m = maps[0].length
    const visited = [...maps].map((r) => r.map((c) => 0));

    const queue = []
    queue.push([0, 0])
    visited[0][0] = 1

    while (queue.length) {
        const [currX, currY] = queue.shift()
        for (let i = 0; i < 4; i++) {
            const [nextX, nextY] = [currX + dirX[i], currY + dirY[i]]
            if (0 <= nextX && nextX < n && 0 <= nextY && nextY < m && visited[nextX][nextY] === 0 && maps[nextX][nextY] === 1) {
                queue.push([nextX, nextY])
                visited[nextX][nextY] = visited[currX][currY] + 1
            }
        }
    }

    return !visited[n - 1][m - 1] ? -1 : visited[n - 1][m - 1]
}

// console.log는 전 부 지 우 자 

console.log(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))