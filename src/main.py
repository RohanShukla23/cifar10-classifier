import argparse
import yaml
from train import train_model

def main():
    parser = argparse.ArgumentParser(description='CIFAR-10 Classification Training')
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()

    with open(args.config, 'r') as f:
        config = yaml.safe_load(f)

    print("Starting training with configuration:")
    print(yaml.dump(config, default_flow_style=False))
    
    trained_model = train_model(config)

if __name__ == '__main__':
    main()