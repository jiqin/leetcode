import java.util.*;

public class Solution126 {
    public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
        Set<String> free_word_set = new HashSet<String>();
        Map<String, List<List<String>>> map1 = new HashMap<String, List<List<String>>>();
        Map<String, List<List<String>>> map2 = new HashMap<String, List<List<String>>>();

        free_word_set.addAll(wordList);
        free_word_set.remove(beginWord);
        free_word_set.remove(endWord);

        List<String> tmpl1 = new ArrayList<String>();
        tmpl1.add(beginWord);
        List<List<String>> tmpll1 = new ArrayList<List<String>>();
        tmpll1.add(tmpl1);
        map1.put(beginWord, tmpll1);

        List<String> tmpl2 = new ArrayList<String>();
        tmpl2.add(endWord);
        List<List<String>> tmpll2 = new ArrayList<List<String>>();
        tmpll2.add(tmpl2);
        map2.put(endWord, tmpll2);

        List<List<String>> result = new ArrayList<List<String>>();
        boolean is_forward = true;

        while (map1.size() > 0 && map2.size() > 0) {
            for (String w1 : map1.keySet()) {
                List<List<String>> list1 = map1.get(w1);

                for (String w2 : map2.keySet()) {
                    List<List<String>> list2 = map2.get(w2);

                    if (is_distance_one(w1, w2)) {
                        List<List<String>> l1 = list1;
                        List<List<String>> l2 = list2;
                        if (!is_forward) {
                            l1 = list2;
                            l2 = list1;
                        }

                        for (List<String> ll1 : l1) {
                            for (List<String> ll2 : l2) {
                                List<String> r = new ArrayList<String>();
                                r.addAll(ll1);
                                for (int i = ll2.size() - 1; i >= 0; i--) {
                                    r.add(ll2.get(i));
                                }

                                result.add(r);
                            }
                        }
                    }
                }
            }

            if (result.size() > 0) {
                break;
            }

            Map<String, List<List<String>>> tmp_map = new HashMap<String, List<List<String>>>();
            Set<String> used_word_set = new HashSet<String>();


            for (String w1 : map1.keySet()) {
                List<List<String>> list1 = map1.get(w1);
                for (String w : free_word_set) {
                    if (is_distance_one(w1, w)) {
                        List<List<String>> l = tmp_map.get(w);
                        if (l == null) {
                            l = new ArrayList<List<String>>();
                            tmp_map.put(w, l);
                        }

                        for (List<String> l1 : list1) {
                            List<String> ll = new ArrayList<String>();
                            ll.addAll(l1);
                            ll.add(w);

                            l.add(ll);
                        }
                    }
                }
            }

            free_word_set.removeAll(used_word_set);
            if (tmp_map.size() < map2.size()) {
                map1 = tmp_map;
            } else {
                map1 = map2;
                map2 = tmp_map;
                is_forward = !is_forward;
            }
        }

        return result;
    }

    public boolean is_distance_one(String w1, String w2) {
        int n = 0;
        for (int i = 0; i < w1.length(); ++i) {
            if (w1.charAt(i) != w2.charAt(i)) {
                n += 1;
                if (n > 1) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String [] args) {
        Set<String> wl = new HashSet<String>();
        wl.add("hot");
        wl.add("dot");
        wl.add("dog");
        wl.add("lot");
        wl.add("log");

        Solution126 s = new Solution126();
        List<List<String>> result = s.findLadders("hit", "cog", wl);
        for (List<String> l : result) {
            for (String w : l) {
                System.out.print(w);
                System.out.print(" ");
            }
            System.out.print("\n");
        }
    }
}
