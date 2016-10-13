import java.math.*;
import java.util.*;

public class MaximumValueContiguousSubsequence {
	
	public static void main(String args[]) {

		// maxValues(j) = max sum of all windows ending at j

		int a[] = {
			-2, 11, -4, 13, -5, 2
			//-15, 29, -36, 3, -22, 11, 19, -5
		};

		List<Integer> maxValues = new ArrayList<Integer>();

		maxValues.add(a[0]);

		for(int i = 1; i < a.length; i++) {

			maxValues.add(Math.max(maxValues.get(i-1)+a[i], a[i]));
		}

		int max = Collections.max(maxValues);

		int i = 0, j = 0;

		while(i < maxValues.size()) {
			if (maxValues.get(i) == max)
				break;
			i++;
		}

		j = i-1;
		int temp = a[i];

		while(j >= 0) {
			temp += a[j];
			if(temp == max)
				break;

			j--;
		}

		System.out.println(maxValues);		

		//the value
		System.out.println(max);

		//the indices between which the subsequence is max
		System.out.println(j + " " + i);
	}
}