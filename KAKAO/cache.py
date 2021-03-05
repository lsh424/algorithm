import collections

def solution(cacheSize, cities):
    cache = collections.deque([])
    cities = map(lambda x: x.lower(), cities)
    answer = 0

    def lru(cache, city):
        if cacheSize == 0:
            return 5

        if city in cache:
            cache.remove(city)
            cache.appendleft(city)
            return 1
        else:
            if len(cache) == cacheSize:
                cache.pop()

            cache.appendleft(city)
            return 5

    for city in cities:
        answer += lru(cache, city)

    return answer