#Consumer Affairs API

Users can submit reviews for different companies and retrieve their own reviews. To accomplish this, users register themselves and are returned an authenticity token. (If users lose/forget this token, they can login using their registered information to get their token.)

###All following actions require the user's authenticity token.
1. Users can submit/create a company for the database.
2. Users can retrieve all companies and their information (useful to finding the company id which is necessary to submitting a review).
3. Users can retrieve one company's information (useful to finding the company id which is necessary to submitting a review) through an exact name search.
4. Users can submit a review for any one company.
5. Users can retrieve all the reviews they've written.

All API routes have been tested with [Postman](https://www.getpostman.com/collections/ef9469016f86acb06af1).

A more thorough explanation of all API routes are documented in specifications.txt found in root directory.
