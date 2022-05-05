// 프로그래머스 예상 대진표

// 게임대회
// n명 참가 토너먼트 형식
// 1번 ~ n번
// (1, 2), (3, 4), (n-1, n) 형식
// 이긴 사람은 다음 라운드 진출
// 번호 1번부터 N/2번 다시 배정
// 2번 -> 1번, 3번 -> 2번
// 최종 한명이 남을 때까지 진행

// 서로 붙게 되기 전까지 항상 이긴다고 가정
// a와 b가 몇번째 라운드에서 만나는지? return

// 3, 7, 11, 15 

function solution(n,a,b)
{ 

  let count = 1;
  let na = a;
  let nb = b;
  while (true) {
    if (Math.abs(na-nb) === 1) {
      if (na < nb) {
       if (na % 2 === 1) {
         return count
       }
      } else {
        if (nb % 2 === 1) {
          return count;
        }
      }
    }
    na = Math.ceil(na / 2)
    nb = Math.ceil(nb / 2)
    count += 1;
  }
}

console.log(solution(8, 4, 7))
// 3