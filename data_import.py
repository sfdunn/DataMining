import json

def build_adjacency_list():
    file_path = 'web-Google.txt'
    adjacency_list = {}  # Initialize an empty dictionary for the adjacency list
    with open(file_path, 'r') as file:
        for x in range(4):
            next(file)  # Skip the header line
        for line in file:
            from_node, to_node = line.strip().split('\t')  # Split each line by tab character
            from_node, to_node = int(from_node), int(to_node)  # Convert node IDs to integers
            
            # Invert the relationship for PageRank's needs
            if to_node in adjacency_list:
                adjacency_list[to_node].append(from_node)
            else:
                adjacency_list[to_node] = [from_node]

            # Ensure all nodes are in the list, even if they only link out
            if from_node not in adjacency_list:
                adjacency_list[from_node] = []
    
    return adjacency_list

def save_to_json(adjacency_list):
    json_file_path = 'edges.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(adjacency_list, json_file, indent=4)

def main():  
    adjacency_list = build_adjacency_list()   
    save_to_json(adjacency_list)
main()