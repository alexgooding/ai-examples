from k_nearest_neighbours_helper import k_nearest_neighbours_helper

if __name__ == "__main__":
    ship_locations = [(0, 1), (3, 2), (2, 2), (4, 3), (8, 9), (10, 10), (7, 9), (6, 5)]
    ship_labels = ["Axis", "Axis", "Axis", "Axis", "Allies", "Allies", "Allies", "Allies"]
    k = 3
    helper = k_nearest_neighbours_helper(ship_locations, ship_labels, k)
    new_point_1 = (1, 2)
    new_point_2 = (8, 8)
    new_point_3 = (5, 4)
    helper.classify_new_point(new_point_1)
    helper.classify_new_point(new_point_2)
    helper.classify_new_point(new_point_3)
    helper.print_data()