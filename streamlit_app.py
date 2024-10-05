import streamlit as st

st.title("🤖 Machine Learning | EMG | G29")
st.header("Introduction & Background", divider="rainbow")
st.markdown(
"""
What is an EMG (Electromyogram)?
- Bioelectrical signals generated by muscle cells when they are activated. 
- Captured using electrodes placed on a skin surface. 
  - In regards to our dataset, The Myo Thalmic bracelet captures signals from the forearm. It does this by utilizing 8 EMG sensors and a bluetooth module. 
"""
)

st.markdown(
"""
What is EMG Gesture Classification?
- Process in which electric signals gendered by muscle contractions are monitored inorder to identify specific gestures. 
"""
)

st.subheader("Literature Review", divider="blue")
st.markdown(
"""
Article: “Human Hand Movement Classification based on EMG Signal using different Feature Extractor”
DOI: ​​https://dx.doi.org/10.13005/bpj/2835
- Bioelectrical signals generated by muscle cells when they are activated.  
"""
)
st.markdown(
"""
Article: “Electromyogram-Based Classification of Hand and Finger Gestures Using Artificial Neural Networks”
DOI: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8749583/
- Bioelectrical signals generated by muscle cells when they are activated.  
"""
)
st.markdown(
"""
Article: “Gesture Classification in Electromyography Signals for Real-Time Prosthetic Hand Control Using a Convolutional Neural Network-Enhanced Channel Attention Model”
DOI: https://www.mdpi.com/2306-5354/10/11/1324
- Bioelectrical signals generated by muscle cells when they are activated.  
"""
)
st.markdown(
"""
Article: “EMG-based online classification of gestures with recurrent neural networks”
DOI: https://www.sciencedirect.com/science/article/pii/S0167865519302089?casa_token=S5bUDUK0LzwAAAAA:4ITvJzw3veWQvbAnLJTPRQTyMjddRZSMujJ_Lw-bqfIBOvSjje_uXd69xGUXXIplcwjLH-KNbQ
- Discusses EMG classification through sequential classification rather than through splitting into dynamic and static segments 
"""
)

st.subheader("Dataset Description", divider="blue")
st.write("URL: https://archive.ics.uci.edu/dataset/481/emg+data+for+gestures")
st.write("Consists of gesture EMG recordings from a bluetooth MYO Thalmic bracelet. Time based data with raw EMG output, where each “datapoint” is a static hand gesture held for 3 seconds with a 3 second pause between different gestures. We can classify a total of 7 gestures. Each gesture is not uniformly represented in the dataset.")


st.header("Problem Definition", divider="rainbow")
st.subheader("Problem", divider="blue")
st.write("Electromyography (EMG) data, captured from muscle movements, is an important source of info which allows us to develop and create systems and technology that can properly interpret hand gestures. With proper interpretation, EMG data is useful in aiding the development of prosthetics and nuanced rehabilitation techniques. However, raw EMG data remains inherently variable and quite complicated, therefore making it quite difficult to accurately read and classify hand gestures.")
st.subheader("Motivation", divider="blue")
st.write("Properly reading and interpreting EMG data has massive implications in physical rehabilitation and prosthetic developments, as it would allow us to better mimic natural and intuitive control of limbs, allowing those with amputations and disabilities greater independence and mobility in their lives. In this project, we will be exploring the use of ML to enhance the accuracy and reliability of hand gesture recognition, providing a foundation for real-world applications by tackling the inherent variability of EMG data.")



st.header("Methods", divider="rainbow")
st.subheader("Data Preprocessing", divider="blue")
st.write("1: Signal Smoothing - Use a low-pass filter to reduce signal noise")
st.write("2: Normalizing Trial Data with Z-score  - Minimizes inter-subject variability")
st.write("3: Feature Extraction - Extract important data information, reduce dimension")

st.subheader("Candidate ML Algorithms/Models", divider="blue")
st.write("1: Random Forests [Supervised] We would be able to get the most prominent features from the data and classify them based on that to the respective hand gesture")
st.write("2: GMM [Supervised] GMM has the capability to group each hand gesture into a cluster")
st.write("3: CNN [Supervised] CNNs are great at classification for “spatial” data, and our multi-channel data is similar to an image’s pixel intensities, except we have electrical intensities instead.")


st.header("Expected Results & Discussion", divider="rainbow")
st.subheader("Quantitative Metrics", divider="blue")
st.write("1: Confusion Matrix")
st.write("2: F-Score")
st.write("3: Accuracy")
st.subheader("Project Goals", divider="blue")
st.write("To be able to classify hand gestures based on EMG data so that we would be able to help people who use prosthetics")
st.subheader("Expected Results", divider="blue")
st.write("We expect to classify the results by all the 3 techniques. We assume that CNN would perform the best, followed by GMM then Random Forests. We picked these 3 topics as we thought it would be the most diverse set of topics to explore.")

st.header("References", divider="rainbow")
st.write("[1]K. H. Lee, J. Y. Min, and S. Byun, “Electromyogram-Based Classification of Hand and Finger Gestures Using Artificial Neural Networks,” Sensors, vol. 22, no. 1, p. 225, Dec. 2021, doi: https://doi.org/10.3390/s22010225.")
st.write("[2]G. Yu, Z. Deng, Z. Bao, Y. Zhang, and B. He, “Gesture Classification in Electromyography Signals for Real-Time Prosthetic Hand Control Using a Convolutional Neural Network-Enhanced Channel Attention Model,” Bioengineering, vol. 10, no. 11, pp. 1324–1324, Nov. 2023, doi: https://doi.org/10.3390/bioengineering10111324.")
st.write("[3]Swati Shilaskar, Shripad Bhatlawande, Ranveer Chavare, Aditya Ingale, R. Joshi, and Aditya Vaishale, “Human Hand Movement Classification based on EMG Signal using different Feature Extractor,” Biomedical and Pharmacology Journal, vol. 17, no. 1, pp. 71–82, Mar. 2024, Available: https://biomedpharmajournal.org/vol17no1/human-hand-movement-classification-based-on-emg-signal-using-different-feature-extractor/")


st.header("Gantt Chart", divider="rainbow")
st.image("4641_gantt.png")
st.header("Contributions", divider="rainbow")
st.image("4641_proposal_contributions.png")


