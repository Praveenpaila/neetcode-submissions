class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String,List<String>> hash=new HashMap<>();
        for (String i:strs){
            char[] arr=i.toCharArray();
            Arrays.sort(arr);
            String s=new String(arr);
            if (hash.containsKey(s)){
                hash.get(s).add(i);
            }
            else{
                hash.put(s,new ArrayList<>(Arrays.asList(i)));
            }
        }
            return new ArrayList<>(hash.values());
    }
}