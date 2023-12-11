#include <vector>
#include <map>
#include <iostream>
#include <utility>
#include <fstream>
#include <string>

int main() {
    std::ifstream file("input.txt");
    std::vector<std::string> rows;
    std::string line;

    while (std::getline(file, line))
    {
        rows.push_back(line);
    }

    std::vector<char> instructions;
    for(auto& c : rows[0]) {
        instructions.push_back(c);
    }

    // build map
    rows.erase(rows.begin());
    rows.erase(rows.begin());
    std::map<std::string, std::pair<std::string, std::string>> nodes;
    for(auto& row : rows) {
        nodes[row.substr(0, 3)] = {row.substr(7, 3), row.substr(12, 3)};
    }

    // collect initial nodes
    std::vector<std::string> cur;
    for (const auto &myPair : nodes) {
        if (myPair.first[2] == 'A') {
            cur.push_back(myPair.first);
        }
    }

    for (auto i : cur) {
        std::cout << i << "\n";
    }

    size_t inst_pt = 0;
    while (true) {
        const char inst = instructions[inst_pt];
        
        for (auto &node : cur) {
            if (inst == 'L') {
                node = nodes[node].first;
            }
            else {
                node = nodes[node].second;
            }
        }

        for (auto &node : cur) {
            if (node[2] != 'Z') {
                goto label;
            }
        }

        break;

        label:

        inst_pt++;
        if (inst_pt == instructions.size()) {
            inst_pt = 0;
        }
    }



}