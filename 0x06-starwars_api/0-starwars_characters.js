#!/usr/bin/node

const request = require('request');

// Retrieve the movie ID from the command-line arguments
const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a movie ID as the first argument.');
  process.exit(1);
}

function printCharacterNamesSequentially (characterUrls) {
  let currentIndex = 0;

  function nextName () {
    if (currentIndex >= characterUrls.length) {
      return;
    }

    const characterUrl = characterUrls[currentIndex++];
    request({ url: characterUrl, json: true }, (error, response, body) => {
      if (error) {
        console.error(`Error fetching character details: ${error}`);
        return;
      }
      console.log(body.name);
      nextName();
    });
  }

  nextName(); // Start processing the characters
}

function printMovieCharacters (movieId) {
  const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

  request({ url: filmUrl, json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error fetching film details: ${error}`);
      return;
    }

    const charactersUrls = body.characters;
    printCharacterNamesSequentially(charactersUrls);
  });
}

// Call the function with the provided movie ID
printMovieCharacters(movieId);
