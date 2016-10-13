import java.util.*;
import java.io.*;

class Balance_Parantheses {

	public static Stack<Character> st = new Stack<Character>();

	public static void main(String args[]) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		String s = br.readLine();

		System.out.println(verify(s));
	}

	public static String verify(String s) {

		for(int i = 0; i < s.length(); i++) {

			if (s.charAt(i) == '(' || s.charAt(i) == '[' || s.charAt(i) == '{') {

				st.push(s.charAt(i));
			}

			else {

				if (st.isEmpty()) {

					return "Wrong";
				}

				char temp = st.pop();

				if (temp != reverse(s.charAt(i))) {

					return "Wrong";
				}
			}
		}

		if (!st.isEmpty()) {

			return "Wrong";
		}

		return "Right";
	}

	public static char reverse(char c) {

		if (c == ')')
			return '(';

		if (c == ']')
			return '[';

		if (c == '}')
			return '{';

		return 'x';
	}
}