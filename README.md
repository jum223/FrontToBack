# FIN377 (Data Science for Finance) Final Project - Industry Returns throughout the Russia-Ukraine War
### Project Contributors: Luca Fontaine, Matthew Sam, and Juan Mozos Nieto. 

## Project's Purpose

The main goal of this project is to explore how different industries are affected by the Russian-Ukrainian armed conflict that started on the 24th of February of 2022. In order to do so, we analyzed how different industries' returns were affected by a number of major events throughout the course of the war. We used a total of 17 major events and saw how cumulative returns for 5 industries, namely metal, energy, semiconductors, food, and transport industries, changed. In order to perform our analysis we used line-plots and computed return differences between the event date, 3 days after the event and 10 days after the event.

**To see and interact with the visualizations we based our analysis on, please visit the [home page](https://russiaukrainewarindustryreturns.streamlit.app) of our dashboard. This page will allow you to select a number industries at a time (or all of them) and events based on their description which will then output a line graph based on the desired industry and event choices**

**For further details on the data we used to produce the visualization, the methodologies used to produce the code that produces the visualizations, our findings and the conclusions we reached please visit our dashboard's [analysis section](https://russiaukrainewarindustryreturns.streamlit.app/#analysis)**

## Summarized Findings

Enter a very brief summary of our findings here after we are done with the report 

## How to Run the Code

In order to run, test the code, or deploy the dashboard itself please follow these steps:

1. First, clone this repo into your own machine, in order to do this you will have to run the following command <git clone https://github.com/jum223/FrontToBack> wherever you desire to store this repo. 
2. Second, run the file called DataDownload.ipynb found in the code folder of the repo.
3. Third, run the file called MainBuild.ipynb fond in the code folder of the repo.
4. Then, open a terminal in your machine, and access the location where you cloned this repo using a cd statement in the form of ```cd <the path to the repo in your machine>```. Once this is done you will have to run the following command: ```<streamlit run Dashboard.py>```. You will see a tab open up in your browser with the Dashboard created here. 
    
Please refer to the section below for instructions on the necessary installations you will need to run the code.

## Necessary packages and installations

In order to make this code work there are a number of packages and libraries which you will need to download. First you have to download [git](https://git-scm.com/downloads), this will allow you to run the git clone command specified in the section above. It is also necessary to have a environment where you can run python code. I would recommend downloading [anconda](https://www.anaconda.com). This will the allow you to open the cloned repository on jupyter labs, which will allow you to run the python code contained in the .ipynb files. Once that is done, it will be necessary to open a terminal or a command line interface to download the necessary packages. These are the necessary packages:

- pandas
- numpy
- pandas_datareader
- yfinance
- datetime
- seaborn
- matplotlib

In order to download these packages type into the command-line argument interface the following: pip install <library_name>. Once this is done you should be able to run all the code in this directory. Make sure that you run all of the import statements that appear through the .ipynb file. In order to run this then clone this repository from github into your own machine, then use the command line argument interface to access that repository by running the command "jupyter lab". This will open a tab in your web browser that will allow you to successfully run the code on your machine. Remember to follow the running steps highlighted above.

## About the team

<img src="pics/julio.jpg" alt="julio" width="300"/>
<br>
Julio is a senior at Lehigh studying finance.
<br><br><br>
<img src="pics/don2.jpg" alt="don" width="300"/>
<br>
Don is an assistant professor at Lehigh.


## More 

To see the files which produced the visualizations shown in the dashboard please see our [build file](https://github.com/jum223/FrontToBack/blob/main/Code/MainBuild.ipynb).
