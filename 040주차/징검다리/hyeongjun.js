// 프로그래머스 (2018 카카오) 프렌즈4블록 

// 2 x 2 형태로 4개가 붙어있으면 사라지면서 점수
// 한꺼번에 지워지고 위의 블록이 아래로 떨어짐
// 반복
// 4개 이상 직사각형

// 지워지는 블록 갯수 return

// m = row, n = col


function solution(distance, rocks, n) {
	// rocks.sort((a, b) => a - b)
	rocks=[0, ...rocks.sort((a,b) => a - b), distance];

	const BinarySearch = () => {
		let start = 0;
		let end = distance;
		console.log(start, end);

		while (start <= end) {
			let mid = Math.floor((start+end) / 2);
			let count = 0;
			let now = 0;

			for (let i = 1; i < rocks.length; i++) {
				if (rocks[i] - now < mid) {
					count += 1;
				} else {
					now = rocks[i];
				}
			}	

			if (count > n) {
				end = mid - 1;
			} else {
				start = mid + 1;
			}
		}
		answer = end;
	}
	BinarySearch();
	return answer;
}
	
console.log(solution(
	25,
	[2, 14, 11, 21, 17],
	2
))

// 4