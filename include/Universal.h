/*
 * Universal.h
 *
 *  Created on: Oct 25, 2020
 *      Author: Lauren Korbel, Andrew Shine, and Ashley Yeung
 *  This is the header file for the class containing the universal data structure
 *  It will contain the class Universal and its function declarations
 */

#ifndef UNIVERSAL_H_
#define UNIVERSAL_H_

#include <iostream>

#define COUT std::cout
#define CIN std::cin
#define ENDL std::endl

class Universal {
	private:
		// common fields
		std::string text; // status in Twitter
		std::string content; // attachment_url in Twitter
		/*
		// fields specific to Twitter
		std::string in_reply_to_status_id;
		bool auto_populate_reply_metadata;
		std::string exclude_reply_user_ids;
		std::string media_ids;
		bool possibly_sensitive;
		double lat;
		double longitude;
		std::sting place_id;
		bool display_coordinates;
		bool trim_user;
		bool enable_dmcommands;
		bool fail_dmcommands;
		std::string card_uri;
		*/
		/*
		// fields specific to LinkedIn
		std::string activity; // type is activity URN
		std::string agent; // type is return
		std::string created; // type is audit stamp
		std::string distribution; // type is share distribution target
		bool edited;
		std::string id;
		std::string lastModified; // type is audit stamp
		std::string originalShare; // type is share URN
		std::string owner;
		std::string resharedShare; // type is share URN
		std::string subject;
		std::string clientApp; // type is URN
		*/

		// private constructor that will be called in the public member functions
		Universal();
		Universal(std::string, std::string);

	public:

		virtual ~Universal();

		void post_Twitter();

		void post_LinkedIn();
};

#endif /* UNIVERSAL_H_ */
