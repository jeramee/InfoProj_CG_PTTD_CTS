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

if __name__ == "__main__":
    main()
