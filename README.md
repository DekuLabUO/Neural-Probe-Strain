# Finite Element Modeling and Regression Analysis of Neural Probe Strain

This repository contains curated production files used to support a journal submission on finite element modeling of tissue strain around neural microelectrode geometries. It is intended as a compact reproducibility package rather than a complete working history of the manuscript.

## Repository contents

- `FE_Model_MEA_Geometries.mph` - COMSOL Multiphysics model file for the microelectrode array geometries.
- `Regression Model and Least Square Mean Analysis of Combination Effects.jrp` - JMP project containing the regression model and least-squares mean analysis.
- `Dataset/` - Excel workbooks used for figure generation and strain-profile analysis.
- `Scripts/` - Python plotting scripts used to reproduce selected manuscript figures.
- `Images/` - final figure panels and exported figure files included for reference.

## Figure and script naming

Figure files and related scripts use concise GitHub-friendly names while preserving the manuscript figure numbers.

| Figure | Output file or folder | Matching script location |
| --- | --- | --- |
| Figure 1 | `Images/Figure1_MEA_Geometry.png` and `Images/Figure1_MEA_Geometry.pdf` | COMSOL model source: `FE_Model_MEA_Geometries.mph` |
| Figure 2 | `Images/Figure2_Regression_Validation.png` | JMP project source: `Regression Model and Least Square Mean Analysis of Combination Effects.jrp` |
| Figure 3 | `Images/Figure3_LSMean_Strain.pdf` | `Scripts/Figure3_LSMean_Strain.py` |
| Figure 4 | `Images/Figure4_TwoWay_Interaction.pdf` | `Scripts/Figure4_TwoWay_Interaction.py` |
| Figure 5 | `Images/Figure5_ThreeWay_Interaction.pdf` | `Scripts/Figure5_ThreeWay_Interaction.py` |
| Figure 6 | `Images/Figure6_FourWay_Interaction.pdf` | `Scripts/Figure6_FourWay_Interaction.py` |
| Figure 7 | `Images/Figure7_LongThin_Device/` | `Scripts/Figure7_LongThin_Device/` |
| Figure 8 | `Images/Figure8_ShortWide_Device/` | `Scripts/Figure8_ShortWide_Device/` |

The Figure 7 and Figure 8 folders contain separate PDF panels for the 3D volumetric strain distribution, equivalent strain profiles, average-strain heatmap, and quantitative comparison.

## Data files

The `Dataset/` directory includes the tabular files distributed with this submission package:

- `LongTryDiffCutline.xlsx`
- `MichiganData-45.xlsx`
- `NeuropixelData-45.xlsx`
- `TipMidTop.xlsx`
- `TipMidTop_Long.xlsx`
- `TipOnly.xlsx`

These files contain exported finite element or post-processed strain data used by the figure scripts and statistical workflow.

## Software requirements

The Python plotting scripts were prepared for Python 3 and use common scientific Python packages:

```bash
pip install -r requirements.txt
```

Core Python dependencies are listed in `requirements.txt`. The COMSOL model requires COMSOL Multiphysics, and the regression project requires JMP or compatible JMP project support.

## Reproduction workflow

1. Open `FE_Model_MEA_Geometries.mph` in COMSOL Multiphysics to review the finite element model setup.
2. Use the exported workbooks in `Dataset/` as the source data for post-processing and figure reproduction.
3. Run the relevant Python script from `Scripts/` to regenerate a figure panel. For example:

```bash
python "Scripts/Figure5_ThreeWay_Interaction.py"
```

4. Review the corresponding exported figures in `Images/`.
5. Open `Regression Model and Least Square Mean Analysis of Combination Effects.jrp` in JMP to inspect the regression model and least-squares mean analysis.

## Important reproducibility notes

- The scripts are preserved as production plotting scripts and have not been modified in this repository cleanup.
- Several scripts contain absolute local file paths from the original analysis environment. To rerun them on another computer, update those input paths to point to the corresponding files in `Dataset/`.
- A few scripts expect `.csv` input filenames while the distributed datasets are provided as `.xlsx` workbooks. Export the relevant Excel sheets to CSV or update the script input line before rerunning.
- Running scripts may write new `.png` or `.pdf` outputs into the current working directory. The final curated outputs are already provided in `Images/`.
- File and folder names were shortened for GitHub readability while preserving manuscript figure numbering.

## Suggested citation

If using this repository, cite the associated journal article once published. Until publication, cite this repository as the reproducibility package for the submitted manuscript.

## License

No license file is currently included. Reuse permissions should be confirmed with the manuscript authors before redistribution or derivative use.
