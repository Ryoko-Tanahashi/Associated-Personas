## Summary of Artifact

This is the replication package for "Associated Personas: Linking Stakeholders to Traceable Requirements", handling the generation of the AssociatedPersonas.

With the input of several communication logs under [`data_sample/`](data_sample/), sets of Associated Personas are generated under [`outputs_sample/associated_personas`](outputs_sample/associated_personas/).

The replication workflow proceeds as follows:

1. Create an .env file containing your OpenAI API key and other information, using `.devcontainer/.env.sample` as a reference.
2. Start the docker container.
3. Run all the cells inside `pipeline.ipynb` to generate sets of Associated Personas. All generated outputs are saved in the `outputs_sample/` directory.

---

## Authors Information

The artifact accompanies the paper:

> **Associated Personas: Linking Stakeholders to Traceable Requirements**

Authors should cite the paper and this archived artifact when reusing the
software, datasets, generated outputs, or evaluation materials.

**Author list:**

- Ryoko Tanahashi, Waseda University, Tokyo, Japan
  (<ry.tana@fuji.waseda.jp>)
- Hironori Washizaki, Waseda University, Tokyo, Japan
  (<washizaki@waseda.jp>)
- Naoyasu Ubayashi, Waseda University, Tokyo, Japan
  (<ubayashi@aoni.waseda.jp>)
- Ryota Sugiyama, Waseda University, Tokyo, Japan
- Satoshi Okuda, PRIMESTYLE Co., Ltd., Shinjuku, Tokyo, Japan
  (<okuda@primestyle.co.jp>)
- Ken Toriumi, PRIMESTYLE Co., Ltd., Shinjuku, Tokyo, Japan
  (<toriumi@primestyle.co.jp>)

**Software citation:** A machine-readable citation template is provided in
[`CITATION.cff`](CITATION.cff).

## Artifact Location

- Source repository:
  <https://github.com/Ryoko-Tanahashi/Associated-Personas>
- Archival DOI: <https://doi.org/10.5281/zenodo.20508104>

The artifact should be evaluated from the archived DOI version for the final
submission. The GitHub repository is provided as a development mirror and source
code landing page.

---

## Repository Structure

```
├─ .devcontainer/
│ ├─ .env.sample
│ ├─ Dockerfile
│ ├─ devcontainer.json
│ └─ docker-compose.yml
├─ data/
│ └─ neo4j/
│ └─ .gitkeep
├─ data_sample/
│ ├─ 01.txt
│ └─ 02.txt
├─ outputs_sample/
│ ├─ clustering_logs/
│ └─ triples/
├─ prompts_sample/
│ ├─ clustering_issues.txt
│ ├─ clustering_solutions.txt
│ └─ log_extraction.txt
├─ src/
│ └─ pipeline.ipynb
├─ utils/
│ ├─ **init**.py
│ ├─ file_reader.py
│ ├─ langchain.py
│ └─ openai_client.py
├─ README.md
└─ requirements.txt
```

---

## Data Availability

Due to ethical, privacy, or licensing considerations, the original data used in the study cannot be publicly released.
This replication package provides representative samples or templates.

These materials preserve the structure and key characteristics of the original data and are sufficient for understanding the experimental setup and workflow.

---

## Language and Translation

In the original study, all materials were written in another language.
For this replication package, these materials have been translated into English to improve accessibility for international audience.

Due to linguistic differences, running the same prompts under otherwise identical conditions do not necessarily produce identical outputs.

This limitation is inherent to cross-lingual use of LLMs and is therefore acknowledged as a potential threat to reproducibility.
