/*
 * Universal.cpp
 *
 *  Created on: Oct 25, 2020
 *      Author: Lauren Korbel, Andrew Shine, and Ashley Yeung
 *  This file will contain all of the function definitions for class Universal
 */
#include <string>
#include "../include/Universal.h"

//Universal::Universal() {}

Universal::Universal() 
	: text(NULL), content(NULL)  {}

Universal::Universal(std::string post_text, std::string post_content) 
	: text(post_text), content(post_content) {}

Universal::~Universal() {}

void Universal::post_Twitter() {
	std::sring json = "";
	json += "{\"created_at\" : \"Thu Apr 06 15:24:15 +0000 2017\" , "
	json += "\"id_str\" : \"Today\", "
}

//void Universal::post_LinkedIn() {
//}
