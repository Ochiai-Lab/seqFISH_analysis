# Introduction
aaa


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
Execute the following code to download the data:
```
zenodo_get --doi=10.5281/zenodo.10565509
unzip 0_raw_data.zip
rm 0_raw_data.zip
cd X2_jupyter_notebook
jupyter notebook
```

Double-click on 0_image_processing.ipynb to open the jupyter notebook.

After executing everything, close the jupyter notebook. Return to the terminal or Command Prompt and exit by pressing control + c, then execute the following:
```
conda deactivate
```

Next, use [cellpose-napari] for segmentation.
```
conda create -n cellpose_napari python=3.8
conda activate cellpose_napari
pip install "napari[all]"
pip install cellpose-napari 
pip install jupyter pyclesperanto_prototype
jupyter notebook
```

Double-click on 1_cellpose-napari.ipynb to open the jupyter notebook.

After completing all steps, close the jupyter notebook. Return to the terminal or Command Prompt and exit by pressing control + c, then execute the following:
```
conda deactivate
```

Next, use [big-fish] to detect spots on DNA, RNA-seqFISH images.
```
conda create -n bigfish_env python=3.8
conda activate bigfish_env
pip install big-fish "napari[all]" jupyter seaborn
python -m pip install cellpose
jupyter notebook
```

Double-click on 2_DNA-seqFISH_spot_detection.ipynb to open the jupyter notebook.
After completing all steps, close the jupyter notebook.
Double-click on 3_RNA-seqFISH_spot_detection.ipynb to open the jupyter notebook.
After completing all steps, close the jupyter notebook. Return to the terminal or Command Prompt and exit by pressing control + c, then execute the following:
```
conda deactivate
```

Next, use [jie] to select plausible spot regions from DNA-seqFISH spots.
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
Double-click on 4_seq-DNA_RNA_FISH_spots_asignment.ipynb.


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
