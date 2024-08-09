from django.shortcuts import render
from django.http import JsonResponse

from myapp.models import TreeNode
# Create your views here.


def get_tree_structure(node):
    tree={
        'name':node.name,
        'children':[get_tree_structure(child) for child in node.get_children()]
    }
    
    return tree

def reverse_tree(node):
    reversed_nodes=[]
    
    for child in reversed(node.get('children', [])):
        reversed_nodes.extend(reverse_tree(child))
        
    reversed_nodes.append(node['name'])
    return reversed_nodes

def tree_view(request, node_id):
    root=TreeNode.objects.get(pk=node_id)
    tree_structure=get_tree_structure(root)
    print(tree_structure)

    # bottom_child=reverse_tree(tree_structure)[0]
    return JsonResponse({'root':tree_structure}, safe=False)
    # return render(request, 'myapp/tree.html', {'node':root})
