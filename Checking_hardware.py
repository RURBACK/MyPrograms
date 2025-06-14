import platform
import psutil
import wmi  # Только для Windows!
import time


def get_cpu_model():
    if platform.system() == "Windows":
        c = wmi.WMI()
        cpus = c.Win32_Processor()
        return cpus[0].Name.strip()
    elif platform.system() == "Linux":
        cmd = ["lscpu"]
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, _ = process.communicate()
        lines = out.decode('utf-8').splitlines()
        model_line = next((line for line in lines if "Model name:" in line), "")
        return model_line.split(":")[1].strip()
    else:
        return "Unknown"

def show_system_info():
    output = []
    output.append("--- Информация о системе ---")
    output.append(f"Система: {platform.system()}")
    output.append(f"Версия ОС: {platform.release()} ({platform.version()})\n")

    # CPU info
    cpu = psutil.cpu_freq()
    cpu_model = get_cpu_model()
    output.append("\n--- Процессор ---")
    output.append(f"Модель процессора: {cpu_model}")
    output.append(f"Тактовая частота: {cpu.current:.2f} МГц (min={cpu.min}, max={cpu.max})")
    output.append(f"Ядер: {psutil.cpu_count(logical=False)} физических / {psutil.cpu_count()} логических\n")
    
    # Остальные части остаются такими же...
    
    # RAM info
    ram = psutil.virtual_memory()
    output.append("\n--- Оперативная память ---")
    output.append(f"Общий объем памяти: {ram.total // (1024 ** 3)} ГБ")
    output.append(f"Доступно свободной памяти: {ram.available // (1024 ** 3)} ГБ\n")

    # Video card info
    if platform.system() == "Windows":
        def get_gpu_info():
            c = wmi.WMI()
            gpus = c.Win32_VideoController()
            gpu_list = []
            for gpu in gpus:
                gpu_list.append({
                    "Description": gpu.Description,
                    "AdapterRAM": gpu.AdapterRAM
                })
            return gpu_list
        
        gpus = get_gpu_info()
        output.append("\n--- Видеокарта ---")
        for i, gpu in enumerate(gpus):
            output.append(f"Графический процессор №{i + 1}: {gpu['Description']}")
            output.append(f"Объём видеопамяти: {gpu['AdapterRAM'] // (1024*1024)} МБ")
            
    elif platform.system() == "Linux":
        def get_gpu_info():
            cmd = ['lspci', '|', 'grep', '-i', 'VGA']
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = process.communicate()
            return out.decode('utf-8').strip()
        
        gpu_info = get_gpu_info()
        output.append("\n--- Видеокарта ---")
        output.append(gpu_info)

    else:
        output.append("\nИнформация о видеокарте недоступна.")

    # Disk info
    partitions = psutil.disk_partitions(all=True)
    output.append("\n--- Диски ---")
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            output.append(f"{partition.device}: Файловая система: {partition.fstype}, Размер: {usage.total // (1024**3)} ГБ, Использовано: {usage.used // (1024**3)} ГБ, Свободно: {usage.free // (1024**3)} ГБ")
        except PermissionError:
            pass

    return "\n".join(output)

if __name__ == "__main__":
    system_info = show_system_info()
    with open('system_info.txt', 'w', encoding='utf-8') as file:
        file.write(system_info)

    print("Информация успешно сохранена в файле system_info.txt.")
    time.sleep(2)
