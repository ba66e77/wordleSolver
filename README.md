# Wordle Solver

Wordle Solver is a python based application to help solve [Wordle puzzles](https://www.powerlanguage.co.uk/wordle/). Using a pre-defined dictionary, it calculates a score for each word based on the prevalence of letters in that word, suggests the highest scored word (currently `arose`), and prompts the user for results of playing that word. Then it refines the suggestion based on inputs.

## Dictionary.txt
Words in the dictionary.txt file taken from https://wordfind.com/length/5-letter-words/. Thank you, to who ever put that together.

## Use
1. From the command line, run `python wordleSolver.py`. 
2. When prompted, enter the suggested word.
3. The application will then ask you for the new pattern of correct letters, followed by the list of letters which do not appear in the words (grey letters in Wordle). Currently, incoorectly placed letters are not supported.
4. Repeat process until you have the solve, then kill the application with `ctrl+C`

### example
> Booting up. Just a sec while I load all the things.
> 
> Ready to go. Start with arose
> 
> Enter the word, using hyphens for letters you don't know.: -r---
> 
> What letters are known to not appear in the word?: aose
> 
> Try print
> 
> Enter the word, using hyphens for letters you don't know.: -ri--
> 
> What letters are known to not appear in the word?: aosent
> 
> Try drily
> 
> Enter the word, using hyphens for letters you don't know.: -ri--
> 
> What letters are known to not appear in the word?: aosentdly
> 
> Try crimp


## TODO
1. Boot up time takes a while. Cache the dictionary and weighted word list to save time.
2. Make the application stateful so you don't have to reenter all the excluded letters again every time.
3. Handle yellow letters from Wordle; those that are present but in the wrong position.

### Caveat Emptor
Application is provided without warranty or guarantee of suitability. 
There's basically no error handling, so the garbage you put in will be the garbage it spits out. 
Author takes no responsibility for outcomes of its use, up to and including death, dismemberment, sad-panda feelings, self-loathing, scorn of friends and neighbors, or peril of the user's eternal soul.