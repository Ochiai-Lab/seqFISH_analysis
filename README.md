# Introduction
Imaging-based spatial multi-omics technologies, including DNA-seqFISH+ developed by Long Cai's lab ([Takei et al., Nature, 2021](https://www.nature.com/articles/s41586-020-03126-2); [Takei et al., Science, 2021](https://www.science.org/doi/10.1126/science.abj1966)), enable the comprehensive analysis of higher-order genomic structures, gene transcription, and the localization of proteins and post-translational modifications at the single-allele level. These technologies provide unparalleled insights into biological phenomena such as the transcription machinery within cells and tissues. We have recently introduced an application of the seqFISH method to mouse embryonic stem cells, enabling detailed analysis of the spatial relationships between genomic loci, including enhancer-promoter (E-P) interactions, and uncovering the dynamics of protein accumulation at these loci during transcription at single-allele resolution ([Ohishi et al., 2023](https://www.biorxiv.org/content/10.1101/2023.11.27.568629v1)). This protocol offers a step-by-step guide for image analysis methods, utilizing images from our seqFISH experiments targeting the Nanog gene locus on chromosome 6 in mouse embryonic stem cells ([Ohishi et al., 2023](https://www.biorxiv.org/content/10.1101/2023.11.27.568629v1)). 


# Required Tools and Data
-   Scripts available from this github page. 
-   [Fiji]
-   [Anaconda]
-   [Git](https://github.com/git-guides/install-git)
-   [pyimagej]
-   [Maven]
-   [cellpose-napari]
-   [big-fish]
-   [jie]
-   Image files.
    -   See [our paper] for imaging conditions. Test data are available from : [https://zenodo.org/records/10565509]
    -   The "flat_field_image" folder contains images for flat image correction. The "raw data" folder includes seqFISH images, such as seqFISH_1_001.tif. The naming convention for these images is seqFISH_[position id]_[cycle id].tif, where each image is assigned an ID based on its field of view and cycle. Each image comprises data across 51 z-positions and 4 channels. Channels 1 to 4 correspond to fluorescence images excited by lasers at 647, 561, 488, and 405 nm, respectively.


# Usage
First, refer to the following link and install Fiji:
[https://imagej.net/software/fiji/downloads](https://imagej.net/software/fiji/downloads)

Refer to the following link to install Anaconda:
[https://www.anaconda.com/download](https://www.anaconda.com/download)

Refer to the following link to install Git:
[https://github.com/git-guides/install-git](https://github.com/git-guides/install-git)

## 1. Pre-processing of DNA/RNA/IF-seqFISH imaging data
Use the terminal or Command Prompt to execute the following code to download files from this GitHub page and use pyimageJ. Replace [desired path] with your chosen path.
```
cd [desired path]
git clone https://github.com/Ochiai-Lab/seqFISH_analysis_test.git
cd seqFISH_analysis_test
conda create -n pyimagej python=3.8 openjdk=11
conda activate pyimagej
```
Refer to the following link to manually install Maven:
[https://py.imagej.net/en/latest/Install.html](https://py.imagej.net/en/latest/Install.html)

Execute the following in the terminal or Command Prompt to install additional necessary packages.
```
pip install pyimagej jupyter zenodo_get
```

Downloading Sample Image Data Sample image data obtained by sequential DNA/RNA/IF-FISH is uploaded here:
[https://zenodo.org/records/10565509](https://zenodo.org/records/10565509)
To download the data, use the terminal or Command Prompt to execute the following code to perform the above tasks.
```
zenodo_get --doi=10.5281/zenodo.10565509
unzip 0_raw_data.zip
rm 0_raw_data.zip
cd X2_jupyter_notebook
jupyter notebook
```

The browser will automatically launch, making the Jupyter notebook accessible for viewing. On that page, double-click to open the file named "0_image_processing.ipynb" and then execute all the code.

After executing everything, close the jupyter notebook. Return to the terminal or Command Prompt and exit by pressing control + c, then execute the following:
```
conda deactivate
```

## 2. Nuclear segmentation of DNA/RNA/IF-seqFISH data
Next, use [cellpose-napari] for segmentation. Use the terminal or Command Prompt to execute the following code to perform the above tasks.
```
conda create -n cellpose_napari python=3.8
conda activate cellpose_napari
pip install "napari[all]"
pip install cellpose-napari 
pip install jupyter pyclesperanto_prototype
jupyter notebook
```

The browser will automatically launch, making the Jupyter dashboard accessible for viewing. On that page, double-click to open the file named "1_cellpose-napari.ipynb" and then execute all the code.

After completing all steps, close the jupyter notebook. Return to the terminal or Command Prompt and exit by pressing control + c, then execute the following:
```
conda deactivate
```

## 3. Detection of DNA-seqFISH spots
Next, use [big-fish] to detect spots on DNA-seqFISH images. Use the terminal or Command Prompt to execute the following code to perform the above tasks.
```
conda create -n bigfish_env python=3.8
conda activate bigfish_env
pip install big-fish "napari[all]" jupyter seaborn
pip install cellpose
jupyter notebook
```

The browser will automatically launch, making the Jupyter dashboard accessible for viewing. On that page, double-click to open the file named "2_DNA-seqFISH_spot_detection.ipynb" and then execute all the code.
After completing all steps, close the jupyter notebook.

## 4. Detection of RNA-seqFISH spots
Execute the following: Double-click on 3_RNA-seqFISH_spot_detection.ipynb on the Jupyter dashboard to open the jupyter notebook and then execute all the code.
After completing all steps, close the jupyter notebook. Return to the terminal or Command Prompt and exit by pressing control + c, then execute the following:
```
conda deactivate
```

## 5. Removal of false positives in DNA/RNA-seqFISH
Next, use [jie] to select plausible spot regions from DNA-seqFISH spots. Use the terminal or Command Prompt to execute the following code to perform the above tasks.
```
git clone https://github.com/b2jia/jie.git
cd jie
conda env create --name jie --file=environment.yml
conda activate jie
pip install -e .
pip install jupyter
cd ..
jupyter notebook
```
The browser will automatically launch, making the Jupyter dashboard accessible for viewing. On that page, double-click to open the file named "4_seq-DNA_RNA_FISH_spots_assignment.ipynb" and then execute all the code.

## 6. Detection of protein clusters from IF-seqFISH data
Next, use [big-fish] to detect protein clusters on IF-seqFISH images. Use the terminal or Command Prompt to execute the following code to perform the above tasks.
```
conda activate bigfish_env
jupyter notebook
```
The browser will automatically launch, making the Jupyter dashboard accessible for viewing. On that page, double-click to open the file named "5-IF-seqFISH_spot_detection.ipynb" and then execute all the code.


# Citation
[Ohishi, H. et al. Transcription-coupled changes in higher-order genomic structure and transcription hub viscosity prolong enhancer-promoter connectivity. bioRxiv (2023) doi:10.1101/2023.11.27.568629](https://www.biorxiv.org/content/10.1101/2023.11.27.568629v1.full)


# Contact
Hiroaki Ohishi, email : hohishi (at) bioreg dot kyushu-u dot ac dot jp
Hiroshi Ochiai, email : ochiai (at) bioreg dot kyushu-u dot ac dot jp


  [Fiji]: https://fiji.sc/
  [Anaconda]: https://www.anaconda.com/products/distribution
  [pyimagej]: https://github.com/imagej/pyimagej
  [Maven]: https://maven.apache.org
  [cellpose-napari]: https://github.com/MouseLand/cellpose-napari
  [big-fish]: https://github.com/fish-quant/big-fish
  [jie]: https://github.com/b2jia/jie
  [our paper]: https://www.biorxiv.org/content/10.1101/2023.11.27.568629v1.full
  [https://zenodo.org/records/10565509]: https://zenodo.org/records/10565509
