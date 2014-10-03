/*
 * This program is a part of Khoj - The multi-platform Local search engine
 *
 * Copyright (C) 2014 Jiban Prakash, jibanprakash.jp(at)gmail(dot)com
 * Saurabh Araiyer,  sizzsa(at)gmail(dot)com
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
 
 /*
  * This program implements the engine to parse and find the required file
  */

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
int main(int argc, char** argv)
{
    lookupFile obj1("sampleInput");
    vector <string> results = obj1.lookForFilePattern("Sample");
    cout<<"Size is "<<results.size();
    return 0;
}
