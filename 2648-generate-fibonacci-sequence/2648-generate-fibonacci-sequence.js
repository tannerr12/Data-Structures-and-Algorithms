/**
 * @return {Generator<number>}
 */

var fibGenerator = function*() {

    let last1 = 0
    let last2 = 1

    yield 0
    yield 1
    
    while (true) {
        let res = last1 + last2
        last1 = last2
        last2 = res
        yield res
    }

    
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */