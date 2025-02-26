import sys
from os import listdir, chdir
from os.path import isfile, join
from vfb_connect.cross_server_tools import VfbConnect
import re

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

# Initialize VFB connection
vc = VfbConnect()

def save_terms(ids):
    run = 100000
    import os.path
    for id in ids:
        try:
            filename = id + "_v" + str(version) + ".md"
            if not os.path.isfile(filename):
                print(f"Processing {id}...")
                terms = vc.neo_query_wrapper.get_TermInfo([id])
                if terms.empty:
                    print(f"ERROR: No data returned for {id}")
                    continue
                for _, term in terms.iterrows():
                    wrapStringInHTMLMac(term.to_dict())
                    run -= 1
        except Exception as e:
            print(f"ERROR processing {id}: {str(e)}")
            import traceback
            print(traceback.format_exc())

def get_term_url(label, short_form):
    """Create canonical URL for a term"""
    url = label.replace('\\','').replace(' ','-').lower() + "-" + short_form.lower()
    return re.sub("[^0-9a-zA-Z-_]+", "", url)

def format_relationships(term):
    rels = []
    if "relationships" in term:
        for rel in term["relationships"]:
            obj = rel["object"]
            types = ""
            if "types" in obj:
                types = " ".join([f'<span class="label label-{t}">{t}</span>' for t in obj["types"]])
            term_url = get_term_url(obj["label"], obj["short_form"])
            rels.append(f'- {rel["relation"]["label"]} [{obj["label"]}](https://www.virtualflybrain.org/term/{term_url}) <span class="label types">{types}</span>')
    return "\n".join(rels)

def format_classification(term):
    classes = []
    if "parents" in term:
        for parent in term["parents"]:
            types = ""
            if "types" in parent:
                types = " ".join([f'<span class="label label-{t}">{t}</span>' for t in parent["types"]])
            term_url = get_term_url(parent["label"], parent["short_form"])
            classes.append(f'- [{parent["label"]}](https://www.virtualflybrain.org/term/{term_url}) <span class="label types">{types}</span>')
    return "\n".join(classes)

def format_synonyms(term):
    syns = []
    if "pub_syn" in term:
        for syn in term["pub_syn"]:
            pub_link = ""
            if "pub" in syn and "core" in syn["pub"]:
                pub = syn["pub"]["core"]
                term_url = get_term_url(pub["label"], pub["short_form"])
                pub_link = f' ([{pub["label"]}](https://www.virtualflybrain.org/term/{term_url}))'
            syns.append(f'- {syn["synonym"]["scope"]}: {syn["synonym"]["label"]}{pub_link}')
    return "\n".join(syns)

def format_xrefs(term):
    refs = []
    if "xrefs" in term:
        for xref in term["xrefs"]:
            icon = ""
            if "icon" in xref:
                icon = f'<img class="terminfo-siteicon" src="{xref["icon"]}">'
            refs.append(f'- <a href="{xref["link_base"]}{xref["accession"]}" target="_blank">{xref["site"]["label"]}</a>{icon}')
            if "link_text" in xref:
                refs.append(f'  - <a href="{xref["link_base"]}{xref["accession"]}" target="_blank">{xref["link_text"]}</a>')
    return "\n".join(refs)

def format_references(term):
    refs = []
    if "def_pubs" in term:
        for pub in term["def_pubs"]:
            cite = [f'- <a href="?id={pub["core"]["short_form"]}">{pub["core"]["label"]}</a>']
            xrefs = []
            if "FlyBase" in pub:
                xrefs.append(f'<a href="http://flybase.org/reports/{pub["FlyBase"]}" target="_blank">'
                           f'<i class="popup-icon-link gpt-fly" title="FlyBase:{pub["FlyBase"]}"></i></a>')
            if "DOI" in pub:
                xrefs.append(f'<a href="https://doi.org/{pub["DOI"]}" target="_blank">'
                           f'<i class="popup-icon-link gpt-doi" title="doi:{pub["DOI"]}"></i></a>')
            if "PubMed" in pub:
                xrefs.append(f'<a href="http://www.ncbi.nlm.nih.gov/pubmed/?term={pub["PubMed"]}" target="_blank">'
                           f'<i class="popup-icon-link gpt-pubmed" title="PMID:{pub["PubMed"]}"></i></a>')
            if xrefs:
                cite.append(f'<span class="terminfo-pubxref"> {" ".join(xrefs)}</span>')
            if "types" in pub["core"]:
                types = " ".join([f'<span class="label label-{t}">{t}</span>' for t in pub["core"]["types"]])
                cite.append(f'<span class="label types">{types}</span>')
            refs.append(" ".join(cite))
    return "\n".join(refs)

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
        images_list = []
        images = " ".join(find_images(term, "image_folder", set()))
        images_list = ",".join(find_images_list(term, "image_folder", set()))
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
        try:
            if desc == "":
                com += " [" + "; ".join(find_values(term, "label", set())) + "]"
        except Exception as e:
            print('error on label for desc')
            print(e)
            print(traceback.format_exc())
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
        
        classification = format_classification(term)
        relationships = format_relationships(term)
        synonyms = format_synonyms(term)
        xrefs = format_xrefs(term)
        references = format_references(term)
        
        url = term["term"]["core"]["label"].replace('\\','&bsol;').replace(' ','-').lower()+"-"+term["term"]["core"]["short_form"].lower()
        url = re.sub("[^0-9a-zA-Z-_]+", "", url)
        
        term_type = ','.join(term["term"]["core"].get("types", []))
        
        whole = wrapper.format(
            term["term"]["core"]["label"].replace('\\','&bsol;'),  # {0}
            term["term"]["core"]["short_form"],                    # {1}
            desc,                                                  # {2}
            com,                                                   # {3}
            tags,                                                  # {4}
            json.dumps(term, indent=4),                           # {5}
            images,                                               # {6}
            now,                                                  # {7}
            images_list,                                         # {8}
            url,                                                 # {9}
            note,                                                # {10}
            synonyms,                                            # {11}
            term_type,                                          # {12}
            classification,                                      # {13}
            relationships,                                       # {14}
            xrefs,                                              # {15}
            references                                          # {16}
        )
        
        try:
            f.write(whole)
            filename = term["term"]["core"]["short_form"] + "_v" + str(version - 1) + ".md"
            if os.path.isfile(filename):
                os.remove(filename)
                print('Removed: ' + filename)
        except:
            print(whole)
        f.close()

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

