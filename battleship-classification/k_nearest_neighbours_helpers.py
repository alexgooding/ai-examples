from scipy.spatial import distance

class k_nearest_neighbours_helper:

    def __init__(self, labels, data_points):
        # list of the labels corresponding to each data point
        self.labels = labels
        self.data_point = data_points

    @staticmethod
    def calculate_euclidean_distance(point_1, point_2):
        return distance.euclidean(point_1, point_2)

