# Second Order Meta-Optimized Neural Network
<b>By:</b> John Mckinstry <b>Mentor:</b> Dr. Steve Beaty

<b>Summary:</b> During this independent study, I developed a way to improve an existing Neural Evolution of Augmenting Topologies algorithm. The existing algorithm, created by CodeReclaimers, is located here: 
<br /> <br />
https://github.com/CodeReclaimers/neat-python
<br /> <br />
Before I knew I wanted to research this algorithm more, a few weeks was spent trying to understand how they were able to create this algorithm and how I could "hack" it so I could use it on actual datasets. I had looked through their examples and tried to figure out which one would be the easiest example to hack. I eventually used the "XOR" example and adjusted the code to allow the use of custom data instead of their "XOR" data.
<br /> <br />
Once I had adjusted the code and corrected any obvious errors (i.e. creating the inputs/outputs variable for every genome), I started to manipulate the base configuration file and did what I could to understand the overall behavior of the algorithm. After a few weeks of learning and manipulating I realized that I could add another Genetic Algorithm on top of the NEAT algorithm to automate the search for the best set of settings. 
<br /> <br />
The following steps summarize my application of another genetic algorithm (aka GA<sub>2</sub>) to the existing NEAT algorithm:
<br /> <br />
<b>Initialize every genome inside GA<sub>2</sub>'s population with a randomly established configuration file.</b> <br />
I had found that the initial population size of a Genetic Algorithm is an important research topic but I had decided to stick with a small population size (~10) to minimize the total computational time.
<br /> <br />
<b>Let each NEAT run for 300 generations using that unqiue config. file and return the fitness score.</b> <br />
The fitness score, in this particular case, was calculated by finding the difference between the model's fitted value and the dataset's actual value. The dataset was a chaotic time series that was also transformed into a percentage change from t<sub>n-1</sub> to t<sub>n</sub>
<br /> <br />
<b>After GA<sub>2</sub>'s entire population ran, the top 90% were selected for crossover.</b>
<br /> <br />
<b>During the crossover, a new agent is created by selecting a random trait (for every trait under consideration) from every possible pair combination of the top 90%.</b> <br />
The number of hidden layers, which activation function to use, the NEAT's population size, and whether the NEAT was Feedforward or Recurrent were a few of the traits under consideration.
<br /> <br />
<b>Repeat 2-4 until the specified generations for GA<sub>2</sub> is met.</b>
<br /> <br />

<b>Results:</b> Towards the end of the independent study, I discovered that by adding another genetic algorithm to the existing NEAT algorithm I was able to improve the possible application of this algorithm by automating the process of finding which set of settings were needed to optimize the model's ability to map a particular dataset's inputs to expected outputs. The improvement from the NEAT's base configuration file to the Meta-Optimized configuration file was significant even though the time complexity of adding another genetic algorithm increased by almost 110000%.
