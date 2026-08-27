---
layout: single
title: "Research"
permalink: /research/
author_profile: false
---

Our research areas span from developing advanced graph mining algorithms for complex networks to extracting actionable insights from large-scale unstructured social media and spatial-temporal data. Our latest research interest has been implementing deep learning and network science technology for various data-driven applications such as:
* **Dynamic and Heterogeneous Community Detection**: Local exploration and adaptive merging in dynamic graph neural networks (HCD-LEAM & DHCD-iLEAM).
* **Social Computing & Explainable NLP**: Human-validated benchmarks, fake news detection interpretability, and aspect-based sentiment analysis for Indonesian text.
* **Big Data Analytics for Environmental & Societal Systems**: Multitemporal trajectory analysis for deforestation tracking and global aircraft accident network modeling.
* **Predictive Machine Learning & Intelligent Systems**: Bipartite contextual embeddings for Olympiad winner prediction, household energy load profiling, and IoT-integrated agricultural monitoring.

---

### Incremental and Dynamic Community Detection in Complex Heterogeneous Networks

<!--gambar diletakkan di folder images/-->
<p align="center">
  <img src="/images/profile.png" alt="HCD-LEAM Framework" style="width: 85%; max-width: 650px; border-radius: 8px;">
  <br>
  <small><i>Figure 1: Framework of Heterogeneous Community Detection via Local Exploration and Adaptive Merging (HCD-LEAM).</i></small>
</p>

Complex real-world systems—from scientific collaboration platforms to dynamic social media and talent mapping ecosystems—are naturally structured as heterogeneous graphs with diverse node and edge types. Traditional community detection algorithms often collapse these rich topologies into homogeneous graphs or fail to adapt efficiently when the network structure evolves over time. Our research team addresses this bottleneck by developing **HCD-LEAM** (Heterogeneous Community Detection with Local Exploration and Adaptive Merging) and its incremental dynamic expansion, **DHCD-iLEAM**. By focusing on local topology exploration and adaptive cluster merging, our algorithms uncover latent community structures without requiring full graph re-computation whenever new interactions occur. This methodology dramatically reduces computational overhead in large-scale network analysis, paving the way for scalable talent mapping, recommendation systems, and real-time social network auditing.

---

### Human-Validated Benchmarks and Explainable AI for Indonesian Social Computing

<img src="/images/profile.png" alt="Spatial Deforestation Analysis" style="width: 280px; float: right; margin: 0 0 15px 15px; border-radius: 6px;">

While Large Language Models and deep learning transformers have revolutionized Natural Language Processing (NLP), applying them to Indonesian social media and e-commerce text presents severe challenges due to noisy user-generated content, localized slangs, and lack of automatic supervision auditing. Our research group focuses on **Social Computing and Explainable AI (XAI)** to build robust, interpretable NLP frameworks. In our recent studies, we established human-validated benchmarks to audit automatic supervision in aspect-based sentiment analysis and integrated attention-based mechanisms to convert subword attention into clear, word-level explanations for fake news detection. Furthermore, we develop contrastive learning and multi-task transformer models (such as MentalBERT adaptation) to analyze fine-grained user sentiment and mental health signals from digital footprints, ensuring that automated decision-making systems remain transparent, ethically sound, and trustworthy.

---

### Uncovering Hidden Deforestation & Environmental Trajectories via Spatial-Temporal Graph Clustering

Monitoring tropical deforestation across Sumatra and greater Indonesia requires analyzing massive, multitemporal Earth observation datasets where environmental degradation occurs gradually across spatial coordinates. Traditional remote sensing methods often struggle to differentiate between seasonal vegetation fluctuation and permanent land-use changes. To solve this, our lab combines **Google Earth Engine, ESRI Global Land Use data, and spatial graph-based clustering** to analyze multitemporal trajectories of forest cover loss. By treating land pixels and their spatial-temporal relationships as connected graph nodes, our framework reveals hidden deforestation patterns, land conversion velocity, and critical ecological corridors. This data-driven approach empowers policymakers and environmental auditors with actionable spatial intelligence to support Sustainable Development Goals (SDGs) and climate resilience efforts.

---

### Graph-Based Energy Load Profiling and Complex Network Modeling for Societal Resilience

Understanding structural patterns in high-dimensional time-series data—such as daily household energy consumption or global transportation networks—is essential for building resilient smart cities. In our smart energy research, we model daily load profiles as graph structures and utilize similarity-based community detection to uncover latent consumption behaviors without relying on oversimplified statistical averages. Similarly, in aviation safety analytics, we construct global aircraft accident networks using graph clustering to identify hidden systemic risk factors and failure cascades. By transforming unstructured time-series and event records into complex network representations, our research bridges the gap between pure Data Mining algorithms and practical decision-support systems for smart grids, transport logistics, and public policy.

<div style="clear: both;"></div>
