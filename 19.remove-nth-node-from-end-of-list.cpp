/*
 * @lc app=leetcode id=19 lang=cpp
 *
 * [19] Remove Nth Node From End of List
 */

// @lc code=start
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {

        if (head == NULL)
        {
            return NULL;
        }

        ListNode *tmp = head;
        int count = 0;
        while(tmp) {
            count++;
            tmp = tmp->next;
        }

        int move = count - n;

        if (move == 0) {
            tmp = head;
            head = head->next;
            delete tmp;
            return head;
        }

        ListNode *pre = NULL;
        tmp = head;
        while (move) {
            move--;
            pre = tmp;
            tmp = tmp->next;
        }

        pre->next = tmp->next;
        delete tmp;

        return head;
    }
};
// @lc code=end

