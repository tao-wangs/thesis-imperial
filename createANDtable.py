import numpy as np

def create_AND_table(probs):
    if not probs:
        return np.array([[0, 1]])
    else:
        npa = len(probs)
        cpt = np.zeros((2, 2 ** npa))
        cpt[1, -1] = np.prod(probs)
        cpt[0, :] = 1 - cpt[1, :]
        
        return cpt.T

if __name__ == '__main__':
    # Example usage:
    probabilities = [0.7, 0.8]  # Example probabilities
    result_table = create_AND_table(probabilities)

    # Printing the resulting table
    print(result_table)