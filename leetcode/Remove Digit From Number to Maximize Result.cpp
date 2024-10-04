class Solution {
public:
    std::string removeDigit(std::string number, char digit) {
        std::vector<int> indices;
        for (int i = 0; i < number.size(); ++i) {
            if (number[i] == digit) {
                indices.push_back(i);
            }
        }
        std::string max_number = "";
        for (int index : indices) {
            std::string new_number = number.substr(0, index) + number.substr(index + 1);
            if (new_number > max_number) {
                max_number = new_number;
            }
        }

        return max_number;
    }
};