const solution = (id_list, report, k) => {
    let ans = [];

    let stop = [];
    let singo = {};
    let mail = {};

    report.map((temp) => {
        let [a, b] = temp.split(" ");

        if (a in mail) {
            mail[a].add(b)
        } else {
            mail[a] = new Set();
            mail[a].add(b)
        }
        if (b in singo) {
            singo[b].add(a)
        } else {
            singo[b] = new Set();
            singo[b].add(a);
        }
    })

    for (let key in singo) {
        if (singo[key].size >= k) stop.push(key)
    }

    id_list.map((id) => {
        let cnt = 0;
        if (mail[id]) {
            mail[id].forEach(value => {
                console.log(value)
                if (stop.includes(value)) cnt++;
            })
        }
        ans.push(cnt);
    })
    return ans
}

console.log(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))