**EXPLORING NARRATIVES AND EMOTIONAL VALENCE IN INFLUENCER MARKETING: A STUDY OF SHORT-VIDEO CONTENT ON TIKTOK**

**1. THE CHALLENGE**

Influencer marketing is crucial for engaging younger demographics who rely on social media for information and entertainment, especially on platforms like TikTok. The effectiveness of influencer content lies in their storytelling techniques and self-disclosure, which build strong audience connections. However, TikTok's short-form video format presents challenges in analyzing narrative strategies, as this brevity often results in a lack of contextual depth, complicating the use of topic modeling to fully capture influencer narratives.

To address these issues, this research will explore the following questions:

    1. What are the popular narrative strategies employed by TikTok influencers?
    2. How do influencer narratives contribute to engagement among consumers on TikTok?
    3. Does endorsements/sponsorship affect the level of engagement with influencer content on TikTok?
    4. How does emotional valence impact engagement levels in influencer narratives on TikTok?



**2. THE STRATEGY**

To address the challenges of analyzing influencer narratives within TikTok's short-form content, this research adopts a multifaceted approach centered on Natural Language Processing (NLP), specifically through Structural Topic Modeling (STM). STM is chosen over common methods like Latent Dirichlet Allocation (LDA) due to its ability to uncover thematic patterns while accounting for covariates such as influencer type and gender. Unlike LDA, which assumes independence between topics and does not capture inter-topic correlations, STM allows for a more nuanced understanding of how different influencers utilize storytelling techniques. Moreover, by implementing a structured framework based on established narrative strategies—Advising, Enthusing, Educating, and Evaluating—the research aims to categorize and interpret the diverse methods influencers use to engage their audiences. This comprehensive approach, which also includes sentiment analysis, enables us to capture the nuanced storytelling techniques that resonate with viewers, enhancing our insights into the emotional and contextual depth of influencer communication despite the constraints of TikTok's format.



**3. THE PROCESS**

  ****Data Collection and Pre-processing:**** The analysis began with the collection of TikTok videos, which were then transcribed into text using OpenAI's Whisper5 algorithm, known for its high-quality, human-level transcription capabilities, including support for non-English audio. For videos without voiceovers, video captions were included to provide contextual insights. The transcripts and captions underwent extensive preprocessing, which included tokenization, normalization, stemming, and the removal of stop words, numbers, and punctuation. Texts and captions with fewer than three words were excluded, resulting in a final dataset of 3,580 transcripts.
  
  **Sponsorship Disclosure Identification:** A Python script was developed to analyze video captions for sponsorship disclosures, searching for specific hashtags such as "#ad" and "#sponsored." This analysis identified 347 sponsored posts from the dataset of 10,000 videos.
  
  **Topic Modeling:** Structural Topic Modeling (STM) was employed for topic analysis due to its ability to capture thematic patterns while accounting for covariates like influencer type and gender. Unlike Latent Dirichlet Allocation (LDA), STM models topic correlations and allows for variability in word distribution based on document-level covariates. Two covariates were considered: influencer classification (mega, macro, micro) and gender. The number of topics (K) was determined through a comprehensive evaluation involving coherence, exclusivity, held-out likelihood, and residual analysis, resulting in an optimal K of 7.
  
  **Interpretation of Topics:** Following the STM fitting, topics were synthesized using high-probability and FREX words, along with exemplar reviews. The labeling process relied on a pre-established framework and was supported by human judgment to ensure nuanced interpretations, acknowledging that no model can fully replace human insight in topic interpretation.
  
  **Sentiment Analysis:** Sentiment analysis was conducted using the Naive Bayes classifier and the VADER lexicon to categorize the sentiment of the textual data as positive, negative, or neutral. The feature extraction utilized the Term Frequency-Inverse Document Frequency (TF-IDF) method, enhanced by word unigram and emotion lexicon features to improve accuracy. The sentiment analysis was implemented through Python programming, allowing for robust computational analysis.
  
  **Interpretation and Validation:** The derived topics and sentiment analyses were synthesized for meaningful interpretation. ANOVA and MANOVA were employed for validation, complemented by qualitative evaluations of representative content. This human-in-the-loop approach ensured a nuanced understanding that complements automated processes.


**4. THE FINDINGS & INSIGHTS**


**Prevalence of Narrative Strategies:**

The "Enthusing" strategy dominates at 70.79%, reflecting TikTok's creative nature. The "Evaluating" strategy (18.57%) underscores influencers' roles in authentic reviews. "Educating" (6.14%) and "Advising" (4.5%) strategies are less common, likely due to the platform's younger audience. Popular influencers favor entertaining content, while less popular ones adopt educating strategies for niche audiences. Gender impacts are minimal.

![image](https://github.com/user-attachments/assets/b012ce5b-0304-4fb6-ab3f-785ff0dbe39d)
![image](https://github.com/user-attachments/assets/753afc0e-bdb4-4af8-953a-e624a119521d)


**Impact on Engagement:**

"Enthusing" and "Evaluating" posts receive more likes than "Advising," while "Educating" does not significantly boost likes. "Enthusing" also drives comments, highlighting the importance of emotional engagement as per narrative transportation theory.


![image](https://github.com/user-attachments/assets/3c2f8e0d-c2bc-488b-89da-aa1bf55220cf)


**Effect of Sponsorship:**

Sponsored posts attract fewer likes and comments, indicating audience skepticism towards sponsored content. This aversion may diminish the immersive benefits of narrative engagement, suggesting a complex interplay between sponsorship perceptions and audience reactions.

![image](https://github.com/user-attachments/assets/9cb8b39c-efc1-4ee3-9706-bcac36041508)


**Sentiment Analysis:**

"Positive" is the most popular sentiment of the content. The presence of sentiment in content did not significantly affect engagement, pointing to the importance of factors like content relevance and narrative structure. Engagement may arise more from the emotional journey of narratives rather than explicit sentiment.

![image](https://github.com/user-attachments/assets/812aafe0-85f4-4b42-a8ac-58231f6804c1)

![image](https://github.com/user-attachments/assets/80f85f81-ab4b-404b-abb3-35d9f4058369)



