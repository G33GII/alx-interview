#!/usr/bin/node

// Import the 'request' library
const request = require('request');

// Define constant with the base URL of the Star Wars API
const API_URL = 'https://swapi-api.alx-tools.com/api';

// Check if the number of command line arguments is greater than 2
if (process.argv.length > 2) {
    const movieID = process.argv[2];

    // Make a request to the film resource for the specified film ID
    request(`${API_URL}/films/${movieID}/`, (err, _, body) => {
        // If an error occurred during the request, log the error
        if (err) {
            return console.log(`Error: ${err}`);
        }

        // Try to parse the response body and handle potential errors
        let charactersURL;
        try {
            charactersURL = JSON.parse(body).characters;
        } catch (parseErr) {
            return console.log(`Failed to parse JSON: ${parseErr}`);
        }

        // Create an array of Promises that resolve with the names of the characters
        const charactersName = charactersURL.map(
            url => new Promise((resolve, reject) => {
                // Make a request to the character resource
                request(url, (promiseErr, __, charactersReqBody) => {
                    // If an error occurred during the request, reject the Promise with the error
                    if (promiseErr) {
                        return reject(promiseErr);
                    }

                    // Try to parse the character's body to get the name
                    try {
                        resolve(JSON.parse(charactersReqBody).name);
                    } catch (characterParseErr) {
                        reject(`Failed to parse character data: ${characterParseErr}`);
                    }
                });
            })
        );

        // Wait for all Promises to resolve and log the names of the characters, separated by new lines
        Promise.all(charactersName)
            .then(names => console.log(names.join('\n')))
            .catch(allErr => console.log(`Error fetching characters: ${allErr}`));
    });
} else {
    // If no movie ID is provided, display usage instructions
    console.log('Usage: ./script.js <movie_id>');
}
