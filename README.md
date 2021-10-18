# Deep Learning Automated Diagnosis and Quantitative Classification of Cataract Type and Severity
This repository provides evaluation scripts and samples for [BioCreative VII Track 5](https://biocreative.bioinformatics.udel.edu/tasks/biocreative-vii/track-5/). 

## Instructions to run the evaluation script
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
```
Please download the models from [here](https://nih.box.com/s/xz1n6c3rfspc09woo0kk64cpyc5vozyt)
```
### Run the evaluation script
```
python model_classify.py --model_folder=models/ --image_folder=image_set/ --input_file=input_files.csv --output_file=output_test_file.csv
Please note that image_set/ and input_files.csv are provided in the repository
```
### Check the output_test_file file
```
Compare output_test_file.csv with output_file.csv. If they are the same, it is ready for testing other images.
```
