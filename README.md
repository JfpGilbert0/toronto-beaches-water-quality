# toronto ferry tickets
 

# Toronto Beaches Water Quality Analysis

This project analyzes E. coli levels at Toronto beaches using historical data. The analysis aims to identify temporal patterns in contamination to inform public health and beach management decisions.

## Project Structure

The project is organized into the following directories and files:

```
.
├── code/                      # Contains all Python scripts used for data processing, cleaning, analysis, and visualization.
│   ├── model_generation/      # Subdirectory with scripts for generating tables and visualizations used in the analysis.
│
├── data/                      # Contains datasets used in the project.
│   ├── raw_data/              # Subdirectory for storing raw, unprocessed data files.
│   └── cleaned_data/          # Subdirectory for storing cleaned and preprocessed data ready for analysis.
│
├── results/                   # Contains results generated from the analysis, including figures, tables, and reports.
│   ├── figures/               # Subdirectory for all generated plots and figures used in reports and presentations.
│   ├── tables/                # Subdirectory for summary tables and data analysis results.
│   └── reports/               # Directory for compiled reports or final outputs from the analysis.
│
│
├── README.md                  # Project description and structure documentation.
```

## How to Run the Analysis

0. **Install dependancies**: Using th `requirements.txt` file install all dependancies by inputting the following code into terminal: `pip install -r requirements.txt`. Be sure to be in a virtual enviroment to avoid changing your devices core enviroment.

1. **Data Preparation**: Ensure all raw data files are placed in the `data/raw_data/` directory. Run the relevant script in the `code/` directory to clean and preprocess the data, which will be saved in the `cleaned_data/` folder.

2. **Main Analysis**: Run the Quarto paper.qmd file to run the model generation scripts. If singular models wnt to be run be sure to remove `"../"` from all dirctories in python scripts.

3. **Output**: Results, including figures and summary tables, are saved in the `results/` directory under `figures/` and `tables/`, respectively.


## Additional Information

- **GitHub Repository**: The code and data are available at [GitHub](https://github.com/JfpGilbert0/toronto-beaches-water-quality).
- **License**: This project is open-source and available under the MIT License.

## Acknowledgements

- Data provided by Open Data Toronto.
- Analysis tools utilized include Python, Pandas, NumPy, Matplotlib, Seaborn, and Quarto for document compilation.

---

