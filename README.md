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



# Conclusions from project
* Using gpt 4 to evaluate responses didn't prove to be accurate 
** ~80% agreement with my own evaluations (some may be accountted for by ammbiguity of the different criterian to classify as 'safe'/'unsafe' but others were very clearly miscategorized by the model)
* Translating an adversarial prompt into morse code (and telling the model to only respond in morse) is a very easy jailbreak to receive unsafe responses
** ~30% unsafe responses when asked in morse code compared to ~1% when asked in english 
*** most of these unsafe responses from the english questions seem to be from unkown racial slurs and missing the harmful intentions in the questions
* When the model responded in english to a morse question, it was far less likely to be an unsafe response
** 38% of morse questions answered in morse were deemed as unsafe compared to 0 out of the 65 questions in morse that were answered in english being deemed as unsafe 
* While some tags seem to be more resistant to the morse code jailbreak like 'Theft' having 26 safe responses to 1 unsafe response compared to 'Discrimination & injustice' which had 24 safe responses to 23 unsafe responses, the sample size is quite small and could just be skewed by how deceptive the adversarial prompts are