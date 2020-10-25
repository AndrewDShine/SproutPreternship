/*
 * Universal.h
 *
 *  Created on: Oct 25, 2020
 *      Author: andre
 */

#ifndef UNIVERSAL_H_
#define UNIVERSAL_H_

# include <string>

class Universal {
private:
	// twitter members
	std::string status = NULL;
	std::string attachment_url = NULL;
public:
	Universal();
	virtual ~Universal();
};

#endif /* UNIVERSAL_H_ */
