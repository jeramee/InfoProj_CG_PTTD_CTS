# informatics_controller.py

from modules.cheminformatics import Cheminformatics
from modules.bioinformatics import Bioinformatics
from modules.machine_learning import MachineLearning
from modules.cbio_mod import (
    getAllStudies,
    getAllCancerTypes,
    getAllClinicalDataInStudy
)
from simulation.ctss_simulation import run_simulations
from simulation.genome_cancer_analysis import load_chip_seq_data, process_genomic_sequences, random_forest_classifier
from simulation.informatics_analysis import perform_gsea, logistic_regression
import pandas as pd
from sklearn.model_selection import train_test_split

class InformaticsController:
    """
    Informatics Controller Class

    Recommended Data Sources for ALK Targeted Therapy Prediction:
    - **Chemical Data**:
        - Compound Libraries: ChEMBL, ZINC Database, PubChem.
        - Drug-Target Interaction Data: BindingDB, DrugBank.
        - Pharmacokinetics and Toxicity Profiles: ADMET databases like ADMETlab.

    - **Genomic Data**:
        - ALK Mutation and Expression Data: TCGA, CCLE.
        - RNA-Seq and Gene Expression: GEO, GTEx.
        - Protein Interaction Data: STRING Database, Human Protein Atlas.
        - ALK Fusions and Structural Variants: ICGC, COSMIC.
        - Pathway Data: KEGG, Reactome.

    Suggested Integration Strategy:
    - Screen compounds against known ALK mutations and expression data.
    - Assess drug efficacy by analyzing target binding affinities.
    - Evaluate toxicity using ADMET profiles for favorable safety profiles.
    - Incorporate mutation and expression data for patient-specific response predictions.
    
    This information supports machine learning and cheminformatics analyses in the project.
    """
    def __init__(self):
        """
        Initializes the controller by creating instances of the relevant analysis modules.
        """
        self.cheminformatics = Cheminformatics()
        self.bioinformatics = Bioinformatics()
        self.ml = MachineLearning()
        self.ipr_conn = IprConnection(username="user", password="pass", url="https://iprstaging-api.bcgsc.ca/api")  # Replace with real credentials

    def run_analysis(self, molecule, fasta_file, data):
        """
        This function combines various types of analyses. It performs cheminformatics analysis
        on molecular data, bioinformatics analysis on genomic sequences, and machine learning
        predictions on data.

        Args:
            molecule (str): Molecule identifier or data for cheminformatics analysis.
            fasta_file (str): Path to the FASTA file for bioinformatics analysis.
            data (str): Data used for machine learning predictions (e.g., genomic features).
        
        Returns:
            dict: A dictionary containing the results of each analysis type.
        """
        # Cheminformatics Analysis
        struct_result = self.cheminformatics.analyze_structure(molecule)
        
        # Bioinformatics Analysis
        genome_result = self.bioinformatics.analyze_genome(fasta_file)
        
        # Machine Learning Prediction
        ml_result = self.ml.predict_drug_target(data)

        return {
            "structure": struct_result,
            "genome": genome_result,
            "prediction": ml_result
        }

    def run_simulation_tests(self):
        """
        This function runs a suite of tests and simulations, including CTSS clinical trial simulations,
        genome analysis, gene set enrichment analysis (GSEA), and logistic regression modeling.
        """
        # 1. Run Clinical Trial Simulation
        print("Running CTSS Simulation...")
        results = run_simulations(num_trials=1000, sample_size=200, effect_size=0.5, dropout_rate=0.1)
        print("CTSS Results:", results.head())

        # 2. Genome and Cancer Analysis
        print("Running Genome and Cancer Analysis...")
        load_chip_seq_data("data/fake_data/chip_seq_peaks.csv")
        process_genomic_sequences("data/fake_data/genome.fa")

        X = pd.read_csv("data/fake_data/genomic_features.csv")
        y = pd.read_csv("data/fake_data/cancer_outcomes.csv")
        
        # Run Random Forest Classifier
        random_forest_classifier(X_train=X, y_train=y, X_test=X, y_test=y)

        # 3. Perform GSEA (Gene Set Enrichment Analysis)
        print("Running GSEA Analysis...")
        expression_data = pd.read_csv("data/fake_data/gene_expression.csv")
        perform_gsea(expression_data)

        # 4. Logistic Regression on Genomic Pathways
        print("Running Logistic Regression Analysis...")
        X = pd.read_csv("data/fake_data/pathway_features.csv")
        y = pd.read_csv("data/fake_data/outcomes.csv")

        # Ensure that both gene expression data and outcomes have the same sample sizes
        if expression_data.shape[0] == y.shape[0]:
            X_train, X_test, y_train, y_test = train_test_split(expression_data, y, test_size=0.3, random_state=42, stratify=y)
            if len(y_train['outcome'].unique()) > 1 and len(y_test['outcome'].unique()) > 1:
                logistic_regression(X_train, y_train, X_test, y_test)
            else:
                print("Error: Train or test set has only one class, logistic regression cannot proceed.")
        else:
            print("Error: Gene expression data and outcomes have different sample sizes.")

    # New method to fetch study information
    def fetch_study_data(self):
        studies = getAllStudies()
        print("Available Studies:", studies)

    # New method to fetch cancer types
    def fetch_cancer_types(self):
        cancer_types = getAllCancerTypes()
        print("Cancer Types:", cancer_types)

    # New method to fetch clinical data for a given study
    def fetch_clinical_data(self, study_id):
        clinical_data = getAllClinicalDataInStudy(study_id)
        print(f"Clinical Data for Study {study_id}:", clinical_data)
        
    def load_expression_data(self, filename):
        return load_zscore_data(filename)

    def generate_expression_density_plot(self, expression_df, sample_id, gene, plot_name):
        plot_expression_density(expression_df, sample_id, gene, plot_name)

    def upload_density_plots(self, expression_df, sample_id, content):
        upload_expression_density_plots(self.ipr_conn, expression_df, sample_id, content)