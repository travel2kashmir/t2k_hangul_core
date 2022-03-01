from typing import Any, Dict, Iterator

_instance: 'ConfigStore' = None


class ConfigStore:

    _config: Dict[str, Any] = {}

    @classmethod
    def get_instance(cls) -> 'ConfigStore':
        global _instance
        if not _instance:
            _instance = cls()
        # END IF
        return _instance
    # END get_instance

    @classmethod
    def initialize(cls, config: Dict[str, Any]) -> 'ConfigStore':
        instance = cls.get_instance()
        instance.load(config)
        return instance
    # END get_instance

    def get(self, key: str) -> Any:
        return self._config.get(key)
    # END get

    def get_many(self, *keys: str) -> Iterator[Any]:
        return map(self.get, keys)
    # END get_many

    def load(self, config: Dict[str, Any]):
        self.set_many(**config)
    # END load

    def reset(self):
        self._config = {}
    # END reset

    def set(self, key: str, value: Any):
        self._config[key] = value
    # END set

    def set_many(self, **kwargs):
        for key, value in kwargs.items():
            self.set(key, value)
        # END LOOP
    # END set_many

# END ConfigStore
