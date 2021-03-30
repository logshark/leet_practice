/*
 * @lc app=leetcode id=61 lang=cpp
 *
 * [61] Rotate List
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

#define DEBUG 0
#if DEBUG
#include <stdio.h>
#include <algorithm>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};
#endif

// Input: head = [1,2,3,4,5], k = 2
// Output: [4,5,1,2,3]
// 1-> 2-> 3-> 4-> 5
// 5-> 1-> 2-> 3-> 4
// 4-> 5-> 1-> 2-> 3

class Solution {
public:
    ListNode* rotateRight(ListNode* head, int k) {
        int move = k;
        int count = 0;

        if (head == NULL) {
            return head;
        }

        ListNode* tmp = head;
        while(tmp) {
            tmp = tmp->next;
            count++;
        }

        move = k%count;
        while (move) {
            // printf("move=%d\n", move);
            ListNode* cur = head;
            ListNode* pre = NULL;
            ListNode* nxt = NULL;
            while (cur) {
                // printf("cur:%d, count:%d\n", cur->val, count);
                nxt = cur->next;

                if (nxt == NULL) {
                    cur->next = head;
                    pre->next = NULL;
                    head = cur;
                    break;
                }
                pre = cur;
                cur = cur->next;
            }
            move--;
        }
        return head;
    }
};
// @lc code=end

#if DEBUG
int main(int argc, char* argv[])
{
    ListNode *l1_node5 = new ListNode(5);
    ListNode *l1_node4 = new ListNode(4, l1_node5);
    ListNode *l1_node3 = new ListNode(3, l1_node4);
    ListNode *l1_node2 = new ListNode(2, l1_node3);
    ListNode *l1_node1 = new ListNode(1, l1_node2);

    int k = 2;

    for (ListNode *tmp = l1_node1; tmp != NULL; tmp=tmp->next)
    {
        printf("l1 %d\n", tmp->val);
    }

    Solution solution;
    ListNode *result = solution.rotateRight(l1_node1, k);

    for (ListNode *tmp = result; tmp != NULL; tmp=tmp->next)
    {
        printf("result %d\n", tmp->val);
    }



    printf("end\n");
    return 0;
}
#endif