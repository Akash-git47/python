def min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()
    platforms = max_platforms = 0
    i = j = 0
    while i < len(arrivals):
        if arrivals[i] <= departures[j]:
            platforms += 1   # train arrives before one departs
            i += 1
        else:
            platforms -= 1   # one platform freed
            j += 1
        max_platforms = max(max_platforms, platforms)
    return max_platforms

arr = [900,940,950,1100,1500,1800]
dep = [910,1200,1120,1130,1900,2000]
print(min_platforms(arr, dep))  # 3