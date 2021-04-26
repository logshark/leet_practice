/*
 * @lc app=leetcode id=1114 lang=cpp
 *
 * [1114] Print in Order
 */

// @lc code=start

#include <mutex>

class Foo {
private:
    std::mutex m1, m2;
public:
    Foo() {
        m1.lock();
        m2.lock();
    }

    void first(function<void()> printFirst) {
        // printFirst() outputs "first". Do not change or remove this line.
        printFirst();
        m1.unlock();
    }

    void second(function<void()> printSecond) {
        // printSecond() outputs "second". Do not change or remove this line.
        m1.lock();
        printSecond();
        m1.unlock();
        m2.unlock();
    }

    void third(function<void()> printThird) {
        // printThird() outputs "third". Do not change or remove this line.
        m2.lock();
        printThird();
        m2.unlock();
    }
};
// @lc code=end

