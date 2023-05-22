/**
 * @param {any} object
 * @return {string}
 */

var jsonStringify = function(obj) {
    if(obj === null){
        return 'null';
    }
  if (Array.isArray(obj)) {
    const elements = obj.map((element) => jsonStringify(element));
    return `[${elements.join(',')}]`;
  }
    
 if (typeof obj === 'object') {
    const keys = Object.keys(obj);
    const keyValuePairs = keys.map((key) => `"${key}":${jsonStringify(obj[key])}`);
    return `{${keyValuePairs.join(',')}}`;
  }
  if (typeof obj === 'string') {
    return `"${obj}"`;
  }
    return String(obj)


};