import sys
import os
import subprocess
import shlex

fn = sys.argv[1]
if os.path.exists(fn):
    print ("Directory of genomes to anotate: ",os.path.dirname(fn))
else:
    print("Directory",fn, "do not exist\n\n ")

direct = fn
os.chdir(direct)

for file in os.listdir(direct):
        print (file)
        if file.endswith(".fasta"):
            print(file)
            in_file  = str(file)
            out_file = in_file.replace(".fasta", "")

            outdir = os.path.join(fn, out_file)
            strain_tag = in_file.split(".")[0]
            print('#####',outdir)

            print("annotating genome: ",strain_tag)

            to_comand_line = str('prokka '+in_file+' --outdir '+outdir+'_prokka'+' --prefix '+out_file+'_prokka'+' --locustag '+strain-tag)
            comand_line = to_comand_line
            subprocess.call(comand_line, shell=True)
        
            print(strain_tag, " ... Finished")
        else:
            pass 
            #print("ERROR ... ",file,"\t could not identify annotation format")
