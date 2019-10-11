from k_nearest_neighbours_helper import k_nearest_neighbours_helper
import matplotlib.pyplot as plt
import random

"""
A function to show our simple battleships example more clearly
"""
def create_2d_plot_for_two_classifiers(data_dict, label_names, new_points, distances_to_furthest_neighbour):
    # Prepare data for plotting
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
    fig, ax = plt.subplots()
    # Plot the two classes of points
    ax.plot(data_points_1_x, data_points_1_y, 'bo')
    ax.plot(data_points_2_x, data_points_2_y, 'ro')
    # Annotate the new points on the graph
    for i in range(0, len(new_points)):
        ax.annotate("New Point " + str(i+1), xy=new_points[i], xytext=(-15, 25), textcoords='offset points',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='bottom')
    # Draw on circles to indicate which neighbours were selected
    for i in range(len(new_points)):
        ax.add_artist(plt.Circle(new_points[i], distances_to_furthest_neighbour[i], color='g'))
    # Add a title to the graph
    fig.text(0.4, 0.95, label_names[0], ha="left", va="center", size="large", color="red")
    fig.text(0.5, 0.95, "vs", ha="center", va="center", size="large")
    fig.text(0.6, 0.95, label_names[1], ha="right", va="center", size="large", color="blue")
    # Save the graph
    fig.savefig('k_nearest_neighbours_graph.pdf')

"""
Use the example of classification of unknown Axis and Allies ships in WW2.
We also assume assume that it is likely ships travel in fleets - justifying the suitability of this algorithm.
"""
if __name__ == "__main__":
    ship_locations = [(random.random() * 10.0, random.random() * 10.0) for _ in range(100)]
    ship_labels = ["Axis"] * 50 + ["Allies"] * 50
    k = 3
    helper = k_nearest_neighbours_helper(ship_locations, ship_labels, k)
    list_of_new_points = [(1, 2), (8, 8), (5, 4)]
    distances_to_furthest_neighbour = []
    for point in list_of_new_points:
        distances_to_furthest_neighbour.append(helper.classify_new_point(point))
    helper.print_data()
    create_2d_plot_for_two_classifiers(helper.data_point_dict, helper.label_names, list_of_new_points, distances_to_furthest_neighbour)

