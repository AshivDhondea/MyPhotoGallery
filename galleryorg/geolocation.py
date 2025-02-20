# Refer to https://stackoverflow.com/questions/69409255/how-to-get-city-state-and-country-from-a-list-of-latitude-and-longitude-coordi
from geopy.extra.rate_limiter import RateLimiter
from geopy.geocoders import Nominatim


def city_state_country(coord, user_agent):
    geolocator = Nominatim(user_agent=user_agent)
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    location = geolocator.reverse(coord, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    province = address.get('state', '')
    country = address.get('country', '')
    return city, province, country


def geolocate_dict(photo_dict, user_agent):
    location_dict = {}
    coordinates = (photo_dict['geoData']['latitude'], photo_dict['geoData']['longitude'])
    if coordinates[0] != 0.0 or coordinates[1] != 0.0:
        location_dict['city'], location_dict['province'], location_dict['country'] = city_state_country(coordinates, user_agent)
    else:
        location_dict['city'], location_dict['province'], location_dict['country'] = None, None, None

    photo_dict.update(location_dict)
    return photo_dict
