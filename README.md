# Generalized Top-k Mallows Model for Ranked Choices

This repository includes the implementation of algorithms and experimental results of the paper:

Generalized Top-k Mallows Model for Ranked Choices @ NurIPS 2025

The classic Mallows model is a foundational tool for modeling user preferences.
However, it has limitations in capturing real-world scenarios, where users often
focus only on a limited set of preferred items and are indifferent to the rest. To
address this, extensions such as the top-k Mallows model have been proposed,
aligning better with practical applications. In this paper, we address several chal-
lenges related to generalized top-k Mallows model, with a focus on analyzing
buyer choices. Our key contributions are: (1) a novel sampling scheme tailored
to generalized top-k Mallows models, (2) an efficient algorithm for computing
choice probabilities under this model, and (3) an active learning algorithm for
estimating the model parameters from observed choice data. These contributions
provide new tools for analysis and prediction in critical decision-making scenarios.
We present rigorous mathematical analysis for the performance of our algorithms.
Furthermore, through extensive experiments on synthetic data and real world data
we demonstrate the scalability and accuracy of our proposed methods and we
compare the predictive power of Mallows model for top-k lists compared to the
simpler Multinomial Logit model.
