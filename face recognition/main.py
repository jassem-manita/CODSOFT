# main.py

from src.generate import extract_features, generate_caption, define_model
from PIL import Image
import matplotlib.pyplot as plt
import pickle
import numpy as np

def main(image_path):
    # Load the tokenizer
    with open('tokenizer.pkl', 'rb') as f:
        tokenizer = pickle.load(f)
    
    # Load the model
    model = define_model(vocab_size=5000, max_length=34)  # Replace with actual values
    model.load_weights('model.h5')  # Replace with the path to your trained model

    # Extract features from the image
    features = extract_features(image_path)
    
    # Generate caption
    caption = generate_caption(model, tokenizer, features, max_length=34)
    print("Generated Caption:", caption)

    # Display the image and caption
    image = Image.open(image_path)
    plt.imshow(image)
    plt.title(caption)
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    # Path to the image
    image_path = "data/images/img.jpg"  # Replace with your image path
    
    # Call the main function
    main(image_path)
