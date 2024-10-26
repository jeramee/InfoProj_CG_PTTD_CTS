# Informatics Project for Cancer Genomics, Predictive Targeted Therapy Design, and Clinical Trials Simulation

## Project Overview

This project integrates bioinformatics, cheminformatics, and machine learning tools to support cancer genomics research, particularly focused on targeted therapy drug discovery and clinical trials for ALK-related cancers. While optimized for ALK, the system is adaptable to a broad range of cancer types. The core of the system includes gene expression analysis, epigenetic profiling, prediction of therapy-targeted genes, and the Clinical Trials Simulation System (CTSS), which models clinical trial designs to optimize statistical power and improve patient outcomes.

## Key Features

- **Gene Expression Analysis**: Identifies critical pathways by analyzing gene expression data.
- **Epigenetic Profiling**: Examines histone modifications and chromatin structures to understand cancer progression.
- **Therapy-Targeted Gene Prediction**: Uses machine learning to suggest compounds effective against specific genetic traits.
- **Clinical Trials Simulation System (CTSS)**: Models clinical trials, optimizing sample size, patient compliance, and statistical analyses.

## cbio_ml_pl: Machine Learning Pipeline for Targeted Therapy Prediction

The `cbio_ml_pl` pipeline is a specialized machine learning component within this project. It is designed for targeted drug discovery and is optimized for ALK-driven cancers, though it can be adapted for other cancer types.

- **Data Integration**: Combines bioinformatics and cheminformatics data, including mutation profiles, drug-target interactions, and pathway analyses.
- **Predictive Modeling**: Uses AI to predict therapies suited to individual genetic profiles.
- **Clinical Trial Optimization**: Simulates patient cohort selection and statistical methods for optimized trial outcomes.

## Download Options

- **Complete Project Download**: Includes `cbio_ml_pl`, data sources, and additional tools.
- **Standalone Download of `cbio_ml_pl`**: Allows for independent use of the machine learning pipeline.

## Recommended Data Sources for ALK Targeted Therapy Prediction

### Chemical Data

- **Compound Libraries**:
  - **ChEMBL**: Provides bioactivity data for ALK inhibitors and similar compounds.
  - **ZINC Database**: Contains purchasable compound structures, ideal for virtual screening against ALK targets.
  - **PubChem**: Rich in assay data, essential for evaluating compound effectiveness against ALK-driven pathways.

- **Drug-Target Interaction Data**:
  - **BindingDB**: Contains data on ALK inhibitors’ binding affinities, useful for comparing potential candidates.
  - **DrugBank**: Offers drug, target, and mechanism information, which is key for understanding ALK-targeted therapy mechanisms.

- **Pharmacokinetics and Toxicity Profiles**:
  - **ADMET databases** like **ADMETlab**: Crucial for evaluating the toxicity and metabolism of candidate drugs.

### Genomic Data

- **ALK Mutation and Expression Data**:
  - **The Cancer Genome Atlas (TCGA)**: Offers a comprehensive dataset on ALK mutations and expression, especially relevant to non-small cell lung cancer (NSCLC).
  - **CCLE (Cancer Cell Line Encyclopedia)**: Contains mutation data for cell lines, providing insights into drug efficacy.

- **RNA-Seq and Gene Expression**:
  - **GEO (Gene Expression Omnibus)**: Vital for expression profiling, helping to identify upregulated ALK pathways in cancer.
  - **GTEx (Genotype-Tissue Expression)**: Useful for comparing ALK expression in normal vs. cancerous tissues.

- **Protein Interaction Data**:
  - **STRING Database**: Essential for understanding how ALK mutations influence downstream signaling pathways and interact with other proteins.
  - **Human Protein Atlas**: Contains expression and localization data, important for refining drug targeting.

- **ALK Fusions and Structural Variants**:
  - **ICGC (International Cancer Genome Consortium)**: Provides fusion and rearrangement data, including EML4-ALK fusions, common in NSCLC.
  - **COSMIC (Catalogue of Somatic Mutations in Cancer)**: Aggregates specific ALK mutations that impact drug efficacy.

- **Pathway Data**:
  - **KEGG and Reactome**: Catalog pathways activated by ALK, helping to map potential compensatory mechanisms and resistance pathways.

### Suggested Integration Strategy

Combining these datasets in a predictive model can enhance drug prediction accuracy:

1. **Screening Compounds** against known ALK mutations and expression data.
2. **Assessing Drug Efficacy** by analyzing target binding affinities from BindingDB and DrugBank.
3. **Evaluating Toxicity** with ADMET profiles to ensure candidate drugs have favorable safety profiles.
4. **Incorporating Mutation and Expression Data** from TCGA and COSMIC for predictive modeling on patient responses.

Together, these data sources create a solid foundation for machine learning and cheminformatics analyses aimed at identifying, ranking, and predicting the efficacy of ALK-targeted therapies. This integration also enables customization for specific mutations, fusion variants, and expression profiles found in ALK-related cancers.

## Key Features

### 1. Clinical Trials Simulation System (CTSS)

- Simulates clinical trial designs with a focus on:
  - **Sample Size Determination**
  - **Patient Dropout Modeling**
  - **Compliance Tracking**
  - **Statistical Test Comparisons**
  
- CTSS helps researchers simulate hypothetical trials to optimize costs, duration, and statistical power, primarily for Phase II/III trials and specific Phase I designs.

### 2. Genome Research for Epigenetic Profiling

- Studies histone methylation (H3K27me3, H3K9me3) and chromatin domains (BGRDs) to understand gene regulation, tumor suppression, and cancer progression.
  
- Utilizes:
  - **ChIP-Seq** for histone modification analysis
  - **CRISPR-Cas9 screening** for targeted gene disruptions
  - **RNA-Seq** to investigate gene expression differences between cancer and control samples.

### 3. Bioinformatics and Informatics Analysis

- Uses advanced tools to analyze gene expression, chromatin, and other genomic data to identify cancer drivers and potential therapeutic targets.
  
- Includes:
  - **KEGG Pathway and Enrichment Analysis**
  - **Visualization of Genome-Wide Data**
  - **Machine Learning Models** for drug response prediction.

### 4. Modular Python Structure

- The project’s modular structure allows flexible analysis and easy expansion:
  - Modules focus on tasks like loading genomic data, parsing clinical trial parameters, and machine learning predictions on therapy targets.

## Directory Structure

```plaintext
/informatics_project
    ├── data/
    │   └── text_input/
    │       ├── control_genes.txt
    │       ├── down_genes.txt
    │       ├── up_genes.txt
    │       ├── regionsToGenes.xls
    │       ├── mm9.20150218.knownGene.xls
    │       ├── up_genes.txt.regionsToGenes.xls.100.10.1000.cumulative.txt
    ├── modules/
    │   ├── bioinformatics.py
    │   ├── cheminformatics.py
    │   └── machine_learning.py
    ├── simulation/
    │   ├── ctss_simulation.py
    │   ├── genome_cancer_analysis.py
    │   ├── informatics_analysis.py
    │   └── random_forest_classifier.py
    ├── informatics_controller.py
    ├── main.py
    └── parse_test_input.py
```
## Research Context and Goals

### Histone Methylation & Chromatin Domains

This project focuses on the analysis of broad repressive chromatin domains (e.g., H3K27me3) that are critical in the regulation of oncogenes and tumor suppressor genes. These chromatin features provide insights into cancer progression and gene silencing mechanisms.

### Cancer Genomics & Targeted Therapy

The system integrates CRISPR-Cas9 screening, RNA-Seq, and pathway analysis to study the roles of long non-coding RNAs (lncRNAs) such as HOTAIR and SChLAP1. These lncRNAs are key regulators of chromatin structure and gene expression, driving cancer progression.

### Clinical Trials Simulation

The CTSS models patient behavior (dropouts, compliance, etc.) and responses to treatment in clinical trials. By simulating different trial configurations, researchers can optimize trial designs for drugs targeting specific cancer mutations, improving both efficacy and efficiency.

## Installation and Setup

### Prerequisites

- **Python 3.8+**
- **Required libraries:**

    Install with Conda (recommended):

    ```bash
    conda install pandas numpy scikit-learn gseapy matplotlib openpyxl xlrd
    conda install -c conda-forge biopython lifelines
    ```

### Environment Setup

### 1. Clone the Repository and Set Up the Conda Environment

```bash
git clone <repository-url>
cd InfoProj_CG_PTTD_CTS
conda create -n informatics_env python=3.8
conda activate informatics_env
```

## Research Context and Goals

### Histone Methylation & Chromatin Domains

This project focuses on the analysis of broad repressive chromatin domains (e.g., H3K27me3) that are critical in the regulation of oncogenes and tumor suppressor genes. These chromatin features provide insights into cancer progression and gene silencing mechanisms.

### Cancer Genomics & Targeted Therapy

The system integrates CRISPR-Cas9 screening, RNA-Seq, and pathway analysis to study the roles of long non-coding RNAs (lncRNAs) such as HOTAIR and SChLAP1. These lncRNAs are key regulators of chromatin structure and gene expression, driving cancer progression.

### Clinical Trials Simulation

The CTSS models patient behavior (dropouts, compliance, etc.) and responses to treatment in clinical trials. By simulating different trial configurations, researchers can optimize trial designs for drugs targeting specific cancer mutations, improving both efficacy and efficiency.

## Installation and Setup

### Prerequisites

- **Python 3.8+**
- **Required libraries:**

  - Install with Conda (recommended):

    ```bash
    conda install pandas numpy scikit-learn gseapy matplotlib openpyxl xlrd
    conda install -c conda-forge biopython lifelines
    ```

### Environment Setup

1. Clone the repository and set up a Conda environment:

    ```bash
    git clone <repository-url>
    cd InfoProj_CG_PTTD_CTS
    conda create -n informatics_env python=3.8
    conda activate informatics_env
    ```

2. Install the required dependencies:
    ```bash
    conda install pandas numpy scikit-learn gseapy matplotlib openpyxl xlrd
    conda install -c conda-forge biopython lifelines
    ```

## Usage

### Parsing Test Input Files

Run `parse_test_input.py` to parse gene, genomic, and clinical trial parameter files located in `/data/text_input`:

```bash
python parse_test_input.py
```

### Usage

This script loads `.txt` and `.xls` files, prints their contents, and checks for supported file formats.

### Running Analysis and Simulations

- **Main Workflow Controller**: Run the main analysis workflows combining cheminformatics, bioinformatics, and machine learning tasks:

    ```bash
    python main.py
    ```

- **Clinical Trials Simulation (CTSS)**: Simulate clinical trial outcomes, model patient responses, and analyze statistical test results:

    ```bash
    python simulation/ctss_simulation.py
    ```

- **Cancer Genomics Analysis**: Run genome-wide analysis, including ChIP-Seq and RNA-Seq data for cancer research:

    ```bash
    python simulation/genome_cancer_analysis.py
    ```

### Customization Options

Researchers can modify trial parameters, statistical models, or analysis features in each module. For example, the CTSS module allows dynamic modification of sample sizes, treatment group allocations, and statistical tests to suit specific clinical trial designs.

### Troubleshooting

- **Excel File Errors**:
    - Ensure Excel files are not corrupted. The script uses `openpyxl` for `.xlsx` and `xlrd` for `.xls`. It attempts to load files as TSV if unsupported format errors occur.
- **Missing Files**:
    - Ensure that the required `.txt` and `.xls` files are placed in the `/data/text_input` directory.

### Research Applications

- **Pharmaceuticals**:
    - Simulate trial designs for new drug treatments, optimizing cost and trial efficiency.
- **Genome Analysis**:
    - Analyze histone modifications, chromatin domains, and gene expression for cancer studies.
- **Personalized Medicine**:
    - Identify patient-specific biomarkers and therapy targets, tailoring treatments based on genomic profiles.

### Alternate Setup for the Environment

1. Clone the repository:
    ```bash
    git clone https://github.com/jeramee/InfoProj_CG_PTTD_CTS.git
    cd InfoProj_CG_PTTD_CTS
    ```

2. Create the Conda environment using the `myenv.yml` file:
    ```bash
    conda env create -f myenv.yml
    ```

3. Activate the environment:
    ```bash
    conda activate myenv
    ```

4. Verify the installation:
    ```bash
    conda list
    ```

This setup ensures anyone cloning the repository can recreate the environment exactly as intended using the `myenv.yml` file.

### License

This project is licensed under the MIT License.
