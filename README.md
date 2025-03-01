## Poster and paper
Accessible through TU Delft's repository. [Poster](https://cse3000-research-project.github.io/static/4ffa082bc95cd3179672eb958e640682/poster.pdf), [paper](https://repository.tudelft.nl/record/uuid:d25aa97c-af96-4219-863f-ce874ab85d8e).

## Code Reproducibility
The experiment consisted of 2 phases: data collection and data analysis. 

## Data Collection
First, the integral WikiArt dataset has been downloaded locally as an [archive](https://archive.org/download/wikiart-dataset/wikiart.tar.gz) from the [WikiArt website](https://www.wikiart.org/). Then, the file was unarchived, revealing over 80,000 artworks from 27 styles. Due to resources and time constraints, the script <em>sample_from_WikiArt.py</em> has been run in order to sample only 10 images from each style and collect them in the <em>wikiart_samples</em> folder, also split in styles. For the process of self-poisoning, the script <em>WikiArt_self_poisoning.ipynb</em> was ran on the free versions of the Google Colab and Kaggle platforms using the available T4 GPUs. The results of these generations were downloaded locally and organized manually in the <em>results</em> folder to facilitate data analysis. These results consists of the generated images, the generated captions, plus the semantic and visual similarities between the first image/caption and the others, as well as between consecutive images/captions. Each artwork has a dedicated folder containing the generated images, whereas the captions and other metrics corresponding to the respective artwork are stored in a json file.

## Data Analysis
The <em>results</em> folder initially contained only the original and generated images, captions and some of the metrics described in the paper per artwork (not aggregated yet). The notebook <em>creative_novelty.ipynb</em> contains the data processing, as well as the resulting plots used in the paper. Please unarchive <em>results.zip</em> in order to see the generated images, captions and plots.
