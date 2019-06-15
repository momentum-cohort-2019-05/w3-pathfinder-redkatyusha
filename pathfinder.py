from PIL import Image


def read_line_of_ints(text):
    ints = []
    ints_as_strs = split_line(text)

    for int_as_str in ints_as_strs:
        ints.append(int(int_as_str))
    return ints


def split_line(line):
    return line.split()


def read_file_into_list(filename):
    with open(filename) as file:
        return file.readlines()


def read_file_into_ints(filename):
    lines = read_file_into_list(filename)

    list_of_lists = []
    for line in lines:
        list_of_lists.append(read_line_of_ints(line))
    return list_of_lists


class ElevationMap:
    def __init__(self, elevations):
        self.elevations = elevations

    def elevation_at_coordinate(self, x, y):
        return self.elevations[y][x]

    def min_elevation(self):
        return min([min(row) for row in self.elevations])

    def max_elevation(self):
        return max([max(row) for row in self.elevations])

    def intensity_at_coordinate(self, x, y, min_elevation, max_elevation):
        elevation = self.elevation_at_coordinate(x, y)

        return ((elevation - min_elevation) / (max_elevation - min_elevation)) * 255


    def draw_grayscale_gradient(self, filename, width, height):
        image = Image.new("RGBA", (width, height))
        min_elevation = self.min_elevation()
        max_elevation = self.max_elevation()
        for x in range(width):
            for y in range(height):
                intensity = int(self.intensity_at_coordinate (x, y, min_elevation, max_elevation))
                image.putpixel((x, y), (intensity, intensity, intensity))
        image.save(filename)


if __name__ == "__main__":

    elevations = read_file_into_ints('elevation_small.txt')

    e_map = ElevationMap(elevations)

    e_map.draw_grayscale_gradient('map.png', 600, 600)
