**Processing Small File ("customer-100000.csv") – Pandas Approach**

The dataset `"customer-100000.csv"` is processed using `pandas`, which provides a straightforward and efficient solution for datasets that fit comfortably into memory. Operations such as `df.shape`, `df.head()`, and `df.info()` indicate that the full dataset is loaded into a `pandas.DataFrame`. Loading the entire file into RAM allows quick and simple data exploration and manipulation without additional memory management considerations.

**Processing Large File ("customers-2000000.csv") – Dask Approach**

For the larger dataset `"customers-2000000.csv"`, `dask.dataframe` is employed to handle memory constraints. Due to the dataset size, loading all rows into memory at once is not feasible. Dask partitions the data into smaller chunks that are processed sequentially or in parallel, enabling efficient computation while keeping memory usage within limits. Lazy evaluation ensures that computations are only executed when necessary, further optimizing resource utilization.

**Comparison of Approaches**

| Feature            | Small File ("customer-100000.csv") | Large File ("customers-2000000.csv")            |
| ------------------ | ---------------------------------- | ----------------------------------------------- |
| Dataframe          | `pandas.DataFrame`                 | `dask.dataframe`                                |
| Memory Load        | Entire dataset loaded into memory  | Partitioned, loaded on demand                   |
| Code Complexity    | Simple, direct Pandas operations   | Higher, requires Dask setup and lazy evaluation |
| Scalability        | Limited by available RAM           | Scalable to datasets exceeding memory           |
| Compute Efficiency | Fast for small datasets            | Optimized for large datasets via parallelism    |
