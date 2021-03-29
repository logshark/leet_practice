/*
 * @lc app=leetcode id=21 lang=cpp
 *
 * [21] Merge Two Sorted Lists
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

#define DEBUG 1
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

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *result = new ListNode();
        ListNode *tmp = result;

        while (l1 != NULL && l2 != NULL)
        {
            if (l1->val <= l2->val) {
                printf("l1 %d\n", l1->val);
                tmp->next = l1;
                l1 = l1->next;
            } else {
                printf("l2 %d\n", l2->val);
                tmp->next = l2;
                l2 = l2->next;
            }
            tmp = tmp->next;
        }

        while (l1)
        {
            printf("l1 %d\n", l1->val);
            tmp->next = l1;
            l1 = l1->next;
        }
        
        while (l2)
        {
            printf("l2 %d\n", l2->val);
            tmp->next = l2;
            l2 = l2->next;
        }

        return result->next;
    }
};
// @lc code=end

#if DEBUG
int main(int argc, char* argv[])
{
    // ListNode *l1_node3 = new ListNode(4);
    // ListNode *l1_node2 = new ListNode(2, l1_node3);
    // ListNode *l1_node1 = new ListNode(1, l1_node2);

    // ListNode *l2_node3 = new ListNode(4);
    // ListNode *l2_node2 = new ListNode(3, l2_node3);
    // ListNode *l2_node1 = new ListNode(1, l2_node2);

    // for (ListNode *tmp = l1_node1; tmp != NULL; tmp=tmp->next)
    // {
    //     printf("l1 %d\n", tmp->val);
    // }

    // for (ListNode *tmp = l2_node1; tmp != NULL; tmp=tmp->next)
    // {
    //     printf("l2 %d\n", tmp->val);
    // }

    ListNode *l1_node2 = new ListNode(3);
    ListNode *l1_node1 = new ListNode(-9, l1_node2);

    ListNode *l2_node2 = new ListNode(7);
    ListNode *l2_node1 = new ListNode(5, l2_node2);

    
    Solution solution;
    ListNode *result = solution.mergeTwoLists(l1_node1, l2_node1);

    for (; result != NULL; result=result->next)
    {
        printf("result %d\n", result->val);
    }

    printf("end\n");
    return 0;
}
#endif