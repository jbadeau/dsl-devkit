# DSL DevKit

DSL Developer Kit is an extension layer to [Eclipse Xtext](https://eclipse.dev/Xtext/) built for active Xtext users. It extends the Xtext runtime to handle more sophisticated cases in DSL design, support scaling for larger models, and provide better monitoring and recovery in headless frameworks based on Xtext.

## Contents

- [Overview](#overview)
- [Runtime Extensions](#runtime-extensions)
- [Tooling](#tooling)
- [Features](#features)

## Overview

DDK comes with several small DSLs that help standardize implementations of tools for DSLs:

| DSL | Plugins | Purpose |
|-----|---------|---------|
| **Check** | `check.*` | Constraint checking DSL for validation rules |
| **Check Configuration** | `checkcfg.*` | Configuration DSL for Check constraints |
| **Scope** | `scope.*` | Scoping DSL for name resolution |
| **Export** | `export.*` | Export DSL for cross-resource reference indexing |
| **Format** | `format.*` | Formatting DSL for code style |
| **Valid** | `valid.*` | Replaced by Check DSL |

## Runtime Extensions

| Plugin | Description |
|--------|-------------|
| `com.avaloq.tools.ddk.xtext` | Extensions to Xtext runtime library |
| `com.avaloq.tools.ddk.xtext.common.*` | Optional extensions to Xtext runtime library |
| `com.avaloq.tools.ddk.xtext.ui` | Eclipse UI part of runtime library extensions |
| `com.avaloq.tools.ddk.xtext.builder` | Extensions to Xtext builder |
| `com.avaloq.tools.ddk.typesystem` | Basics for building a typesystem for a DSL |

## Tooling

| Plugin | Description |
|--------|-------------|
| `com.avaloq.tools.ddk.workflow` | MWE2 workflows to regenerate DDK languages |
| `com.avaloq.tools.ddk.xtext.generator` | MWE2 workflow fragments for generating DSL implementation |
| `com.avaloq.tools.ddk.test.*` | Support for writing tests for DSLs |

## Features

| Feature | Description |
|---------|-------------|
| `com.avaloq.tools.ddk.runtime.feature` | Runtime extension to Xtext |
| `com.avaloq.tools.ddk.feature` | Toolkit for DSL development on top of Xtext |
