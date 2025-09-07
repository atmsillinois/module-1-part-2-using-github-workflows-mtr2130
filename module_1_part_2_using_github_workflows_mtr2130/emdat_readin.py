import polars as pl


def read_in_certain_disaster_type_or_subtype(filepath, typeorsubtype, disaster):
    all_disaster_data = pl.read_excel(filepath)
    filtered_data = all_disaster_data.filter(pl.col(typeorsubtype) == disaster)
    return filtered_data
