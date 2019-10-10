from scipy.spatial import distance

class k_nearest_neighbours_helper:

    def __init__(self, labels, data_points, k):
        # list of the labels corresponding to each data point
        self.labels = labels
        self.data_points = data_points
        self.label_names = list(dict.fromkeys(self.labels))
        self.data_point_dict = dict(zip(self.data_points, self.labels))
        self.k = k

    @staticmethod
    def calculate_euclidean_distance(point_1, point_2):
        return distance.euclidean(point_1, point_2)

