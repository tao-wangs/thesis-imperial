import subprocess
import argparse

def run_experiment(output_file, num_nodes, max_subnets, num_iterations, max_pa):

    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
            ['python3', 
             'CompositionalAnalysis.py', 
             '--output', output_file, 
             '--num_subnets', str(num_subnets), 
             '--num_nodes', str(num_nodes),
             '--num_iterations', str(num_iterations),
             '--max_pa', str(max_pa)]
            )
        
    print("All experiments completed.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run experiments for Compositional Analysis of Bayesian Attack Graphs.')

    parser.add_argument('--output', type=str, help='Output file for the analysis.')
    parser.add_argument('--num_nodes', type=int, help='Number of nodes in the network.')
    parser.add_argument('--max_subnets', type=int, help='Maximum number of subnetworks in the network.')
    parser.add_argument('--num_iterations', type=int, help='Number of iterations for the analysis.')
    parser.add_argument('--max_pa', type=int, help='Maximum number of parents allowed per node.')

    args = parser.parse_args()

    output_path = args.output 
    num_nodes = args.num_nodes
    max_subnets = args.max_subnets
    num_iterations = args.num_iterations
    max_pa = args.max_pa

    run_experiment(output_path, num_nodes, max_subnets, num_iterations, max_pa)
