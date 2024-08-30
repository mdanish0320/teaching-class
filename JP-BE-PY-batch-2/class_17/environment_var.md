# Passing and Accessing Environment Variables

## Setting Environment Variables from the Terminal

To set environment variables in your terminal, use the `export` command. <br>
This makes the variable available to processes started from that terminal session.

### Syntax
```bash
export DATABASE_URL="mysql://user:password@host:port/dbname"
```

## Accessing Environment Variables in Python
```
import os

# Retrieve the environment variable
database_url = os.environ.get("DATABASE_URL")

# Use the variable in your application
print(f"Connecting to database at {database_url}")
```

