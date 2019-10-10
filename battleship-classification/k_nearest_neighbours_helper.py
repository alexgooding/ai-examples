from scipy.spatial import distance
import operator

"""
A helper class for running the k-nearest neighbours algorithm.
We make the assumption that there are no duplicate data points in this implementation.
"""
class k_nearest_neighbours_helper:

    def __init__(self, data_points, labels, k):
        # list of the labels corresponding to each data point
        self.labels = labels
        self.data_points = data_points
        self.label_names = list(dict.fromkeys(self.labels))
        self.data_point_dict = dict(zip(self.data_points, self.labels))
        self.k = k

    @staticmethod
    def calculate_euclidean_distance(point_1, point_2):
        return distance.euclidean(point_1, point_2)

    def vote_for_label(self, points):
        votes_counted = dict(zip(self.label_names, len(self.label_names)*[0]))
        for point in points:
            votes_counted[self.data_point_dict[point]] += 1
        # return the label with the most votes
        return max(votes_counted.items(), key=operator.itemgetter(1))[0]

    def classify_new_point(self, new_point):
        distance_dict = dict(zip(self.data_points, len(self.data_points)*[None]))
        # calculate distance from each point to the new point
        for point in distance_dict.keys():
            distance_dict[point] = self.calculate_euclidean_distance(point, new_point)
        # extract a sorted list of data points based on proximity to the new point
        sorted_dict = sorted(distance_dict.items(), key=operator.itemgetter(1))
        k_nearest_neighbours = []
        for i in range(self.k):
            k_nearest_neighbours.append(sorted_dict[i][0])
        new_label = self.vote_for_label(k_nearest_neighbours)
        # add the new data point and label to the exist lists
        self.data_points.append(new_point)
        self.labels.append(new_label)
        self.data_point_dict = dict(zip(self.data_points, self.labels))

    def print_data(self):
        print("Current data points: " + str(self.data_point_dict))