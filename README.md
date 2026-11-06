# collaboration

## Pandas demo

Set up the environment (requires [uv](https://docs.astral.sh/uv/)):

```sh
uv sync
```

`sample_data/donors.csv` holds 200 rows of **synthetic** blood donor visits. It
contains no real donor data, and a few values are deliberately blank so the demo
can show missing-value handling.

| Column | Description |
| --- | --- |
| `donor_id` | Made-up donor ID |
| `visit_date` | Visit date in 2025 |
| `age`, `sex` | Donor age and sex (`F`/`M`) |
| `blood_type` | ABO/Rh blood type |
| `region` | North, South, East, or West |
| `weight_kg` | Weight in kilograms |
| `hemoglobin_g_dl` | Hemoglobin in g/dL |
| `systolic_bp`, `diastolic_bp` | Blood pressure in mmHg |
| `first_time_donor` | Whether this was the donor's first donation |
| `deferred` | Whether hemoglobin was too low to donate |
| `volume_ml` | Volume collected (`0` if deferred) |
