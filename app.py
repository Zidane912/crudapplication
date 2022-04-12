from application import app, db
from os import getenv

if __name__ == "__main__":
    # Recreate the table schema in the database if environment variable
    # CREATE_SCHEMA is set to "true". Any other value will not recreate
    # the schema.
    #
    # To set the CREATE_SCHEMA value on Linux, run:
    #   export CREATE_SCHEMA=true

    if getenv("CREATE_SCHEMA") != None:
        if getenv("CREATE_SCHEMA").lower() == "true":
            db.drop_all()
            db.create_all()
            
    app.run(debug=True, host="0.0.0.0", port=5000)