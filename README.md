# 🖼️ CIFAR-10 Image Classifier 

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![PyTorch](https://img.shields.io/badge/PyTorch-1.12%2B-orange.svg)](https://pytorch.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A PyTorch-based neural network that classifies images from the CIFAR-10 dataset. Perfect for learning CNNs or as a starter project for image classification tasks! 🚀

---

## 💻 How to Run This Project

**Let’s get you up and running in 5 minutes!**  
*(Tested on macOS/Linux with Python 3.8+)*

### Step 1: Clone and Navigate
```bash
git clone https://github.com/RohanShukla23/cifar10-classifier.git
cd cifar10-classifier
```

### Step 2: Set Up a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Download the Dataset
The CIFAR-10 dataset will **auto-download** when you first run the project. Just make sure you have ~170MB of free space!

### Step 5: Train the Model
```bash
python train.py
```
Grab some coffee ☕ — training takes ~15 minutes on a decent CPU, or ~5 mins with an NVIDIA GPU.

---

## 🗂️ What’s Inside?
Here’s how the project is organized:
```
cifar10-classifier/
├── data/           # Auto-downloaded CIFAR-10 dataset
├── models/         # Model definitions (ResNet, CustomCNN, etc.)
├── utils/          # Helper scripts (data loaders, metrics)
├── train.py        # Training script
└── requirements.txt
```

---

## 🤝 Contributing
Found a bug? Want to add a new model? Awesome!  
1. Fork the repo  
2. Create a branch (`git checkout -b cool-new-feature`)  
3. Commit your changes  
4. Push to your branch  
5. Open a Pull Request  

---

## 📜 License
MIT License - see [LICENSE](LICENSE) for details.  
*Go wild, but credit me if you reuse this code!*

---

## 🙏 Acknowledgments
- CIFAR-10 dataset by Alex Krizhevsky
- PyTorch community for amazing tutorials
- Coffee, for keeping me awake through debugging

---