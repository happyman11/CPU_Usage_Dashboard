import psutil
import math
import GPUtil

def  cpu_usaage():
    
    total_available_ram=psutil.virtual_memory().total
    total_ram_gb=math.ceil(total_available_ram/(1024 ** 3)) 
    
    available_ram=psutil.virtual_memory().available
    available_ram_gb=available_ram/(1024 ** 3)
    available_ram_per=math.ceil((available_ram_gb/total_ram_gb)*100)
    
    used_ram_gb=math.floor(psutil.virtual_memory().used/(1024 ** 3))
    used_ram_per=math.ceil((used_ram_gb/total_ram_gb)*100)
    
    percentage_used=psutil.virtual_memory().percent
    
    free_ram_gb=psutil.virtual_memory().free/(1024 ** 3)
    free_ram_per=math.ceil((free_ram_gb/total_ram_gb)*100)
    
    cpufreq = psutil.cpu_freq() 
     
    data={
         "total_available_ram":total_ram_gb, 
         "available_ram_gb":available_ram_gb,
         "available_ram_per":available_ram_per,
         "used_ram_gb":used_ram_gb, 
         "used_ram_per":used_ram_per,
         "free_ram_per":free_ram_per,     
         "free_ram_gb":math.ceil(free_ram_gb),
         "percentage_used":percentage_used,
         "Max_Frequency": int(cpufreq.max),
        "Current_Frequency" : int(cpufreq.current),
        "Cpu_usage":psutil.cpu_percent()
        }
    
    return data



def disk_usage():
    
    disk_partitions = psutil.disk_partitions(all=True)
    data={}
    for partition in disk_partitions:
        try:
           disk_usage = psutil.disk_usage(partition.mountpoint)
           
           
           disk_information={
                              "Total_Space":format(disk_usage.total / (1024 ** 3),".2f"),
                              "Used_Space":format(disk_usage.used / (1024 ** 3),".2f"),
                              "Used_Space_percent":format(((disk_usage.used / (1024 ** 3))/(disk_usage.total / (1024 ** 3)))*100,".2f"),
                              "Free_Space_percent":format(((disk_usage.free / (1024 ** 3))/(disk_usage.total / (1024 ** 3)))*100,".2f"),
                              "Free_Space":format(disk_usage.free / (1024 ** 3),".2f"),
                              "Percent_Use":format(disk_usage.percent,".2f")
                            }
           data[partition.device[:-2]]=disk_information
           
        except PermissionError:
             continue
    
    return data
    
    



def gpu_usage():
    gpus = GPUtil.getGPUs()
    list_gpus = {}
    for gpu in gpus:
        
        data={
              "gpu_name": gpu.name,
              "gpu_free_memory":format(gpu.memoryFree/1024,".2f"),
            
              "gpu_used_memory":format(gpu.memoryUsed/1024,".2f"),
              "gpu_used_memory_percent":((gpu.memoryUsed/1024)/gpu.memoryTotal/1024)*100,
              "gpu_free_memory_percent":math.ceil(100-((gpu.memoryUsed/1024)/gpu.memoryTotal/1024)*100),
              "gpu_total_memory":format(gpu.memoryTotal/1024,".2f"),
              "gpu_load": format(gpu.load*100,".2f"),
              "gpu_tempreture":gpu.temperature
              
              
              
            
             }
        list_gpus[gpu.id]=data
   
    
    return list_gpus


    
    
    


def get_cpu_information():
   
    
    cpufreq = psutil.cpu_freq()
    
    core_usage={}
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        core_usage["Core"+str(i+1)]=percentage
       
    data={
        "Physical_cores":psutil.cpu_count(logical=False),
        "Total_cores":psutil.cpu_count(logical=True),
        "Core_Usage":core_usage 
        
        }
    
    return data 
    
