class PrimalityTest {
	
	public static boolean test(int n) {

		for(int i = n/2; i>=2; i--) {

			if (n%i == 0) {

				return false;
			}
		}

		return true;
	}


	public static void main(String args[]) {

		System.out.println(test(3));
	}
}