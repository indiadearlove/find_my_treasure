from coordinates import coordinates
from task_two import nth_trench_deepest_points, find_nth_trench


def trench_from_submarine(summary):
	return summary[-1] == "<"

def get_n(summary):
	if "B" in summary:
		n = summary[1:-1]
	else:
		n = summary[2:-1]
	return int(n)


def find_treasure_with_pirate_summary(summary):
	n = get_n(summary)
	if trench_from_submarine(summary):
		if "B" in summary:
			treasure = nth_trench_deepest_points(n, coordinates)
		else:
			trench_coordinates = find_nth_trench(n, coordinates)
			if summary[0] == "<":
				treasure = trench_coordinates[0]
			else:
				treasure = trench_coordinates[-1]
	else:
		if "B" in summary:
			reverse_treasures = nth_trench_deepest_points(n, coordinates[::-1])
			treasure = []
			for reverse_treasure in reverse_treasures:
				treasure.append(len(coordinates) - 1 - reverse_treasure)

		else:
			trench_coordinates = find_nth_trench(n, coordinates[::-1])
			if summary[0] == "<":
				reverse_treasure = trench_coordinates[-1]
			else:
				reverse_treasure = trench_coordinates[0]
			treasure = len(coordinates) - 1 - reverse_treasure

	return treasure


find_treasure_with_pirate_summary("<C2>")


# Answers
# B5< - [368, 369, 370, 371, 373, 374, 375]
# B1> - [9991, 9990, 9989, 9988, 9987]
# <C7< - 781
# >C5> - 9404
# <C2> - 9931

