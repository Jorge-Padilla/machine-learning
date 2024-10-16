from google_images_download import google_images_download 
from better_bing_image_downloader import downloader 
from multiprocessing import Pool
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm
import os
import joblib
from collections import Counter
from PIL import Image

# Object
#downloader = google_images_download.googleimagesdownload()

# Queries
search = [
    'Alhambra',
    'Amundsen-Scott Research Station',
    'Angkor Wat',
    'Apadana',
    'Big Ben',
    'Biosphere de Montreal',
    'Bolshoi Theatre',
    'Broadway',
    'Casa de Contratacion',
    'Chichen Itza',
    'Christ the Redeemer',
    'Colosseum',
    'Colossus of Rhodes',
    'Eiffel Tower',
    'El Palacio de las Bellas Artes',
    'El Angel de la Independencia',
    'Estadio do Maracana',
    'Etemenaki',
    'Forbidden City',
    'Golden Gate Bridge',
    'Greath Bath',
    'Great Library of Alexandria',
    'Great Pyramid of Giza',
    'Great Wall of China',
    'Great Zimbabwe',
    'Hagia Sophia',
    'Hanging Gardens of Babylon',
    'Hermitage',
    'Huey Teocalli',     # El Templo Mayor
    'Jebel Barkal',
    'Kilwa Kisiwani',
    'Kotokou-in',
    'Leaning Tower of Pisa',
    'Lighthouse of Alexandria',
    'Machu Picchu',
    'Mahabodhi Temple',
    'Mausoleum at Halicarnassus',
    'Meenakshi Temple',
    'Mont St. Michel',
    'Oracle of Delphi',
    'Orszaghaz',
    'Oxford University',
    'Panama Canal',
    'Petra',
    'Potala Palace',
    'Ruhr Valley',
    'St. Basils Cathedral',
    'Statue of Liberty',
    'Statue of Zeus at Olympia',
    'Stonehenge',
    'Sydney Opera House',
    'Taj Mahal',
    'Temple of Artemis at Ephesus',
    'Terracota Army',
    'Torre de Belem',
    'University of Sankore',
    'Venetian Arsenal'
]

# Function that download the images
def downloadimages(query):
    try:
        downloader(query, limit=100,  output_dir=fr'{os.path.abspath(os.getcwd())}\data\download', adult_filter_off=True, force_replace=False, timeout=60, verbose=False)
    except:
        pass

def resize_images(src, name, include, width=32, height=None):
    """
    I am trying to rezise the images to a 32p resolution
    And also store them in RGB format so I can use their variables
    """
    # height will be equal to width if not defined
    height = height if height is not None else width

    data = dict()
    data['description'] = f"resized ({width}x{height})world wonder images in rgb"
    data['label'] = []          # This will be our 'y'
    data['filename'] = []
    data['data'] = []           # This would contain our Xs

    # The pickle file is new for me, not sure if necesary
    pklname = f"{name}_{width}x{height}.pkl"

    for subdir in os.listdir(src):
        if subdir in include:
            print(subdir)
            current = os.path.join(src, subdir)
            for file in os.listdir(current):
                if file[-3:] in {'jpg', 'png', 'peg'}:      # png jpg, maybe jpeg fails?
                    try:
                        image = Image.open(os.path.join(current, file))
                        image = image.resize((width, height))  # is this all?
                        image = image.convert('RGB')
                        data['label'].append(subdir)
                        data['filename'].append(file)
                        data['data'].append(image)
                    except:
                        print(f'{file} failed, skipping')
                        pass
        joblib.dump(data,pklname)

def main():
    # Run the downloader
    # for query in search:
    #     downloadimages(query) 
    #     print() 
    # with Pool() as pool:
    #    out = list(tqdm(pool.imap_unordered(downloadimages, search), total=len(search)))
    resize_images(fr'{os.path.abspath(os.getcwd())}\data\raw', "World_Wonders", search, 32)
    data = joblib.load(fr'{os.path.abspath(os.getcwd())}\World_Wonders_32x32.pkl')
    print('Samples: ', len(data['data']))
    print('Keys: ', list(data.keys()))
    print('Description: ', data['description'])
    print('Labels:', np.unique(data['label']))
    print(Counter(data['label']))
    # Print them with plt
    labels = np.unique(data['label'])

    fig, axes = plt.subplots(1, len(labels))
    fig.set_size_inches(15,4)
    fig.tight_layout()

    # Print only one for each label
    for ax, label in zip(axes, labels):
        idx = data['label'].index(label)
        
        ax.imshow(data['data'][idx])
        ax.axis('off')
        ax.set_title(label)

if __name__ == '__main__':
    main()