# <p align="center">Onions, Jalapenos, Cilantro Calculator </p>



The OJC Calculator is a tool that combats inaccurate prepping by providing recipe dependent calculations of onions, jalapenos, and cilantro that can be used at any and all Chipotle locations. 

Both macOS and Windows versions are available for download in releases.

<p align="center"><img src="https://i.imgur.com/9Mh6Ct9.gif" alt="OJC" /></p>
<p align="center"><img src="http://ForTheBadge.com/images/badges/made-with-python.svg" /><

 
 # What It Does
 The OJC Calculator accurately calculates how many onions, jalapenos, and cilantro are required for the needs of each prep item as entered by the user. The OJC Calculator gives a breakdown of the amount of OJC in each item and gives the total amount needed. Say goodbye to inaccurate prepping!
 
 # How I Built It
 The OJC Calculator is built using the OOP paradigm and MVC design pattern.
 
 I used the following technologies:
 
 * Python 3
 * PyQT5
 * PyInstaller
 * GitHub for version control
 
# About the Project
The OJC Calculator is a passion project I created while working at Chipotle Mexican Grill. 

Each morning we are tasked with dicing fresh onions, jalapenos, and cilantro to add into our rices, salsas, and guacamole. I found that we often had diced more onions, jalapenos, and cilantro than needed. As a result of overprepping, there was an unnecessary increase in food waste and decrease in morning productivity. The culprit of our wastefulness were the calculations being generated by our current prep tools.

The previous system we used to calculate OJC needs relied on two factors: 1) your restaurant has nearly perfect inventory and usage counts and 2) you are opening with no held-overnight prep items. These scenarios are certainly _not impossible_ but are an exception rather than the rule. So why is this the way in which each restaurant's numbers are being generated? Why are the OJC needs different across stores even when they are prepping identical amounts of salsa, rice, or guacamole? 

Rather than relying on the restaurant dependent factors our previous system used, the OJC Calculator combats inaccurate prepping by basing its calculations on the universal Chipotle recipes. The OJC Calculator can be used at any and all Chipotle locations.
 
 # Challenges
 * Gathering Data & Creating a Standard Equation
      * I needed to figure out a way to convert the recipes from cups of OJC to oz of OJC
      * It was necessary to test and find a sweet-spot average weight (in ounces) for each cup of OJC. The trick here was to find an average weight that would never cause us to underprep, but at worst case scenario, cause a very slight overprep. 
      * After many trial runs, I got my numbers and converted our recipes from cups to oz.
      * I then turned each recipe into an equation that factored in the needs of salsas, guac, and rices to calculate the OJC usage directly.
      
 * Designing a GUI 
     * I have never designed a Python GUI before, so naturally there was a learning curve in implementing PyQT. I pretty much self-taught through some Youtube tutorials and a few helpful articles. Things like importing custom fonts, spacing, widget design, and images gave me the most trouble.
     * Organizing the information was another challenging aspect of the GUI. I wanted to present the information in an aesthetically pleasing yet organized way, but often found myself with an app that looked too bare - prep item, needs and a total.
     * After brainstorming, the idea of including a break down of how much OJC is being used in each item came about. Not only would it fill in the gaps of my pretty bare and boring looking app, but it would also give an additional functionality to the app and help to demystify where the calculations are coming from.
     * I also did not use PyDesigner or a layout, instead it is all hard-coded. This caused a lot of headache during packaging. I now know the importance of layouts when it comes to scalability.

* Packaging 
     * This was the first project I have ever packaged into an executable.
     * For some time my pictures and fonts were not being included into my executables, which made my app look pretty crazy, especially when running on Windows. <img src="https://www.simpleimageresizer.com/_uploads/photos/cc516b08/Screen_Shot_2022-07-18_at_2.16.38_PM_2_36.png"/>
     * I learned how to use base64 to ensure that my pictures would be included in my executables by converting my pictures to strings. This was probably the most interesting thing I learned while working on this project.
     * I did some research on custom fonts and how to include them into the directory because the PyInstaller docs are outdated. I found that importing resources required a function to find the absolute path to the resource in the temporary folder that PyInstaller creates when packaging up the project. After including this piece of code, my font databases were imported and this fixed most of my scalability and cross-platform issues.
     * I packaged this on a Mac which created a Mac file when it is suposed to be for Chipotle's computers, which run on Windows. I hopped on a virtual desktop and packaged it up for Windows. Now, I have the executables for both, which is pretty neat. 
     
# What's Next?
 I am very happy with the way my OJC Calculator came out and the results I have seen in using it at my store. As far as the code goes, I would love to fix up the GUI and scrap the hard-coding design elements I did and position everything within a layout. My plan is to keep this thing updated to reflect any new items the company may roll out that requires diced OJC.
