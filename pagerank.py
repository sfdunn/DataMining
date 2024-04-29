import json

def load_adjacency_list():
    json_file_path = 'edges.json'
    with open(json_file_path, 'r') as json_file:
        adjacency_list = json.load(json_file)
    # Convert string keys back to integers if necessary
    adjacency_list = {int(k): v for k, v in adjacency_list.items()}
    return adjacency_list

#Real Data Set
adjacency_list = load_adjacency_list()

#Test Data Set
'''
adjacency_list = {
    "0": ['4'],
    "1": ['0'],
    "2": ['1'],
    "3": ['2'],
    "4": ['3']
}
#'''
'''
ranks_should_be = {
    "0": 0.2,
    "1": 0.2,
    "2": 0.2, 
    "3": 0.2, 
    "4": 0.2
}
#'''
'''
adjacency_list = {
    "0": ['1'],
    "1": ['0','2'],
    "2": ['1','3'],
    "3": ['2']
}
#'''
'''
ranks_should_be = {
    "0": 0.2,
    "1": 0.2,
    "2": 0.2, 
    "3": 0.2, 
    "4": 0.2
}
#'''

def page_rank(adjacency_list, damping_factor=0.85, max_iterations=100, convergence_threshold=1e-6):
    num_nodes = len(adjacency_list)
    # Initialize PageRank values to 1/N for each node
    ranks = {node: 1.0 / num_nodes for node in adjacency_list}

    for iteration in range(max_iterations):
        print("Progress: " + str(int((iteration / max_iterations) * 100)) + "%")
        new_ranks = {}
        total_change = 0
        # Handle nodes with no inbound links (assuming they are in adjacency_list with empty lists)
        no_inbound_nodes = {node for node, links in adjacency_list.items() if len(links) == 0}
        
        for node in adjacency_list:
            rank_sum = 0
            inbound_links = adjacency_list.get(node, [])
            for in_node in inbound_links:
                # Skip if in_node has no outbound links to avoid division by zero
                if in_node in no_inbound_nodes:
                    continue
                rank_sum += ranks[in_node] / len(adjacency_list[in_node])
            new_rank = (1 - damping_factor) / num_nodes + damping_factor * rank_sum
            new_ranks[node] = new_rank
            total_change += abs(new_ranks[node] - ranks[node])

        # Check for convergence
        if total_change < convergence_threshold:
            print(f"Converged after {iteration+1} iterations.")
            break
        
        ranks = new_ranks
    
    return ranks

# Calculate PageRank
ranks = page_rank(adjacency_list)

# Assuming `ranks` is your dictionary of PageRank values
sorted_ranks = sorted(ranks.items(), key=lambda item: item[1], reverse=True)

# `sorted_ranks` is now a list of tuples sorted by PageRank value in descending order
# Each tuple is in the form (node, PageRank)

# Example: Print the top 10 nodes and their PageRank values
for node, rank in sorted_ranks[:10]:
    print(f"Node {node}: PageRank {rank}")
    
sorted_ranks = dict(sorted_ranks)
json_file_path = 'ranks.json'
with open(json_file_path, 'w') as json_file:
    json.dump(sorted_ranks, json_file, indent=4)
