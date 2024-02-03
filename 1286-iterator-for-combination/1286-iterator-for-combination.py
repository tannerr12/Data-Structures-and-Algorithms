class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        self.characters = characters
        self.combinationLength = combinationLength
        self.generator = self._combinations_generator()
        self.next_combination = next(self.generator, None)

    def _combinations_generator(self):
        def generate_combinations(start, path):
            # When the path length equals the target combination length, yield it
            if len(path) == self.combinationLength:
                yield ''.join(path)
                return
            for i in range(start, len(self.characters)):
                # Generate all combinations by picking the next character and moving forward
                yield from generate_combinations(i + 1, path + [self.characters[i]])

        yield from generate_combinations(0, [])

    def next(self) -> str:
        # Return the current combination and prepare the next one
        current_combination = self.next_combination
        self.next_combination = next(self.generator, None)
        return current_combination

    def hasNext(self) -> bool:
        # Check if there's a next combination
        return self.next_combination is not None

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()