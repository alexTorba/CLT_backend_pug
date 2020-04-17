import os

#------------------------------------------------------------------------------

class Node:
	def __init__(self, name, content):
		self.name = name
		self.content = content

nodes = dict() # name => node
current_file_nodes = dict() # num => name

class Edge:
	def __init__(self, node1, node2, content):
		self.node1 = node1
		self.node2 = node2
		self.content = content

edges = list()

#------------------------------------------------------------------------------

def has_duplicates_in_edges(node1, node2):
	for edge in edges:
		if edge.node1 == node1 and edge.node2 == node2:
			return True
	return False

#------------------------------------------------------------------------------

def filter_fun(item):
	return os.path.isfile(item) and os.path.splitext(item)[1] == ".dot"

#------------------------------------------------------------------------------

def get_graph_data(file_name):
	file = open(dot_file, "r")
	file_lines = file.read().split("\n")
	file.close()

	lines_end = len(file_lines) - 2  # removing not needed lines
	return file_lines[3:lines_end]

#------------------------------------------------------------------------------

def process_line(line):
	line_len = len(line)
	if line[4] == '-':
		num1 = int(line[1]) - 48
		num2 = int(line[8]) - 48

		node1 = current_file_nodes[num1]
		node2 = current_file_nodes[num2]
		content = line[11:line_len]

		if has_duplicates_in_edges(node1, node2):
			return

		edge = Edge(node1, node2, content)
		edges.append(edge)

	elif line[4] == '[':
		num = int(line[1]) - 48

		name_end = line.find("|")
		node_name = line[13:name_end]

		node_content = line[4:line_len]
		current_file_nodes[num] = node_name

		node = Node(node_name, node_content)
		nodes[node_name] = node

	else:
		print("ERROR")

#------------------------------------------------------------------------------

source_dir = os.path.dirname(os.path.realpath(__file__))
dir_content = os.listdir(source_dir)
dot_files = filter(filter_fun, dir_content)

for dot_file in dot_files:
	current_file_nodes.clear()
	lines = get_graph_data(dot_file)
	for line in lines:
		process_line(line)

#------------------------------------------------------------------------------

output = list()

for node in nodes.values():
	output.append(f"\"{node.name}\" {node.content}")

for edge in edges:
	output.append(f"\"{edge.node1}\" -> \"{edge.node2}\" {edge.content}")

output_file = open("result.txt", "w")
output_str = "\n".join(output)
output_file.write(output_str)
