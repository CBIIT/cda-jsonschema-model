import os
import re
from pathlib import Path
from warnings import warn
import json
from pdb import set_trace
import yaml
from yaml import CDumper as Dumper

def get_thing(refstr):
    thing_match  = re.compile(".*/([^/]+)$").match(refstr)
    if not thing_match:
        warn("Bad format for items $ref '{}'".
             format(refstr))
        return None
    return thing_match.group(1)
    

def ent_and_spec(hdl, p, defn, reqd=[]):
    ent = None
    spec = {"Desc":defn.get("description")}
    if p in reqd:
        spec["Req"] = True
    if defn.get("oneOf"):  # kludge - choose relationship over string property
        for t in defn["oneOf"]:
            if t.get("$ref"):
                defn["$ref"] = t["$ref"]
                break
    if defn.get("type") or defn.get("$ref"):
        if not defn.get("$ref") and defn.get("type") != "array":
            # simple attribute
            ent = "PropDefinition"
            spec["Type"] = defn["type"]
        elif defn.get("$ref"):
            thing = get_thing(defn["$ref"])
            if thing == "CodeableConcept":
                ent = "PropDefinition"
                spec["Enum"] = ["TBD"]
            else: # another CDA entity
                ent = "Relationship"
                spec["Props"] = None
                spec["Ends"] = spec.get("Ends") or []
                spec["Ends"].append(
                    { "Src": hdl, "Dst": thing })
                spec["Mul"] = "one_to_one"
        elif defn.get("type") == "array":
            if not defn.get("items"):
                set_trace()
                warn("No 'items' in schema with type 'array' for '{}'".
                     format(p))
                return (None,None)
            if defn["items"].get("oneOf"):  # kludge - choose relationship over string property
                for t in defn["items"]["oneOf"]:
                    if t.get("$ref"):
                        defn["items"]["$ref"] = t["$ref"]
                        break
            if defn["items"].get("$ref"):
                ent = "Relationship"
                spec["Props"] = None
                thing = get_thing(defn["items"]["$ref"])
                spec["Ends"] = spec.get("Ends") or []
                spec["Ends"].append(
                    { "Src": hdl, "Dst": thing })
                spec["Mul"] = "one_to_many"
            else:
                ent = "PropDefinition"
                spec["Type"] = {
                    "value_type": "list",
                    "item_type": defn["items"].get("type") or defn["items"].get("oneOf"),

                    }
        else:
            warn("Huh?")
            return(None, None)
    else:
        warn("Baking powder?")
        return(None,None)
    return (ent, spec)

schemadir = os.environ.get("SCHEMADIR") or "./cda-data-model/src/schema/json"
mdf = { 
    "Nodes": {},
    "Relationships": {},
    "PropDefinitions": {},
    "Terms": {},
}
schemas = {}

    
for j in [x for x in os.listdir(schemadir) if x.find("json") >= 0]:
    p = Path(schemadir, j)
    hdl = re.compile("(.*)[.]json$").match(p.name).group(1)
    schemas[hdl] = json.load(open(p,"r"))

for (d, defn) in schemas["definitions"]["definitions"].items():
    schemas[d] = defn

for hdl in schemas:
    if hdl == "definitions":
        continue
    mdf["Nodes"][hdl] = { "Props":[] }
    for (p,defn) in schemas[hdl]["properties"].items():
        (ent,spec) = ent_and_spec(hdl,p,defn, schemas[hdl].get("required") or [])
        phdl = p.translate(str.maketrans(":","_"))
        if ent == "PropDefinition":
            mdf["Nodes"][hdl]["Props"].append(phdl)
            mdf["PropDefinitions"][phdl] = spec
        elif ent == "Relationship":
            mdf["Relationships"][phdl] = spec
        else:
            warn("Failed to parse entity {} in {}".format(p, hdl))
mdf_y = yaml.dump(mdf,default_style="'",default_flow_style=False,tags=None)
# remove tags
print(re.compile("!!(?:bool|null) '([^']+)'").sub("\\1",mdf_y))


