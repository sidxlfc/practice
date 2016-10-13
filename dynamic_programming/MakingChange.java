import java.math.*;

public class MakingChange {

	public static void main(String args[]) {

		int denominations[] = {
			1, 10, 20, 25
		};

		int C = 30;

		System.out.println(minCoinsRequired(new int[]{1, 5, 6, 8}, 11));
	}

	public static int minCoinsRequired(int[] denominations, int amount) {

		int coinReq[][] = new int[denominations.length][amount+1];

		for (int i = 0; i < denominations.length; i++) {
			
			for (int j = 0; j <= amount; j++) {

				if (j==0) {

					coinReq[i][j] = 0;
					continue;
				}

				if (j < denominations[i]) {

					coinReq[i][j] = coinReq[i-1][j];
				}

				else {

					if (i > 0)
						coinReq[i][j] = Math.min(coinReq[i][j - denominations[i]] + 1, coinReq[i-1][j]);

					else
						coinReq[i][j] = j;
				}			
			}
		}

		for (int i = 0; i < denominations.length; i++) {
			
			for (int j = 0; j <= amount; j++) {
				
				System.out.print(coinReq[i][j] + "  ");
			}

			System.out.println();
		}

		return coinReq[denominations.length-1][amount];
	}
}