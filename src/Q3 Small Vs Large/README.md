Difference between small vs large file parsing

| Aspect               | Small CSV (\~100k rows)     | Large CSV (\~2M rows or more)          |
| -------------------- | --------------------------- | -------------------------------------- |
| **Loading method**   | Direct `pd.read_csv`        | Chunking (`chunksize`) or Dask         |
| **Memory usage**     | Fits in RAM easily          | Risk of running out of memory          |
| **Processing style** | In-memory operations        | Streaming / lazy execution             |
| **Speed**            | Usually faster (all in RAM) | May be slower due to chunking overhead |
| **Scalability**      | Limited by RAM              | Scales beyond RAM with Dask/streaming  |
| **Best use case**    | Exploratory analysis        | Production, big data pipelines         |

👉 **Key idea**:

* Small file = treat it like a regular pandas DataFrame.
* Large file = treat it as a **stream** or **distributed dataset**, only load what you need.
