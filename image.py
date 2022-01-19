import os, urllib.request, json # json for pretty output
from serpapi import GoogleSearch
import requests


"""
'The Red Fort, Delhi',
'The Taj Mahal, Agra',
'Pangong Lake, Ladakh',
'Valley of Flowers, Nainital',
'Jaisalmer Fort, Jaisalmer',
'Ruins of Hampi, Karnataka',
'Ghats at Varanasi, Uttar Pradesh',
'Backwaters, Kerala',
'Old Goa, Goa',
'Umaid Bhavan Palace, Jodhpur',
'Jama Masjid, Delhi',
'Akshardham Temple, Delhi',
'Old Bombay, Mumbai',
'Ajanta and Ellora Caves, Aurangabad',
'The Golden Temple, Amritsar',
'Charminar, Hyderabad',
'Amber Fort, Jaipur',
'Rashtrapati Bhavan, Delhi',
'Mahabodhi Temple, Bodh Gaya',
'Meenakshi Amman Temple, Madurai',
'Khajuraho Temples, Chattarpur',
'Elephanta Caves, Mumbai',
'City Palace, Udaipur',
'Havelock Island, Andamans',
'Tirupati, Chittoor',
'Tawang Monastery, Tawang',
'Kaziranga National Park, Assam',
'Kesaria Stupa, Kesaria',
'Palitana Temples, Bhavnagar',
'City Palace, Jaipur',
'Sun Temple, Konark',
'Rani Ki Vav, Patan',
'Chaturbhuj Temple, Orchha',
'Cellular Jail, Port Blair',
'Borra Caves, Vishakhapatnam',
'The Ridge, Shimla',
'Tso Moriri Lake, Ladakh',
'Mysore Palace, Mysore',
'Bangalore Palace and Grounds, Bangalore',
'Gwalior Fort, Gwalior',
'Bhimbetka Rock Shelters, Raisen',
'Victoria Terminus (Chattrapati Shivaji Terminus), Mumbai',
'Jagannath Temple, Puri',
'Lingaraja Temple Complex, Khurda',
'Udayagiri Caves, Bhopal',
'Qila Mubarak, Bhatinda',
'Jallianwala Bagh, Amritsar',
'Chhatrapati Shivaji Maharaj Vastu Sangrahalay, Mumbai',
'Lake Palace, Udaipur',
'Ghats and Old City of Pushkar, Pushkar',
'Ranakpur Jain Temple, Ranakpur',
'Bada Imambara, Lucknow',
'Fatehpur Sikri, Agra',
'Humayun’s Tomb, Delhi',
'The Great Stupa, Sanchi',
'Jantar Mantar Observatory, Jaipur',
'The Great Living Chola Temples, Thanjavur',
'Mahabalipuram, Kanchipuram',
"""




places_array = ['Coonoor', 'Ajmer', 'Varkala', 'Poovar', 'Kanyakumari', 'Khajuraho', 'Pushkar', 'Wayanad', 'Gulmarg', 'Shirdi', 'Madurai', 'Bodh Gaya', 'Ranchi', 'Bokaro Steel City', 'Deoghar', 'Bankura', 'Nalanda', 'Hazaribagh']
def get_google_images(items):
    params = {
      "api_key": "1809de930db96ce3fe60b331af16ab94152518f54049954c07b611cd209e24b5",
      "engine": "google",
      "q": items,
      "tbm": "isch"
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    # print(results)
    
    url = results['images_results'][1]["original"]
    return url

place = {}
for items in places_array:
    
    image_url = get_google_images(items)
    
    place[items.strip()] = image_url
    print(place)


    
print("========================================= FINAL ========================================")    
print(place)
places_array = places_array[20:]
print(places_array)
