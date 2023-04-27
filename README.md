# py-db-benchmark

A tool designed to benchmark various Python database drivers. Performance is also affected by how the database is setup.

## Setup

1.  ```bash
    git clone https://github.com/esgameco/py-db-benchmark.git
    pip install -r requirements.txt
    ```
2.  Set environment variables
    - `export DB_POSTGRES=fill_in`
    - `export DB_SQLITE=fill_in`
    - `export DB_REDIS=fill_in`
3. ```bash
   python main.py
   ```

## Results (personal)

- Postgres - asyncpg
    ```bash
    Average: 668.0549144744873 ms
    b_create_pool: 626.9266366958618 ms
    b_create_table: 13.405466079711914 ms
    b_insert: 6.372976303100586 ms
    b_update: 5.007719993591309 ms
    b_get: 4.140663146972656 ms
    b_delete_table: 5.392670631408691 ms
    b_delete_pool: 6.808781623840332 ms
    ```
- SQLite - aiosqlite
    ```bash
    Average: 36.29621744155884 ms
    b_create_table: 10.523924827575684 ms
    b_insert: 6.109802722930908 ms
    b_update: 3.7161803245544434 ms
    b_get: 3.9947032928466797 ms
    b_delete_table: 11.951606273651123 ms
    ```
- Redis - redis-py
    ```bash
    Average: 7.129123210906982 ms
    b_create_pool: 0.5557537078857422 ms
    b_insert: 3.8783669471740723 ms
    b_update: 1.2389063835144043 ms
    b_get: 1.4164018630981445 ms
    b_delete_pool: 0.03969430923461914 ms
    ```
- Python - pycache (python list caching)
    ```bash
    Average: 0.022802615165710447 ms
    b_insert: 0.011410260200500488 ms
    b_update: 0.0055962085723876955 ms
    b_get: 0.0057961463928222655 ms
    ```

## Notes

- Postgres and Redis run on docker vms
- Postgres uses connection pools which slow it down initially
- Sqlite and redis not using pooling
- This project was mainly for testing database performance for NPAPI, so tests were made with that in mind.

## Conclusions

- Use caching unless absolutely necessary