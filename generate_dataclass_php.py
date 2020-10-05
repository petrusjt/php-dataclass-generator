import sys
import codecs

var_names = sys.argv[2:]

with codecs.open(sys.argv[1], "w", "utf-8") as f:
    f.write(
f"""<?php

class {sys.argv[1][:-4]}
\u007B
""")
    for var_name in var_names:
        f.write(f"\tprivate ${var_name};\n")
    
    f.write("\n")

    f.write("\t//Konstruktor null alapértelmezett paraméterekkel\n\n")
    # Constructor generation with nulled out default values for all the fields
    f.write("\tpublic function __construct(")
    for var_name in var_names:
        if var_name != var_names[-1]:
            f.write(f"${var_name}=null, ")
        else:
            f.write(f"${var_name}=null")
    f.write(")\n")
    f.write("\t{\n")
    for var_name in var_names:
        f.write(f"\t\t$this->{var_name} = ${var_name};\n")
    f.write("\t}\n")

    f.write("\n")

    f.write("\t//Getterek/Setterek\n\n")
    # Getters/setters
    for var_name in var_names:
        f.write(f"\tpublic function get{var_name[0].upper() + var_name[1:]}()\n")
        f.write("\t{\n")
        f.write(f"\t\treturn $this->{var_name};\n")
        f.write("\t}\n")
        f.write(f"\tpublic function set{var_name[0].upper() + var_name[1:]}(${var_name})\n")
        f.write("\t{\n")
        f.write(f"\t\t$this->{var_name} = ${var_name};\n")
        f.write("\t}\n")
    f.write("\n")
    
    f.write("\t//Builder pattern-szerűség\n\n")
    # Builder pattern
    for var_name in var_names:
        f.write(f"\tpublic function {var_name[0].upper() + var_name[1:]}()\n")
        f.write("\t{\n")
        f.write(f"\t\t$this->{var_name} = ${var_name};\n")
        f.write("\t\treturn $this;\n")
        f.write("\t}\n")

    f.write("}\n")
    f.write("?>\n")







