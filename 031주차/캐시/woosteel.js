function solution(cacheSize, cities) {
    var answer = 0;
    let cache = [];

    //LRU(페이지 교체 알고리즘) : 가장 마지막에 사용 된 페이지를 교체
    const cities_len = cities.length;

    if (cacheSize == 0) return cities_len * 5; //캐시크기가 0인 경우 전부 실행시간이 5이기 때문에 반환

    //도시 개수만큼 loop
    for (let i = 0; i < cities_len; i++) {
        const citie = cities[i].toLowerCase(); //도시 이름
        if (cache.indexOf(citie) !== -1) //cache hit
        {
            answer += 1; //1초 추가
            cache.splice(cache.indexOf(citie), 1); //hit 된 도시 배열에서 제거
            cache.push(citie); //가장 최근에 hit됨으로 마지막 index에 위치
        }
        else //cache miss
        {
            if (cache.length < cacheSize) //cache max size 미 도달
            {
                cache.push(citie);
            }
            else //LRU Logic 실행
            {
                cache.shift(); //가장 마지막에 사용된 페이지 제거
                cache.push(citie); //새로운 페이지 추가
            }
            answer += 5;
        }
    }
    return answer;
}