# econ-fed

### ABSTRACT
This is a special report that will detail the economic landscape in May of 2018 and recommend a monetary policy response based on those details. Recognizing that the Federal Reserve monetary policy actions can essentially be approximated as a complex mathematical function that receives a large amount of different variables (economic indicators such as inflation, unemployment, capital flows, retail sales, personal income, or balance of payments) and outputs a single number (the target federal funds rate), we exploited the inherent effectiveness of neural networks of regression tasks on high dimensional inputs and implemented a novel algorithm which does effectively the exact same job as the Federal Reserve: it can take a high number of economic indicator inputs and outputs the target federal funds rate. To ensure that the output is appropriate, the algorithm learned from the past 64 years of Federal Reserve behavior since 1954 and associated economic conditions, continually learning to emulate the actions of the Federal Reserve in various economic situations. Once trained, the neural network was evaluated. The neural network performed surprisingly well, deviating from the real federal funds rate on average by 1.8% compared to the Taylor rule, which deviates by 2.3% on average. Finally, the neural network was run on current economic indicators, predicting that the Federal Reserve will set a short-term federal funds rate of 3.49%. Thus, we conclude that the Fed has set interest rates far too low, and should hike up interest rates to return to equilibrium and avoid a possible recession.

The network is not temporal, in that for predicting interest rate of month `n` it does not take into account the interest rate in month `n-1`. It is only told the unemployment rate, GDP growth rate, and the inflation rate for month `n`.

- Ground truth interest rates: https://raw.githubusercontent.com/rodrigo-castellon/econ-fed/master/analysis/ground_truths.json

- Interest rate predictions by neural network: https://raw.githubusercontent.com/rodrigo-castellon/econ-fed/master/analysis/predicted_rates.json

- Directory "econ-fed/econ-data" contains data downloaded from the BLS as well as extractor scripts.

- Directory "econ-fed/econ-fed" contains saved weights of the neural network throughout training.

- Directory "econ-fed/analysis" contains plotting scripts, plots/graphs, and a training log.

![image](https://github.com/rodrigo-castellon/econ-fed/blob/master/analysis/timegraph5.png?raw=true)

Black represents the real federal funds rate in any given year. Blue represents the output of the Taylor rule. Red represents the output of the neural network.
