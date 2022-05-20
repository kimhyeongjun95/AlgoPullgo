// 프로그래머스 징검다리

function solution(distance, rocks, n) {

	rocks=[0, ...rocks.sort((a,b) => a - b), distance];

	const BinarySearch = () => {
		let start = 0;
		let end = distance;

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