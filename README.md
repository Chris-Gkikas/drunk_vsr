# drunk_vsr
AFFECTS OF ALCOHOL ON ARTICULATED VISUAL SPEECH

# Set Up Instructions

0.. make sure you have [miniconda](https://docs.conda.io/en/latest/miniconda.html) (or [anaconda](https://docs.anaconda.com/anaconda/install/linux/)) installed

1.. open a terminal and cd to the preferred project download directory:
```bash
git clone https://github.com/Chris-Gkikas/drunk_vsr.git
```

2.. cd to project directory:
```bash
cd drunk_vsr/ytb_crawler     
```

3.. create new conda virtual env and install conda packages:
```bash
conda create --name drunk --file conda_requirements.txt    
```

4.. activate the newly created virtual environment:
```bash
conda activate drunk     
```

5.. fire it up
```bash
python ytb_crawler_v2.py
```

NOTES:
- in ytb_crawler/vids_n_trans directory, the X_not.txt indicates that the correspondent video (X.mp4) has no available transcript. :( 
