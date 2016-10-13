import java.util.Arrays;

class Node {

	Object data;
	public Node leftChild;
	public Node rightChild;

	public Node(Object data) {

		this.data = data;
		this.leftChild = null;
		this.rightChild = null;
	}

	public Node(Object data, Node leftChild, Node rightChild) {

		this.data = data;
		this.leftChild = leftChild;
		this.rightChild = rightChild;
	}
}

public class BST {

	static Node buildTree(Object[] a, int start, int stop) {

		if(start <= stop) {

			int mid = (start+stop)/2;
			Node root = new Node(a[mid]);
			root.leftChild = buildTree(a, start, mid - 1);
			root.rightChild = buildTree(a, mid + 1, stop);
			return root;
		}

		else
			return null;
	}

	public static void main(String args[]) {

		Integer[] a = {
			10, 5, 6, 10, 19, 25, 34, 7, -6, 5, -99
		};

		Arrays.sort(a);

		Node root = buildTree(a, 0 , a.length-1);

		printTree(root);
	}

	static void printTree(Node node) {
    // is there actually a node here
    // or was this called from a node with no children
    if(node != null) {
        
        // print everything that's earlier than this node
        printTree(node.leftChild);   

        // print this node's value
        System.out.println(node.data);

        // print everything that's afterthan this node
        printTree(node.rightChild);  
    	}
	}
}


/*

Node[] nodes = new Node[a.length];

		for (int i = 0; i<a.length; i++) {

			nodes[i] = new Node(a[i]);
			System.out.print(a[i] + "\t");
		}

		System.out.println();

		//nodes[0] = new Node(10);

		Node root = nodes[nodes.length/2];

		for (int i = 0; i<nodes.length; i++) {

			//if (i == nodes.length/2)
			//	continue;

			Node pointer = root;
			while (pointer != null) {

				if ((int)nodes[i].data < (int)pointer.data) {

					if (pointer.leftChild != null)
						pointer = pointer.leftChild;

					else
						break;
				}

				else {

					if (pointer.rightChild != null)
						pointer = pointer.rightChild;

					else
						break;
				}
			}

			if ((int)nodes[i].data < (int)pointer.data)
				pointer.leftChild = nodes[i];

			else
				pointer.rightChild = nodes[i];
		}

		*/