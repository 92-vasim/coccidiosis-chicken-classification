# Coccidiosis Chicken Disease Classification

<!-- ![Coccidiosis](link_to_image.jpg) -->

## Table of Contents

- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Technology Stack](#technology-stack)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Deployment](#deployment)
- [Modular Programming](#modular-programming)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Coccidiosis Chicken Disease Classification project utilizes deep learning techniques to classify images of chickens into healthy or infected with Coccidiosis, a common poultry disease. The project leverages state-of-the-art VGGNet architecture for image classification and deploys the model using FastAPI. It also incorporates version control with Git, GitHub, and Data Version Control (DVC), and employs Google Cloud for deployment.

## Project Overview

- **Image Classification**: The project focuses on classifying chicken images into two categories: healthy and Coccidiosis-infected.

- **VGGNet**: We employ the VGGNet architecture, known for its excellent performance in image classification tasks, as the backbone for our model.

- **FastAPI Deployment**: The model is deployed as an API using FastAPI, allowing users to make real-time predictions by sending images to the API endpoint.

- **Version Control**: Git and GitHub are used for version control, making it easy to collaborate, track changes, and manage the project's codebase.

- **Data Version Control (DVC)**: DVC is used to manage large datasets and ensure data reproducibility in machine learning experiments.

- **Google Cloud**: The project utilizes Google Cloud for deployment, ensuring scalability and reliability in serving the model to users.

- **Modular Programming**: The codebase follows a modular programming approach, making it maintainable and extensible.

## Dataset

The dataset used for this project consists of labeled chicken images, categorized as healthy or infected with Coccidiosis. The dataset is available [here](https://github.com/92-vasim/datasets/raw/main/Chicken-fecal-images.zip).

## Technology Stack

- Python
- VGGNet
- FastAPI
- JavaScript
- Bootstrap (CSS Framework)
- Git and GitHub
- Data Version Control (DVC)
- Google Cloud

## Requirements

To run this project locally or deploy it, you need the following dependencies:

- Python 3.6+
- TensorFlow (for VGGNet)
- FastAPI
- Git
- DVC (optional)
- Google Cloud SDK (for deployment)

You can install these dependencies using the instructions in the next section.

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/92-vasim/coccidiosis-chicken-classification.git
   ```

2. Navigate to the project directory:

   ```bash
   cd coccidiosis-chicken-classification
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Preparation**: Download and preprocess the dataset. You can follow the data preparation instructions provided in the `research/data_ingestion.ipynb` notebook.

2. **Model Training**: Train the Coccidiosis classification model using the `research/04_training.ipynb` notebook. You can also experiment with different hyperparameters and data augmentation techniques to improve model performance.

3. **Deployment**: Deploy the trained model using FastAPI.

4. **API Usage**: Once the API is deployed, you can make predictions by sending POST requests with images to the API endpoint.

## Modular Programming

The project codebase is organized into modular components, making it easier to maintain and extend. Each major functionality, such as data preprocessing, model training, and API deployment, is encapsulated in separate modules and notebooks.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
