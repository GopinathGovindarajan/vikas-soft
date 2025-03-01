def count_keyword_in_logs(file_path, keyword):
    with open(file_path, 'r') as log_file:
        logs = log_file.readlines()
        print("logs:",logs)
    print("Outer logs:",logs)
    print("")
    count = sum(1 for line in logs if keyword in line)
    print(f"'{keyword}' occurred {count} times in the log file.")
    
count_keyword_in_logs('application.log', 'ERROR')
