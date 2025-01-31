<h1 align="center">Simulating the Hunger Games</h1>

---

<p align="center">My attempt at simulating the Hunger Games using Python. This includes creating a customisable arena, including its resources, and tributes. We can then use this to play Gamemaker and design the perfect Hunger Games for maximum entertainment.
    <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [👷‍♂️ Current Status ](#️-current-status-)
- [⛏️ Built Using ](#️-built-using-)
- [✍️ Author ](#️-author-)
- [🎉 Acknowledgements ](#-acknowledgements-)

## 🧐 About <a name = "about"></a>

Here I am attempting to simulate the Hunger Games. However, I have made my own version of the games with some tweaks that I believe improve the game and help it provide better entertainment.

One problem with the current Hunger Games is the Cornucopia. Concentrating all of the high value resources in the centre of the arena, and starting all the players in the same place gives the players two choices: fight for the best resources, in which case they are likely to die, or run away and try to survive with what little they can find in the rest of the arena, which can be quite boring to watch. Even minecraft hunger games servers figured that resources should be spread out lol.
To fix this I have decided that resources can be generated anywhere, however with the quantity (likelihood of there being a resource on the tile) decreasing but the quality increasing.

Another problem is dying of natural causes. Whilst I understand the morbid entertainment the veiwers may get from watching the tributes fight and kill each other, watching them die of natural causes is not entertaining. So the players should be encouraged to come into contact with each other, increasing the likelihood of a fight. To do this, I will start all the players around the outside ring of the arena, as this prevents too many of them from dying too quickly, but retain a cornucopia style with some of the best resources in the centre, to incentivise all the players to move towards the centre, meeting others along the way.

## 👷‍♂️ Current Status <a name = "current_status"></a>

So far I have created a circular arena (where the size can be customised) with different elevations and terrains that can be displayed using matplotlib. The terrain is determined by the elevation, and the elevation bounds for each of the 4 terrain types (water, sand, grass and rock) can also be customised.

I have also created a resources grid, which adds the resources to the arena following the system I described above. There is then a basic display of the resources on the arena using matplotlib.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Main language
- [Matplotlib](https://matplotlib.org/) - For visualising the arena
- [Numpy](https://numpy.org/) - For creating the arena
- [Opensimplex](https://code.larus.se/lmas/opensimplex) - For generating the terrain using simplex noise

## ✍️ Author <a name = "author"></a>

- [@kaziksobo](https://github.com/kaziksobo)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- [Inspiration](https://www.youtube.com/watch?v=dS3tgfNN1HM) - This excellent video by Ellie Rasmussen heavily inspired this project, and is what I have based this project on.
