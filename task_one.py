from coordinates import coordinates

def max_depth_location(list):
	max_value = max(list)
	return [index for index, location in enumerate(list) if location == max_value]

max_depth_location(coordinates)

# Answers:
# Locations 8818 & 9232
# Value 2498