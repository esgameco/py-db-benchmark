# py-db-benchmark

A tool designed to benchmark various Python database drivers. Performance is also affected by how the database is setup.

## Setup

```bash
git clone https://github.com/esgameco/py-db-benchmark.git
pip install -r requirements.txt
```

## Results (personal)

- Postgres - asyncpg
    ```bash
    Average: 665.8529996871948 ms
    b_asyncpg_create_pool: 625.2999782562256 ms
    b_asyncpg_create_table: 12.485694885253906 ms
    b_asyncpg_insert: 5.944466590881348 ms
    b_asyncpg_update: 4.715275764465332 ms
    b_asyncpg_get: 4.470968246459961 ms
    b_asyncpg_delete_table: 5.618858337402344 ms
    b_asyncpg_delete_pool: 7.317757606506348 ms
    ```

## Notes

- Postgres run on Docker Desktop