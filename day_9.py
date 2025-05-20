with open('inputs/aoc_9.txt', 'r') as f:
    line = f.readline().strip()
disk_map = [int(ch) for ch in line]

# test_case = [int(x) for x in list('2333133121414131402')]
test_case = [int(x) for x in list('9953877292941')]

# --------------- PART 1 -----------------
def get_updated_disk(disk_map):
    updated_disk= []
    counter = 0
    for i in range(0, len(disk_map)):
        if i%2 == 1:
            for j in range(disk_map[i]):
                updated_disk.append('.')
        else:
            for j in range(disk_map[i]):
                updated_disk.append(counter)
            counter += 1
    return updated_disk
test_disk = get_updated_disk(test_case)

def compact_disk(disk_map):
    p1, p2 = 0, len(disk_map)-1
    while p1 < p2:
        while (disk_map[p1] != '.'):
            p1 += 1
        disk_map[p1], disk_map[p2] = disk_map[p2], '.'
        p2 -= 1
    return disk_map

def get_checksum(disk_map):
    sum = 0
    for i in range(len(disk_map)):
        print(f'{i} * {disk_map[i]}')
        if disk_map[i] == '.':
            return sum
        else:
            sum += i * disk_map[i]
    return sum

print(get_checksum(compact_disk(get_updated_disk(disk_map))))

# --------------- PART 2 -----------------