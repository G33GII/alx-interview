#!/usr/bin/node

const https = require('https');

const getCharacters = (movieId) => {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    https.get(url, (res) => {
        let data = '';

        res.on('data', (chunk) => {
            data += chunk;
        });

        res.on('end', () => {
            try {
                const filmData = JSON.parse(data);
                const charactersUrls = filmData.characters || [];

                charactersUrls.forEach((characterUrl) => {
                    https.get(characterUrl, (charRes) => {
                        let charData = '';

                        charRes.on('data', (chunk) => {
                            charData += chunk;
                        });

                        charRes.on('end', () => {
                            try {
                                const charInfo = JSON.parse(charData);
                                console.log(charInfo.name);
                            } catch (e) {
                                console.error('Error parsing character data:', e);
                            }
                        });
                    }).on('error', (e) => {
                        console.error('Error fetching character:', e);
                    });
                });
            } catch (e) {
                console.error('Error parsing film data:', e);
            }
        });
    }).on('error', (e) => {
        console.error('Error fetching film data:', e);
    });
};

const movieId = parseInt(process.argv[2], 10);

if (Number.isNaN(movieId)) {
    console.error('Invalid Movie ID. Please provide a numerical value.');
    process.exit(1);
}

getCharacters(movieId);
