#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

class lookupFile
{
    ifstream inputFile;
    vector <string> fileList;
    string line;
    bool isFileLeft;

    void populateDS()
    {
        //int counter = 0;
        if (inputFile.is_open())
        {
            while (getline(inputFile, line) /*&& (++counter % 1000 != 0)*/)
                fileList.push_back(line);
        }
    }
public:
    lookupFile(string fileName)
    {
        inputFile.open(fileName.c_str());
        isFileLeft = 0;
    }

    vector <string> lookForFilePattern(string searchString)
    {
        populateDS();
        vector <string> retval;
        for(int i = 0; i < (int)fileList.size(); i++)
        {
            size_t found = fileList[i].find(searchString);
            if (found != std::string::npos)
                retval.push_back(fileList[i]);
        }
        return retval;
    }

    ~lookupFile()
    {
        inputFile.close();
    }
};


//Driver Program
/*
int main(int argc, char** argv)
{
    lookupFile obj1("sampleInput");
    vector <string> results = obj1.lookForFilePattern("Sample");
    cout<<"Size is "<<results.size();
    return 0;
}
*/
