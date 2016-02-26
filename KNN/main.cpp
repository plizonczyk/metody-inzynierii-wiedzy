#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

std::map <std::string, int> iris_classes {{"Iris-setosa", 1}, {"Iris-versicolor", 2}, {"Iris-virginica", 3}};

struct Iris {
    float leaf_length;
    float leaf_width;
    float petal_length;
    float petal_width;
    int iris_class;
};


void parse_iris(std::string* temp, std::vector <Iris*> & irises){
    Iris* iris = new Iris;
    iris->leaf_length = std::stof(temp[0]);
    iris->leaf_width = std::stof(temp[1]);
    iris->petal_length = std::stof(temp[2]);
    iris->petal_width = std::stof(temp[3]);
    iris->iris_class = iris_classes[temp[4]];
    irises.push_back(iris);
}


void print_iris_vector(std::vector <Iris*> & irises){
    for(std::vector<int>::size_type i = 0; i != irises.size(); i++) {
        std::cout << irises[i]->leaf_length << " " << irises[i]->leaf_width << " " << irises[i]->petal_length << " ";
        std::cout << irises[i]->petal_width << " " << irises[i]->iris_class << std::endl;
    }
}


int main() {
    std::vector <Iris*> irises;
    std::fstream file("dane.txt");
    if (!file.is_open()){
        std::cout << "Error while opening file";
        return -1;
    }

    std::string line;
    std::string temp[5];
    while (!file.eof()){
        getline(file, line);
        std::istringstream s(line);
        for(int i=0; i<5; i++)
            s >> temp[i];
        parse_iris(temp, irises);
    }

    print_iris_vector(irises);
    return 0;
}
