class LRUCache {
public:
    unordered_map<int, std::pair<int, std::list<int>::iterator>> hash;
    std::list<int> order;
    int cap;
    
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        auto found = hash.find(key);
        if (found == hash.end()) return -1;
        auto &[val, pos] = found->second;
        order.splice(order.begin(), order, pos);
        return val;
    }
    
    void put(int key, int value) {
        auto found = hash.find(key);
        if (found == hash.end()) {  // NOT found
            order.push_front(key);
            hash.insert({key, {value, order.begin()}});

            if (hash.size() > cap) {
                int last = order.back();
                order.pop_back();
                hash.erase(last);
            }
        } else {                    // Use old
            auto &[val, pos] = found->second;
            order.splice(order.begin(), order, pos);
            hash[key] = {value, pos};
        }
    }
};
