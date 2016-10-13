class IdenticalBinaryTrees {

	public static boolean isIdentical (Node root1, Node root2) {

		if (root1.rightChild != null && root2.rightChild != null) {

			return isIdentical (root1.rightChild, root2.rightChild);
		}

		if (root1.leftChild != null && root2.leftChild != null) {

			return isIdentical (root1.leftChild, root2.leftChild);
		}

		if (root1.rightChild == null && root2.rightChild == null) {

			return true;
		}

		if (root1.leftChild == null && root2.leftChild == null) {

			return true;
		}

		return false;
	}
}