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

class BFS {

	private Queue<Node> q;

	public BFS() {

		this.q = new LinkedList<Node>();
	}

	public void bfs(Node root) {

		if (!root.getVisited())
			q.add(root);

		root.setVisited(true);

		while (!q.isEmpty()) {

			Node current = q.remove();
			//current.setVisited(true);
			System.out.println(current);

			for (Node n : current.getNeighbors()) {

				if(!n.getVisited()) {
					
					q.add(n);
					n.setVisited(true);
				}
			}

			bfs(current);
		}
	}
}

public class RunBFS {

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
		

		BFS bfs = new BFS();
		bfs.bfs(A);
	}
}