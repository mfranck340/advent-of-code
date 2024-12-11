
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

def compact_disk_v2(disk_blocks):
    """Compact the disk blocks by moving whole files to the leftmost free space."""
    # Get a list of file IDs and their positions
    file_positions = {}
    for pos, block in enumerate(disk_blocks):
        if block != '.':
            file_positions.setdefault(block, []).append(pos)
    
    # Process files in decreasing order of file ID
    for file_id in sorted(file_positions.keys(), reverse=True):
        positions = file_positions[file_id]
        file_length = len(positions)

        # Find the leftmost free span that can fit this file
        span_start = None
        free_count = 0
        for pos, block in enumerate(disk_blocks):
            if block == '.':
                free_count += 1
                if span_start is None:
                    span_start = pos
                if free_count == file_length:
                    break
            else:
                span_start = None
                free_count = 0

        # If we found a valid span, move the file
        if free_count == file_length and span_start < positions[0]:
            # Clear the current positions of the file
            for pos in positions:
                disk_blocks[pos] = '.'
            
            # Place the file in the new span
            for i in range(file_length):
                disk_blocks[span_start + i] = file_id

    return disk_blocks

def calculate_checksum(disk_blocks):
    """Calculate the checksum based on the position and file ID of each block."""
    return sum(pos * block for pos, block in enumerate(disk_blocks) if block != '.')

def main_v2():
    disk_map = "2333133121414131402"
    # Input disk map
    with open("input.txt") as f:
        input_text = f.read().strip()
    
    # Parse the disk map
    disk_blocks = parse_disk_map(input_text)
    print("Initial disk blocks:", ''.join(map(str, disk_blocks)))

    # Compact the disk using the new method
    compacted_blocks = compact_disk_v2(disk_blocks)
    print("Compacted disk blocks (v2):", ''.join(map(str, compacted_blocks)))

    # Calculate the checksum
    checksum = calculate_checksum(compacted_blocks)
    print("Filesystem checksum (v2):", checksum)

if __name__ == "__main__":
    main_v2()
