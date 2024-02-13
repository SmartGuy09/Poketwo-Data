# Pokétwo-Data
## I was bored so some of my discord friends introduced me to [@Pokétwo](https://poketwo.net/) Bot

But since I have no knowledge of pokemon it just made it more boring. SO I made it interesting for myself 😎

_Note : I have provided the `data` folder too so that if any of you just wants the images you can access then **without running the script**_
# FAQs
## What DID you do?
Its simple, I found out that every pokemon image present in this bot is hosted ON ITS OWN CDN `https://cdn.poketwo.net/images/N.png`, then I just played with some numbers and found out that the range on **N** is [1,1010].
Wrote a simple python script `pokemon.py` and downloaded the images by just adding `1` in at the place of `N` in the url {*i am not good at explaining stuff*}

## *huh?* You downloaded THE IMAGES with just numbers (no names)?
Well Initially, Yes! I just downloaded all the `1010` images named as `pokemon_N.png` {*again N ranging [1,1010]*} and saved them in `Data/` directory, 
BUT🍑 I did't stop there I searched a bit and found out about an API **THE POKEAPI** `https://pokeapi.co/api/v2/pokemon/`
I am guessing that the bot uses it too coz the numbers were  BUT that's not important, whats important it I made another script 🎉🎉 `rename.py` (_unique name ik_) to rename all of them.

## What does this `rename.py` do?
It basically fetches the respective number of pokemon with the help of **THE POKEAPI** and renames the image files (having that number in its name in the `Data/` directory) to the actual Name of the pokemon,and that's it

# ⚠ UPDATE ⚠
**I have been scamed!** there are more pokemons in the CDN then I had initially downloaded and I found this **accidentally**. How? you might ask, well I mistakenly add an extra `zero [0]` to the link `https://cdn.poketwo.net/images/10010.png` and it WORKED 🤯 but remember THE LIMIT was from `1` to `1010` then how did `10010` worked?

## How did it work?
Well it looks like there is another series of pokemons starting from `10001` to `10238` but there are many and I mean MANY empty slots in between this series.
Who knows if there are more?

## What did you do about it?
I just downloaded all of them using the `pokemon.py` script by just changing the value of `total_images` from `1010` to `10238` and changed the `start_index` from `1` to `10001`, and when i was done I just ran the `rename.py` without any changes and it just worked **like magic**
