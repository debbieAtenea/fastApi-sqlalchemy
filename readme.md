# Set up confi.py

Enter the environment variables in the `confi.py` vars:

| Variables    | Value                                                                          |
|--------------|--------------------------------------------------------------------------------|
| localhost    | `<my_localhost>`                                                               |
| username     | `<my_username>`                                                                |
| password     | `<my_password>`                                                                |
| port         | `<my_port>`                                                                    |
| database     | `<my_database>`                                                                |
| DATABASE_URI | `f"postgresql+psycopg2://{username}:{password}@{localhost}:{port}/{database}"` |
