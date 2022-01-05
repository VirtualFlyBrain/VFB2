import sys
from os import listdir, chdir
from os.path import isfile, join
from vfb_connect.cross_server_tools import VfbConnect



note = """
{{% alert title="Note" color="primary" %}}This page displays the raw VFB json record for this term. Please use the link below to open the term inside the Virtual Fly Brain viewer{{% /alert %}}
"""
wrapper = """---
    title: "{0} [{1}]"
    linkTitle: "{0}"
    tags: [{4}]
    content: [term]
    date: 2022-01-01
    description: >
        {2} {3}
    weight: 1000
    sitemap_exclude: true
---

{8}

<span style="font-size:larger;">[Open **{0}** in **VFB**](https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id={1})</span>

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
                dest.add('<img src="' + v + 'thumbnail.png" alt="{{< param linkTitle >}}" width="200"/>')
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
            if not v in str(dest) and not v.endswith("_c") and not v.endswith("-c"):
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
            if run > 1:
                filename = id + ".md"
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
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = term["term"]["core"]["short_form"] + ".md"
    if not os.path.isfile(filename):
        f = open(filename, "w", encoding="utf-8")
        images = ""
        images = " ".join(find_images(term, "image_folder", set()))
        if "<img" in images:
            images = '## Available images\n<a href="https://v2.virtualflybrain.org/org.geppetto.frontend/geppetto?id=' + term["term"]["core"]["short_form"] + '">' + images + '</a>'
        desc = ""
        com = ""
        tags = ""
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
        
        whole = wrapper.format(term["term"]["core"]["label"].replace('\\','&bsol;'),term["term"]["core"]["short_form"],desc,com,tags,json.dumps(term, indent=4),images,now,note)
        try:
            f.write(whole)
        except:
            print(whole)
        f.close()


vc=VfbConnect(neo_endpoint='http://pdb.v4.virtualflybrain.org', neo_credentials=('neo4j', 'vfb'), owlery_endpoint='http://owl.virtualflybrain.org/kbs/vfb/')


mypath = sys.argv[1]
print("Updating all files in " + mypath)
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

chdir(mypath + 'fbbt/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbt' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbbi/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBbi' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbcv/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBcv' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'fbdv/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FBdv' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + 'vfb/')
vfb = vc.nc.commit_list(["MATCH (n:Individual) WHERE n.short_form starts with 'VFB_' AND NOT n.short_form starts with 'VFB_internal' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0]
save_terms(vfb)
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'VFBexp_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

save_terms(vc.nc.commit_list(["MATCH (n:pub) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])
chdir(mypath + '../datasets/')

save_terms(vc.nc.commit_list(["MATCH (n:DataSet) with n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'go/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'GO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'so/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'SO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'ioa/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'IAO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'geno/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'GENO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'pato/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'PATO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'pco/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'PCO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'uberon/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'UBERON_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'ro/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'RO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'obi/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'OBI_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'ncbitaxon/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'NCBITaxon_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'zp/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'ZP_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'wbphenotype/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'WBPhenotype_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'caro/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'CARO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'bfo/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'BFO_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

chdir(mypath + 'flybase/')
save_terms(vc.nc.commit_list(["MATCH (n:Class) WHERE n.short_form starts with 'FB' AND NOT n.short_form contains '_' AND NOT n:Deprecated WITH n.short_form as id ORDER BY id ASC RETURN collect(distinct id) as ids"])[0]['data'][0]['row'][0])

