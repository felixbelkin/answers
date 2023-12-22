def total_volume(boxes):
    total = 0
    for box in boxes:
        volume = box['length'] * box['width'] * box['height']
        total += volume
    return total

boxes_list = [
    {'length': 2, 'width': 3, 'height': 4},
    {'length': 1, 'width': 2, 'height': 1},
    {'length': 3, 'width': 2, 'height': 3}
]

total = total_volume(boxes_list)
print(f"Общий объем коробок: {total}")