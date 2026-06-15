from dataclasses import dataclass, field

@dataclass
class EDAConfig:
    target_column: str

    categorical_columns: list[str] = field(default_factory=list)
    numeric_columns: list[str] = field(default_factory=list)
    datetime_columns: list[str] = field(default_factory=list)
    id_columns: list[str] = field(default_factory=list)

    high_missing_threshold: float = 0.40
    near_constant_threshold: float = 0.95
    high_cardinality_threshold: int = 100
    id_uniqueness_threshold: float = 0.95