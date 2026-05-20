/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* reverseList(ListNode* head) {
        if (head == NULL) {
            return NULL;
        }
        return flipper(NULL, head);
    }

    ListNode* flipper(ListNode *prev, ListNode *curr) {
        if (curr->next != NULL) {
            ListNode* oldNext = curr->next;
            curr->next = prev;
            return flipper(curr, oldNext);
        }
        // base case
        curr->next = prev;
        return curr;
    }
};
