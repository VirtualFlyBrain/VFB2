import sys
from os import listdir, chdir
from os.path import isfile, join
from vfb_connect.cross_server_tools import VfbConnect

version = 6

note = """
{{% alert title="Note" color="primary" %}}This page displays the raw VFB json record for this term. Please use the link below to open the term inside the Virtual Fly Brain viewer{{% /alert %}}
"""
wrapper = """---
    title: "{0} [{1}]"
    linkTitle: "{0}"
    tags: [{4}]
    content: [term]
    date: 2022-01-01
    images: [{7}]
    description: >
        {2} {3}
    weight: 10000
    sitemap_exclude: true
    canonicalUrl: "https://www.virtualflybrain.org/term/{9}/"
---

{8}

[Open **{0}** in **VFB**](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1})

## Term Information

- **ID**: {1}
- **Name**: {0}
- **Definition**: {2}
- **Synonyms**: {10}
- **Type**: {11}
- **Comment**: {3}

{6}

## VFB Term Json

```json
{5}
```

"""

def find_images(src, key, dest=set()):
    for k, v in zip(src.keys(), src.values()):
        if key == k:
            if not v in str(dest):
                dest.add('<a href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?i=' + v.replace("https://www.virtualflybrain.org/data/", "").replace("https://virtualflybrain.org/data/", "").replace("http://virtualflybrain.org/data/", "").replace("http://www.virtualflybrain.org/data/", "").replace("/data/","").replace("/VFB_",",VFB_").replace("/i/","_").replace("/","") +'" ><img src="' + v + 'thumbnail.png" alt="{{< param linkTitle >}}" width="200"/></a>')
        elif isinstance(v, dict):
            if key in str(v):
                dest.union(find_images(v, key, dest))
        elif isinstance(v, list):
            if key in str(v):
                for i in v:
                    if key in str(i):
                        if isinstance(i, dict):
                            dest.union(find_images(i, key, dest))
    return dest

def find_images_list(src, key, dest=set()):
    for k, v in zip(src.keys(), src.values()):
        if key == k:
            if not v in str(dest):
                dest.add('"' + v + '"')
        elif isinstance(v, dict):
            if key in str(v):
                dest.union(find_images(v, key, dest))
        elif isinstance(v, list):
            if key in str(v):
                for i in v:
                    if key in str(i):
                        if isinstance(i, dict):
                            dest.union(find_images(i, key, dest))
    return dest

def find_values(src, key, dest=set()):
    for k, v in zip(src.keys(), src.values()):
        if key == k:
            if not v in str(dest) and not v.endswith("_c") and not v.endswith("-c") and not v.endswith(" c"):
                dest.add(v)
        elif isinstance(v, dict):
            if key in str(v):
                dest.union(find_values(v, key, dest))
        elif isinstance(v, list):
            if key in str(v):
                for i in v:
                    if key in str(i):
                        if isinstance(i, dict):
                            dest.union(find_values(i, key, dest))
    return dest

def save_terms(ids):
    run = 100000
    import os.path
    for id in ids:
        try:
                filename = id + "_v" + str(version) + ".md"
                if not os.path.isfile(filename):
                    print(id)
                    terms = vc.neo_query_wrapper.get_TermInfo([id])
                    for term in terms:
                        wrapStringInHTMLMac(term)
                        run -= 1
        except:
            print("ERROR:" + id)


def wrapStringInHTMLMac(term):
    import datetime
    import json
    import os.path
    import traceback
    import re
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = term["term"]["core"]["short_form"] + "_v" + str(version) + ".md"
    if not os.path.isfile(filename):
        f = open(filename, "w", encoding="utf-8")
        images = ""
        images = " ".join(find_images(term, "image_folder", set()))
        if "<img" in images:
            images = '## Example Images\n' + images
        desc = ""
        com = ""
        tags = ""
        synonyms = ""
        term_type = ""
        try:
            desc = ' '.join(term["term"]["description"]).replace("\n", " ").replace('\r', ' ')
            com = ' '.join(term["term"]["comment"]).replace("\n", " ").replace('\r', ' ')
        except:
            print('missing desc')
        # If no description then combine all 'label' in the json to give a a crude description of term, xrefs, technique & examples.
        try:
            if desc == "":
                com += " [" + "; ".join(find_values(term, "label", set())) + "]"
        except Exception as e:
            print('error on label for desc')
            print(e)
            print(traceback.format_exc())
        # Add Ontology to tags list (XXX from XXX_YYYYYYYY)
        try:
            tags = ','.join(term["term"]["core"]["types"])
            if "_" in term["term"]["core"]["short_form"]:
                tags += "," + term["term"]["core"]["short_form"].split("_")[0]
            elif term["term"]["core"]["short_form"].startswith("FB"):
                tags += "," + term["term"]["core"]["short_form"][0:4]
        except Exception as e:
            print('error on tag creation')
            print(e)
            print(traceback.format_exc())
        # Add extra meta 
        try:
            synonyms = ", ".join([syn["val"] for syn in term["term"].get("synonyms", [])])
            term_type = term["term"].get("type", "")
        except Exception as e:
            print('error on extra meta creation')
            print(e)
            print(traceback.format_exc())
        url = term["term"]["core"]["label"].replace('\\','&bsol;').replace(' ','-').lower()+"-"+term["term"]["core"]["short_form"].lower()
        url = re.sub("[^0-9a-zA-Z-_]+", "", url)
        whole = wrapper.format(term["term"]["core"]["label"].replace('\\','&bsol;'),term["term"]["core"]["short_form"],desc,com,tags,json.dumps(term, indent=4),images,now,note,url,synonyms,term_type)
        try:
            f.write(whole)
            filename = term["term"]["core"]["short_form"] + "_v" + str(version - 1) + ".md"
            if os.path.isfile(filename):
                os.remove(filename)
                print('Removed: ' + filename)
        except:
            print(whole)
        f.close()


vc=VfbConnect(neo_endpoint='http://pdb.virtualflybrain.org', neo_credentials=('neo4j', 'vfb'), owlery_endpoint='http://owl.virtualflybrain.org/kbs/vfb/')


mypath = sys.argv[1]
print("Updating all files in " + mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

chdir(mypath + 'fbbt/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbt' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbbi/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbi' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbcv/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBcv' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbdv/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBdv' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'vfb/')
vfb = vc.nc.commit_list(["MATCH (n:Individual) WHERE n.short_form starts with 'VFB_' AND NOT n.short_form starts with 'VFB_internal' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0]
save_terms(vfb)
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'VFBexp_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

# TODO: replace once VFBconnect pub queries added
#save_terms(vc.nc.commit_list(["MATCH (n:pub) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + '../datasets/')

save_terms(vc.nc.commit_list(["MATCH (n:DataSet) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'go/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'GO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'so/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'SO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'ioa/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'IAO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'geno/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'GENO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'pato/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'PATO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'pco/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'PCO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'uberon/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'UBERON_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'ro/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'RO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'obi/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'OBI_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'ncbitaxon/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'NCBITaxon_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'zp/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'ZP_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'wbphenotype/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'WBPhenotype_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'caro/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'CARO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'bfo/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'BFO_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'flybase/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FB' AND NOT n.short_form contains '_' WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

