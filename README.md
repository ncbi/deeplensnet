# Deep Learning Automated Diagnosis and Quantitative Classification of Cataract Type and Severity
This repository provides scripts, test image samples, and attention map samples for the paper titled 'Deep Learning Automated Diagnosis and Quantitative Classification of Cataract Type and Severity'.

## Instructions to set up
### Prerequisites
Have python3.8 installed locally.

### Clone the repository
```
git clone https://github.com/ncbi/lens-cataract.git
cd lens-cataract
```

### Create a virtual environment
```
python3.8 -m venv cataract_lens_external

source cataract_lens_external/bin/activate 
```
### Install the required libraries
```
pip install -r requirements.txt
```
### Download the models
Please download the models from [here](https://drive.google.com/drive/folders/1iOd7jGKgivShyhSM5JM206QQDBpNxerX?usp=sharing)

### Run the script
```
python model_classify.py --model_folder=models/ --image_folder=image_set/ --input_file=input_files.csv --output_file=output_test_file.csv
Please note that image_set/ and input_files.csv are provided in the repository
```
### Check the output_test_file file
Compare output_test_file.csv with output_file.csv. If they are the same, it is ready for testing other images.

## Attention map samples 
The samples can be accessed from [here](https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/cataract_lens/)
