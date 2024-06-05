import webbrowser

def find_city(city_name,street):

    # format the url eith google search

    google_map_url = f'https://earth.google.com/web/search/{city_name}/{street}'

    webbrowser.open(google_map_url)

    # enter city name
city_name = input("enter city name :")
street= input('enter street name:')
find_city(city_name,street)    