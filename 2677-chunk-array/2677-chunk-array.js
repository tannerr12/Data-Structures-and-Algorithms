/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    
    let a = []
    let res = []
    for (let i = 0; i < arr.length; i++){
        a.push(arr[i])
        if (a.length === size){
            res.push(a)
            a = []
        }
    
    }
    
    if (a.length > 0){
        res.push(a)
    }
    return res
    
};
