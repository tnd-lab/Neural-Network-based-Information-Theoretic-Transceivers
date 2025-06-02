# Neural Network-based Information-Theoretic Transceivers for High-Order Modulation Schemes
**Ngoc Long Pham and Tri Nhu Do**

## Abstract

Neural network (NN)-based end-to-end (E2E) communication systems, where each system component can be a portion of a neural network, have been explored as potential tools for developing artificial intelligence (AI)-native E2E systems. In this paper, we propose a NN-based bitwise receiver that enhances computational efficiency while maintaining performance comparable to baseline demappers. Building on this foundation, we introduce a novel symbol-wise autoencoder (AE)-based E2E system that jointly optimizes the transmitter and receiver at the physical layer. We evaluate the proposed NN-based receiver using bit-error rate (BER) analysis to validate that the numerical BER achieved by NN-based receivers or transceivers is accurate. Results demonstrate that the AE-based system outperforms baseline architectures, particularly under higher-order modulation schemes. We further show that the training signal-to-noise ratio (SNR) level significantly impacts the performance of NN-based systems when inference is performed at different SNR levels.

_Keywords: AI/ML, End-to-End Learning, Log-likelihood Ratio, CNN, AE, Bit-error-rate (BER)_

## Paper
- [PDF on GitHub](./manuscript_v1.pdf)

## Result
### AE-based E2E
![AE-based E2E](https://github.com/tnd-lab/Neural-Network-based-Information-Theoretic-Transceivers/blob/main/images/fig1.png   "AE-based E2E")
### NN-based Demapper
![NN-based Demapper](https://github.com/tnd-lab/Neural-Network-based-Information-Theoretic-Transceivers/blob/main/images/fig2.png    "NN-based Demapper")
### Training Effect of Eb/No on Performance
![Training Effect of Eb/No on Performance](https://github.com/tnd-lab/Neural-Network-based-Information-Theoretic-Transceivers/blob/main/images/fig3.png   "Training Effect of Eb/No on Performance")

##  Setup
```
# create conda env
conda create --name <your-env>
# activate conda
conda activate <your-env>
# install packages
pip install -r requirements.txt
```
In the directory of project, please install the module:
```
pip install -e .
```
