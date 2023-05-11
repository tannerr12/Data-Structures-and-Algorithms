/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        total = x
        for (i = functions.length-1; i >= 0; i --){
            fn = functions[i]
            //console.log(fn)
            total = fn(total)
        }
        
        return total
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */