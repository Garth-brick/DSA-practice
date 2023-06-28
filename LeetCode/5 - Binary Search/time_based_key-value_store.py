from typing import Dict, List, Any

class TimeMap:
    def __init__(self) -> None:
        self.mappy: Dict[str, List[List[Any]]] = {}
        # every key will have a list of value-timestamp pairs associated with it
    
    def set(self, key: str, timestamp: int, value: str) -> None:
        if key not in self.mappy.keys():
            # if key doesn't already exist then create the key with an empty list
            self.mappy[key] = []
        # once the key has been made, add a new value-timestamp pair to it
        self.mappy[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        result = ""
        value_timestamp_pairs = self.mappy.get(key, [])

        # binary searching for the appropoiate timestamp
        l, r = 0, len(value_timestamp_pairs)-1
        while (l <= r):
            mid = (l+r)//2
            if (value_timestamp_pairs[mid][1] == timestamp):
                result = value_timestamp_pairs[mid][0]
                break
            elif (value_timestamp_pairs[mid][1] < timestamp):
                result = value_timestamp_pairs[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return result
        
        
        
tm = TimeMap()
tm.set("foo", 1, "bar")
tm.set("foo", 2, "bar2")
tm.set("foo", 3, "bar3")
tm.set("foo", 5, "bar4")
print(tm.get("foo", 7))