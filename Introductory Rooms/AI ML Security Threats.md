# AI/ML Security Threats

## The Building Blocks of AI

Artificial intelligence refers to a machine or computer system that is able to carry out tasks that would otherwise require human reasoning, comprehension, problem-solving, or creativity.

### Machine Learning
ML follows a structured lifecycle to ensure the reliable development and deployment of models. 

This process begins with defining the problem, such as determining whether an email is spam. Next, data is collected, cleaned, and prepared through feature engineering, ensuring meaningful patterns are extracted while avoiding overfitting (When a model's familiarity with the training data causes a failure to make generalisations on unseen/raw data).

The model is then trained using a selected algorithm, followed by evaluation and tuning to optimise performance. 

Once refined, the model is deployed into a production environment for real-world use, such as classifying emails in real-time. 

However, the lifecycle doesn’t end there—ongoing monitoring ensures the model maintains accuracy over time, triggering retraining when needed. Since models require continuous improvement, the Machine Learning Lifecycle remains an iterative process.

### Machine Learning Algorithms

ML algorithms are the mathematical methods used to learn patterns from data, while ML models are the trained outputs derived from these algorithms. 

These algorithms consist of three key components: 
- a decision process, which makes predictions or classifications based on input data;
- an error function, which evaluates performance and provides feedback; 
- and a model optimisation process, which fine-tunes the algorithm to minimise errors and improve accuracy.

This iterative process continues until the model reaches a satisfactory performance level

ML algorithms fall into four main categories: supervised, unsupervised, semi-supervised, and reinforcement learning. 

Supervised learning relies on labeled data to train models for classification or regression tasks, such as predicting house prices or identifying spam emails.

Unsupervised learning, on the other hand, works with unlabeled data to discover hidden patterns, often using clustering, association, or dimensionality reduction techniques. 

Semi-supervised learning combines elements of both, using a small portion of labeled data to guide the learning process. 

Finally, reinforcement learning mimics human learning by rewarding correct decisions and penalizing mistakes, allowing an agent to refine its actions over time to achieve the best outcome

### Neural Networks and Deep Learning

The main objective of AI is to enable computers to behave like humans. One method that allows us to do this is through the use of neural networks.

The human brain processes information using interconnected neurons (a type of cell responsible for transmitting communications between the body and brain), which communicate with each other using synapses. 

Synapses allow the brain to send electrical/chemical signals from neuron to neuron; in other words, they are a connection. 

This network of neurons learns by adjusting the strengths of these connections when we experience something new based on patterns we encounter. 

It's this behaviour that is replicated in a neural network.

Like the human brain processes sensory input, the input layer receives raw data, with the number of nodes depending on the data type (e.g., a 4x4 pixel image has 16 nodes). 

Each node represents a neuron, and connections between them act as synapses. 

The hidden layers process and refine the input, bringing the network closer to a prediction. Each connection has a weight, determining its importance—for example, in email classification, the body text might have more weight than the subject line. 

The output layer then produces the final prediction.

When a network has more than three layers, it is classified as a DL algorithm—hence the term "deep learning."

But the key difference is that DL doesn't need the data to be labelled. A DL algorithm can take unlabelled, unstructured raw data and determine its key features, which separate it from other categories. The important advantage here over ML is that the data doesn't need labelling; this means DL doesn't require human interaction 

### Answer the questions below
1. What category of machine learning combines both labelled and unlabelled data?

Semi-supervised Learning

2. What is the first layer in a neural network that handles incoming raw data?

Input layer

3. Which learning method does not require human-labeled data and can extract features from raw, unstructured input?

Deep Learning

4. What are the weighted connections between nodes in a neural network meant to simulate in the human brain?

Synapses
