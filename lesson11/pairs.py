from pprint import pprint

biggest_cities = ["Tokyo", "Delhi", "Shanghai", "Mexico City", "Sao Paulo",
                  "Mumbai", "Kinki major metropolitan area", "Cairo"]


pairs = zip(biggest_cities, range(1, len(biggest_cities) + 1))


pprint(list(pairs))
