def parse_disk_map(disk_map):
    """Parse the disk map into a list of file IDs and free spaces."""
    disk_blocks = []
    is_file = True
    file_id = 0

    for length in map(int, disk_map):
        if is_file:
            disk_blocks.extend([file_id] * length)
            if length > 0:
                file_id += 1
        else:
            disk_blocks.extend(['.'] * length)
        is_file = not is_file

    return disk_blocks

def compact_disk(disk_blocks):
    """Compact the disk blocks by moving file blocks to the leftmost free space."""
    i = 0
    limit = len(disk_blocks)

    while i < limit:
        if disk_blocks[i] == '.':
            if disk_blocks[limit - 1] != '.':
                disk_blocks[i], disk_blocks[limit - 1] = disk_blocks[limit - 1], disk_blocks[i]
                i += 1
                limit -= 1
            else: 
                limit -= 1
        else:
            i += 1
    
    return disk_blocks

def calculate_checksum(disk_blocks):
    """Calculate the checksum based on the position and file ID of each block."""
    return sum(pos * block for pos, block in enumerate(disk_blocks) if block != '.')

def main():
    # Input disk map
    disk_map = "2333133121414131402"

    with open("input.txt") as f:
        input_text = f.read()
    # Parse the disk map
    disk_blocks = parse_disk_map(input_text)
    print("Initial disk blocks:", ''.join(map(str, disk_blocks)))
    print(disk_blocks)

    # Compact the disk
    compacted_blocks = compact_disk(disk_blocks)
    print("Compacted disk blocks:", ''.join(map(str, compacted_blocks)))

    # Calculate the checksum
    checksum = calculate_checksum(compacted_blocks)
    print("Filesystem checksum:", checksum)

if __name__ == "__main__":
    main()
