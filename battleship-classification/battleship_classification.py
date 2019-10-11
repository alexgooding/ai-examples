from k_nearest_neighbours_helper import k_nearest_neighbours_helper
import matplotlib.pyplot as plt
import random

"""
A function to show our simple battleships example more clearly
"""
def create_2d_plot_for_two_classifiers(data_dict, label_names, new_points):
    data_points_1 = []
    data_points_2 = []
    for point, label in data_dict.items():
        if label == label_names[0]:
            data_points_1.append(point)
        else:
            data_points_2.append(point)
    data_points_1_x = [point[0] for point in data_points_1]
    data_points_1_y = [point[1] for point in data_points_1]
    data_points_2_x = [point[0] for point in data_points_2]
    data_points_2_y = [point[1] for point in data_points_2]
    plt.plot(data_points_1_x, data_points_1_y, 'bo')
    plt.plot(data_points_2_x, data_points_2_y, 'ro')
    for i in range(0, len(new_points)):
        plt.annotate("New Point " + str(i+1), xy=new_points[i], xytext=(-15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')
    plt.show()

if __name__ == "__main__":
    ship_locations = [(random.random() * 10.0, random.random() * 10.0) for _ in range(100)]
    ship_labels = ["Axis"] * 50 + ["Allies"] * 50
    k = 3
    helper = k_nearest_neighbours_helper(ship_locations, ship_labels, k)
    new_point_1 = (1, 2)
    new_point_2 = (8, 8)
    new_point_3 = (5, 4)
    list_of_new_points = [new_point_1, new_point_2, new_point_3]
    for point in list_of_new_points:
        helper.classify_new_point(point)
    helper.print_data()
    create_2d_plot_for_two_classifiers(helper.data_point_dict, helper.label_names, list_of_new_points)

