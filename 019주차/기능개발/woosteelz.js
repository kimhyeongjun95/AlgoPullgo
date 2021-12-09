function solution(progresses, speeds) {
    var answer = [];

    while (progresses.length > 0) {
        for (var i = 0; i < progresses.length; i++) {
            progresses[i] = progresses[i] + speeds[i];
        }
        var cnt = 0;
        while (progresses.length > 0 && progresses[0] >= 100) {
            progresses.shift()
            speeds.shift()
            cnt++;
        }
        if (cnt > 0) {
            answer.push(cnt);
        }
    }

    return answer;
}