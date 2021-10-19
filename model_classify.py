"""

Evaluates cataract quantification results in external datasets.

Usage:
    model_classify.py --model_folder=<str> --image_folder=<str> --input_file=<str> --output_file=<str>

Options:
    --model_folder=<str>       the path of the models
    --image_folder=<str>        the path of the images
    --input_file=<str>        the input file
    --output_file=<str>        the output file
"""


import sys 
import os 
import numpy as np
import pandas as pd
from docopt import docopt
from keras.models import load_model
from keras.preprocessing import image
import keras.applications.inception_v3 as inception_v3

def preprocess_image(image_path):
    
    img = image.load_img(image_path, target_size=None)

    width, height = img.size

    img = img.resize((334, 501))#img.resize((height//8, width//8)) 
    img = np.expand_dims(img, axis=0)
    img = inception_v3.preprocess_input(img)
    
    return img


def classify_main(model_folder, image_folder, input_file, output_file, variables=['NS', 'PCTCOL', 'PCTPSC']):
    df = pd.read_csv(input_file)
    
    for variable in variables:
        print('Classifying', variable)
        model_path = os.path.join(model_folder, variable+'.h5')
        model = load_model(model_path)
        print('Loading the model', variable+'.h5')
        #model.summary()
        #sys.exit(0)
        predictions = []
        for file_name in df[variable+'_NAME']:
            if pd.isnull(file_name):
                predictions.append('N/A')
            else:
                file_path = os.path.join(image_folder, file_name)
                image = preprocess_image(file_path)
                pred = model.predict([image])
                predictions.append(pred[0][0])
        df[variable+'_PRED'] = predictions
    
    df.to_csv(output_file, index=False)
    
            

if __name__ == "__main__":
    argv = docopt(__doc__, sys.argv[1:])
    

    model_folder = argv['--model_folder']
    image_folder = argv['--image_folder']
    input_file = argv['--input_file']
    output_file = argv['--output_file']
    
    classify_main(model_folder, image_folder, input_file, output_file)























