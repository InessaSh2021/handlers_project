import logging  

def process_logs(log_files):  
    """  
    Обрабатывает логи файлов и формирует отчет.  

    Args:  
        log_files: Список путей к файлам логов.  
    """  

    # Настройка логирования  
    logging.basicConfig(filename="report.txt",   
                        level=logging.INFO,   
                        format='%(asctime)s - %(levelname)s - %(message)s')  

    # Словарь для хранения количества запросов по уровням логирования  
    log_counts = {  
        'DEBUG': 0,  
        'INFO': 0,  
        'WARNING': 0,  
        'ERROR': 0,  
        'CRITICAL': 0  
    }  
    
    total_requests = 0  

    for log_file in log_files:  
        try:  
            with open(log_file, 'r', encoding='utf-8') as f:  
                for line in f:  
                    parts = line.split()  
                    # Проверка длины строки  
                    if len(parts) < 3:  
                        continue  # Пропускаем строки, которые не соответствуют формату  
                    
                    timestamp = parts[0] + ' ' + parts[1]  # Временной штамп  
                    log_level = parts[2]  # Уровень логирования  

                    # Обрабатываем логи в формате app2.log и app3.log  
                    if log_level == 'INFO' and len(parts) > 3:  
                        total_requests += 1  # Увеличиваем общее количество запросов  
                        # Считаем количество запросов только для INFO уровня  
                        log_counts['INFO'] += 1  
                    
                    # Увеличиваем счетчик для других уровней логирования  
                    if log_level in log_counts:  
                        log_counts[log_level] += 1  

            logging.info(f"Обрабатывал файл: {log_file}")  

        except FileNotFoundError:  
            print(f"Файл не найден: {log_file}")  
        except Exception as e:  
            print(f"Ошибка при обработке файла {log_file}: {e}")  

    # Записываем отчет в лог  
    logging.info("Итоговая статистика:")  
    for level, count in log_counts.items():  
        logging.info(f"{level}: {count}")  

    print(f"Total requests: {total_requests}")  
    for level, count in log_counts.items():  
        print(f"{level}: {count}")  

if __name__ == "__main__":
    logs_files = ["app1.log", "app2.log", "app3.log"]  # Замените на ваши пути к логам.  
    process_logs(logs_files)  



