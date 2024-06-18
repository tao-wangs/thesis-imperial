import subprocess

if __name__ == '__main__':

    # Running experiments for MRF (DYNAMIC ANALYSIS)

    # Uncomment the evidence code from the runLBP function in BayesianAttackGraph.py

    # Experiment 1: 3 iterations for 25, 50, 100, 200 nodes

    # num_iterations = 3
    # p = 0.1

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/dynamic/3_iterations/25_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(25),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'dynamic']
    #         )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/dynamic/3_iterations/50_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(50),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'dynamic']
    #         )

    # max_subnets = 25
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/dynamic/3_iterations/100_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(100),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'dynamic']
    #         )
    
    # max_subnets = 12
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/dynamic/3_iterations/200_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(200),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'dynamic']
    #         )

    # Experiment 2: 5 iterations for 25, 50, 100, 200 nodes

    num_iterations = 5
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/5_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/5_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/5_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/5_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )


    # Experiment 3: 7 iterations for 25, 50, 100, 200 nodes

    num_iterations = 7
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/7_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/7_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/7_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/7_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )


    # Experiment 4: 10 iterations for 25, 50, 100, 200 nodes

    num_iterations = 10
    p = 0.1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/10_iterations/25_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(25),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/10_iterations/50_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(50),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )

    max_subnets = 25
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/10_iterations/100_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(100),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
    
    max_subnets = 12
        
    for num_subnets in range(1, max_subnets + 1):
            
        subprocess.run(
            ['python3', 
            'ClusteredBayesianAttackGraph.py', 
            '--output', 'mrf_eval/dynamic/10_iterations/200_times.txt', 
            '--num_subnets', str(num_subnets), 
            '--num_nodes', str(200),
            '--num_iterations', str(num_iterations),
            '--p', str(p),
            '--analysis_type', 'dynamic']
            )
        
    # # FINAL EXPERIMENT, VARYING P 

    # num_iterations = 5

    # # Experiment 1: 

    # p = 0.2

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.2/25_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(25),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.2/50_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(50),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )

    # max_subnets = 25
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.2/100_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(100),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
    
    # max_subnets = 12
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.2/200_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(200),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )

    # # Experiment 2: 5 iterations for 25, 50, 100, 200 nodes

    # p = 0.3

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.3/25_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(25),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.3/50_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(50),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )

    # max_subnets = 25
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.3/100_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(100),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
    
    # max_subnets = 12
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.3/200_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(200),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )


    # # Experiment 3: 7 iterations for 25, 50, 100, 200 nodes

    # p = 0.4

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.4/25_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(25),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.4/50_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(50),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )

    # max_subnets = 25
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.4/100_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(100),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
    
    # max_subnets = 12
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.4/200_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(200),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )


    # # Experiment 4: 

    # p = 0.5

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.5/25_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(25),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.5/50_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(50),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )

    # max_subnets = 25
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.5/100_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(100),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
    
    # max_subnets = 12
        
    # for num_subnets in range(1, max_subnets + 1):
            
    #     subprocess.run(
    #         ['python3', 
    #         'ClusteredBayesianAttackGraph.py', 
    #         '--output', 'mrf_eval/p/p_0.5/200_times.txt', 
    #         '--num_subnets', str(num_subnets), 
    #         '--num_nodes', str(200),
    #         '--num_iterations', str(num_iterations),
    #         '--p', str(p),
    #         '--analysis_type', 'static']
    #         )
    
    # print("All experiments completed.")