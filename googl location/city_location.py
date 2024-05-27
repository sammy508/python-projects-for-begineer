import webbrowser

def find_city(city_name):

    # format the url eith google search

    google_map_url = f'https://earth.google.com/web/search/{city_name}'

    webbrowser.open(google_map_url)

    # enter city name
city_name = input("enter city name :")
find_city(city_name)    