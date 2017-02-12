#Consumer Affairs API

Users can submit reviews for different companies and retrieve their own reviews. To accomplish this...
- Users register themselves and are returned an authenticity token. (If users lose/forget this token, they can login using their registered information to get their token.)

###All following actions require the user's authenticity token.
- Users can submit/create a company for the database.
- Users can retrieve all companies and their information (useful to finding the company id which is necessary to submitting a review).
- Users can retrieve one company's information (useful to finding the company id which is necessary to submitting a review) through an exact name search.

- Users can submit a review for any one company.
- Users can retrieve all the reviews they've written.

All API routes have been tested with [Postman](https://www.getpostman.com/collections/ef9469016f86acb06af1).
