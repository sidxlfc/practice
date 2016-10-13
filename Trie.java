import java.util.Map;
import java.util.HashMap;

class Node {

	boolean endNode;
	Map<Character, Node> children = null;

	public Node(boolean endNode){

		this.endNode = endNode;
		children = new HashMap<Character, Node>();
	}
}

public class Trie {

	public static void printTree(Node root) {

		Node currentNode = root;

		while (currentNode.endNode != true) {

			for (char c : currentNode.children.keySet()) {
				
				System.out.println(c);
				currentNode = currentNode.children.get(c);
			}
		}
	}

	public static boolean search(Node root, String s) {

		Node currentNode = root;

		boolean flag = false;

		for (int i = 0; i < s.length(); i++) {

			char currentChar = s.charAt(i);

			if (currentNode.children.containsKey(currentChar)) {

				if (i == s.length() - 1) {

					currentNode = currentNode.children.get(currentChar);
					
					if (currentNode.endNode) {

						flag = true;
						return true;
					}

					else {

						flag = false;
						return false;
					}
				}

				currentNode = currentNode.children.get(currentChar);
			}

			else {

				flag = false;
				return false;
			}
		}

		return flag;		
	}

	public static void insert(Node root, String s) {

		Node currentNode = root;

		for (int i = 0; i < s.length(); i++) {

			char currentChar = s.charAt(i);

			if (!currentNode.children.containsKey(currentChar)) {

				if (i < s.length() - 1) {
				
					currentNode.children.put(currentChar, new Node(false));
					currentNode = currentNode.children.get(currentChar);
					//System.out.println(currentNode.children);
				}

				else
					currentNode.children.put(currentChar, new Node(true));					
			}

			else {

				if (i < s.length() - 1)
					currentNode = currentNode.children.get(currentChar);

				else {

					currentNode = currentNode.children.get(currentChar);
					currentNode.endNode = true;
				}
			}
		}		
	}

	public static void main(String args[]) {

		Node root = new Node(false);

		insert(root, "abcdefghi");
		insert(root, "abc");
		insert(root, "siddharth");

		System.out.println(search(root, "siddharth"));
	}
}