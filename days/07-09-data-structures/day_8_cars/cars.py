import re
import itertools


cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    output_str = ""
    cnter = 0
    models = cars['Jeep']

    for model in models:
        cnter += 1
        if cnter >= len(models):
            output_str += str(model)
        else:
            output_str += str(model) + ', '

    # print(output_str)
    return output_str


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    first_place_models = []
    for key in cars.keys():
        first_place_models.append(cars[key][0])
    return first_place_models


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    models_nested = list(cars.values())
    models_flat = list(itertools.chain(*models_nested))
    r = re.compile((".*" + grep), re.IGNORECASE)
    grep_models = list(filter(r.match, models_flat))
    grep_models.sort()
    return grep_models


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    temp_cars = []
    for keys in list(cars.keys()):
        temp_cars = cars[keys]
        temp_cars.sort()
        cars[keys] = temp_cars
    return cars
