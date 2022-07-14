# ⚡ Hate Speech Detection 🔬

This App is a Poster on Hate Speech Detection.
It showcases [paper](https://arxiv.org/pdf/2004.06465.pdf), poster and model demo where you can try out the model from
UI.

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

[//]: # (You should see something like this in your browser:)

[//]: # ()
[//]: # (> ![image]&#40;./assets/demo.png&#41;)

You can modify the content of this app and customize it to your research.
At the root of this template, you will find [app.py](./app.py) that contains the `ResearchApp` class. This class
provides arguments like a link to a paper, a blog, and whether to launch a Gradio demo. You can read more about what
each of the arguments does in the docstrings.

### Highlights

- Provide the link for paper, blog, or training logger like WandB as an argument, and `ResearchApp` will create a tab
  for each.
- Make a poster for your research by editing the markdown file in the [resources](./resources/poster.md) folder.
- Add interactive model demo with Gradio app, update the gradio component present in the \[research_app (
  ./research_app/components/model_demo.py) folder.
- View a Jupyter Notebook or launch a fully-fledged notebook instance (Sharing a Jupyter Notebook instance can expose
  the cloud instance to security vulnerability.)
- Reorder the tab layout using the `tab_order` argument.

### Example

```python
# update app.py at the root of the repo
poster_dir = "resources"
paper = "https://arxiv.org/pdf/2004.06465"
blog = "https://paperswithcode.com/sota/hate-speech-detection-on-automatic"
github = "https://github.com/hate-alert/DE-LIMIT"
tabs = ["Poster", "Model Demo", "Blog", "Paper", "Notebook Viewer"]

app = L.LightningApp(
    ResearchApp(
        poster_dir=poster_dir,
        paper=paper,
        github=github,
        blog=blog,
        launch_gradio=True,
        tab_order=tabs,
        launch_jupyter_lab=False,  # don't launch for public app, can expose to security vulnerability
    )
)

```

## FAQs

1. How to pull from the latest template
   code? [Answer](https://stackoverflow.com/questions/56577184/github-pull-changes-from-a-template-repository)
