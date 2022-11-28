from coordinates import coordinates
from task_one import max_depth_location


def is_trench(list):
	if (
		list[0] > list[1] - 10 or
		list[-1] > list[-2] - 10
	):
		return False
	for coord in list[1:-1]:
		if (
			coord > list[1] + 2 or
			coord < list[1] - 2
		):
		  return False

	return True


def find_10_drop(list):
	previous_value = list[0]
	for coord_index, coord in enumerate(list):
		if previous_value + 10 < coord:
			return coord_index - 1
		previous_value = coord


def find_10_increase(list):
	previous_value = list[0]
	for coord_index, coord in enumerate(list):
		if previous_value > coord + 10:
			return coord_index
		previous_value = coord


def find_trench(list):
	trench_found = False
	start_coord = -1
	while not trench_found:
		start_coord += 1
		start_coord = find_10_drop(list[start_coord:]) + start_coord
		end_coord = find_10_increase(list[start_coord:-1]) + start_coord
		trench_found = is_trench(list[start_coord:end_coord + 1])
		
	return start_coord, end_coord

def find_nth_trench(n, list):
	original_end_coord = 0
	for _ in range(n):
		start_coord, end_coord = find_trench(list[original_end_coord:])
		start_coord += original_end_coord
		original_end_coord += end_coord
	return (start_coord, original_end_coord)


def nth_trench_deepest_points(n, list):
	start_coord, end_coord = find_nth_trench(n, list)
	deepest_points = []
	for coordinate in max_depth_location(list[start_coord: end_coord]):
		deepest_points.append(coordinate + start_coord)
	return deepest_points

nth_trench_deepest_points(3, coordinates)



# Answers:
# First trench coordinates (13, 19)
# Second trench coordinates (75, 77)
# Third trench coordinates (123, 125)
# Treasure in third trench location 124
