class HashEntry {

	private int key;
	private Object value;

	HashEntry(int key, Object value) {

		this.key = key;
		this.value = value;
	}

	public int getKey() {

		return key;
	}

	public Object getValue() {

		return value;
	}	
}

class HashMap {

	private final static int TABLE_SIZE = 128;

	HashEntry[] table;

	HashMap() {

		table = new HashEntry[TABLE_SIZE];

		for (int i = 0; i < TABLE_SIZE; i++) {

			table[i] = null;
		}
	}

	public Object get(int key) {

		int hash = key % TABLE_SIZE;

		while (table[hash] != null && table[hash].getKey() != key) {

			hash = (hash + 1) % TABLE_SIZE;
		}

		if (table[hash] == null)
			return "No value found for the given key";
		else
			return table[hash].getValue();
	}

	public void put(int key, Object value) {

		int hash = key % TABLE_SIZE;

		while (table[hash] != null && table[hash].getKey() != key) {

			hash = (hash + 1) % TABLE_SIZE;
		}

		table[hash] = new HashEntry(key, value);
	}
}

public class Hashing {

	public static void main(String args[]) {

		HashMap hm = new HashMap();

		hm.put(1, "First Entry");
		hm.put(2, "Second Entry");

		hm.put(129, "129th Entry");

		System.out.println(hm.get(1));
		System.out.println(hm.get(2));
		System.out.println(hm.get(128));
		System.out.println(hm.get(129));
	}
}