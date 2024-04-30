# morse_code_jailbreak


## ~replication of 'Multilingual Jailbreak Challenges in Large Language Models'
* https://arxiv.org/html/2310.06474v3

* multijail.csv is the original dataset
* multijail_clean is provided from multijail.csv being ran through data_cleaning.ipynb
* evaluated_data.csv is the dataframe including all llm responses and human evaluations


## Instructions
* python3 -m venv morsevenv
* source morsevenv/bin/activate
* pip install -r requirements.txt
* create '.env' file
* In '.env' file create a variable ' OPENAI_API_KEY= "[your key]" '



## Costs to run for self
* ~ 5$ through gpt4 turbo
* ~ 2 hours runtime 
