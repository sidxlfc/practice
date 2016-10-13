import java.util.*;

class MergeSort {


	static int[] merge(int[] a, int[] b) {

		int leftSize = a.length;
		int rightSize = b.length;

		int ret[] = new int[leftSize + rightSize];

		int i = 0;
		int j = 0;
		int k = 0;

		while(i < leftSize && j < rightSize) {

			if (a[i] <= b[j]) 
				ret[k++] = a[i++];

			else 
				ret[k++] = b[j++];
		}

		while (i < leftSize)
			ret[k++] = a[i++];

		while(j < rightSize)
			ret[k++] = b[j++];

	    return ret; 		
	}

	static int[] mergeSort(int[] a) {
		
		if (a.length == 1) {

			return a;
		}

		else {

			int[] l = mergeSort(Arrays.copyOfRange(a, 0, a.length/2));
			int[] r = mergeSort(Arrays.copyOfRange(a, a.length/2, a.length));
			return merge(l, r);
		}
	}

	public static void main(String args[])
	{
		int[] a = {
			10, 35, 96, 74, -56, 75, 1, 0, 99, 110
		};

		a = mergeSort(a);

		for(int intValue : a) {

		    System.out.println(intValue);
		}
	}
}