# beat-name-maker
Simple generator of names (not only) for beats.

When I make beats, often I find myself thinking too much about the name of the beat, so I wanted to make some tool to help me do that. 

The idea of this generator is to put two basic nouns back-to-back to make some interesting new word or a fraze.

I got 600 basic nouns from https://www.thoughtco.com/learn-the-most-important-english-nouns-4087688. They were all in a numbered list so first I had to convert them to JSON for better handeling.

After that I ran into a problem with loading the JSON into javascript because loading local files is not permitted anymore, so I pasted the JSON contents directly to JS. 

And now it's done.
