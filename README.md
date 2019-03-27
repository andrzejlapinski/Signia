------------------------------------------------------------------
# Programmer test
------------------------------------------------------------------

Your task is to implement the following items into the existing project:
1) A data class to fetch test data via https from our test data resource (see test data below).
2) Implement an api class in the api folder for the data class.
	2.1) The api should have a method that returns the test data
	2.2) The api should be secured using Ouath2
3) Unit tests for both classes


Test data:

curl https://www.mocky.io/v2/5c76b900320000b31cf46398

{
    "data": {
        "test": 123
    },
    "success": true
}



------------------------------------------------------------------
# Project setup
------------------------------------------------------------------

# Prerequisites:
* Python 2.7
* Node.js > 6.9, with npm > 3.0.0

# Setup:
* npm install
* (optional) run pydevproject.py to set up paths for pydev/eclipse

# Run all tests:
* npm run test

# Serve backend (localhost:7070 as default):
* npm run backend
