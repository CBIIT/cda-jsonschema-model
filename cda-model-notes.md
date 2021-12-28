# CDA Model
=========

[cda-to-mdf.py](./cda-to-mdf.py) uses the following observations to transform the CDA JSONSchema model to the [MDF in this repo](./model-desc/cda-model.yaml).

Based the latest prototype documentation, the CDA model appears to still be officially defined at 

* https://github.com/CancerDataAggregator/cda-data-model

even though the last commit to this repo was in Aug 2021.

Additional pages of interest:
* https://cda.readthedocs.io/en/latest/ReleaseNotes.html#introduction-to-cda
* https://cda.readthedocs.io/en/latest/Schema.html


The CDA model is defined in terms of a [set of json files written in JSONSchema](https://github.com/CancerDataAggregator/cda-data-model/tree/main/src/schema/json). Each file essentially specifies a Node in a property-graph interpretation.

The `properties` entry for each node defines attribute subschemas that are effectively the Property or Relationship specifications for each Node. Attributes that are defined with scalar types can be interpreted as Properties. Attributes with types described by a `$ref` key, which reference a top-level schema (one that is given in an individual file) can be interpreted as (`one_to_one`) Relationships, whose source is the Node in which the attribute is specified, and whose destination is the referenced entity. This is similar in structure the Gen3 YAML schema spec, which also depends on such "inferred Relationships".

An attribute of a top-level entity may also have a type of `array`, for which the component `item`s are `$ref`s to another top-level entity. This should evidently be interpreted to mean that the attribute is a `one_to_many` Relationship. 

`$ref`s to a top-level entity are given as a placeholder URL, with a path whose final token is the name of the entity.


## Value Sets

Properties whose values are meant (eventually) to come from acceptable value sets are given a placeholder `$ref` type "https://example.org/cda-data-model/definitions/CodeableConcept".
`CodeableConcept` is specified in [`definitions.json`](https://github.com/CancerDataAggregator/cda-data-model/blob/main/src/schema/json/definitions.json). 

No instances of CodeableConcept are given yet in the repo, but these would ultimately contain enumerations of values in the following structure:

     { "coding" : <string desc of this value set>,
	   "items" : [
	      { "code" : <term value>
		    "display" : <term handle or human-readable name>
			"system" : <basically the origin>
			"version" : < the origin version > },
		  { ... },
		  ...
		]
	 }

So a CodableConcept essentially maps to a ValueSet [MDB](https://github.com/CBIIT/bento-meta) object, and each item in a Coding list would be an MDB Term.

## Mappings

One-to-one mappings of CRDC Node model elements to the CDA model are given in `*_mapping.yml` files in the [transform](https://github.com/CancerDataAggregator/transform) repo.

These mappings only cover properties (not terms). They should be implemented in the MDB by connecting Property nodes via a single Concept node.
