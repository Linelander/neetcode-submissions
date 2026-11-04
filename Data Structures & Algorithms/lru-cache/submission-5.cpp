class LRUCache {
public:
    std::list<int> order;
    int cap;
    unordered_map<int, pair<int, std::list<int>::iterator>> hash;
    
    LRUCache(int capacity) : cap(capacity) {
    
    }
    
    int get(int key) {
        auto found = hash.find(key);
        if (found == hash.end()) {
            return -1;
        }
        auto &[val, pos] = found->second;
        order.splice(order.begin(), order, pos); // use
        return val;                              // return
    }
    
    void put(int key, int value) {
        auto found = hash.find(key);
        if (found == hash.end()) { // add new
            order.push_front(key);
            hash.insert({key, {value, order.begin()}});
            if (hash.size() > cap) {
                int last = order.back();
                hash.erase(last);
                order.pop_back();
            }
        } else { // update
            auto &[val, pos] = found->second;           
            order.splice(order.begin(), order, pos);   // use
            hash[key] = {value, order.begin()}; // update
        }
    }
};
