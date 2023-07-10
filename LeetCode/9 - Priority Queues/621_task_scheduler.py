from typing import List

# THIS FAILS BECAUSE WE NEED TO PRIORITISE DOING TASKS WHICH OCURR MORE FREQUENTLY


def leastInterval(tasks: List[str], n: int) -> int:

    # this dict will be storing how many of each task do we need to do
    taskMap = {}
    for task in tasks:
        if task not in taskMap:
            taskMap[task] = 0
        taskMap[task] += 1

    # this dict will store which tasks have currently been put on hold and for how long
    waiting = {}
    time = 0

    while taskMap:
        keyList = list(taskMap.keys())
        taskDone = False
        for key in keyList:
            if key not in waiting.keys():
                taskMap[key] -= 1
                time += 1
                taskDone = True
                if taskMap[key] == 0:
                    taskMap.pop(key)
                else:
                    if n > 0: waiting[key] = n+1
                break
        if not taskDone:
            time += 1
        for key in list(waiting.keys()):
            waiting[key] -= 1
            if waiting[key] <= 0:
                waiting.pop(key)
    return time

print(leastInterval(["A","A","A","B","B","B", "C","C","C", "D","D", "E"], 2))

"""
A --> B --> C --> A --> B --> C --> A 
"""