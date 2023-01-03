import os
import dataclasses
from functools import lru_cache

@dataclasses.dataclass
class AppConfig:
    database_uri: str
    buckets_root: str    

    @lru_cache
    @staticmethod
    def from_env() -> "AppConfig":
        def read_env(key: str) -> str:
            result = os.getenv(key)
            if not result:
                raise ValueError(f'Expected {key} environment var')
            return result

        return AppConfig(
            database_uri = read_env('DATABASE_URI'),
            buckets_root =  read_env('BUCKETS_ROOT')
        )
