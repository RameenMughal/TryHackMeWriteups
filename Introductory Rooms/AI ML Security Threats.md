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
- a **decision process**, which makes predictions or classifications based on input data;
- an **error function**, which evaluates performance and provides feedback; 
- and a **model optimisation process**, which fine-tunes the algorithm to minimise errors and improve accuracy.

This iterative process continues until the model reaches a satisfactory performance level

ML algorithms fall into four main categories: supervised, unsupervised, semi-supervised, and reinforcement learning. 

**Supervised learning** relies on labeled data to train models for classification or regression tasks, such as predicting house prices or identifying spam emails.

**Unsupervised learning**, on the other hand, works with unlabeled data to discover hidden patterns, often using clustering, association, or dimensionality reduction techniques. 

**Semi-supervised learning** combines elements of both, using a small portion of labeled data to guide the learning process. 

Finally, **Reinforcement learning** mimics human learning by rewarding correct decisions and penalizing mistakes, allowing an agent to refine its actions over time to achieve the best outcome

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

## LLMs

Large Language Models (or LLMs) are deep learning-based AI models that can process and generate text by predicting the next word in a sequence.

LLMs are first trained in a "pre-training" phase, where they process vast amounts of text, GPT-3 alone was trained on data that would take a human 2,600 years to read nonstop. 

More advanced models, like GPT-4, require even greater datasets, made possible by DL. 

Instead of relying on labelled data, LLMs use billions of parameters that function like puzzle pieces, enabling them to understand and generate human-like language when assessed together. 

These parameters are fine-tuned automatically as the model processes text, adjusting based on prediction accuracy to improve response quality. 

They begin by generating a word at random to finish the text

The guess is then compared with what the correct final word actually was, and the parameters are fine-tuned to make it more likely to predict what, in fact, was the right word until the model can accurately predict the correct word to end the sentence (and less likely to choose the incorrect words) using an algorithm called backpropagation

The sheer scope of what is being discussed here is only possible due to advancements in hardware, like GPUs (Graphics Processing Units), enabling masses of parallel operations and processing of large datasets as well as advancements in neural networks, specifically a type of neural network called transformer neural networks.

Introduced in Google's 2017 paper Attention is All You Need, transformer neural networks revolutionized LLMs by enabling parallel text processing instead of sequential word-by-word analysis. This breakthrough allowed models to assign "attention" to key words, improving contextual understanding. By encoding words into numerical values and calculating attention scores, transformers enhance accuracy, helping models correctly interpret ambiguous references, like distinguishing whether "it" in this sentence refers to "the bank" or "the loan."

"The bank approved the loan because it was financially stable." 

After the pre-training, humans come back into play, performing a step called RLHF (Reinforcement Learning from Human Feedback). 

This is when predictions are reviewed, and any that would be considered unhelpful by a user or have issues are flagged and the parameters are adjusted accordingly. 

Once trained and reinforced, the LLM can be used, whether as a translator, chatbot, etc.

A query is fed to it, and using its trained model, it predicts what the next word would be as a response, and so on and so on until the user has a complete response.

Generative AI as a whole extends beyond text, enabling the creation of images, music, and more. 

**Artificial Intelligence (AI)** is the overarching field, encompassing all systems that mimic human intelligence. 

**Machine learning (ML)** is a subfield of AI that enables systems to learn patterns from data without explicit programming. 

**Deep learning (DL)** is then a specialised branch of ML, which uses neural networks to process vast amounts of data in complex ways without the need for human interaction, making it effectively scalable ML. 

**Large Language Models (LLMs)**, like GPT, are advanced DL models built on neural networks, specifically transformers, designed to understand and generate human-like text.

### Answer the questions below

1. What type of AI model enabled major advancements in ChatGPT and similar tools?

Large Language Models

2. What is the first training stage where an LLM processes massive amounts of data?

Pre-training

3. What type of neural network introduced by Google in 2017 powers modern LLMs?

Transformer

## AI Security Threats

We will discuss AI security threats across two categories: Vulnerability in AI Models (New threats introduced by the inclusion of AI technology in business operations) and existing attacks that can now be enhanced by leveraging AI.
the ATT&CK Framework goes over cyber security attacks, breaking down the steps an attacker could take to compromise a system.

### Vulnerabilities in AI Models

1. **Prompt Injection**: Prompts are used to instruct the model on how to perform. Prompt injection occurs when the original instructions provided to the model are overridden, often for malicious purposes such as disclosing more information than it should, or generating harmful content.

2. **Data Poisoning**: Data poisoning is when an attacker manipulates the training data/corpus used to train an AI model so its generated output is incorrect or biased. 

3. **Model Theft**: Model theft occurs when an attacker gains unauthorised access to an AI model. From there, the attacker could potentially steal the intellectual property that lies within and even use it for malicious purposes. This attack is possible by querying the API of the ML model they want to steal. They would then use the output to train a clone model that mimics the behaviour of the original.  

4. **Privacy Leakage**: A privacy leakage vulnerability in AI models refers to the possibility of an AI model inadvertently revealing sensitive information about the data it was trained on, even if the data was supposed to be kept confidential.

5. **Model Drift**: Model drift refers to the potential for a Model's performance to drift over time due to changes in the data or the environment surrounding it. You may recall the discussion of the need to retrain models over time in earlier tasks; this is due to model drift, which is why monitoring an AI model once it has been deployed and is being used is so important. For example, this can occur when a model trained on historical data starts to perform poorly when new data is being processed.

### Enhanced Attacks

1. **Malware**: Attackers can generate malware instantly by a few taps through chatbot, simplifying the task and making it easier for them to attack using this method. 

2. **DeepFakes**: A key cornerstone of security is authentication. The recent advancements in generative AI have led to an explosion of rapid progress in the DeepFake field. This means that if trained on enough data, an AI can now generate a person's likeness, whether that be their voice or their image, to a stunning degree of accuracy, fooling even the technically savvy.

3. **Phishing**: With generative AI, attackers can now generate detailed, fluent, context-based emails that replicate an email a certain user might receive, with little effort and regardless of their writing abilities. With this enhancement to phishing attacks, phishing emails have suddenly become a lot harder to spot using solely our instinct. Of course, models like GPT, for example, have built-in mechanics to stop users from asking for malicious content to be generated, like a phishing email (or malware), but using some of the model vulnerabilities discussed above, attackers are sometimes able to bypass this by engineering their prompts.

### Answer the questions below

1. What framework was developed by MITRE to guide the understanding of AI-specific cyber threats?

ATLAS

2. What type of attack involves cloning an AI model by interacting with its API?

Model Theft

3. What generative AI technique can replicate a person’s voice or appearance with high realism?

DeepFake

4. What common social engineering attack has become harder to detect due to AI-generated fluent and convincing messages?

Phishing

## Defensive AI

Let's consider some ways AI can help us in this industry and what we can leverage to see the results just discussed. AI can enhance: 

1. **Our ability to analyse**: If you think about the tasks we do in cyber security every day, many of them involve some kind of analysis. We take in data points and look for patterns and, within those patterns, anomalies. Consider, for example, intrusion detection, where we analyse network traffic patterns to identify unusual activity that may indicate a cyber attack. We can use AI to create a model that can identify the patterns and indicate the attack.

2. **Our ability to predict**: Like the phishing attacks that are hard to predict with the rise of AI,  we can use the help of AI to create a model and train it on various phishing to help us identify phishing emails which can be missed by humans.

3. **Our ability to summarise/digest(?)**: Artefacts that we have to read, understand and digest to gauge the implications of what has happened. These artefacts could be documents or incident reports, and reading them can take up a lot of our time. Now, with the power of AI, we could have these tools summarise the contents of a document for us so we get the cliff notes of it, now being able to move on in minutes or have them summarise an incident that has occurred, even drawing correlations between other incidents which we may not have picked up on.

4. **Our ability to investigate**: Another large part of security is troubleshooting and investigating, working out the root cause of a security issue or identifying what kind of attack we are suffering. We can ask the chatbot about the situation such as logs and it will help us to further investigate by giving output to diagnose the issue.

### Secure AI

Here are some things that can be done to secure AI:

1. **Securing AI Models**: Many of the vulnerabilities mentioned in the previous task involved an attacker getting access to sensitive data the model has access to. The key to preventing these kinds of attacks is to secure the models themself. One method of preventing unauthorised access to AI models is by enforcing strict controls over who can interact with them. This will involve implementing strong authentication measures and carefully defining access permission. The use of RBAC (Role-Based Access Control) and MFA (Multi-Factor Authentication) can help restrict access and add an extra layer of security to AI systems.

2. **Privacy Protection**: As discussed, the training data a model is trained on can sometimes contain confidential or sensitive information. For this reason, training data should be treated as any other sensitive data and encrypted.

3. **Implementation of AI Security Standards**: To ensure the security of an AI system, you must implement well-established standards and frameworks. Incorporating these recognised security standards throughout the development, deployment, and maintenance stages means organisations can proactively address potential risks. 

4. **Model Monitoring**: In addition to spotting when a model's performance drops and flagging when it needs to be retrained, monitoring should also detect unexpected behaviour, biases, or anomalies that may indicate a security attack. This can be done using "explainability tools" examples of which include SHAP and LIME.

### Answer the questions below

1. According to IBM, how many days faster does AI help identify and contain breaches?

108

2. What cybersecurity task benefits from AI helping to imagine attacker behavior we might not consider?

Threat Hunting

3. Explainability tools such as SHAP and LIME help with what?

Model Monitoring

## Practical

**Log Analysis**: Logs are the first line of defence in cyber security, but interpreting them quickly is critical, especially when responding to an active incident.

**Phishing Email Detection**: AI can help defenders identify phishing attempts by analysing suspicious emails for common red flags.

**Threat Hunting Scenario**: Threat hunting relies heavily on creativity; defenders must think like attackers to find hidden threats. As previously mentioned, the limit of the human imagination can sometimes lead us to missing potential attack scenarios.

**Content Generation**: AI can assist by generating technical resources like detection rules or regex.

### Answer the questions below

What's the flag? 

THM{443/60/16384}

<img width="766" height="238" alt="image" src="https://github.com/user-attachments/assets/94751e6f-7ceb-42ee-b9b3-d1ac393db784" />

