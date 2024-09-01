class Solution {
public:
    PolyNode* addPoly(PolyNode* poly1, PolyNode* poly2) {
        PolyNode* sum = new PolyNode();
        PolyNode* current = sum;

        map<int, int, greater<int>> table;

        // Calculate terms for sum
        processNodes(table, poly1);
        processNodes(table, poly2);

        // Iterate over sorted keys and build sum
        for (auto& [key, val] : table) {
            current->next = new PolyNode(val, key);
            current = current->next;
        }

        return sum->next;
    }

private:
    void processNodes(map<int, int, greater<int>>& table, PolyNode* node) {
        while (node != nullptr) {
            if (table.find(node->power) != table.end()) {
                int newCoefficient = node->coefficient + table[node->power];
                if (newCoefficient == 0) {
                    table.erase(node->power);
                } else {
                    table[node->power] = newCoefficient;
                }
            } else {
                table[node->power] = node->coefficient;
            }
            node = node->next;
        }
    }
};