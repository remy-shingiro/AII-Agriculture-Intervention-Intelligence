# Agricultural Intervention Intelligence — Engineering Constitution

## 1. Project Mission

Agricultural Intervention Intelligence is a production-quality data and machine-learning platform for the NISR Rwanda 2026 Big Data Hackathon.

The system will use NISR agricultural data and appropriate public external data to:

1. measure agricultural productivity;
2. identify areas with meaningful productivity gaps;
3. identify evidence-based agricultural constraints;
4. estimate intervention-priority signals;
5. explain why an area receives a given priority;
6. expose the results through an API and user-facing web application.

The system is decision support. It must not present predictive results as causal evidence unless an appropriate causal methodology has actually been implemented and validated.

---

# 2. Core Engineering Principles

## 2.1 Inspect Before Modifying

Before changing code, data pipelines, configuration, or architecture:

* inspect the relevant existing implementation;
* understand the current behavior;
* inspect tests;
* inspect Git status and relevant diffs;
* identify existing conventions;
* determine whether the requested functionality already exists.

Never modify code based solely on assumptions.

## 2.2 Do Not Invent

Never invent:

* files;
* APIs;
* classes;
* interfaces;
* database schemas;
* NISR variables;
* variable meanings;
* dataset relationships;
* statistical definitions;
* business rules;
* external-data fields;
* model behavior.

When information is unavailable, verify it from the authoritative source or explicitly document the uncertainty.

## 2.3 Smallest Correct Change

Prefer:

* small changes;
* explicit implementations;
* understandable code;
* incremental commits;
* focused pull requests.

Do not introduce abstractions, dependencies, frameworks, services, databases, or infrastructure merely because they might be useful later.

## 2.4 No Unrelated Changes

A task must not modify unrelated:

* source files;
* configuration;
* formatting;
* dependencies;
* tests;
* documentation.

If an unrelated problem is discovered, report it separately unless fixing it is necessary for the requested change.

---

# 3. Clean Architecture

The project follows Clean Architecture.

```text
src/agri_intelligence/
├── domain/
├── application/
├── infrastructure/
└── interfaces/
```

Dependencies must point inward.

```text
interfaces
    ↓
application
    ↓
domain

infrastructure
    ↓
application/domain
```

The exact dependency direction must be preserved even as the project grows.

## 3.1 Domain

The domain contains business concepts and rules.

Domain code must not depend on:

* pandas;
* NumPy;
* scikit-learn;
* XGBoost;
* SHAP;
* GeoPandas;
* Rasterio;
* FastAPI;
* Pydantic framework-specific behavior;
* database clients;
* HTTP clients;
* filesystem-specific infrastructure.

Domain objects should represent meaningful business concepts rather than technical data structures.

## 3.2 Application

Application code coordinates use cases.

Application code should:

* orchestrate domain behavior;
* define use-case boundaries;
* use explicit DTOs/models;
* remain independent of HTTP framework details;
* remain independent of pandas DataFrames;
* remain independent of specific ML frameworks.

Application code must not receive FastAPI request objects as business inputs.

## 3.3 Infrastructure

Infrastructure implements technical concerns such as:

* NISR data ingestion;
* CSV/Excel/Parquet handling;
* pandas transformations;
* geospatial processing;
* ML frameworks;
* model persistence;
* external data access;
* configuration;
* filesystem access.

Infrastructure details must not leak unnecessarily into the domain.

## 3.4 Interfaces

Interfaces contain delivery mechanisms such as:

* FastAPI routes;
* request/response schemas;
* CLI commands;
* web/API adapters.

HTTP concerns must remain outside domain logic.

---

# 4. Architecture Quality Rules

## 4.1 No Empty Architecture

Do not create classes or interfaces solely to make the directory structure appear sophisticated.

Introduce an abstraction when there is a concrete reason, such as:

* multiple implementations;
* dependency inversion;
* testability;
* external-system isolation;
* meaningful domain/application boundary.

## 4.2 No Premature Infrastructure

Do not introduce:

* PostgreSQL;
* PostGIS;
* Redis;
* message queues;
* cloud services;
* Docker services;
* microservices;

unless an actual requirement demonstrates that they are necessary.

The current architecture intentionally uses Parquet-based storage and offline model training.

---

# 5. Data Engineering Rules

## 5.1 Authoritative Metadata

NISR variable names and meanings must be verified against:

* the actual downloaded dataset;
* the official NISR dictionary;
* official survey documentation;
* authoritative metadata.

Never infer semantics from names such as `V1`, `V2`, etc.

## 5.2 Raw Data Immutability

Raw datasets must be treated as immutable inputs.

Never:

* edit raw files;
* overwrite raw files with processed data;
* silently rename raw columns;
* silently remove observations from raw data.

Transform raw data into separate intermediate/processed datasets.

## 5.3 Data Provenance

Every production dataset should eventually have traceable provenance:

```text
source
→ version/year
→ transformation
→ output
```

Important transformations and assumptions must be documented.

## 5.4 Units

Before calculations:

* verify measurement units;
* verify denominators;
* verify reference periods;
* verify agricultural-season semantics;
* convert units explicitly;
* document conversions.

Never assume that two variables with similar names use the same unit.

## 5.5 Missing Values

Distinguish where the source data allows:

* zero;
* missing;
* not applicable;
* unknown;
* refused;
* not reported.

Never automatically convert all missing values to zero.

Never silently drop missing observations without documenting why.

## 5.6 Duplicates

Never blindly call `drop_duplicates()` on analytical data.

First determine:

* the expected observation key;
* why duplicates exist;
* whether they represent legitimate repeated observations;
* whether aggregation is appropriate.

Document the resolution.

---

# 6. Unit of Analysis

The intended canonical modeling unit is:

> plot/crop × agricultural season

This must be verified against the actual datasets before implementation.

Every dataset must have an explicitly documented:

* observation unit;
* time reference;
* geographic level;
* population;
* sampling design where relevant.

Do not combine observations with incompatible units of ana
