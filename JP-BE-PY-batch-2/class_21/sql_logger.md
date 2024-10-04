# Logging Queries

You can enable logging of all SQL queries by configuring Django's logging settings.

## Steps to Enable SQL Query Logging:

1. **Edit `settings.py`:**

   Add the following to your logging configuration:

   ```python
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
           },
       },
       'loggers': {
           'django.db.backends': {
               'handlers': ['console'],
               'level': 'DEBUG',
           },
       },
   }
   ```

2. **Run Your Application:** 

   Once you have this setup, any SQL queries executed will be logged to the console. This is especially useful for debugging and performance tuning.

