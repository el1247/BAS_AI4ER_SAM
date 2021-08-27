# Notebooks
## Structure
Exploratory notebooks for initial explorations go into the `notebooks/exploratory` folder.
Polished work for reporting and demonstration purposes goes into `notebooks/reports`

## Naming convention
We use the following naming convention for notebooks (inspired by [cookiecutter-datascience](https://drivendata.github.io/cookiecutter-data-science/#notebooks-are-for-exploration-and-communication))
```<step>_<initials>_<description>.ipynb```

For example, for `Tom Baker Adams` a valid name would be `1.0_tba_data-analysis,ipynb`. 

## Useful initialization cell
To avoid having to reload the notebook when you change code from underlying imports, we recommend the following handy initialization cell for jupyter notebooks:
```
%load_ext autoreload             # loads the autoreload package into ipython kernel
%autoreload 2                    # sets autoreload mode to automatically reload modules when they change
%config IPCompleter.greedy=True  # enables tab completion
```


#NotebookGuide (Version numbers reflect key stages in notebooks development)
dj_gmmTemperatureProfileClassification.ipynb - Notebook made by Dan Jones detailing GMM modelling basics for temperature profiles
el_CMIP6DataAccess.ipynb - Notebook demonstrating principles for accessing CMMIP6 Data sets
el_CartpyTest.ipynb - Notebook demonstrating methods to use cartopy libary for orthographic plots
el_ESM3Analysis.ipynb - Notebook used to analyse ESM data set, looking at surface temperatures
el_ESM3AnalysisTemplate.ipynb - Template notebook for accessing and preparing ESM3 data to be manipulated
el_ESM3CalcFuncs.ipynb - Notebook containing various calculation and plotting functions used in the start of the project. This was not fully maintained and is incomplete.
el_ESM3SampleLoad.ipynb - Notebook used to download and save ESM sample data from a sample meta file made by el_GMMSampleCreator.ipynb
el_ESMClimatologySST.ipynb - Notebook containing climatology analysis of sea surface temperature data from ESM
el_ESMvsWOA.ipynb - Notebook comparing ESM sea surface temperature data with World Ocean Atlas data
el_GMMLoading.ipynb - Notebook containing GMM loading and saving code for future use
el_GMMSampleCreator.ipynb - Notebook used to generate random ESM meta data (lat, lon, time) with relevant distribution
el_GMMScalerSetup.ipynb - Notebook used to create scalers for GMM creation (not used in final notebooks)
el_GMMTemperatureProfileClassification.ipynb - Notebook used to create GMMs
el_SAMAnalysis.ipynb - Notebook used to calculate SAM index
el_TempMaskCreator.ipynb - Notebook used to create geographical mask to remove unwanted data points
el_TempProfile.ipynb - Notebook used to investigate temperature profiles for a latitude slice and single data points
el_UKESM1SampleLoad.ipynb - Notebook used to test random generation method for UKESM (counterpart of GMMSampleCreator)
el_maskTest.ipynb - Notebook used to load and verify geographical masks

Key Files:
2.0_el_TempMaskCreator.ipynb - Used to create OceanMaskVolcello, which was applied to UKESM data
OceanMaskVolcello - Mask containing valid geographical locations for temperature profiles at a depth of -2000m sea level
3.0_el_GMMTemperatureProfileClassification2_R1A.ipynb - First GMM creator, also generated GMM_UK_2Class_R1_Mask.npy from which all other 3.0_el_GMMTemperatureProfileClassification2_RxA.ipynb (x varies) import and copy.
GMM_UK_2Class_ [Scaler, PCA.pkl] files containing scaler and PCA for the associated GMM Created by 3.0_el_GMMTemperatureProfileClassification2_RxA.ipynb (x varies)
GMM_UK_2Class_ [covariances.npy, means.npy and weights.npy] files contain the GMM for the associated id (R1, R2, R3). Created by 3.0_el_GMMTemperatureProfileClassification2_RxA.ipynb (x varies)
3.1_el_GMMTemperatureProfileClassification2_RxB.ipynb (x varies) - Used to apply GMM to full data set, returns GMM_UK_2Class_Rx_MetaFull.
3.2_el_GMMTemperatureProfileClassification2_RxC.ipynb (x varies) - Applies analysis to GMM_UK_2Class_Rx_MetaFull, calculated mean Lat values and exports GMM_UK_2Class_Rx_LatMeans.npy
1.3_el_SAMAnalysis.ipynb - Imports various GMM_UK_2Class_Rx_LatMeans.npy and compares with SAM index.
SAMIndex.txt - Contains NCAR SAM index for 1957 - 2018