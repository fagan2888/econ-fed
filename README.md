# econ-fed

- Ground truth interest rates: https://raw.githubusercontent.com/rodrigo-castellon/econ-fed/master/analysis/ground_truths.json

- Interest rate predictions by neural network: https://raw.githubusercontent.com/rodrigo-castellon/econ-fed/master/analysis/predicted_rates.json

- Directory "econ-fed/econ-data" contains data downloaded from the BLS as well as extractor scripts.

- Directory "econ-fed/econ-fed" contains saved weights of the neural network throughout training.

- Directory "econ-fed/analysis" contains plotting scripts, plots/graphs, and a training log.

![image](https://github.com/rodrigo-castellon/econ-fed/blob/master/analysis/timegraph5.png?raw=true)

Black represents the real federal funds rate in any given year. Blue represents the output of the Taylor rule. Red represents the output of the neural network.
