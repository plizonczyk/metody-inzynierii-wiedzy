#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>

using namespace std;

map <string, int> iris_classes {{"Iris-setosa", 1}, {"Iris-versicolor", 2}, {"Iris-virginica", 3}};

struct Iris {
    float leaf_length;
    float leaf_width;
    float petal_length;
    float petal_width;
    int iris_class;
};


void parse_iris(string* temp, vector <Iris*> & irises){
    Iris* iris = new Iris;
    iris->leaf_length = stof(temp[0]);
    iris->leaf_width = stof(temp[1]);
    iris->petal_length = stof(temp[2]);
    iris->petal_width = stof(temp[3]);
    iris->iris_class = iris_classes[temp[4]];
    irises.push_back(iris);
}


void print_iris_vector(vector <Iris*> & irises){
    for(std::vector<int>::size_type i = 0; i != irises.size(); i++) {
        cout << irises[i]->leaf_length << " " << irises[i]->leaf_width << " " << irises[i]->petal_length << " ";
        cout << irises[i]->petal_width << " " << irises[i]->iris_class << endl;
    }
}


int main() {
    vector <Iris*> irises;
    fstream file("dane.txt");
    if (!file.is_open()){
        cout << "Error while opening file";
        return -1;
    }

    string line;
    string temp[5];
    while (!file.eof()){
        getline(file, line);
        istringstream s(line);
        for(int i=0; i<5; i++)
            s >> temp[i];
        parse_iris(temp, irises);
    }
    return 0;
}
