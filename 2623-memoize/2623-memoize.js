/**
 * @param {Function} fn
 */
function memoize(fn) {
    let memo = new Map()
    return function(...args) {
        if (memo.has(fn.name + ' ' + args)){
            return memo.get(fn.name + ' ' + args)
        }
        res = fn(...args)
        memo.set(fn.name + ' ' + args, res)
        return res
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */