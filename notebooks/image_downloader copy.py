from google_images_download import google_images_download 
from bing_image_downloader import downloader 
from multiprocessing import Pool
from tqdm import tqdm
import joblib
from collections import Counter
from PIL import Image

# Object
#downloader = google_images_download.googleimagesdownload()

# Queries
search = [
    'Huey Teocalli',     # El Templo Mayor
    'Great Pyramid of Giza',
    'Stonehenge',
    'Lighthouse of Alexandria',
    'Hanging Gardens of Babylon',
    'Hagia Sophia',
    'Colossus of Rhodes',
    'Mausoleum at Halicarnassus',
    'Statue of Zeus at Olympia',
    'Temple of Artemis at Ephesus',
    'Golden Gate Bridge',
    'CN Tower',
    'Channel Tunnel',
    'Delta Works',
    'Panama Canal',
    'Empire State Building',
    'Itaipu Dam',
    'Catacombs of Kom el Shoqafa',
    'Great Wall of China',
    'Colosseum',
    'Chichen Itza',
    'Leaning Tower of Pisa',
    'Porcelain Tower of Nanjing',
    'Machu Picchu',
    'Christ the Redeemer',
    'Petra',
    'Taj Mahal',
    'Hoover Dam',
    'Brooklyn Bridge',
    'Bell Rock Lighthouse',
    'SS Great Eastern',
    'London Sewerage System',
    'First Transcontinental Railroad',
    'Mundo Perdido Maya',
    'Papahanaumokuakea Marine National Monument',
    'Potala Palace',
    'El Palacio de las Bellas Artes',
    'El Angel de la Independencia',
    'Alhambra',
    'Amundsen-Scott Research Station',
    'Angkor Wat',
    'Apadana',
    'Big Ben',
    'Bolshoi Theatre',
    'Broadway',
    'Casa de Contratacion',
    'Eiffel Tower',
    'Estadio do Maracana',
    'Etemenaki',
    'Forbidden City',
    'Greath Bath',
    'Great Library of Alexandria',
    'Great Zimbabwe',
    'Hermitage',
    'Jebel Barkal',
    'Kilwa Kisiwani',
    'Kotokou-in',
    'Mahabodhi Temple',
    'Meenakshi Temple',
    'Mont St. Michel',
    'Oracle of Delphi',
    'Orszaghaz',
    'Oxford University',
    'Potala Palace',
    'Ruhr Valley',
    'St. Basils Cathedral',
    'Statue of Liberty',
    'Sydney Opera House',
    'Terracota Army',
    'Torre de Belem',
    'University of Sankore',
    'Venetian Arsenal'
]

# Function that download the images
def downloadimages(query):
    # keywords: search query
    # format: image file format
    # limit: number of images to be downloaded
    # print urls:  print the image file url
    # size: image size ("large, medium, icon")
    # aspect ratio: the height width ratio ("tall, square, wide, panoramic")
    args = {
        # "keywords": query,
        # "format": "jpg",
        # "limit":5,
        # "print_urls":True,
        # "size": "medium",
        # "aspect_ratio": "wide",
        "query_string": query,
        "limit": 10,
        "output_dir": 'downloads',
        "adult_filter_off": True,
        "force_replace": True,
        "timeout": 60,
        "verbose": True,
    }

    try:
        #downloader.download(args)
        downloader.download(query, limit=100,  output_dir='../data/downloads', adult_filter_off=True, force_replace=False, timeout=60)
    except FileNotFoundError:
        pass

def main():
    # Run the downloader
    # for query in search:
    #     downloadimages(query) 
    #     print() 
    with Pool() as pool:
       out = list(tqdm(pool.imap_unordered(downloadimages, search), total=len(search)))

if __name__ == '__main__':
    main()