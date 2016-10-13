class ABBA {
    
    public String canObtain(String initial, String target) {
        
        StringBuffer t = new StringBuffer(target);

        int l = t.toString().length();

        while (initial.length() < t.toString().length()) {

            l = t.toString().length();
            
            if (t.toString().charAt(l-1) == 'B') {

                t.deleteCharAt(l-1);
                t.reverse();
                //System.out.println("if : " + t.toString());
            }

            else {

                t.deleteCharAt(l-1);
                ///System.out.println("else : " + t.toString());
            }
        }

        return (initial.equals(t.toString())) ? "Possible" : "Impossible";
    }

    public static void main(String args[]) {

        ABBA test = new ABBA();

        System.out.println(test.canObtain("B", "ABBA"));
        System.out.println(test.canObtain("BBAB", "ABABABABB"));
        System.out.println(test.canObtain("BBBBABABBBBBBA", "BBBBABABBABBBBBBABABBBBBBBBABAABBBAA"));
    }
}