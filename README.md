# ⚡ Hate Speech Detection 🔬

As any social media user might have experienced by now, it's becoming effortless to get likes, comments, and shares on
posts with divisive content due to the recommendation algorithms used in these applications. Increasingly, online hate
speech is leading to real-world harm, and these companies are struggling to identify hateful posts, with users & groups
altering their speech patterns online to avoid detection.

We propose building any applications with natural language user input in an Inclusive First approach with an easy-to-use
multilingual hate speech detector running in a production-ready and enterprise-grade environment. Our approach makes it
easier develop and deploy inclusive applications, without any cloud prerequisites, as a quick way to build any
distributed ML system. In this app, we will show you how to use this hate speech detector component within an
application & deploy it to Lightning.ai

> Credits to Sai Saketh Aluru, Binny Mathew, Punyajoy Saha and Animesh Mukherjee for their
> work [DE-LIMIT](https://github.com/hate-alert/DE-LIMIT)

## Getting started

You can install this app via the [Lightning CLI](https://lightning.ai/lightning-docs/) or
clone the repo from GitHub to manually install the app as mentioned below.

### Installation

#### With Lightning CLI

`lightning install app lightning/hate-speech-detection`

#### From Github

```
git clone https://github.com/lightning-AI/LAI-hate-speech-detection-App.git
cd LAI-hate-speech-detection-App
pip install -r requirements.txt
pip install -e .
```

Once you have installed the app, you can goto the `LAI-hate-speech-detection-App` folder and
run `lightning run app app.py --cloud` from terminal.
This will launch the template app in your default browser with tabs containing research paper, blog, Training
logs, and Model Demo.
