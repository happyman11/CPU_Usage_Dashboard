import psutil
import math
import GPUtil

def  cpu_usaage():
    
    total_available_ram=psutil.virtual_memory().total
    total_ram_gb=math.ceil(total_available_ram/(1024 ** 3)) 
    
    available_ram=psutil.virtual_memory().available
    available_ram_gb=available_ram/(1024 ** 3)
    
    used_ram_gb=psutil.virtual_memory().used/(1024 ** 3)
    
    percentage_used=psutil.virtual_memory().percent
    
    free_ram_gb=psutil.virtual_memory().free/(1024 ** 3)
    
    data={
         "total_available_ram":total_ram_gb,
         "available_ram_gb":available_ram_gb,
         "used_ram_gb":used_ram_gb,
         "free_ram_gb":free_ram_gb,
         "percentage_used":percentage_used,
        }
    
    return data

print(cpu_usaage())

def disk_usage():
    
    disk_partitions = psutil.disk_partitions(all=True)
    data={}
    for partition in disk_partitions:
        try:
           disk_usage = psutil.disk_usage(partition.mountpoint)
           
           
           disk_information={
                              "Total_Space":disk_usage.total / (1024 ** 3),
                              "Used_Space":disk_usage.used / (1024 ** 3),
                              "Free_Space":disk_usage.free / (1024 ** 3),
                              "Percent_Use":disk_usage.percent
                            }
           data[partition.device[:-2]]=disk_information
           
        except PermissionError:
             continue
    
    return data
    
    

print(disk_usage())

def gpu_usage():
    gpus = GPUtil.getGPUs()
    list_gpus = {}
    for gpu in gpus:
        
        data={
              "gpu_name": gpu.name,
              "gpu_free_memory":gpu.memoryFree/1024,
              "gpu_used_memory":gpu.memoryUsed/1024,
              "gpu_total_memory":gpu.memoryTotal/1024,
              "gpu_load":gpu.load*100,
              "gpu_tempreture":gpu.temperature
              
              
              
            
             }
        list_gpus[gpu.id]=data
    
    return list_gpus


    
    
    

print(gpu_usage())

def get_cpu_information():
   
    
    cpufreq = psutil.cpu_freq()
    
    core_usage={}
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        core_usage["Core - "+str(i+1)]=percentage
       
    data={
        "Physical_cores":psutil.cpu_count(logical=False),
        "Total_cores":psutil.cpu_count(logical=True),
        "Max Frequency": cpufreq.max,
        "Min Frequency": cpufreq.min,
        "Current Frequency" : cpufreq.current,
        "Total CPU Usage": psutil.cpu_percent(),
        "Core USage":core_usage 
        
        }
    
    return data 
    
print(get_cpu_information())
