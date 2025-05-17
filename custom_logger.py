def write_log(filename, file_mode = 'a', log_note='':
    
    """
    Writes a message to a text file
      filename: filename to save in current dir or provide '/path/to/filename.mylog' 
      file_mode: 'a' for append (the default) or 'w'
      log_note: text string to log.  Can be multi-line. If log_note is blank or not provided then "NO ERRORS" is written
    """
  
    if len(log_note) == 0: 
        print("NO ERRORS") 
        return True 
     
    with open (log_file, file_mode) as f: 
        logwriter = csv.writer(f, sys.stdout, lineterminator='\n') 
        for line in log_note: 
            logwriter.writerow(line) 

    f.close() 
    
    return True
