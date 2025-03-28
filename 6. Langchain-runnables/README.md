

### 1. RunnableSequence

RunnableSequence is a sequential chain of runnables in LangChain that executes each step one after another, passing the output of one step as the input to the next.
It is useful when you need to compose multiple runnables together in a structured workflow.


### 2. RunnableParallel

RunnableParallel is a runnable primitive that allows multiple runnables to execute in parallel.
Each runnable receives the same input and processes it independently, producing a dictionary of outputs.

### 3. RunnablePassthrough

RunnablePassthrough is a special Runnable primitive that simply returns the input as output
without modifying it.

### 4. RunnableLambda

RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an Al pipeline.
It acts as a middleware between different Al components, enabling preprocessing, transformation, API calls, filtering, and post-processing in a LangChain workflow.


### 5. RunnableBranch

 RunnableBranch is a control flow component in LangChain that allows you to conditionally route input data to different chains or runnables based on custom logic.functions like an if/elif/else block for chains — where you define a set of condition functions, each associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching condition is executed. If no condition matches, a default runnable is used (if provided).