# Technical AI Engineer Test

## Rules:

*   The answer must be on the public git repo.
*   You can use whatever programming language you can, but preferably (Rust, Python, Golang, Java, Javascript, Typescript)
*   Create the video of the coding test result.
*   *No LLM permitted at this stage.*

## Engineering Knowledge AI Agent Test

1.  Describe differences between REST API, MCP in the context of AI.
2.  How REST API, MCP, can improve the AI use case.
3.  How do you ensure that your AI agent answers correctly?
4.  Describe what can you do with Docker / Containerize environment in the context of AI
5.  How do you finetune the LLM model from raw?

## Coding Test

1.  Please parse this csv, get the insight of the data `customer-100000.csv`
2.  Please parse large CSV, `customers-2000000.csv` and keep the memory low.
3.  Explain how it's different from splitting the small vs large files.
4.  Deploy the vector DB on your own, and implement the `vector cosine similarity` without using a high level library.
5.  Create a platform with UI, for
    *   a. Upload `food online receipt`
    *   b. Extract with computer vision
    *   c. Get the insight on the receipt, and store it to DB.
    *   d. Design and implement the AI tools to make sure whenever user asking,
        *   "What food did i buy yesterday"
        *   "Give me total expenses for food on 20 June"
        *   "Where did i buy hamburger from last 7 day"
        *   The LLM can answer it.
    *   e. Wrap your application into a container image using docker, and run it in your local.
    *   f. Write CI/CD to wrap your application into the container. You can use github-actions or gitlab-ci.