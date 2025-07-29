# CIFAR-10 Image Classifier 

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-orange.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A PyTorch-based neural network that classifies images from the CIFAR-10 dataset.

---

## 💻 how to run
 
*(Tested on macOS/Linux with Python 3.8+)*

### step 1: clone & navigate
```bash
git clone https://github.com/RohanShukla23/cifar10-classifier.git
cd cifar10-classifier
```

### step 2: set up a virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

### Step 3: install dependencies
```bash
pip install -r requirements.txt
```

### Step 4: download dataset
The CIFAR-10 dataset will auto-download when you first run the project. Just make sure you have ~170MB of free space.

### Step 5: train the model
```bash
python train.py
```
brew some coffee like I did ☕ — training takes ~15 minutes on a decent CPU (or ~5 mins with an NVIDIA GPU).

---

## 🗂️ what’s inside?
project organization:
```
cifar10-classifier/
├── cifar/ # Auto‑downloaded CIFAR‑10 dataset
├── configs/ # Configuration files (e.g. training hyperparameters)
├── logs/ # Training and evaluation logs
├── models/ # Saved model checkpoints
├── src/ # Source code (data loaders, models, training & eval scripts)
├── .gitattributes # Git attributes configuration
├── LICENSE # MIT license file
└── README.md # This file
```

---

## 🤝 contributions
found a bug? want to add a new model? great!  
1. Fork the repo  
2. Create a branch (`git checkout -b cool-new-feature`)  
3. Commit your changes  
4. Push to your branch  
5. Open a PR  

---

## 📜 License
MIT License - see [LICENSE](LICENSE) for details.  
*credit me if you reuse this code please*

---

## 🙏 Acknowledgments
- CIFAR-10 dataset by Alex Krizhevsky
- my coffee machine :)

---
