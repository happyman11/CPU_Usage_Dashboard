from django import template
from .utilities  import *

register = template.Library()

@register.simple_tag()
def ram():
    
    ram_info=cpu_usaage()
    
    return ram_info    

@register.simple_tag()
def gpu():
    
    gpu_info=gpu_usage()
    
    return gpu_info  

@register.simple_tag()
def disk():
    
    disk_info=disk_usage()
    
    return disk_info  

@register.simple_tag()
def cpu():
    
    cpu_info=get_cpu_information()
    
    return cpu_info  


