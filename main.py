# main.py

from informatics_controller import InformaticsController

def main():
    """
    Main entry point for running the bioinformatics, cheminformatics, and machine learning tasks.
    Users can run different analyses by passing different datasets to the controller.
    """
    # Initialize the controller
    controller = InformaticsController()

    # Example: Running combined cheminformatics, bioinformatics, and machine learning analysis
    molecule = "Example Molecule"
    fasta_file = "data/fake_data/genome.fa"
    ml_data = "data/fake_data/genomic_features.csv"

    print("Running combined analysis...")
    results = controller.run_analysis(molecule, fasta_file, ml_data)

    print("Analysis Results:")
    print(f"Structure Analysis: {results['structure']}")
    print(f"Genome Analysis: {results['genome']}")
    print(f"Machine Learning Prediction: {results['prediction']}")

    # Run the full set of simulations and analyses
    print("\nRunning simulation tests...")
    controller.run_simulation_tests()
    
    # Fetch and display data from cBioPortal
    print("\nFetching study data...")
    controller.fetch_study_data()

    print("\nFetching cancer types...")
    controller.fetch_cancer_types()

    # Replace "example_study_id" with a valid study ID
    print("\nFetching clinical data for a specific study...")
    controller.fetch_clinical_data("example_study_id")
    
    # Expression data handling
    expression_file = "data/fake_data/data_RNA_Seq_v2_mRNA_median_all_sample_Zscores.txt"
    expression_df = controller.load_expression_data(expression_file)
    
    # Generate and upload density plots for a specific gene
    sample_id = "sample_01"
    gene = "TP53"
    plot_name = f"output/{gene}_density_plot.png"
    controller.generate_expression_density_plot(expression_df, sample_id, gene, plot_name)
    print(f"Density plot saved at {plot_name}")
    
    # Upload plots
    content = {'kbMatches': [], 'expressionVariants': [{'key': gene, 'gene': gene}], 'ident': "example_report"}
    controller.upload_density_plots(expression_df, sample_id, content)
    print("Expression density plots uploaded.")

if __name__ == "__main__":
    main()
