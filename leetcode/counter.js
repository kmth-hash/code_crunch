// https://leetcode.com/problems/counter/description/?envType=study-plan-v2&envId=30-days-of-javascript

/**
 * @param {number} n
 * @return {Function} counter
 */
 var createCounter = function(n) {
    let c = n;
    return function() {
        return c++;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */