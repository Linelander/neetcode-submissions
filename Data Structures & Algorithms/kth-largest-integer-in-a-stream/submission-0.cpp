class KthLargest {
public:
    vector<int> stream;
    int k;

    KthLargest(int k, vector<int>& nums) {
        this->k = k;
        for (int num : nums) {
            add(num);
        }
    }
    
    int add(int val) {
        stream.push_back(val);
        std::push_heap(stream.begin(), stream.end(), std::greater<int>());
        
        if (stream.size() > k) {
            std::pop_heap(stream.begin(), stream.end(), std::greater<int>());
            stream.pop_back();
        }
        return stream.front();
    }
};
