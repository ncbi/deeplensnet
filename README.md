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
Please download the models from [here](https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/cataract_lens/models.zip)

### Run the script
```
python model_classify.py --model_folder=models/ --image_folder=image_set/ --input_file=input_files.csv --output_file=output_test_file.csv
Please note that image_set/ and input_files.csv are provided in the repository
```
### Check the output_test_file file
Compare output_test_file.csv with output_file.csv. If they are the same, it is ready for testing other images.

## Attention map samples 
The samples can be accessed from [here](https://ftp.ncbi.nlm.nih.gov/pub/lu/Suppl/cataract_lens/attention_map_samples.zip)

## NCBI's Disclaimer
This tool shows the results of research conducted in the [Computational Biology Branch](https://www.ncbi.nlm.nih.gov/research/), [NCBI](https://www.ncbi.nlm.nih.gov/home/about). 

The information produced on this website is not intended for direct diagnostic use or medical decision-making without review and oversight by a clinical professional. Individuals should not change their health behavior solely on the basis of information produced on this website. NIH does not independently verify the validity or utility of the information produced by this tool. If you have questions about the information produced on this website, please see a health care professional. 

More information about [NCBI's disclaimer policy](https://www.ncbi.nlm.nih.gov/home/about/policies.shtml) is available.

About [text mining group](https://www.ncbi.nlm.nih.gov/research/bionlp/).

## For Research Use Only
The performance characteristics of this product have not been evaluated by the Food and Drug Administration and is not intended for commercial use or purposes beyond research use only. 

## Cite our work
Keenan, T.D*., Chen, Q*., Agrón, E., Tham, Y.C., Goh, J.H.L., Lei, X., Ng, Y.P., Liu, Y., Xu, X., Cheng, C.Y. and Bikbov, M.M., 2022. Deep Learning Automated Diagnosis and Quantitative Classification of Cataract Type and Severity. Ophthalmology.
