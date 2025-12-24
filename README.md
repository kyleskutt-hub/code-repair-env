# Code Repair Environment

A verifiers-compatible RL environment for training LLMs to fix buggy Python code.

## Installation
`ash
pip install -e .
`

## Usage
`python
from code_repair import load_environment

# Create environment with 100 buggy code examples
env = load_environment(num_examples=100)

# View a sample
print(env.dataset[0])
`

## Bug Types

- wrong_operator (+ instead of *)
- off_by_one (index errors)
- wrong_base_case (recursion errors)
- missing_guard (no null checks)
- type_error (string/int confusion)
- type_conversion (missing int()/str())
- And more...

## With OpenAI API
`python
from openai import OpenAI
from code_repair import load_environment

env = load_environment(num_examples=10)
client = OpenAI()

results = env.evaluate(
    client=client,
    model="gpt-4.1-mini",
    num_examples=10
)
`

## Prime Intellect Integration

This environment is compatible with the Prime Intellect verifiers framework and can be published to their Environments Hub.

## License

Apache 2.0
