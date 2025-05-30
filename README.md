# Neural Network-based Information-Theoretic Transceivers for High-Order Modulation Schemes
**Ngoc Long Pham and Tri Nhu Do**

## Abstract

Neural network (NN)-based end-to-end (E2E) communication systems, where each system component can be a portion of a neural network, have been explored as potential tools for developing artificial intelligence (AI)-native E2E systems. In this paper, we propose a NN-based bitwise receiver that enhances computational efficiency while maintaining performance comparable to baseline demappers. Building on this foundation, we introduce a novel symbol-wise autoencoder (AE)-based E2E system that jointly optimizes the transmitter and receiver at the physical layer. We evaluate the proposed NN-based receiver using bit-error rate (BER) analysis to validate that the numerical BER achieved by NN-based receivers or transceivers is accurate. Results demonstrate that the AE-based system outperforms baseline architectures, particularly under higher-order modulation schemes. We further show that the training signal-to-noise ratio (SNR) level significantly impacts the performance of NN-based systems when inference is performed at different SNR levels.

##  Setup
```
pip install -r requirements.txt
```
In the directory of project, please install the module:
```
pip install -e .
```
##  Plotting 
We save our results in csv file then illustrate them in the [plot](https://github.com/tnd-lab/NgocLongPham_E2E_journal_conf/tree/main/plot) folder


