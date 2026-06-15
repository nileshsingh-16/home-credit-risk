from dataclasses import dataclass
import pandas as pd

@dataclass
class Metadata:
    column_summary: pd.DataFrame

    target_column: str

    numeric_columns: list
    categorical_columns: list
    datetime_columns: list
    id_columns: list
    binary_columns: list 