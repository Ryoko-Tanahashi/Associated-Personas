## Summary of Artifact

This artifact provides the source code and sample data for "Associated Personas: Linking Stakeholders to Traceable Requirements".

**Motivation & General Use Case:**
Beyond simple replication, this framework is designed to help requirements engineers extract interdependent stakeholder groups (Associated Personas) directly from unstructured interaction logs (e.g., call center transcripts, interview logs). By modeling stakeholders as interacting pairs rather than isolated profiles, the tool explicitly captures behavioral triggers and structural conflicts, enabling practitioners to identify collaborative, win-win requirements.

**Getting Started:**

1. **Install Docker:** Ensure you have Docker and Docker Compose installed on your system. If not, please follow the [official Docker installation guide](https://docs.docker.com/get-docker/).
2. **Setup Environment Variables:** Create an `.env` file in the root directory using `.devcontainer/.env.sample` as a reference. You need to provide:
   - `OPENAI_API_KEY`: Your OpenAI API key (required for GPT-5).
   - `NEO4J_USER`: The username for the local Neo4j database (e.g., `neo4j`).
   - `NEO4J_PASSWORD`: The password for the local Neo4j database.
3. **Start the Environment:** Run the docker container using Docker Compose.
4. **Execute the Pipeline:** Open and run all the cells inside `src/pipeline.ipynb`. Ensure that the phase names in the notebook match the two phases described in the paper.

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
├─ .devcontainer/           - Configuration files for the Docker environment.
│ ├─ .env.sample            - Template for environment variables (e.g., OpenAI API key, Neo4j credentials).
│ ├─ Dockerfile             - Docker image configuration.
│ ├─ devcontainer.json      - VSCode DevContainer settings.
│ └─ docker-compose.yml     - Docker Compose configuration for the app and Neo4j database.
├─ data/
│ └─ neo4j/                 - Local storage directory for the Neo4j graph database.
│ └─ .gitkeep
├─ data_sample/             - Representative synthetic samples of unstructured communication logs.
│ ├─ en/                    - Supplementary English-translated data samples for international accessibility.
│ ├─ 01.txt                 - Raw log text file (Original language) used as input.
│ ├─ 02.txt                 - Raw log text file (Original language) used as input.
│ └─ ...
├─ outputs_sample/          - Directory where the pipeline saves its generated artifacts.
│ ├─ associated_personas/   - Final outputs containing the generated interdependent persona profiles, ready for requirements analysis.
│ ├─ clustering_logs/       - Intermediate logs showing how the LLM grouped related issues and solutions. Useful for tracing abstraction.
│ ├─ islands/               - Extracted subgraphs (scenarios) representing connected end-to-end histories.
│ └─ triples/               - Extracted relationships (nodes and edges) from logs, formatted for Neo4j import to build the Context Graph.
├─ prompts_sample/          - Original language prompts used in the empirical study to ensure authentic replication.
│ ├─ en/                    - Supplementary English-translated prompts.
│ ├─ clustering_issues.txt  - Prompt for semantically grouping nodes into Abstract Issues.
│ ├─ clustering_solutions.txt - Prompt for semantically grouping nodes into Abstract Solutions.
│ ├─ create_personas.txt    - Prompt for generating the final Associated Personas from the scenario subgraphs.
│ ├─ group_peoples.txt      - Prompt for grouping individual stakeholders into representative user groups.
│ └─ log_extraction.txt     - Prompt for extracting initial triplets (Stakeholders, Issues, Solutions, and relations) from raw logs.
├─ src/
│ └─ pipeline.ipynb         - The main execution script (Jupyter Notebook).
├─ utils/                   - Python utility modules.
│ ├─ __init__.py
│ ├─ file_reader.py         - Helper functions for reading input logs.
│ ├─ langchain.py           - Wrappers for LangChain components.
│ └─ openai_client.py       - OpenAI API client management.
├─ CITATION.cff             - Machine-readable citation file.
├─ LICENSE                  - GNU Affero General Public License version 3 (AGPL-3.0).
├─ LICENSE.md               - License documentation details.
├─ README.md                - This documentation file.
└─ requirements.txt         - Python dependencies required to run the pipeline.
```

---

## Data Availability

Due to a strict Non-Disclosure Agreement (NDA) and privacy protection policies regarding the call center data of our partner insurance company, the original full dataset used in the study cannot be publicly released.

To facilitate reproducibility and allow other researchers to test the framework, this replication package provides representative synthetic samples (`data_sample/`) crafted to preserve the exact structure, complexity, and key characteristics of the original data. These samples are fully sufficient for understanding the experimental setup, running the pipeline, and validating the workflow.

---

## Language and Translation

In the original empirical study, all unstructured logs and LLM prompts were in Japanese.

To maximize reproducibility and authenticity, the primary artifacts provided in this package (under `data_sample/` and `prompts/`) are in their original language, encoded in UTF-8. Running the pipeline with these primary artifacts will yield results that closely mirror our study.

Additionally, to improve accessibility for an international audience, we have provided English-translated versions of the prompts under the `prompts_en/` directory as a supplementary resource. Please note that due to inherent linguistic differences in cross-lingual LLM use, running the English prompts may not produce structurally identical outputs to the original language version.

---

## Using Your Own Data

Researchers and practitioners are encouraged to apply this framework to their own datasets (e.g., customer interviews, meeting transcripts). To do so:

1. Format your unstructured logs as plain text files (`.txt`).
2. Place them into a new directory (e.g., `data_custom/`).
3. Update the data loading path in the Phase 1 cell of `src/pipeline.ipynb` to point to your new directory.
4. Execute the pipeline. The framework will automatically construct a new Context Graph in Neo4j and generate the corresponding Associated Personas.

---

**Optional: Using OpenAI API for Free (Free Daily Token Settings)**

If you want to try the pipeline without incurring API costs, you can opt-in to OpenAI's free daily token allowance by agreeing to share your API input and output data for their model improvement. This allows you to use 10 million to 100 million tokens per day for free, depending on the model.

To enable this feature, follow these steps:

1. Access your OpenAI Data Controls page: [https://platform.openai.com/settings/organization/data-controls/sharing](https://platform.openai.com/settings/organization/data-controls/sharing).
2. Check the "Share inputs and outputs with OpenAI" option at the bottom of the page.
3. Select "Enabled for all projects" to apply it globally, or "Enabled for selected projects" to restrict it to specific projects.
4. Click "Save" to finish the setup.

_Warning: By enabling this setting, the data exchanged via the API will be sent to OpenAI for model training. If you plan to run the pipeline with your own proprietary, sensitive, or confidential datasets, we strongly recommend keeping this setting disabled._
