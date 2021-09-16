if __name__ == '__main__':
    n = int(input())
    l = [] 
    for i in range(n):
        cmd = input().split() 
        command = cmd[0] 
        if len(cmd) > 1: 
            index = int(cmd[1]) 
        if len(cmd) > 2: 
            number=int(cmd[2])
        if command=='insert': 
            l.insert(index,number) 
        if command=='append': 
            l.append(index) 
        elif command=='remove': 
            l.remove(index) 
        if command=='print': 
            print(l) 
        elif command=='pop': 
            l.pop() 
        elif command=='reverse':
            l.reverse() 
        elif command=='sort': 
            l.sort()