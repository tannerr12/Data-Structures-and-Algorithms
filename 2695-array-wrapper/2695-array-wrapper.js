/**
 * @param {number[]} nums
 */
var ArrayWrapper = function(nums) {
    this.arr = nums
};

ArrayWrapper.prototype.valueOf = function() {
    let tot = 0
    for (let i =0; i< this.arr.length; i ++){
        tot += this.arr[i]
    }
    return tot
}

ArrayWrapper.prototype.toString = function() {
    let str = '['
    for (let i =0; i< this.arr.length; i ++){
        if (i == this.arr.length - 1){
            str += String(this.arr[i])
        }
        else{
            str += String(this.arr[i]) + ','
        }
    }
    str += ']'
    
    return str
}

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */