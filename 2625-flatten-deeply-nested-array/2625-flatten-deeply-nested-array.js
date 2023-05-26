/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
    let res = []
    let mx = n
    function dfs(arr, n){
        if (n > mx){
            return
        }
        
        for (let j = 0; j < arr.length; j++){
            if (typeof arr[j] == 'object' && n + 1 <= mx){
                dfs(arr[j], n + 1)
            }
            else{
                res.push(arr[j])
            }
            
        }
    }
    
    dfs(arr,0)
    return res
};