import streamlit as st

st.title("🤖 Machine Learning | EMG | G29")
st.header("Introduction & Background", divider="rainbow")
st.markdown(
"""
What is an EMG (Electromyogram)?
- Bioelectrical signals generated by muscle cells when they are activated [1]. 
- Captured using electrodes placed on a skin surface. 
  - In regards to our dataset, The Myo Thalmic bracelet captures signals from the forearm. It does this by utilizing 8 EMG sensors and a bluetooth module. 
"""
)

st.markdown(
"""
What is EMG Gesture Classification?
- Process in which electric signals gendered by muscle contractions are monitored inorder to identify specific gestures [1]. 
"""
)

st.subheader("Literature Review", divider="blue")
st.markdown(
"""
Article: “Human Hand Movement Classification based on EMG Signal using different Feature Extractor”
DOI: ​​https://dx.doi.org/10.13005/bpj/2835
- This paper focuses on applying certain feature selection techniques for classifiers in the medical sector [1].

"""
)
st.markdown(
"""
Article: “Electromyogram-Based Classification of Hand and Finger Gestures Using Artificial Neural Networks”
DOI: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8749583/
- This paper attempts to use time-domain features only to reduce the computational complexity instead of including frequency domain features. They also attempted to develop personalized classifiers for each person’s EMG data. They found that overall Artificial Neural Networks did best compared to SVMs, Random Forests, and Logistic Regression [2]. 
"""
)
st.markdown(
"""
Article: “Gesture Classification in Electromyography Signals for Real-Time Prosthetic Hand Control Using a Convolutional Neural Network-Enhanced Channel Attention Model”
DOI: https://www.mdpi.com/2306-5354/10/11/1324
- This paper describes the approach of using a CNN-ECA gesture recognition framework, utilizing a combination of the CNN architecture and ECA module to better enhance the focus and capture ability of important features. It also shows techniques for reducing the influence of noise and improving signal steadiness [3].
"""
)
st.markdown(
"""
Article: “EMG-based online classification of gestures with recurrent neural networks”
DOI: https://www.sciencedirect.com/science/article/pii/S0167865519302089?casa_token=S5bUDUK0LzwAAAAA:4ITvJzw3veWQvbAnLJTPRQTyMjddRZSMujJ_Lw-bqfIBOvSjje_uXd69xGUXXIplcwjLH-KNbQ
- This paper involves using RNNs for online hand gesture classification with EMG signals, avoiding motion detection calibration. In the paper they compare FFNN, RNN, LSTM, and GRU models finding that they achieve similar accuracy but that LSTM/GRU are most efficient/faster to train [4].
"""
)

st.subheader("Dataset Description", divider="blue")
st.write("URL: https://archive.ics.uci.edu/dataset/481/emg+data+for+gestures")
st.write("Consists of gesture EMG recordings from a bluetooth MYO Thalmic bracelet. Time based data with raw EMG output, where each “datapoint” is a static hand gesture held for 3 seconds with a 3 second pause between different gestures. We can classify a total of 7 gestures. Each gesture is not uniformly represented in the dataset.")


st.header("Problem Definition", divider="rainbow")
st.subheader("Problem", divider="blue")
st.write("Electromyography (EMG) data, captured from muscle movements, is an important source of info which allows us to develop and create systems and technology that can properly interpret hand gestures. With proper interpretation, EMG data is useful in aiding the development of prosthetics and nuanced rehabilitation techniques. However, raw EMG data remains inherently variable and quite complicated, therefore making it quite difficult to accurately read and classify hand gestures.")
st.subheader("Motivation", divider="blue")
st.write("Properly reading and interpreting EMG data has massive implications in physical rehabilitation and prosthetic developments [2], as it would allow us to better mimic natural and intuitive control of limbs, allowing those with amputations and disabilities greater independence and mobility in their lives. In fact, functional prosthetics can improve mental well-being and reduce muscle-atropphy [3]. In this project, we will be exploring the use of ML to enhance the accuracy and reliability of hand gesture recognition, providing a foundation for real-world applications by tackling the inherent variability of EMG data.")



st.header("Methods", divider="rainbow")
st.subheader("Data Preprocessing", divider="blue")
st.write("1: Signal Smoothing - Use a low-pass filter to reduce signal noise")
st.write("2: Normalizing Trial Data with Z-score  - Minimizes inter-subject variability")
st.write("3: Feature Extraction - Extract important data information, reduce dimension")

st.subheader("Candidate ML Algorithms/Models", divider="blue")
st.write("1: Random Forests [Supervised] We would be able to get the most prominent features from the data and classify them based on that to the respective hand gesture")
st.write("2: GMM [Supervised] GMM has the capability to group each hand gesture into a cluster")
st.write("3: CNN [Supervised] CNNs are great at classification for “spatial” data, and our multi-channel data is similar to an image’s pixel intensities, except we have electrical intensities instead.")


st.header("Results & Discussion", divider="rainbow")
st.subheader("Visualization (Confusion Matrix)", divider="blue")
st.image("ConfMatrixRandomForest_EMG_4641.png")
st.write("We can see that the diagonal dominance in the confusion matrix above indicates that the model was able to correctly classify most samples in each seperate class. We are also able to see how the model doesn't perform as well with classes 3 and 6 (high values not on the diagonal for those class intersections), which could suggest some class imbalance. It is also more apparent because it seems like class 7 did not have nearly as many samples as the other classes, further signifying a potential class imbalance. To fix this, one could resample the data or use synthetic data generation, which would improve the model's performance on the classes with less samples.")
st.subheader("Quantitative Metrics (Accuracy, Precision, Recall)", divider="blue")
st.markdown("""
- **Accuracy:** With the model achieving an accuracy of ~86%, we can see that it is able to successfully classify a significant majority of our data, supporting the fact that the random forest classifier performed relatively well overall. However, it is important to note that this accuracy, while good, doesn't account for the misclassification jumps in specific classes that could be significant in specific use cases.
- **Precision:** Our precision gives us an indicator of the proportion of correctly predicted gestures out of all gestures that the model predicted for each class. Overall, we can see that we obtained a weighted average precision of 0.87, which is fairly good. This precision does vary by class however, with a minimum of 0.81 and a maximum of 1.0. 
- **Recall:** The recall score helps us understand the proportion of actual gestures that were correctly predicted by the model. We were able to obtain a weighted average recall of 0.86, which is also fairly good. Unfortunately, this varies all the way down to a recall of 0.26 for class 7.0. 

With an F1 score of ~0.86, we are able to see that the model is able to act precisely with decent recall. The high precision shown in most classes compared to a slightly lower recall signify that the model is good at picking up negatives (e.g doesn't classify many false positives), but it is missing some true positives at times as well.
""")
st.subheader("Analysis of Algorithm: Random Forest", divider="blue")
st.markdown("""
For making classifications, we use the **random forest** method with scikit-learn, which is an ensemble method of multiple decision trees, combining their results to make more accurate classifications and control overfitting. 

A **decision tree** is a structure where classification flows from the root to a leaf node, where each intermediary node represents a decision based on a feature, each branch represents the subsequent outcome and choices based on the parent decision made, and each leaf node represents a final classification. When splitting the data based on a feature, the decision tree uses the metric of **Gini Impurity** to make each subset of data as pure as possible and improve classification accuracy (by reducing uncertainty about what a classification should be based on feature information). 

When $D$ is the dataset, $C$ is the number of classes, and $p_i$ is the probability that a randomly selected point in $D$ belongs to class $i$, Gini Impurity can be calculated as follows:

$$Gini(D) = 1 - \sum_{i=1}^{C} (p_i)^2$$

When using the random forest method, we randomly select subsets of the training data to create diverse datasets, and for each of these subsets we build a decision tree by finding the best feature to split the data at each node. For the actual broader classification, each tree votes for a class assignment and the majority becomes the final prediction. T

When $\hat{y}$ is the prediction in a Random Forest, and $DT_i$ is the classification made by the $i$-th Decision Tree, this voting can be formalized with $n$ many trees as follows:

$$\hat{y} = mode\{ DT_1(x), DT_2(x), \ldots, DT_n(x) \}$$

This technique is a solid fit for our problem space, because it is relatively good at robustly handling datasets that are large with high dimensionality (such as our EMG dataset) and the use of multiple decision trees "voting" can help cancel out imperfections caused by signal noise, which is difficult to fully remove from sensor data datasets, such as the dataset we use. Random forests are also convenient in that they lend themselves to being more interpretable than some other methods, since you can see how a classification was made in the decision trees that voted and can directly observe and visualize what features were important for that classification.

For our implementation, we use a Random Forest of 1000 decision trees, with a starting seed of 42, no max depth (allowing for more purity), a minimum samples required to split of 20 (reducing overfitting for very small sample numbers), and a minimum number of samples in a leaf node of 10. Our model has decently solid performance, with an accuracy score of about 0.8634. Additionally, there is a decent balance between precision and recall, with an f1 score of about 0.8621. However as discussed in the "Quantitative Metrics" section, there is still room to improve. The most important features were derived from channel 7 of the signal data.
            """)
st.subheader("Next Steps", divider="blue")
st.markdown("""
Moving forward, we aim to both refine our methods for data preprocessing and attempt to improve our classification accuracy by implementing two other methods for gesture classification: Gaussian Mixture Models (GMMs) and Convolutional Neural Networks (CNNs).  

- **Gaussian Mixture Models**, as we've discussed in class, are unsupervised probabilistic models that are helpful for clustering and provide soft assignments, which is helpful for gestures with somewhat overlapping EMG gesture signals. We will likely use GMMs in a more supervised way, by training separate GMMs for each class and using probabilistic reasoning to assign class labels to new data points.

- **Convolutional Neural Networks** are deep learning models which have proven incredibly useful for application to computer vision problems, and deal well with spatial hierarchies. Similarly, CNNs might be adept at extracting spatial patterns from multi-channel EMG data. Further, CNNs are known to be robust and accurate in other classification tasks. 

Finally, we would like to test all three of our models with variable real-world data (if we get the chance), by using our own sensors to test how well the models respond to the change that comes from a new data source. 
""")

st.header("References", divider="rainbow")
st.write("[1]Swati Shilaskar, Shripad Bhatlawande, Ranveer Chavare, Aditya Ingale, R. Joshi, and Aditya Vaishale, “Human Hand Movement Classification based on EMG Signal using different Feature Extractor,” Biomedical and Pharmacology Journal, vol. 17, no. 1, pp. 71–82, Mar. 2024, Available: https://biomedpharmajournal.org/vol17no1/human-hand-movement-classification-based-on-emg-signal-using-different-feature-extractor/")
st.write("[2]K. H. Lee, J. Y. Min, and S. Byun, “Electromyogram-Based Classification of Hand and Finger Gestures Using Artificial Neural Networks,” Sensors, vol. 22, no. 1, p. 225, Dec. 2021, doi: https://doi.org/10.3390/s22010225.")
st.write("[3]G. Yu, Z. Deng, Z. Bao, Y. Zhang, and B. He, “Gesture Classification in Electromyography Signals for Real-Time Prosthetic Hand Control Using a Convolutional Neural Network-Enhanced Channel Attention Model,” Bioengineering, vol. 10, no. 11, pp. 1324–1324, Nov. 2023, doi: https://doi.org/10.3390/bioengineering10111324.")
st.write("[4]M. Simão, P. Neto, and O. Gibaru, “EMG-based online classification of gestures with recurrent neural networks,” Pattern Recognition Letters, vol. 128, pp. 45–51, Dec. 2019, doi: https://doi.org/10.1016/j.patrec.2019.07.021. ‌")


st.header("Gantt Chart", divider="rainbow")
st.image("4641_gantt.png")
st.header("Contributions", divider="rainbow")
st.image("4641_proposal_contributions.png")


