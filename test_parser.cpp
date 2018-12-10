#include <iostream>
#include <fstream>
#include <stdio.h>
#include <cstring>
#include <string>

using namespace std;

int main()
{
    ifstream file( "all-tests.txt" );

    std::string line, method, path;

    if( file.is_open() )
    {
        while( std::getline( file, line ) )
        {
            const char * char_line = line.c_str();
            char *charLine = strdup( char_line );

            method = std::strtok( charLine, "(" );
            path = std::strtok( NULL, ")" );
            std::cout << path << "::" << method << std::endl;
        }
    }
    file.close();
    return 0;
}
