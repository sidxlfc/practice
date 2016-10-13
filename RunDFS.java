import java.util.*;

class Node {

	public String name;
	private boolean visited;

	private List<Node> neighbors;

	public Node(String name) {

		this.name = name;
		this.neighbors = new ArrayList<Node>();
	}

	public void addNeighbor(Node n) {

		this.neighbors.add(n);
	}

	public boolean getVisited() {

		return this.visited;
	}

	public void setVisited(boolean visited) {

		this.visited = visited;
	}

	public List<Node> getNeighbors() {

		return this.neighbors;
	}

	@Override
	public String toString() {
		return this.name;
	}
}

class DFS {

	private Stack<Node> st;

	public DFS() {

		this.st = new Stack<Node>();
	}

	public void dfs(Node root) {

		st.push(root);

		root.setVisited(true);

		while (!st.isEmpty()) {

			Node current = st.pop();
			System.out.println(current);

			for (Node n : current.getNeighbors()) {

				if(! n.getVisited())
					dfs(n);
			}
		}
	}
}

public class RunDFS {

	public static void main(String args[]) {

		Node A = new Node("A");
		Node B = new Node("B");
		Node C = new Node("C");
		Node D = new Node("D");
		Node E = new Node("E");
		Node F = new Node("F");
		Node G = new Node("G");
		Node H = new Node("H");
		Node I = new Node("I");

		A.addNeighbor(B);
		A.addNeighbor(C);

		B.addNeighbor(D);

		D.addNeighbor(E);
		D.addNeighbor(F);

		C.addNeighbor(G);
		C.addNeighbor(H);

		G.addNeighbor(I);
		G.addNeighbor(H);

		DFS dfs = new DFS();
		dfs.dfs(A);
	}
}