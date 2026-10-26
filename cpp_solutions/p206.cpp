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
        ListNode* prev=nullptr;
        ListNode* curr=head;

        while(curr != nullptr){
            ListNode* nextnode = curr -> next; // points ti the next node
            curr -> next = prev; // reverses the list by changing the pointer to prev
            prev = curr; // changes the prev to curr (moves forward:iterate)
            curr = nextnode; // changes the curr to nectnode (moves forward)
        }
    return prev;
        
    }
};