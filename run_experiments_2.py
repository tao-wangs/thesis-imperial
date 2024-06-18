import subprocess
        
if __name__ == '__main__':

    # Now I am doing Max-Product LBP.

    # Experiment 1: 3 iterations for 25, 50, 100, 200 nodes

    num_iterations = 5
    max_pa = 1

    max_subnets = 100 

    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_1/25_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(25),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_1/50_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(50),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )
        
    max_subnets = 25
    
    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_1/100_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(100),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )
        
    max_subnets = 12
    
    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_1/200_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(200),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )

    print("All experiments completed.")

    # Experiment 2: 5 iterations for 25, 50, 100, 200 nodes

    num_iterations = 5
    max_pa = 5

    max_subnets = 100 

    for num_subnets in range(89, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_5/25_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(25),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )
        
    max_subnets = 50
    
    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_5/25_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(50),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )
        
    max_subnets = 25
    
    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_5/100_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(100),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )
        
    max_subnets = 12
    
    for num_subnets in range(1, max_subnets + 1):

        subprocess.run(
                ['python3', 
                'CompositionalAnalysis.py', 
                '--output', 'max_parents_5/200_comp_times.txt', 
                '--num_subnets', str(num_subnets), 
                '--num_nodes', str(200),
                '--num_iterations', str(num_iterations),
                '--max_pa', str(max_pa)]
                )

    print("All experiments completed.")

    # Experiment 3: 7 iterations for 25, 50, 100, 200 nodes

    # num_iterations = 7

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '7_iterations/dynamic_25_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(25),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '7_iterations/dynamic_50_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(50),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )
        
    # max_subnets = 25
    
    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '7_iterations/dynamic_100_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(100),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )
        
    # max_subnets = 12
    
    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '7_iterations/dynamic_200_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(200),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )

    # print("All experiments completed.")

    # # Experiment 4: 10 iterations for 25, 50, 100, 200 nodes

    # num_iterations = 10

    # max_subnets = 100 

    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '10_iterations/dynamic_25_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(25),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )
        
    # max_subnets = 50
    
    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '10_iterations/dynamic_50_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(50),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )
        
    # max_subnets = 25
    
    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '10_iterations/dynamic_100_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(100),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )
        
    # max_subnets = 12
    
    # for num_subnets in range(1, max_subnets + 1):

    #     subprocess.run(
    #             ['python3', 
    #             'CompositionalAnalysis.py', 
    #             '--output', '10_iterations/dynamic_200_times.txt', 
    #             '--num_subnets', str(num_subnets), 
    #             '--num_nodes', str(200),
    #             '--num_iterations', str(num_iterations),
    #             '--max_pa', str(max_pa)]
    #             )

    # print("All experiments completed.")