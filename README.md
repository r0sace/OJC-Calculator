# Onions, Jalapenos, Cilantro Calculator

The OJC Calculator is a tool that combats inaccurate prepping by providing recipe dependent calculations of onions, jalapenos, and cilantro that can be used at any and all Chipotle locations.

<img src="https://im3.ezgif.com/tmp/ezgif-3-72822f3bf9.gif" alt="OJC" />

# About the Project
The OJC Calculator is a passion project I created while working at Chipotle Mexican Grill. 

Each morning we are tasked with dicing fresh onions, jalapenos, and cilantro to add into our rices, salsas, and guacamole. I found that we often had diced more onions, jalapenos, and cilantro than needed. As a result of overprepping, there was an unnecessary increase in food waste and decrease in morning productivity. The culprit of our wastefulness was the calculations being generated by our current prep tools.

The previous system we used to calculate OJC needs relied on two factors: 1) your restaurant has nearly perfect inventory and usage counts and 2) you are opening with no held-overnight prep items. These scenarios are certainly _not impossible_ but are an exception rather than the rule. So why is this the way in which each restaurant's numbers are being generated? Why are the OJC needs different across stores even when they are prepping identical amounts of salsa, rice, or guacamole? Thus the idea of the OJC Calculator was born! 

Rather than relying on the restaurant dependent factors our previous system used, the OJC Calculator combats inaccurate prepping by basing its calculations on the universal Chipotle recipes. The OJC Calculator can be used at any and all Chipotle locations.
 
 # Challenges
 * Gathering Data & Ensuring Proper Calculations
      * I needed to figure out a way to convert the recipes from cups of OJC to oz of OJC
      * After weighing out each ingredient, it was necessary to test and find a sweet-spot average weight of each cup that would never result in underprepping, but could result in very slight overprep for worst case scenarios
      * After many trial runs, I landed on a few magic numbers and converted our recipe's cup unit into oz units per item. I then turned each recipe into an equation that would calculate the amount of OJC depending on the needs of that ingredient.
 * Designing a GUI
     * I spent a lot of time figuring out a design that would be aesthetically pleasing while also optimally organizing the information it provided. 

