#include <windows.h>
#include <Lmcons.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;


int main(int arc, char** argv) {

	char username[UNLEN+1];
	DWORD username_len = UNLEN+1;
	GetUserName(username, &username_len);
//	cout << username;
	string user = username;
	
	string filepath = "C:\\Users\\" + user + "\\AppData\\Local\\osu!" + "\\osu!." + user;
	
   string test = "C:\\Users\\1\\Appdata\\Local\\osu!\\osu!.1.cfg";
   
   ifstream file(test.c_str());
   string data = "";
   string line;
   
   while (!file.eof()) {
   	getline(file, line);
   	data += line;
   	data += "\n";
	}
   
   cout << data << endl;
   
	return (EXIT_SUCCESS);
}

