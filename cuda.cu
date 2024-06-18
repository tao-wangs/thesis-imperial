#include <cuda_runtime.h>
#include <vector>

__global__ void myKernel(int node) {
    // Example kernel work
}

// Launch n amount of kernels in parallel
for (int i = 0; i < numNodes; ++i) {
    if (dependencyCounts[i] == 0) {
        myKernel<<<1, 256, 0, streams[i]>>>(i);
        cudaEventRecord(events[i], streams[i]);
    }
}

int main() {
    // Example DAG represented with dependency counts and adjacency list
    std::vector<int> dependencyCounts = {0, 1, 1, 2}; // Number of dependencies for each node
    std::vector<std::vector<int>> dependents = {{1, 2}, {}, {}, {}}; // Nodes dependent on each node

    int numNodes = dependencyCounts.size();
    std::vector<cudaStream_t> streams(numNodes);
    std::vector<cudaEvent_t> events(numNodes);

    // Initialize streams and events
    for (int i = 0; i < numNodes; ++i) {
        cudaStreamCreate(&streams[i]);
        cudaEventCreate(&events[i]);
    }

    // Launch initial nodes with zero dependencies
    for (int i = 0; i < numNodes; ++i) {
        if (dependencyCounts[i] == 0) {
            myKernel<<<1, 256, 0, streams[i]>>>(i);
            cudaEventRecord(events[i], streams[i]);
        }
    }

    // Process nodes as their dependencies are resolved
    for (int i = 0; i < numNodes; ++i) {
        for (int dep : dependents[i]) {
            // Wait on the event in the dependent node's stream
            cudaStreamWaitEvent(streams[dep], events[i], 0);
            if (--dependencyCounts[dep] == 0) {
                // Dependencies resolved, launch the kernel
                myKernel<<<1, 256, 0, streams[dep]>>>(dep);
                cudaEventRecord(events[dep], streams[dep]);
            }
        }
    }

    // Synchronize all streams at the end
    for (int i = 0; i < numNodes; ++i) {
        cudaStreamSynchronize(streams[i]);
    }

    // Cleanup
    for (int i = 0; i < numNodes; ++i) {
        cudaStreamDestroy(streams[i]);
        cudaEventDestroy(events[i]);
    }

    return 0;
}


// Assume dependencyCounts and dependents are initialized appropriately
while (not all nodes processed) {
    for each node in DAG {
        if (node's dependencies are resolved and not yet processed) {
            Launch kernel for node in its stream
            Record event for node's completion
            Mark node as processed
        }
    }
    for each node in DAG {
        if (node's kernel was launched) {
            Wait for node's event to complete
            Update dependency counts of node's dependents
        }
    }
}

