class TimeMap:

    def __init__(self):
        self.store = {} # key : [value , timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
           self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        vals = self.store.get(key,[]) 
        '''
            vals would get as list containing list of two elements
            [[value, timestamp][][] . . . .]
            we operate the binary search to find the mid.
            if the mid index's array's timestamp is equal to 
            given timestamp then return the value for that timestamp
            if the given timestamp is 5 for example and the last
            time stamp added is 4 then store the vlaue for that timestamp
            
        '''
        left, right = 0, len(vals) - 1
        while left <= right:
            mid = (left + right) // 2
            if timestamp == vals[mid][1]:
                return vals[mid][0]
            elif timestamp > vals[mid][1]: 
                '''
                think the timestamp as a key value .
                in binary search if the key is larger than the 
                value of the mid, then we search at the right portion 
                of the array. and here we stored the mid[value] becuase
                if the key is larger than the mid value then it is also a valid case
                '''
                res = vals[mid][0]
                left = mid + 1
            else:
                right = mid -1
        return res
       
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)