const solution = (rectangle, characterX, characterY, itemX, itemY) => {
    const SIZE = 103
    const graph = Array.from(Array(SIZE), () => Array(SIZE).fill(false))
    const ans = []

    rectangle.map(([x1, y1, x2, y2]) => {
        for (let i = x1 * 2; i <= x2 * 2; i++) {
            for (let j = y1 * 2; j <= y2 * 2; j++) {
                graph[i][j] = true
            }
        }
    })
    rectangle.map(([x1, y1, x2, y2]) => {
        for (let i = x1 * 2 + 1; i < x2 * 2; i++) {
            for (let j = y1 * 2 + 1; j < y2 * 2; j++) {
                graph[i][j] = false
            }
        }
    })

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2
    console.log(graph[itemX][itemY])
    graph[itemX][itemY] = []
    graph[characterX][characterY] = 1

    const dirX = [1, -1, 0, 0]
    const dirY = [0, 0, -1, 1]

    const queue = [[characterX, characterY]]

    while (queue.length > 0) {
        console.log(queue)
        const [x, y] = queue.shift()
        for (let i = 0; i < 4; i++) {
            if (x + dirX[i] === itemX && y + dirY[i] === itemY) {
                graph[itemX][itemY].push(graph[x][y])
            }
            if (graph[x + dirX[i]][y + dirY[i]] === true) {
                graph[x + dirX[i]][y + dirY[i]] = graph[x][y] + 1
                queue.push([x + dirX[i], y + dirY[i]])
            }
        }
    }
    return Math.min(...graph[itemX][itemY]) / 2

}

solution([[1, 1, 7, 4], [3, 2, 5, 5], [4, 3, 6, 9], [2, 6, 8, 8]], 1, 3, 7, 8)