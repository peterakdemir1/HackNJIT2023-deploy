import piexif

def get_gps_info(image_path):
    # Load metadata
    exif_dict = piexif.load(image_path)
    # Get the GPS data
    gps_info = exif_dict.get('GPS', {})
    return gps_info

def get_coords(gps_data):
    # this takes in gps exif dict as input so use the return value of get_gps_info()
    latitude = {
        'degree': 0,
        'minute': 0,
        'second': 0,
        'reference': 'N'
    }

    longitude = {
        'degree': 0,
        'minute': 0,
        'second': 0,
        'reference': 'W'
    }

    coordinates = [latitude, longitude]

    latitude['degree'] = gps_data[2][0][0] / gps_data[2][0][1]
    latitude['minute'] = gps_data[2][1][0] / gps_data[2][1][1]
    latitude['second'] = gps_data[2][2][0] / gps_data[2][2][1]
    latitude['reference'] = gps_data[1]

    longitude['degree'] = gps_data[4][0][0] / gps_data[4][0][1]
    longitude['minute'] = gps_data[4][1][0] / gps_data[4][1][1]
    longitude['second'] = gps_data[4][2][0] / gps_data[4][2][1]
    longitude['reference'] = gps_data[3]

    return coordinates