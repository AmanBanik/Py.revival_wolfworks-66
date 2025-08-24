# Match Cases

def http_status(status):
    match status:
        case 200:
            return 'OK'
        case 404:
            return 'Not Found'
        case 500:
            return 'Internal Server Error'
        case _:# for '_' or any otrher code
            return 'Unknown Status'
        
print(http_status(7777))