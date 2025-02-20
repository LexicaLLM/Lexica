<p align="center">
  <img
    src="https://cdn.discordapp.com/attachments/1338605972398280737/1342263888925822997/asd.png?ex=67b90029&is=67b7aea9&hm=289365e37a4ba6d234e2674ef29f9260b3b976579b0d165f7724b226084c6717&"
    alt="screencast"
  >
</p>
<div align="center">
  <strong> <h1>The Open source LLMOps Platform </h1></strong>
  Prompt playground, prompt management, evaluation, and observability
</div>
<p align="center">
    <a href="https://lexica.gitbook.io/lexica">Documentation</a> |
    <a href="https://www.lexica.dev">Website</a> |
    <a href="https://x.com/LexicaLLM">Twitter</a>
  </p>
</br>

<br/>
  <br />
      <div align="center" >
        <a href="">
          <picture >
            <img width="800" alt="Screenshot Lexica" src="https://github.com/user-attachments/assets/32e95ddb-e001-4462-b92e-72bf4cc78597" >
          </picture>
        </a>
    </div>
</div>
<br />
<br />

---

## What is Lexica?

Lexica is a platform for building production-grade LLM applications. It helps **engineering and product teams** create reliable LLM apps faster.


Lexica provides end-to-end tools for the entire LLMOps workflow:  building (**LLM playground**, **evaluation**), deploying (**prompt and configuration management**), and monitoring (**LLM observability and tracing**).

## Features
- **Prompt Playground**: Experiment, iterate on prompts, and compare outputs from over 50 LLM models side by side
- **Custom Workflows**: Build a playground for any custom LLM workflow, such as RAG or agents. Enable all the team to easily iterate on its parameters and evaluate it from the web UI.
- **LLM evaluation**: Run evaluation suite from the webUI using predefined evaluators like LLM-as-a-judge, RAG evaluators, or custom code evaluators.
- **Human evaluation**: Collaborate with subject matter experts for human annotation evaluation, including A/B testing and annotating golden test sets.
- **Prompt Management**: Version your prompts and manage them across different environments
- **LLM Tracing**: Observe and debug your apps with integrations to most providers and frameworks
- **LLM Monitoring**: Track cost and latency and compare different deployments.

  
## Getting Started 
   
### Self-hosting Lexica

#### Quick Setup (Port 80)
```bash
mkdir Lexica && cd Lexica
curl -L https://raw.githubusercontent.com/LexicaLLM/Lexica/main/docker-compose.gh.yml -o docker-compose.gh.yml
docker compose -f docker-compose.gh.yml up -d
```

## Disabling Anonymized Tracking

By default, Lexica automatically reports anonymized basic usage statistics. This helps us understand how Lexica is used and track its overall usage and growth. This data does not include any sensitive information. To disable anonymized telemetry, follow these steps:

- For web: Set `TELEMETRY_TRACKING_ENABLED` to `false` in your `Lexica-web/.env` file.
- For CLI: Set `telemetry_tracking_enabled` to `false` in your `~/.Lexica/config.toml` file.



