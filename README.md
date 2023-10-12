OUTPUT Parsers
1. langchain_pydantic_parser_gpt.py -> works(need to make modular and work with llama)

2. langchain_pydantic_parser_sagemaker_llama2.py -> Works on sagemaker notebook, but json output produced is unpredictable(find details in example output file)

3. guidance_guaranteed_json_llama.py -> works on workstation by downloading model from hugging face. Not working yet with llama chat model. To do : try prompt containing user/system/assistance prompts by importing chat model with guidance support

4. openai_pydantic_program_gpt.py -> working for gpt, To do : llama pending

5. llama_index_guidance_pydantic_gpt.py -> not working yet(try troubleshooting locally on notebook)

