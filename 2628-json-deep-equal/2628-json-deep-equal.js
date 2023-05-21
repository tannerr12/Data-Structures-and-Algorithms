/**
 * @param {any} o1
 * @param {any} o2
 * @return {boolean}
 */
var areDeeplyEqual = function(o1, o2) {

    if (o1 === o2){
        return true
    }else if (o1 === null || o1 === undefined){
        return false
    }
    if (typeof o1 === typeof o2){
        if (typeof o1 !== "object"){
            return o1 === o2
        }else{
            if (Array.isArray(o1) !== Array.isArray(o2)){
                return false
            }else if(Array.isArray(o1) === true && Array.isArray(o2) === true){
                if (o1.length !== o2.length){
                    return false
                }
                if (o1.length === 0){
                    return true
                }
                for(i=0;i<o1.length;i++){
                    if (!areDeeplyEqual(o1[i], o2[i])){
                        return false
                    }
                }
                return true
            }else{
                
                for (const [key, value] of Object.entries(o1)) {
                    if (key in o2){

                        if (!areDeeplyEqual(value, o2[key])){
                            return false
                        }
                    }else{
                        return false
                    }
                }
                return true
            }
        }
        
    }else{
        return false
    }


};