// https://zerodayhacker.com/exporting-a-postman-collection-to-openapi-3-0/

const fs = require('fs');

const collection = require('./data/postman-collection'); // any Postman collection JSON file

const { transpile } = require('postman2openapi');

// Returns a JavaScript object representation of the OpenAPI definition.
const openapi = transpile(collection);

fs.writeFileSync(
    './data/swagger-api.json', 
    JSON.stringify(openapi, null, 2)
);
