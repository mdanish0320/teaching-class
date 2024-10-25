1. **Install MySQL Client Library**:
   Install the MySQL client library for Python, which Django uses to connect to MySQL. You can do this with pip:

   ```bash
   pip install mysqlclient
   ```

2. **Update Django Database Settings**:
   Open your project’s settings file (`settings.py`) and update the `DATABASES` configuration to use MySQL. Replace the existing `sqlite` configuration with the following:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_mysql_user',
           'PASSWORD': 'your_mysql_password',
           'HOST': 'your_mysql_host',  # Set to 'localhost' if running on the same server
           'PORT': '3306',             # Default MySQL port
       }
   }
   

### Difference Between the library `mysqlclient` and `PyMySQL`

| Feature                | `mysqlclient`                                | `PyMySQL`                                    |
|------------------------|----------------------------------------------|----------------------------------------------|
| **Library Type**       | Written in C (C extension)                   | Pure Python                                  |
| **Performance**        | Faster (due to C implementation)             | Slower (pure Python implementation)          |
| **Installation**       | May require `mysql_config` and C compiler    | Easier to install (no compiler required)     |
| **Compatibility**      | Generally better for production environments | Good for lightweight or development use      |
| **Usage**              | Default choice for Django + MySQL            | Alternative for environments without C compilers |

### Which to Choose?

- **`mysqlclient`** is generally preferred for production due to its better performance.
- **`PyMySQL`** is convenient if you're facing issues installing `mysqlclient`, especially in environments without a C compiler.