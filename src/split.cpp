
#include <cstdlib>
#include <string>
#include <fstream>
#include <iostream>

int main(int argc, char* argv[])
{
    if (argc != 2) {
        std::cout << "Usage: "
                  << argv[0]
                  << " <input file>\n";
        exit(EXIT_SUCCESS);
    }

    std::string word;
    std::fstream file;
    file.open(argv[1]);

    while (file >> word) {
        std::cout << word << '\n';
    }
}


