/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function(fn) {
    mp = {}
    for (let i = 0; i < this.length; i ++){
        val = fn(this[i])
        if (val in mp){
            mp[val].push(this[i])
        }else{
            mp[val] = [this[i]]
        }
    }
    return mp
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */