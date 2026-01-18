from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

# Add CORS middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Node(BaseModel):
    id: str

class Edge(BaseModel):
    source: str
    target: str

class Pipeline(BaseModel):
    nodes: List[Node]
    edges: List[Edge]

@app.get('/')
def read_root():
    return {'Ping': 'Pong'}

@app.post('/pipelines/parse')
def parse_pipeline(pipeline: Pipeline):
    """
    Parse the pipeline and return:
    - num_nodes: Number of nodes in the pipeline
    - num_edges: Number of edges in the pipeline
    - is_dag: Whether the pipeline forms a Directed Acyclic Graph
    """
    nodes = pipeline.nodes
    edges = pipeline.edges
    
    num_nodes = len(nodes)
    num_edges = len(edges)
    
    # Check if the graph is a DAG using DFS-based cycle detection
    is_dag = is_directed_acyclic_graph(nodes, edges)
    
    return {
        'num_nodes': num_nodes,
        'num_edges': num_edges,
        'is_dag': is_dag
    }

def is_directed_acyclic_graph(nodes: List[Node], edges: List[Edge]) -> bool:
    """
    Check if the graph formed by nodes and edges is a DAG.
    Uses DFS with color marking to detect cycles.
    
    Returns:
        bool: True if the graph is a DAG, False if it contains cycles
    """
    # Build adjacency list
    graph = {node.id: [] for node in nodes}
    for edge in edges:
        if edge.source in graph:
            graph[edge.source].append(edge.target)
    
    # Color states: 0 = white (unvisited), 1 = gray (visiting), 2 = black (visited)
    color = {node.id: 0 for node in nodes}
    
    def has_cycle_dfs(node_id: str) -> bool:
        """DFS helper to detect cycles"""
        color[node_id] = 1  # Mark as visiting (gray)
        
        for neighbor in graph.get(node_id, []):
            if neighbor not in color:
                continue
                
            if color[neighbor] == 1:  # Back edge found (cycle detected)
                return True
            
            if color[neighbor] == 0:  # Unvisited neighbor
                if has_cycle_dfs(neighbor):
                    return True
        
        color[node_id] = 2  # Mark as visited (black)
        return False
    
    # Check all nodes for cycles
    for node in nodes:
        if color[node.id] == 0:  # Unvisited node
            if has_cycle_dfs(node.id):
                return False  # Cycle found, not a DAG
    
    return True  # No cycles found, is a DAG
