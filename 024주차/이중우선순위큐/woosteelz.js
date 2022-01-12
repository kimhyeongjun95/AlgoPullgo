// 프로그래머스 이중우선순위큐

function solution(operations) {
    let answer = [];

    while (operations.length > 0) {
        let command = operations.shift().split(" ")
        if (command[0] === "I") {
            answer.push(Number(command[1]))
            answer.sort((a, b) => {
                return a - b;
            })
        }
        else {
            answer.sort((a, b) => {
                return a - b;
            })
            if (command[1] === '-1') {
                answer.shift();
            }
            else {
                answer.pop();
            }
        }
    }

    if (answer.length > 0) {
        return [answer[answer.length - 1], answer[0]];
    }
    return [0, 0]
}