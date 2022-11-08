import typer
import os
from termcolor import colored

app = typer.Typer()

@app.command()
def config_checker(variable):


    memory = os.popen("sudo docker container inspect " + variable + " |grep -w " + "Memory")
    memory = memory.read().split()[1].strip(",")
    if memory == "null" or memory == "0":
    	print("Memory Limit is currently set to : ", colored(memory, 'red'))
    else:
    	print("Memory Limit is currently set to : ", colored(memory, 'green')) 
    	
    	 	
    cpus = os.popen("sudo docker container inspect " + variable + " |grep -w " + "NanoCpus")
    cpus = cpus.read().split()[1].strip(",")
    if cpus == "null" or cpus == "0":
    	print("cpus Limit is currently set to : ", colored(cpus, 'red'))
    else:
    	print("cpus Limit is currently set to : ", colored(cpus, 'green'))     

    
    
    pids = os.popen("sudo docker container inspect " + variable + " |grep -w " + "PidsLimit")
    pids = pids.read().split()[1].strip(",")
    if pids == "null" or pids == "0":
    	print("pids Limit is currently set to : ", colored(pids, 'red'))
    else:
    	print("pids Limit is currently set to : ", colored(pids, 'green'))
    
    
    ulimit = os.popen("sudo docker container inspect " + variable + " |grep -w " + "Ulimits")
    ulimit = ulimit.read().split()[1].strip(",")
    if ulimit == "null" or ulimit == "0":
    	print("ulimit is currently set to : ", colored(ulimit, 'red'))
    else:
    	print("ulimit is currently set to : ", colored(ulimit, 'green'))

    
    
    capdrop = os.popen("sudo docker container inspect " + variable + " |grep -w " + "CapDrop")
    capdrop = capdrop.read().split()[1].strip(",")
    if capdrop == "null" or capdrop == "0":
    	print("capdrop is currently set to : ", colored(capdrop, 'red'))
    else:
    	print("capdrop is currently set to : ", colored(capdrop, 'green'))


if __name__ == "__main__":
    print("Check docker container vulnerabilities")
    container=input('container name: ')
    config_checker(container)