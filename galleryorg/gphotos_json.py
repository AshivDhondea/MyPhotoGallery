from datetime import datetime
import json


def parse_json(file_path):
    output_dict = dict().fromkeys(('title', 'people', 'photoTakenTime', 'geoData'))

    with open(file_path, encoding='utf-8') as f:
        photo_dict = json.load(f)

    for key in output_dict.keys():
        if key in photo_dict.keys():
            if key == 'photoTakenTime':
                photo_time = photo_dict["photoTakenTime"]["formatted"]
                photo_time_split = photo_time.split(", ")
                photo_date = datetime.strptime(f"{photo_time_split[0]} {photo_time_split[1]}", '%b %d %Y').date()

                output_dict['photoTakenTime'] = {
                    "year": photo_date.year,
                    "month": photo_date.month,
                    "day": photo_date.day,
                    "formatted": photo_time
                }


            #elif key == 'geoData':
            #    output_dict['geoData'] = photo_dict['geoData']#[(k, v) for k, v in photo_dict['geoData'].items()]
            else:
                output_dict[key] = photo_dict[key]

    return output_dict
