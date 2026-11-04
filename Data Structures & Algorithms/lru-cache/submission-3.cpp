class LRUCache {
public:
    unordered_map<int, pair<int, list<int>::iterator>> hash;
    int cap;
    list<int> order;

    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        auto result = hash.find(key);
        if (result == hash.end()) return -1;
        auto &[val, pos] = result->second;
        order.splice(order.begin(), order, pos);
        return val;
    }
    
    void put(int key, int value) {
        auto result = hash.find(key);
        
        if (result == hash.end()) { // New
            order.push_front(key);
            hash.insert({key, {value, order.begin()}});

            if (hash.size() > cap) {
               int last = order.back();
               order.pop_back();
               hash.erase(last);
            }

            return;
        }
        else {                      // Use existing
            auto exist = hash.find(key);
            auto &[val, pos] = result->second;
            order.splice(order.begin(), order, pos);
            val = value;
        }
    }
};
