import pandas as pd

class MetadataBuilder:

    def __init__(self, config):
        self.config = config

    def fit(self, df):
        pass

    def _build_column_summary(self, df):
        rows = []

        for col in df.columns:
            s = df[col]

            value_counts = s.value_counts(normalize=True.dropna=False)

            dominant_pct = (value_counts.iloc[0] if len(value_counts) > 0 else 0)

            rows.append({
                "column_name": col,
                "pandas_dtype": str(s.dtype),
                "dominant_pct": dominant_pcy
            })

        return pd.dataFrame(rows)

    def _infer_type(self, series, column_name, unique_pct):
        pass

    def _generate_flags(self, row):
        pass