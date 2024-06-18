import numpy as np

# THOUGHT: Consider replacing CVSS with an alternative security risk measure, for reasons in my notes

#Distribution of CVSS scores (OUTDATED)
# 0-1   50      0.10
# 1-2 	518 	0.70
# 2-3 	2855 	4.10
# 3-4 	1565 	2.30
# 4-5 	13469 	19.40
# 5-6 	14320 	20.70
# 6-7 	8218 	11.90
# 7-8 	18258 	26.40
# 8-9 	278 	0.40
# 9-10 	9721 	14.00 

#Distribution of CVSS scores (AS OF 27/11/23)
# 0-1   315     0.19
# 1-2 	208 	0.13
# 2-3 	1032 	0.63
# 3-4 	2128 	1.30
# 4-5 	14381 	8.77
# 5-6 	27255 	16.61
# 6-7 	26595 	16.21
# 7-8 	41704 	25.42
# 8-9 	18954 	11.55
# 9-10 	31477 	19.19

def draw_random_CVSS(n):
    """
    Randomly samples CVSS scores from the distribution of CVSS scores and normalises them to [0, 1]. 
    """
    # Define the distribution of CVSS scores
    perc = np.array([0.19, 0.13, 0.63, 1.30, 8.77, 16.61, 16.21, 25.42, 11.55, 19.19]) / 100

    # Values of CVSS scores
    vals = np.array([0.05, 0.15, 0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95])
    
    probs = np.zeros(n)
    
    for i in range(n):
        r = np.random.multinomial(1, perc)
        c = np.where(r == 1)[0][0]
        probs[i] = vals[c]
    
    return probs

if __name__ == '__main__':
    # Example usage:
    num_samples = 10  # Number of CVSS scores to generate
    result = draw_random_CVSS(num_samples)

    # Printing the generated CVSS scores
    print("Generated CVSS Scores:", result)
