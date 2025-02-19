import json


def parse_json(file_path):
    output_dict = dict().fromkeys(('title', 'people', 'photoTakenTime', 'geoData'))

    with open(file_path, encoding='utf-8') as f:
        photo_dict = json.load(f)

    for key in output_dict.keys():
        if key in photo_dict.keys():
            if key == 'photoTakenTime':
                output_dict['photoTakenTime'] = photo_dict['photoTakenTime']['formatted']
            elif key == 'geoData':
                output_dict['geoData'] = [(k, v) for k, v in photo_dict['geoData'].items()]
            else:
                output_dict[key] = photo_dict[key]

    return output_dict