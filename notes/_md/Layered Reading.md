---
publish: true
---

# Layered Reading

How ought one to engage with a lengthy and dense text such as a papal encyclical, and might we create AI tools that encourage deeper engagement with such texts rather than quick summaries? 

I want to hear what Pope Leo XIV has to say about AI in *[[~Magnifica Humanitas|Magnifica Humanitas]]*, not read an LLM summary or hear what other people think he has to say. But given that the text is 42,000 words[^length], it will take me some time to get through it. I also fear that some of the audience that would benefit from Leo's insights will never read the text due to its length. 

Rather than skimming the text, reading news articles about the text, or—more likely—just not getting around to it—I'm trying an approach I'm calling **layered reading**: using AI to surface the most essential parts of a text at multiple levels of depth, while preserving the author's original words throughout, presented in an interface that encourages diving deeper.

[^length]: Pope Leo XIV chose his name to honor [[Pope Leo XIII]], who wrote *[[2025-06-25-Rerum Novarum|Rerum Novarum]]*, launching the modern tradition of Catholic social teaching. Leo XIII was both prolific and concise: he published 86 encyclicals averaging about 7,000 words each. Even *Rerum Novarum*, one of his longest, was only around 12,000 words. Encyclical length has grown steadily since: *[[~Quadragesimo Anno|Quadragesimo Anno]]* (Pius XI, 1931) was about 17,000 words, *[[~Centesimus Annus|Centesimus Annus]]* (John Paul II, 1991) reached 25,000, and *[[~Laudato Si|Laudato Si']]* (Francis, 2015) crossed 40,000.


## The Prototype

See a prototype of this interface [here](https://matthewkudija.com/magnifica-humanitas/index.html). You select the amount of time you want to spend with the text initially (2 minutes, 10 minutes, 30 minutes, 60 minutes, or the full document), and the interface surfaces relevant passages that can be read in that timeframe. The the parts hidden are annotated if you want to expand any section and go deeper.

The prototype is designed with these principles in mind:
1. **Time-budget driven:** Engage with the text now, using the amount of time you have available. It's ok to progressively engage with a text over time rather than giving it your full attention on the first pass.[^talk] 

2. **Original text, not summary:** Read the original text, not a summary or commentary. Additional scaffolding may be added in the form of human- or AI-generated summaries, but selections from the original text are preserved without alteration.

3. **AI-scored essentiality.** Each paragraph of the document is scored for how much a reader would lose by skipping it, and the highest-scored paragraphs are shown. Thesis statements, key definitions, and pivotal arguments score highest. Historical surveys and rhetorical amplification score lower. The scoring was calibrated against my own annotations from the introduction and conclusion. 

4. **Bidirectional depth:** You can dive into a section and then resurface. Layered reading supports dipping in and out, following your curiosity.[^related] 

[^talk]: cf. my notes on *[[2021-06-01-How to Talk About Books You Haven't Read|How to Talk About Books You Haven't Read]]*, where I first started thinking about progressive or periodic engagement with a text.



## Extensions

The prototype works for a single document, but the idea generalizes:

- **Corpus-level layered reading:** *Magnifica Humanitas* cites over 20 prior encyclicals. Each of those could be processed with the same pipeline, with cross-references linking between them. You could start with a 10-minute overview of Catholic social teaching from *Rerum Novarum* to the present, then drill into any document that interests you or follow a theme or topic across documents.

- **Expert-augmented scoring:** The current importance scores are AI-generated, trained on my annotations. An expert could provide their own rankings, offer more granular rankings at the sentence-level, or include additional notes, synthesis, or analysis.

- **Integrated commentary:** The sidenotes currently show only the original footnotes. Future versions could include curated commentary, cross-references to related passages in other documents, or study questions, all visually distinct from the source text.

- **Any long text:** The processing pipeline (parse, score, generate context notes) is document-agnostic. It could be applied to legislation, legal opinions, technical specifications, or any structured long-form text where readers need to engage at varying depths.

## How It's Built

The prototype is HTML, CSS, and JavaScript deployed as static files. The processing pipeline uses Python scripts with Claude (Sonnet for essentiality scoring, Haiku for context notes and footnote enrichment). All AI processing happens offline during build; the deployed site makes no API calls. The full source is on [GitHub](https://github.com/mkudija/magnifica-humanitas).


---
Created: [[2026-06-01-Sun]]
Updated: `=dateformat(this.file.mtime, "yyyy-MM-dd-ccc")`
