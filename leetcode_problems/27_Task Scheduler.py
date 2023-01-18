class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cnt = collections.Counter(tasks)
        itn = [ -i for i in cnt.values()]
        heapq.heapify(itn)
        q=deque()
        time=0
        while itn or q:
            time+=1
            if itn:
                m = 1 + heapq.heappop(itn)
                if m:
                    q.append([m,time+n])
            if q and q[0][1] == time:
                p=q.popleft()
                heapq.heappush(itn,p[0])
        return time

