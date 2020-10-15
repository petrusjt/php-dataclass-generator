import sys
import codecs

var_names = sys.argv[2:]

with codecs.open(sys.argv[1] + ".php", "w", "utf-8") as f:
    f.write(
f"""<?php

class {sys.argv[1]}
{{
""")
    for var_name in var_names:
        f.write(f"\tprivate ${var_name};\n")
    
    f.write("\n")

    f.write("\t//Konstruktor null alapértelmezett paraméterekkel\n\n")
    # Constructor generation with nulled out default values for all the fields
    f.write("\tpublic function __construct(")
    # Listing all the parameters for the constructor
    for var_name in var_names:
        if var_name != var_names[-1]:
            f.write(f"${var_name}=null, ")
        else:
            f.write(f"${var_name}=null)\n")
    f.write("\t{\n")
    for var_name in var_names:
        f.write(f"\t\t$this->{var_name} = ${var_name};\n")
    f.write("\t}\n")

    f.write("\n")

    f.write("\t//Getterek/Setterek\n")
    # Getters/setters
    for var_name in var_names:
        f.write(f"""
    public function get{var_name[0].upper() + var_name[1:]}()
    {{
        return $this->{var_name};
    }}
    public function set{var_name[0].upper() + var_name[1:]}(${var_name})
    {{
        $this->{var_name} = ${var_name};
    }}
        """)
    f.write("\n")
    
    f.write("\t//Builder pattern-szerűség\n")
    # Builder pattern
    for var_name in var_names:
        f.write(f"""
    public function {var_name[0].upper() + var_name[1:]}(${var_name})
    {{
        $this->{var_name} = ${var_name};
    }}
""")

    f.write("}\n")
    f.write("?>\n")







