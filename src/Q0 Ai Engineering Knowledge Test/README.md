
## Describe differences between REST API, MCP in the context of AI.

**REST API (Representational State Transfer)**:
- Traditional web service architecture using HTTP methods (GET, POST, PUT, DELETE)
- Stateless communication between client and server
- In AI context: Used for model inference endpoints, data retrieval, and integration with external services
- Request-response pattern with JSON/XML payloads
- Well-established with extensive tooling and documentation

**MCP (Model Context Protocol)**:
- Relatively new protocol specifically designed for AI agent interactions
- Enables structured communication between AI systems and external tools/resources
- Focuses on context sharing and tool integration for AI agents
- Designed for more complex, stateful interactions that AI agents require
- Optimized for the specific needs of LLM-based systems

## How REST API, MCP, can improve the AI use case.

**REST API Benefits**:
- **Integration**: Connects AI systems with existing enterprise services and databases
- **Scalability**: Load balancing and horizontal scaling for AI inference services
- **Modularity**: Separates AI logic from application logic, enabling microservices architecture
- **Accessibility**: Makes AI capabilities available to web and mobile applications
- **Standardization**: Familiar interface for developers to consume AI services

**MCP Benefits**:
- **Enhanced Context**: Provides richer context sharing between AI agents and tools
- **Tool Integration**: Streamlined connection to databases, APIs, and external services
- **Agent Orchestration**: Better coordination between multiple AI agents
- **Semantic Understanding**: Protocol designed with AI workflow patterns in mind
- **Efficiency**: Reduced overhead for AI-specific communication patterns


## How do you ensure that your AI agent answers correctly?

**Validation Strategies**:
- **Ground Truth Comparison**: Validate against known correct answers in test datasets
- **Multi-model Consensus**: Use multiple models and compare outputs for consistency
- **Human-in-the-Loop**: Implement review processes for critical decisions
- **Confidence Scoring**: Analyze model confidence levels and uncertainty quantification

**Technical Approaches**:
- **Retrieval-Augmented Generation (RAG)**: Verify answers against authoritative sources
- **Fact-checking Pipelines**: Automated verification against knowledge bases
- **Output Parsing**: Structured validation of response formats and constraints
- **A/B Testing**: Compare different model versions or prompting strategies

**Monitoring and Feedback**:
- **Continuous Evaluation**: Regular testing on benchmark datasets
- **User Feedback Loops**: Collect and incorporate user corrections
- **Error Analysis**: Systematic analysis of failure modes and edge cases
- **Version Control**: Track model performance across different deployments

## Describe what can you do with Docker / Containerize environment in the context of AI

**Model Deployment**:
- **Reproducible Environments**: Ensure consistent runtime across development, staging, and production
- **Dependency Management**: Package AI frameworks (PyTorch, TensorFlow) with specific versions
- **GPU Support**: NVIDIA Docker containers for CUDA-enabled AI workloads
- **Model Serving**: Containerized inference servers (TensorFlow Serving, TorchServe, Triton)

**Development Benefits**:
- **Isolation**: Separate different AI projects with conflicting dependencies
- **Scalability**: Kubernetes orchestration for auto-scaling AI services
- **CI/CD Integration**: Automated testing and deployment pipelines for ML models
- **Resource Management**: CPU/GPU allocation and limits for AI workloads

**Operational Advantages**:
- **Multi-environment Consistency**: Same container runs identically across cloud providers
- **Microservices Architecture**: Break complex AI systems into manageable components
- **Rolling Updates**: Deploy new model versions with zero downtime
- **Monitoring**: Containerized logging and metrics collection for AI services


## How do you finetune the LLM model from raw?

**Data Preparation**:
- **Dataset Curation**: Collect and clean domain-specific training data
- **Tokenization**: Process text using the model's specific tokenizer
- **Data Formatting**: Structure data for the chosen fine-tuning approach (instruction-following, completion, etc.)
- **Train/Validation Split**: Prepare evaluation datasets to monitor overfitting

**Fine-tuning Approaches**:
- **Full Fine-tuning**: Update all model parameters (resource-intensive)
- **Parameter-Efficient Methods**: LoRA, QLoRA, or adapter-based approaches
- **Instruction Tuning**: Train on instruction-response pairs for better task following
- **RLHF (Reinforcement Learning from Human Feedback)**: Align model outputs with human preferences

**Technical Implementation**:
- **Framework Selection**: Use libraries like Hugging Face Transformers, DeepSpeed, or Axolotl
- **Hardware Requirements**: Multi-GPU setups or cloud instances with sufficient VRAM
- **Hyperparameter Tuning**: Learning rate scheduling, batch size optimization, gradient accumulation
- **Checkpointing**: Save intermediate model states for recovery and evaluation

**Evaluation and Deployment**:
- **Performance Metrics**: Perplexity, BLEU scores, task-specific benchmarks
- **Safety Testing**: Check for harmful outputs or bias amplification
- **Model Optimization**: Quantization, pruning, or distillation for deployment efficiency
- **Version Management**: Track model lineage and performance across iterations