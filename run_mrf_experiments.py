import subprocess

if __name__ == '__main__':

    # Running experiments for MRF 

    # Experiment 1: 3 iterations for 25, 50, 100, 200 nodes

    num_iterations = 3
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/3_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/3_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/3_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/3_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )

    # Experiment 2: 5 iterations for 25, 50, 100, 200 nodes

    num_iterations = 5
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/5_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/5_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/5_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/5_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )


    # Experiment 3: 7 iterations for 25, 50, 100, 200 nodes

    num_iterations = 7
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/7_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/7_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/7_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/7_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )


    # Experiment 1: 10 iterations for 25, 50, 100, 200 nodes

    num_iterations = 10
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/10_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/10_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/10_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/10_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p)]
            )
