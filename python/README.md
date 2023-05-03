# Python implementation of in-toto attestations

This package contains Python bindings for in-toto/attestation. Its contents
are autogenerated using
[protobuf definitions](https://github.com/in-toto/attestation/tree/main/protos).

For more information, see the
[in-toto Attestation Framework](https://github.com/in-toto/attestation).

## Usage

Install via `pip install in-toto-attestation`.

The Python bindings for the attestation layers and predicates are provided in
the `in_toto_attestation.v1` and `in_toto_attestation.predicates` packages,
respectively. Please note that our package names use the term "attestation"
in the _singular_.

## Versioning

At the moment, this library is versioned <1.0 as we work towards stabilizing
the protobuf definitions and the available predicates.